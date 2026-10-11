extends Control
## Image-space selection and camera state remain independent of viewport dimensions.

signal region_selected(id: String)

const ATLAS = preload("res://assets/art/world_atlas.png")
var regions: Array = []
var selected_id := ""
var zoom := 1.0
var pan := Vector2.ZERO
var dragging := false
var press_position := Vector2.ZERO
var moved := false
var touches: Dictionary = {}
var pinch_distance := 0.0
var gesture_had_pinch := false


func _ready() -> void:
	mouse_filter = Control.MOUSE_FILTER_STOP
	clip_contents = true
	resized.connect(_resized)
	set_process_unhandled_key_input(true)


func image_rect() -> Rect2:
	var scale_factor := minf(size.x / ATLAS.get_width(), size.y / ATLAS.get_height())
	var dimensions := ATLAS.get_size() * scale_factor * zoom
	return Rect2((size - dimensions) * 0.5 + pan, dimensions)


func _resized() -> void:
	_clamp_pan()
	queue_redraw()


func _clamp_pan() -> void:
	var extent := (image_rect().size - size) * 0.5
	pan.x = clampf(pan.x, -maxf(extent.x, 0.0), maxf(extent.x, 0.0))
	pan.y = clampf(pan.y, -maxf(extent.y, 0.0), maxf(extent.y, 0.0))


func _draw() -> void:
	draw_rect(Rect2(Vector2.ZERO, size), Color("071218"))
	var rect := image_rect()
	draw_texture_rect(ATLAS, rect, false)
	for region in regions:
		if str(region.id) != selected_id:
			continue
		var polygon := PackedVector2Array()
		for point in region.polygon:
			polygon.append(rect.position + Vector2(point[0], point[1]) * rect.size)
		draw_colored_polygon(polygon, Color(0.9, 0.72, 0.37, 0.10))
		polygon.append(polygon[0])
		draw_polyline(polygon, Color("e4c68b"), 2.0, true)
		var marker := rect.position + Vector2(region.marker[0], region.marker[1]) * rect.size
		draw_arc(marker, 13.0, 0.0, TAU, 48, Color("ffe0a5"), 2.0, true)


func select_region(id: String) -> void:
	selected_id = id
	queue_redraw()
	region_selected.emit(id)


func region_at(local: Vector2) -> String:
	var rect := image_rect()
	if not rect.has_point(local):
		return ""
	var normalized := (local - rect.position) / rect.size
	for region in regions:
		var polygon := PackedVector2Array()
		for point in region.polygon:
			polygon.append(Vector2(point[0], point[1]))
		if Geometry2D.is_point_in_polygon(normalized, polygon):
			return str(region.id)
	return ""


func _select_at(local: Vector2) -> void:
	var id := region_at(local)
	if not id.is_empty():
		select_region(id)


func change_zoom(multiplier: float, focal := Vector2(-1, -1)) -> void:
	if focal.x < 0:
		focal = size * 0.5
	var old_rect := image_rect()
	var old_zoom := zoom
	var image_point := (focal - old_rect.position) / old_rect.size
	zoom = clampf(zoom * multiplier, 1.0, 3.5)
	var new_dimensions := old_rect.size * (zoom / old_zoom)
	pan = focal - (size - new_dimensions) * 0.5 - image_point * new_dimensions
	_clamp_pan()
	queue_redraw()


func reset_view() -> void:
	zoom = 1.0
	pan = Vector2.ZERO
	queue_redraw()


func _gui_input(event: InputEvent) -> void:
	if (event is InputEventMouseButton or event is InputEventMouseMotion) and event.device == InputEvent.DEVICE_ID_EMULATION:
		return
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_WHEEL_UP and event.pressed:
			change_zoom(1.2, event.position)
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN and event.pressed:
			change_zoom(1.0 / 1.2, event.position)
		elif event.button_index == MOUSE_BUTTON_LEFT:
			if event.pressed:
				dragging = true
				moved = false
				press_position = event.position
			else:
				if dragging and not moved:
					_select_at(event.position)
				dragging = false
	elif event is InputEventMouseMotion:
		if dragging:
			moved = moved or event.position.distance_to(press_position) > 10.0
			if moved:
				pan += event.relative
				_clamp_pan()
				queue_redraw()
	elif event is InputEventScreenTouch:
		if event.pressed:
			touches[event.index] = event.position
			if touches.size() == 1:
				press_position = event.position
				moved = false
				gesture_had_pinch = false
			if touches.size() == 2:
				gesture_had_pinch = true
				var points := touches.values()
				pinch_distance = points[0].distance_to(points[1])
		else:
			if touches.size() == 1 and not moved and not gesture_had_pinch:
				_select_at(event.position)
			touches.erase(event.index)
			pinch_distance = 0.0
	elif event is InputEventScreenDrag:
		touches[event.index] = event.position
		moved = moved or event.position.distance_to(press_position) > 10.0
		if touches.size() == 2:
			var points := touches.values()
			var distance: float = points[0].distance_to(points[1])
			if pinch_distance > 0.0:
				change_zoom(distance / pinch_distance, (points[0] + points[1]) * 0.5)
			pinch_distance = distance
		elif moved:
			pan += event.relative
			_clamp_pan()
			queue_redraw()
	accept_event()
