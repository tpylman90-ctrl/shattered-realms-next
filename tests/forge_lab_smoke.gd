extends SceneTree
## Regression: Foundry must be visible after entering from title.
var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _check(ok: bool, message: String) -> void:
	if not ok:
		failures.append(message)
		push_error(message)

func _run() -> void:
	var app: Control = load("res://scenes/front_end.tscn").instantiate()
	root.add_child(app)
	for i in range(8):
		await process_frame
	app.motion_enabled = false
	app.show_forge_lab()
	for i in range(8):
		await process_frame
	_check(app.screen == "forge_lab", "Forge button must navigate into Foundry")
	var lab: Control = app.page.get_child(0) as Control
	_check(lab != null, "Foundry control missing")
	if lab != null:
		_check(lab.size.x > 300 and lab.size.y > 250, "Foundry root has collapsed dimensions: %s" % lab.size)
		var scroll: ScrollContainer = lab.find_children("*", "ScrollContainer", true, false)[0] as ScrollContainer
		_check(scroll != null, "Foundry missing controls")
		if scroll != null:
			_check(scroll.size.x > 200 and scroll.size.y > 200, "Foundry scroll is invisible: %s" % scroll.size)
		var heading: Label = lab.find_child("*", true, false) as Label
		_check(lab.family.item_count == 15, "All 15 weapon families must appear")
		_check(lab.core.item_count == 60, "All 60 cores must appear")
		_check(lab.browser_category.item_count == 6, "All 6 catalog groups must appear")
		_check(lab.icon_previews.size() == 3, "Three artwork slots must render")
		lab._heat()
		_check(lab.active, "Forging should start")
		lab._strike()
		_check(lab.hits == 1, "Strike button must record an attempt")
	print("Foundry smoke: ", "FAILED" if not failures.is_empty() else "PASSED")
	quit(1 if not failures.is_empty() else 0)
