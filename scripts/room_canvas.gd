extends Control
## Hotspots share the exact painted image transform, including letterboxing.
signal hotspot_activated(hotspot: Dictionary)
var texture: Texture2D
var hotspots: Array = []
var markers_visible := true

func _ready() -> void:
	clip_contents = true
	resized.connect(_position_buttons)

func image_rect() -> Rect2:
	if texture == null:
		return Rect2()
	var factor := minf(size.x / texture.get_width(), size.y / texture.get_height())
	var dimensions := texture.get_size() * factor
	return Rect2((size - dimensions) * 0.5, dimensions)

func show_room(definition: Dictionary) -> void:
	texture = load(str(definition.art))
	hotspots = definition.hotspots
	for child in get_children():
		remove_child(child)
		child.queue_free()
	for hotspot in hotspots:
		var button := Button.new()
		button.text = ("› " if hotspot.kind == "exit" else "• ") + str(hotspot.label)
		button.custom_minimum_size = Vector2(110, 54)
		button.add_theme_font_size_override("font_size", 20)
		button.tooltip_text = str(hotspot.label)
		button.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
		button.pressed.connect(func(): hotspot_activated.emit(hotspot))
		add_child(button)
	_position_buttons()
	queue_redraw()

func set_markers(value: bool) -> void:
	markers_visible = value
	_position_buttons()

func _position_buttons() -> void:
	var rect := image_rect()
	for index in range(get_child_count()):
		var button := get_child(index) as Button
		var spot: Dictionary = hotspots[index]
		button.size = button.get_combined_minimum_size()
		var point := rect.position + Vector2(spot.at[0], spot.at[1]) * rect.size
		button.position = point - button.size * 0.5
		button.position.x = clampf(button.position.x, rect.position.x, maxf(rect.position.x, rect.end.x - button.size.x))
		button.position.y = clampf(button.position.y, rect.position.y, maxf(rect.position.y, rect.end.y - button.size.y))
		button.visible = markers_visible
	queue_redraw()

func _draw() -> void:
	draw_rect(Rect2(Vector2.ZERO, size), Color("070e11"))
	if texture != null:
		draw_texture_rect(texture, image_rect(), false)
