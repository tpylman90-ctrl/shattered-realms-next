extends SceneTree
## Opens the live Foundry and tests inventory stages and reveal.
var failures: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _check(ok: bool, message: String) -> void:
	if not ok:
		failures.append(message)
		push_error(message)

func _settle() -> void:
	for i in range(7):
		await process_frame

func _run() -> void:
	var app: Control = load("res://scenes/front_end.tscn").instantiate()
	root.add_child(app)
	await _settle()
	app.motion_enabled = false
	app.show_forge_lab()
	await _settle()
	_check(app.screen == "forge_lab", "Forge button must open Foundry")
	var lab: Control = app.page.get_child(0) as Control if app.page.get_child_count() > 0 else null
	_check(lab != null, "Foundry root is missing")
	if lab != null:
		_check(lab.size.x > 300 and lab.size.y > 250, "Forge screen must fill viewport")
		_check(lab.families.size() == 15, "15 families must be selectable")
		_check(lab.total_entries == 702, "Expanded catalog should contain 702 entries")
		_check(lab.cards.get_child_count() == 15, "Inventory should begin with 15 family cards")
		lab._choose(0)
		lab._advance()
		_check(lab.step == 1, "Selecting a family advances to framework")
		_check(lab.cards.get_child_count() == 10, "All families must now have ten framework cards")
		lab._choose(0)
		lab._advance()
		_check(lab.step == 2, "Framework advances to striker")
		_check(lab.cards.get_child_count() == 12, "All families must now have twelve striker cards")
		lab._choose(0)
		lab._advance()
		_check(lab.step == 3, "Striker advances to core")
		_check(lab.cards.get_child_count() == 60, "Sixty core cards must populate")
		lab._choose(0)
		lab._advance()
		_check(lab.step == 4, "Core advances to forge tier")
		lab._advance()
		_check(lab.result_view.visible, "Start Craft should show result")
		_check(lab.center_label.text != "", "Result needs a weapon name")
		_check(lab.details.text.contains("Framework"), "Result must include assembly details")
		lab._craft_again()
		_check(lab.step == 0 and lab.selection_view.visible, "Craft Again returns to item grid")
	print("Foundry inventory smoke: ", "FAILED" if not failures.is_empty() else "PASSED")
	quit(1 if not failures.is_empty() else 0)
