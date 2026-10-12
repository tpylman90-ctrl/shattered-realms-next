extends Control
## One coordinate system for both parts; only the completed assembly is fitted.
var frame: Dictionary = {}
var blade: Dictionary = {}
var overlap_px: float = 5.0
var padding_px: float = 18.0

func _ready() -> void:
	clip_contents = true
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	resized.connect(queue_redraw)

func configure(frame_record: Dictionary, blade_record: Dictionary, overlap: float = 5.0) -> bool:
	frame = _prepare_part(frame_record)
	blade = _prepare_part(blade_record)
	overlap_px = overlap
	queue_redraw()
	return not frame.is_empty() and not blade.is_empty()

func _prepare_part(record: Dictionary) -> Dictionary:
	var path: String = "res://" + str(record.get("file", ""))
	if not ResourceLoader.exists(path):
		return {}
	var texture: Texture2D = load(path) as Texture2D
	var source: Image = texture.get_image()
	var region: Array = record.get("region_px", [])
	var socket: Array = record.get("socket_px", [])
	if source == null or region.size() != 4 or socket.size() != 2:
		return {}
	var rect := Rect2i(int(region[0]), int(region[1]), int(region[2]), int(region[3]))
	var cropped: Image = source.get_region(rect)
	var local_socket := Vector2(float(socket[0]) - rect.position.x, float(socket[1]) - rect.position.y)
	var angle := deg_to_rad(float(record.get("rotation_degrees", 0.0)))
	var rotation_transform := Transform2D(angle, Vector2.ZERO)
	var bounds := Rect2(rotation_transform * Vector2.ZERO, Vector2.ZERO)
	for corner in [Vector2(rect.size.x, 0), Vector2(rect.size), Vector2(0, rect.size.y)]:
		bounds = bounds.expand(rotation_transform * corner)
	var part_scale: float = float(record.get("display_length_px", 200.0)) / bounds.size.x
	return {"texture": ImageTexture.create_from_image(cropped), "size": bounds.size * part_scale,
		"socket": (rotation_transform * local_socket - bounds.position) * part_scale,
		"origin": -bounds.position * part_scale, "angle": angle, "part_scale": part_scale,
		"source_file": path}

func layout_for_canvas(canvas: Vector2) -> Dictionary:
	if frame.is_empty() or blade.is_empty():
		return {}
	# Put the hilt's forward socket at the origin, blade root 5px behind it.
	var frame_pos: Vector2 = -Vector2(frame["socket"])
	var blade_pos: Vector2 = Vector2(-overlap_px, 0.0) - Vector2(blade["socket"])
	var frame_rect := Rect2(frame_pos, Vector2(frame["size"]))
	var blade_rect := Rect2(blade_pos, Vector2(blade["size"]))
	var bounds: Rect2 = frame_rect.merge(blade_rect)
	var usable: Vector2 = (canvas - Vector2.ONE * padding_px * 2.0).max(Vector2.ONE)
	var fit: float = minf(usable.x / bounds.size.x, usable.y / bounds.size.y)
	var offset: Vector2 = (canvas - bounds.size * fit) * 0.5 - bounds.position * fit
	return {"frame": Rect2(offset + frame_pos * fit, frame_rect.size * fit), "blade": Rect2(offset + blade_pos * fit, blade_rect.size * fit), "hilt_socket": offset, "blade_socket": offset + Vector2(-overlap_px * fit, 0.0), "scale": fit}

func _draw() -> void:
	var placed: Dictionary = layout_for_canvas(size)
	if placed.is_empty():
		return
	# The hilt collar conceals the tiny insertion seam, never the whole blade.
	_draw_part(blade, placed["blade"], float(placed["scale"]))
	_draw_part(frame, placed["frame"], float(placed["scale"]))
	draw_set_transform(Vector2.ZERO)

func _draw_part(part: Dictionary, rect: Rect2, fit: float) -> void:
	draw_set_transform(rect.position + Vector2(part["origin"]) * fit,
		float(part["angle"]), Vector2.ONE * float(part["part_scale"]) * fit)
	draw_texture(part["texture"] as Texture2D, Vector2.ZERO)
