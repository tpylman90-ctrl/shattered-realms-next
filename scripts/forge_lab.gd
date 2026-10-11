extends Control
## Developer-only forging sandbox. No save or inventory mutations.
signal return_requested

const GOLD := Color("e6c58b")
const DATA_PATH := "res://data/entropic_forge/forge_test_catalog.json"

var data: Dictionary = {}
var family: OptionButton
var frame: OptionButton
var head: OptionButton
var core: OptionButton
var forge: OptionButton
var info: RichTextLabel
var timing: ProgressBar
var feedback: Label
var frame_items: Array = []
var head_items: Array = []
var core_items: Array = []
var active := false
var phase := 0.0
var hits := 0
var precision := 0
var browser_category: OptionButton
var browser_item: OptionButton
var browser_details: RichTextLabel
var browser_entries: Array = []
var forged_history: RichTextLabel
var forged_count := 0
var icon_previews: Array[TextureRect] = []
var browser_icon: TextureRect

func _ready() -> void:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(DATA_PATH))
	if not parsed is Dictionary:
		push_error("Forge test data is missing")
		return
	data = parsed
	var background: Control
	if ResourceLoader.exists("res://assets/forge/forge_room.png"):
		var plate := TextureRect.new()
		plate.texture = load("res://assets/forge/forge_room.png")
		plate.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		plate.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		background = plate
	else:
		background = Control.new()
		background.set_script(load("res://scripts/forge_room_backdrop.gd"))
	background.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(background)
	background.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var scroll := ScrollContainer.new()
	scroll.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(scroll)
	var margin := MarginContainer.new()
	margin.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	for side in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + side, 18)
	scroll.add_child(margin)
	var column := VBoxContainer.new()
	column.add_theme_constant_override("separation", 12)
	margin.add_child(column)
	var top := HBoxContainer.new()
	column.add_child(top)
	var back := Button.new()
	back.text = "‹ TITLE"
	back.pressed.connect(func(): return_requested.emit())
	top.add_child(back)
	var heading := Label.new()
	heading.text = "ENTROPIC FORGE  ·  SANDBOX"
	heading.add_theme_font_size_override("font_size", 28)
	heading.add_theme_color_override("font_color", GOLD)
	top.add_child(heading)
	var disclaimer := Label.new()
	disclaimer.text = "Full 512-entry catalog · unlimited materials · practice mode only · no campaign save changes."
	column.add_child(disclaimer)
	family = _picker(column, "Weapon family")
	frame = _picker(column, "Framework")
	head = _picker(column, "Striker")
	core = _picker(column, "Entropic core")
	forge = _picker(column, "Forge tier")
	for value in ["Standard", "Mistvale", "Sands"]:
		forge.add_item(value)
	var artwork_row := HBoxContainer.new()
	artwork_row.add_theme_constant_override("separation", 10)
	column.add_child(artwork_row)
	for title in ["FRAMEWORK", "STRIKER", "CORE"]:
		var cell := VBoxContainer.new()
		cell.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		artwork_row.add_child(cell)
		var cap := Label.new()
		cap.text = title
		cap.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		cell.add_child(cap)
		var image := TextureRect.new()
		image.custom_minimum_size = Vector2(0, 108)
		image.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		image.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		cell.add_child(image)
		icon_previews.append(image)
	info = RichTextLabel.new()
	info.bbcode_enabled = true
	info.custom_minimum_size.y = 250
	column.add_child(info)
	var actions := HBoxContainer.new()
	column.add_child(actions)
	for pair in [["HEAT", "_heat"], ["STRIKE", "_strike"], ["RESET", "_reset_trial"]]:
		var button := Button.new()
		button.text = pair[0]
		button.custom_minimum_size = Vector2(150, 54)
		button.pressed.connect(Callable(self, pair[1]))
		actions.add_child(button)
	timing = ProgressBar.new()
	timing.max_value = 100
	timing.custom_minimum_size.y = 34
	column.add_child(timing)
	feedback = Label.new()
	feedback.text = "Heat the metal, then strike while the indicator is in the 70–82% zone. Five strikes."
	column.add_child(feedback)
	for item in data.get("cores", []):
		core_items.append(item)
		core.add_item(str(item.get("name", "?")))
	var family_names: Array[String] = []
	for item in data.get("frameworks", []):
		var value := str(item.get("family", ""))
		if not family_names.has(value):
			family_names.append(value)
	family_names.sort()
	for value in family_names:
		family.add_item(value)
	family.item_selected.connect(func(_i: int): _select_family())
	frame.item_selected.connect(func(_i: int): _refresh())
	head.item_selected.connect(func(_i: int): _refresh())
	core.item_selected.connect(func(_i: int): _refresh())
	forge.item_selected.connect(func(_i: int): _refresh())
	if family.item_count > 0:
		family.select(0)
	if core.item_count > 0:
		core.select(0)
	_select_family()

	var browser_heading := Label.new()
	browser_heading.text = "CATALOG INSPECTOR · ALL 512 ENTRIES"
	browser_heading.add_theme_font_size_override("font_size", 23)
	browser_heading.add_theme_color_override("font_color", GOLD)
	column.add_child(browser_heading)
	browser_category = _picker(column, "Item category")
	browser_item = _picker(column, "Catalog entry")
	for group in ["Frameworks", "Strikers", "Cores", "Gathering stocks", "Salvage", "Named weapons"]:
		browser_category.add_item(group)
	browser_icon = TextureRect.new()
	browser_icon.custom_minimum_size = Vector2(0, 110)
	browser_icon.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	browser_icon.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	column.add_child(browser_icon)
	browser_details = RichTextLabel.new()
	browser_details.bbcode_enabled = true
	browser_details.custom_minimum_size.y = 145
	column.add_child(browser_details)
	browser_category.item_selected.connect(func(_i: int): _fill_browser())
	browser_item.item_selected.connect(func(_i: int): _inspect_item())
	browser_category.select(0)
	_fill_browser()
	var history_heading := Label.new()
	history_heading.text = "THIS SESSION'S FORGING RESULTS"
	history_heading.add_theme_color_override("font_color", GOLD)
	column.add_child(history_heading)
	forged_history = RichTextLabel.new()
	forged_history.bbcode_enabled = true
	forged_history.custom_minimum_size.y = 75
	forged_history.text = "[i]Finish five strikes to add a trial result here.[/i]"
	column.add_child(forged_history)

