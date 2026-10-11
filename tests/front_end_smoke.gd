extends SceneTree

var failures: Array[String] = []
var app: Control


func _initialize() -> void:
	call_deferred("run")


func check(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)
		push_error(message)


func settle() -> void:
	for frame in range(5):
		await process_frame


func run() -> void:
	app = load("res://scenes/front_end.tscn").instantiate()
	app.persistent_city_progress = false
	root.add_child(app)
	await settle()
	app.motion_enabled = false
	check(app.screen == "title", "Project must open at title")
	var start: Button = app.find_child("StartCampaign", true, false)
	check(start != null, "Start Campaign must be present")
	start.pressed.emit()
	await settle()
	check(app.screen == "atlas", "Start Campaign must open atlas")
	check(app.selected_region == "ravenwood", "Campaign must start with Ravenwood selected")
	check(app.regions.size() == 18, "Expanded atlas must include all 18 selectable lands")
	for region in app.regions:
		var rect: Rect2 = app.atlas.image_rect()
		var point := rect.position + Vector2(region.marker[0], region.marker[1]) * rect.size
		check(app.atlas.region_at(point) == str(region.id), "Map hit area must match " + str(region.name))
	# Camera changes must not detach the click regions from the painted map.
	app.atlas.change_zoom(2.0)
	app.atlas.pan = Vector2(45, 30)
	var transformed: Rect2 = app.atlas.image_rect()
	check(app.atlas.region_at(transformed.position + transformed.size * Vector2(.22, .20)) == "ravenwood", "Zoomed Ravenwood selection must align")
	var enter: Button = app.find_child("EnterBlackthorn", true, false)
	enter.pressed.emit()
	await settle()
	check(app.screen == "blackthorn", "Blackthorn location button must open arrival scene")
	app.go_back()
	await settle()
	check(app.screen == "atlas" and app.selected_region == "ravenwood", "Back must restore Ravenwood")
	check(is_equal_approx(app.atlas.zoom, 2.0), "Returning from city must retain atlas zoom")
	# Newly added regions are inspectable, but must not enter the wrong city.
	app.atlas.select_region("copperfen_basin")
	await settle()
	check(app.find_child("EnterBlackthorn", true, false) == null, "Copperfen must not expose Blackthorn")
	app.open_location("unknown")
	check(app.screen == "atlas", "Unknown location must not navigate")
	# Pinch release must never be mistaken for a tap.
	app.atlas.reset_view()
	app.atlas.select_region("copperfen_basin")
	var r: Rect2 = app.atlas.image_rect()
	var p := r.position + r.size * Vector2(.22, .20)
	for i in range(2):
		var down := InputEventScreenTouch.new()
		down.index = i
		down.position = p + Vector2(i * 50, 0)
		down.pressed = true
		app.atlas._gui_input(down)
	for i in range(2):
		var up := InputEventScreenTouch.new()
		up.index = i
		up.position = p
		up.pressed = false
		app.atlas._gui_input(up)
	check(app.selected_region == "copperfen_basin", "Pinch release must not navigate")
	var down := InputEventScreenTouch.new()
	down.index = 0
	down.position = p
	down.pressed = true
	app.atlas._gui_input(down)
	var up := InputEventScreenTouch.new()
	up.index = 0
	up.position = p
	app.atlas._gui_input(up)
	check(app.selected_region == "ravenwood", "Single touch must select Ravenwood")
	# Reflow at desktop, phone landscape, ultrawide, and portrait viewport sizes.
	for dimensions in [Vector2i(1600, 900), Vector2i(1280, 720), Vector2i(2400, 1080), Vector2i(720, 1280)]:
		root.size = dimensions
		await settle()
		var viewport_rect := Rect2(Vector2.ZERO, app.size)
		check(viewport_rect.encloses(app.region_panel.get_global_rect()), "Location panel must fit " + str(dimensions))
		check(app.atlas.size.x > 100 and app.atlas.size.y > 100, "Map must retain visible space " + str(dimensions))
	app.go_back()
	await settle()
	check(app.screen == "title", "Atlas back must return to title")
	app.show_settings()
	await settle()
	check(is_instance_valid(app.settings_dialog), "Settings must open")
	app.go_back()
	await settle()
	check(not is_instance_valid(app.settings_dialog), "Back must close settings")
	if failures.is_empty():
		print("FRONT END PASS: navigation, atlas hit regions, zoom, touch gestures, resize and settings")
	quit(0 if failures.is_empty() else 1)
