extends Control
## Procedural forge-room backdrop until the approved full-resolution plate is committed.

var ember_time := 0.0

func _ready() -> void:
	mouse_filter = Control.MOUSE_FILTER_IGNORE

func _process(delta: float) -> void:
	ember_time += delta
	queue_redraw()

func _draw() -> void:
	var s := size
	draw_rect(Rect2(Vector2.ZERO, s), Color("1d1715"))
	var wall_h := s.y * 0.72
	draw_rect(Rect2(0, 0, s.x, wall_h), Color("322521"))
	draw_rect(Rect2(0, wall_h, s.x, s.y - wall_h), Color("2d2a27"))
	for i in range(11):
		var y := wall_h * float(i) / 10.0
		draw_line(Vector2(0, y), Vector2(s.x, y), Color("51372d"), 3.0)
	for i in range(8):
		var x := float(i) * s.x / 7.0
		draw_rect(Rect2(x, 0, s.x * 0.018, wall_h), Color("1e1614"))
		draw_line(Vector2(x + s.x * 0.016, 0), Vector2(x + s.x * 0.016, wall_h), Color("74533b"), 2.0)
	# Weapon-rack silhouettes and workshop shelving.
	var rail_y := s.y * 0.24
	draw_rect(Rect2(s.x * 0.05, rail_y, s.x * 0.38, 11), Color("140e0d"))
	for i in range(8):
		var x := s.x * (0.085 + i * 0.046)
		var height := s.y * (0.14 + 0.04 * (i % 3))
		draw_line(Vector2(x, rail_y + 4), Vector2(x, rail_y + height), Color("9e9786"), 5.0)
		draw_line(Vector2(x - 6, rail_y + 7), Vector2(x + 6, rail_y + 7), Color("c2a068"), 4.0)
	# Furnace masonry and layered glow to establish lighting.
	var furnace := Rect2(s.x * 0.71, s.y * 0.18, s.x * 0.25, s.y * 0.53)
	draw_rect(furnace.grow(18), Color("181515"))
	draw_rect(furnace, Color("65605b"))
	for i in range(6):
		var x := furnace.position.x + float(i) * furnace.size.x / 6.0
		draw_line(Vector2(x, furnace.position.y), Vector2(x, furnace.end.y), Color("27201f"), 4.0)
	draw_rect(Rect2(s.x * 0.755, s.y * 0.33, s.x * 0.16, s.y * 0.33), Color("190e0a"))
	var center := Vector2(s.x * 0.835, s.y * 0.54)
	for i in range(14, 0, -1):
		var radius := s.x * (0.007 + float(i) * 0.004)
		var alpha := 0.045 + 0.018 * (14 - i) / 14.0
		draw_circle(center, radius, Color(1.0, 0.32, 0.07, alpha))
	for i in range(6):
		var phase := ember_time * 3.0 + float(i) * 0.9
		var x := center.x + sin(phase) * s.x * 0.029
		var top := center.y - s.y * (0.03 + 0.045 * (0.5 + 0.5 * sin(phase * 1.8)))
		var p := PackedVector2Array([Vector2(x - 18, center.y + 27), Vector2(x + 22, center.y + 29), Vector2(x + 3, top)])
		draw_colored_polygon(p, Color("f7a036") if i % 2 == 0 else Color("ffda68"))
	# Foreground workbench and anvil create depth behind the controls.
	draw_rect(Rect2(s.x * 0.48, s.y * 0.76, s.x * 0.42, s.y * 0.062), Color("3b2821"))
	draw_rect(Rect2(s.x * 0.54, s.y * 0.81, s.x * 0.055, s.y * 0.19), Color("1a1615"))
	draw_rect(Rect2(s.x * 0.79, s.y * 0.81, s.x * 0.055, s.y * 0.19), Color("1a1615"))
	var anvil := PackedVector2Array([Vector2(s.x * 0.63, s.y * 0.71),Vector2(s.x * 0.81,s.y * 0.71),Vector2(s.x * 0.84,s.y * 0.75),Vector2(s.x * 0.74,s.y * 0.775),Vector2(s.x * 0.69,s.y * 0.89),Vector2(s.x * 0.64,s.y * 0.89)])
	draw_colored_polygon(anvil, Color("454b4c"))
	draw_line(Vector2(s.x * 0.635,s.y * 0.73),Vector2(s.x * 0.80,s.y * 0.73),Color("a2a5a0"),6.0)
	# Darken on the left to keep selectors legible.
	draw_rect(Rect2(0, 0, s.x * 0.60, s.y), Color(0.015, 0.02, 0.026, 0.45))