func _picker(parent: VBoxContainer, label_text: String) -> OptionButton:
	var line := HBoxContainer.new()
	parent.add_child(line)
	var label := Label.new()
	label.text = label_text
	label.custom_minimum_size.x = 220
	line.add_child(label)
	var selector := OptionButton.new()
	selector.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	selector.custom_minimum_size.y = 46
	line.add_child(selector)
	return selector

func _select_family() -> void:
	frame_items.clear()
	head_items.clear()
	frame.clear()
	head.clear()
	if family.selected < 0:
		return
	var chosen := family.get_item_text(family.selected)
	for item in data.get("frameworks", []):
		if str(item.get("family", "")) == chosen:
			frame_items.append(item)
			frame.add_item(str(item.get("name", "")))
	for item in data.get("strikers", []):
		if str(item.get("family", "")) == chosen:
			head_items.append(item)
			head.add_item(str(item.get("name", "")))
	if frame.item_count > 0:
		frame.select(0)
	if head.item_count > 0:
		head.select(0)
	_refresh()

func _refresh() -> void:
	if frame.selected < 0 or head.selected < 0 or core.selected < 0:
		return
	var a: Dictionary = frame_items[frame.selected]
	var b: Dictionary = head_items[head.selected]
	var c: Dictionary = core_items[core.selected]
	for idx in range(3):
		var item: Dictionary = [a, b, c][idx]
		icon_previews[idx].texture = _item_texture(item)
	var result := "Uncharted assembly"
	var formula := ""
	for recipe in data.get("recipes", []):
		if str(recipe.get("framework", "")) == str(a.get("name", "")) and str(recipe.get("striker", "")) == str(b.get("name", "")) and str(recipe.get("core", "")) == str(c.get("name", "")):
			result = str(recipe.get("name", ""))
			var ranks := str(recipe.get("attack", "")).split(" → ")
			var rank: int = mini(forge.selected, ranks.size() - 1)
			formula = "\n[b]Catalog benchmark:[/b] %s physical / elemental\nDurability: %s; seconds/action: %s" % [ranks[rank], str(recipe.get("durability", "")), str(recipe.get("interval", ""))]
			break
	if formula.is_empty():
		formula = "\n[i]Compatible component set; production stat formula not installed. No invented attack result.[/i]"
	info.text = "[b]%s[/b]\nFramework: %s · Tier %s · Durability %s\nHandling: %s\nStriker: %s · Physical %s\nTrait: %s\nCore: %s · Elemental %s · Chance %s\nEffect: %s%s" % [result, str(a.get("name","")),str(a.get("tier","")),str(a.get("durability","")),str(a.get("handling","")),str(b.get("name","")),str(b.get("physical","")),str(b.get("trait","")),str(c.get("name","")),str(c.get("elemental","")),str(c.get("chance","")),str(c.get("effect","")),formula]

