extends Control
## One coordinate system for both parts; only the completed assembly is fitted.
var front_part: String = "frame"
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
	blade = _prepare_mounted_pieces(blade_record) if blade_record.has("mount_pieces") else _prepare_part(blade_record)
	overlap_px = overlap
	queue_redraw()
	return not frame.is_empty() and not blade.is_empty()

func _prepare_mounted_pieces(record: Dictionary) -> Dictionary:
	# Bow arms attach independently to the two riser studs. Never overlap two
	# complete limb roots at the centre or cut them short to hide a bad join.
	var ports: Array = frame.get("ports", [])
	var records: Array = record.get("mount_pieces", [])
	if ports.size() != records.size() or ports.is_empty():
		return {}
	var children: Array = []
	var bounds := Rect2()
	for index in range(records.size()):
		var child_record: Dictionary = records[index].duplicate(true)
		child_record["file"] = record["file"]
		var part := _prepare_part(child_record)
		if part.is_empty():
			return {}
		var target: Vector2 = Vector2(ports[index]) - Vector2(frame["socket"])
		var position: Vector2 = target - Vector2(part["socket"])
		var rect := Rect2(position, Vector2(part["size"]))
		bounds = rect if index == 0 else bounds.merge(rect)
		children.append({"part": part, "position": position, "target": target})
	for child in children:
		child["position"] -= bounds.position
	return {"children": children, "size": bounds.size, "socket": -bounds.position,
		"source_file": "res://" + str(record["file"])}

func _prepare_part(record: Dictionary) -> Dictionary:
	var path: String = "res://" + str(record.get("file", ""))
	if not FileAccess.file_exists(path):
		return {}
	var texture: Texture2D = load(path) as Texture2D
	var source: Image
	if texture != null:
		source = texture.get_image()
	else:
		source = Image.new()
		var load_error := source.load(ProjectSettings.globalize_path(path))
		if load_error != OK:
			push_error("Unable to load weapon component: " + path)
			return {}
	var region: Array = record.get("region_px", [])
	var socket: Array = record.get("socket_px", [])
	if source == null or region.size() != 4 or socket.size() != 2:
		return {}
	for excluded in record.get("exclude_rects", []):
		source.fill_rect(Rect2i(excluded[0], excluded[1], excluded[2], excluded[3]), Color.TRANSPARENT)
	var rect := Rect2i(int(region[0]), int(region[1]), int(region[2]), int(region[3]))
	var cropped: Image = source.get_region(rect)
	var local_socket := Vector2(float(socket[0]) - rect.position.x, float(socket[1]) - rect.position.y)
	if record.get("flip_h", false):
		cropped.flip_x()
		local_socket.x = rect.size.x - local_socket.x
	var angle := deg_to_rad(float(record.get("rotation_degrees", 0.0)))
	var rotation_transform := Transform2D(angle, Vector2.ZERO)
	var bounds := Rect2(rotation_transform * Vector2.ZERO, Vector2.ZERO)
	for corner in [Vector2(rect.size.x, 0), Vector2(rect.size), Vector2(0, rect.size.y)]:
		bounds = bounds.expand(rotation_transform * corner)
	var part_scale: float = float(record.get("display_length_px", 200.0)) / (bounds.size.y if record.get("scale_axis", "x") == "y" else bounds.size.x)
	# Fit the visible artwork, not the transparent padding in square inventory icons.
	# Keep the authored scale and socket so trimming cannot move the join.
	var used := cropped.get_used_rect()
	if used.has_area():
		cropped = cropped.get_region(used)
		local_socket -= Vector2(used.position)
		bounds = Rect2(rotation_transform * Vector2.ZERO, Vector2.ZERO)
		for corner in [Vector2(used.size.x, 0), Vector2(used.size), Vector2(0, used.size.y)]:
			bounds = bounds.expand(rotation_transform * corner)
	var ports: Array = []
	for point in record.get("ports_px", []):
		var delta := Vector2(float(point[0]) - float(socket[0]), float(point[1]) - float(socket[1]))
		if record.get("flip_h", false):
			delta.x = -delta.x
		ports.append((rotation_transform * (local_socket + delta) - bounds.position) * part_scale)
	return {"texture": ImageTexture.create_from_image(cropped), "size": bounds.size * part_scale,
		"socket": (rotation_transform * local_socket - bounds.position) * part_scale,
		"origin": -bounds.position * part_scale, "angle": angle, "part_scale": part_scale,
		"source_file": path, "ports": ports}

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
	if front_part == "blade":
		_draw_part(frame, placed["frame"], float(placed["scale"]))
		_draw_part(blade, placed["blade"], float(placed["scale"]))
	else:
		_draw_part(blade, placed["blade"], float(placed["scale"]))
		_draw_part(frame, placed["frame"], float(placed["scale"]))
	draw_set_transform(Vector2.ZERO)

func _draw_part(part: Dictionary, rect: Rect2, fit: float) -> void:
	if part.has("children"):
		for child in part["children"]:
			_draw_part(child["part"], Rect2(rect.position + Vector2(child["position"]) * fit, Vector2(child["part"]["size"]) * fit), fit)
		return
	draw_set_transform(rect.position + Vector2(part["origin"]) * fit,
		float(part["angle"]), Vector2.ONE * float(part["part_scale"]) * fit)
	draw_texture(part["texture"] as Texture2D, Vector2.ZERO)