func _item_texture(item: Dictionary) -> Texture2D:
	var path := str(item.get("icon", ""))
	if path != "" and ResourceLoader.exists(path):
		return load(path)
	return null

func _fill_browser() -> void:
	browser_item.clear()
	browser_entries.clear()
	var group := browser_category.selected
	var key := ["frameworks", "strikers", "cores", "stocks", "salvage", "recipes"][group]
	for entry in data.get(key, []):
		browser_entries.append(entry)
		browser_item.add_item(str(entry.get("name", "?")))
	if not browser_entries.is_empty():
		browser_item.select(0)
	_inspect_item()

func _inspect_item() -> void:
	if browser_item.selected < 0 or browser_entries.is_empty():
		browser_details.text = ""
		return
	var entry: Dictionary = browser_entries[browser_item.selected]
	browser_icon.texture = _item_texture(entry)
	var lines := PackedStringArray()
	for key in entry.keys():
		if key != "name":
			lines.append("%s: %s" % [str(key).replace("_", " ").capitalize(), str(entry[key])])
	browser_details.text = "[b]%s[/b]\\n%s" % [str(entry.get("name", "")), "\\n".join(lines)]

func _heat() -> void:
	active = true
	phase = 0.0
	hits = 0
	precision = 0
	feedback.text = "Metal heated. Strike at 70–82%."

func _process(delta: float) -> void:
	if active:
		phase += delta
		timing.value = 50.0 + 50.0 * sin(phase * 3.6)

func _strike() -> void:
	if not active:
		feedback.text = "Heat the metal first."
		return
	hits += 1
	var accurate := timing.value >= 70.0 and timing.value <= 82.0
	if accurate:
		precision += 1
	if hits >= 5:
		active = false
		var grade := "ROUGH"
		if precision >= 4:
			grade = "MASTERWORK"
		elif precision >= 2:
			grade = "SERVICEABLE"
		feedback.text = "%s · %d of 5 precise strikes. Prototype feedback only; nothing was consumed." % [grade, precision]
		forged_count += 1
		var a: Dictionary = frame_items[frame.selected]
		var b: Dictionary = head_items[head.selected]
		var c: Dictionary = core_items[core.selected]
		var found := "Uncharted %s assembly" % family.get_item_text(family.selected)
		for recipe in data.get("recipes", []):
			if recipe["framework"] == a["name"] and recipe["striker"] == b["name"] and recipe["core"] == c["name"]:
				found = str(recipe["name"])
				break
		forged_history.text = "[b]#%d %s — %s[/b] · %d/5 precise strikes\\n%s" % [forged_count, found, grade, precision, forged_history.text]
	else:
		feedback.text = "Strike %d of 5: %s (%.0f%%)" % [hits, "PRECISE" if accurate else "MISSED", timing.value]

func _reset_trial() -> void:
	active = false
	phase = 0.0
	hits = 0
	precision = 0
	timing.value = 0
	feedback.text = "Trial reset."
