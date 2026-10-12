extends Control
## Entropic Forge selection flow. Sandbox-only, does not mutate campaign data.
signal return_requested

const CATALOG := "res://data/entropic_forge/forge_test_catalog.json"
const ART := "res://assets/forge/forge_room.png"
const SWORD_MANIFEST := "res://sword_snap_manifest.json"
var sword_snap: Dictionary = {}
const GOLD := Color("#e9c889")
const INK := Color("#081923")
const BLUE := Color("#16304a")
const WARM := Color("#aa7142")
const STEPS := ["FAMILY", "FRAMEWORK", "STRIKER", "CORE", "FORGE TIER"]
var catalog: Dictionary = {}
var step := 0
var choice := [-1,-1,-1,-1,0]
var families: Array[String] = []
var selected_parts: Array = [null,null,null]
var total_entries := 0

var step_line: HBoxContainer
var center_label: Label
var stage_heading: Label
var details: RichTextLabel
var cards: GridContainer
var tray_scroll: ScrollContainer
var slot_pictures: Array[TextureRect] = []
var slot_names: Array[Label] = []
var action: Button
var prev: Button
var content_root: VBoxContainer
var selection_view: Control
var result_view: Control
var stage_description: Label
var assembly_row: HBoxContainer
var result_art: TextureRect
var composite_preview: Control
var result_note: Label

func _ready() -> void:
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(CATALOG))
	if not parsed is Dictionary:
		_show_error("Forge catalog is missing or invalid.")
		return
	catalog = parsed
	if FileAccess.file_exists(SWORD_MANIFEST):
		var snap_data: Variant = JSON.parse_string(FileAccess.get_file_as_string(SWORD_MANIFEST))
		if snap_data is Dictionary:
			sword_snap = snap_data
	for entry in catalog.get("frameworks", []):
		var name := str(entry.get("family", ""))
		if not families.has(name):
			families.append(name)
	families.sort()
	for group in ["frameworks","strikers","cores","stocks","salvage","recipes"]:
		total_entries += (catalog.get(group, []) as Array).size()
	_build()
	_set_step(0)

func _show_error(message: String) -> void:
	var label := Label.new()
	label.text = message
	add_child(label)

func _panel(bg: Color, edge: Color = WARM) -> PanelContainer:
	var p := PanelContainer.new()
	var st := StyleBoxFlat.new()
	st.bg_color = bg
	st.border_color = edge
	st.set_border_width_all(2)
	st.set_corner_radius_all(7)
	st.content_margin_left = 12
	st.content_margin_right = 12
	st.content_margin_top = 9
	st.content_margin_bottom = 9
	p.add_theme_stylebox_override("panel", st)
	return p

func _label(value: String, pts: int = 20, tint: Color = Color.WHITE) -> Label:
	var x := Label.new()
	x.text = value
	x.add_theme_font_size_override("font_size",pts)
	x.add_theme_color_override("font_color",tint)
	return x

func _build() -> void:
	var backdrop: Control
	if ResourceLoader.exists(ART):
		var image := TextureRect.new()
		image.texture = load(ART)
		image.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		image.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		backdrop = image
	else:
		backdrop = Control.new()
		backdrop.set_script(load("res://scripts/forge_room_backdrop.gd"))
	backdrop.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(backdrop)
	backdrop.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var shade := ColorRect.new()
	shade.color = Color(0.018,0.029,0.042,0.53)
	shade.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(shade)
	shade.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)

	var margin := MarginContainer.new()
	add_child(margin)
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	for side in ["left","right","top","bottom"]:
		margin.add_theme_constant_override("margin_"+side,12)
	content_root = VBoxContainer.new()
	content_root.add_theme_constant_override("separation",8)
	margin.add_child(content_root)
	var header := HBoxContainer.new()
	content_root.add_child(header)
	var exit := Button.new()
	exit.text = "‹ TITLE"
	exit.custom_minimum_size = Vector2(118,48)
	exit.pressed.connect(func(): return_requested.emit())
	header.add_child(exit)
	var title := _label("ENTROPIC FORGE",29,GOLD)
	title.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	header.add_child(title)
	header.add_child(_label("CRAFTING SANDBOX  ·  %d ITEMS" % total_entries,16,Color("#d4d0c7")))
	step_line = HBoxContainer.new()
	step_line.add_theme_constant_override("separation",6)
	content_root.add_child(step_line)
	var explanation := _panel(Color(0.03,0.08,0.12,0.95))
	content_root.add_child(explanation)
	var excol := VBoxContainer.new()
	explanation.add_child(excol)
	stage_heading = _label("",23,GOLD)
	excol.add_child(stage_heading)
	stage_description = _label("",16)
	stage_description.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	excol.add_child(stage_description)
	# Above the scrolling grid we keep all three assembly slots on display.
	assembly_row = HBoxContainer.new()
	assembly_row.add_theme_constant_override("separation",8)
	content_root.add_child(assembly_row)
	for index in range(3):
		var panel := _panel(Color(0.035,0.09,0.14,0.93),Color("#665c4b"))
		panel.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		assembly_row.add_child(panel)
		var inside := HBoxContainer.new()
		panel.add_child(inside)
		var pic := TextureRect.new()
		pic.custom_minimum_size = Vector2(86,82)
		pic.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		pic.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		inside.add_child(pic)
		slot_pictures.append(pic)
		var names := VBoxContainer.new()
		names.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		inside.add_child(names)
		names.add_child(_label(["FRAMEWORK","STRIKER","CORE"][index],13,GOLD))
		var value := _label("Empty",16)
		value.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		value.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		names.add_child(value)
		slot_names.append(value)
	selection_view = Control.new()
	selection_view.size_flags_vertical = Control.SIZE_EXPAND_FILL
	content_root.add_child(selection_view)
	var selection_stack := VBoxContainer.new()
	selection_stack.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	selection_view.add_child(selection_stack)
	var inventory := _panel(Color(0.018,0.055,0.09,0.96),Color("#9d845a"))
	inventory.size_flags_vertical = Control.SIZE_EXPAND_FILL
	selection_stack.add_child(inventory)
	var ic := VBoxContainer.new()
	inventory.add_child(ic)
	tray_scroll = ScrollContainer.new()
	tray_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	ic.add_child(tray_scroll)
	cards = GridContainer.new()
	cards.columns = 4
	cards.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	cards.add_theme_constant_override("h_separation",9)
	cards.add_theme_constant_override("v_separation",9)
	tray_scroll.add_child(cards)
	result_view = Control.new()
	result_view.size_flags_vertical = Control.SIZE_EXPAND_FILL
	content_root.add_child(result_view)
	result_view.visible = false
	var result_scroll := ScrollContainer.new()
	result_scroll.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	result_view.add_child(result_scroll)
	var result_panel := _panel(Color(0.02,0.05,0.09,0.95),GOLD)
	result_panel.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	result_scroll.add_child(result_panel)
	var result_stack := VBoxContainer.new()
	result_stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	result_stack.add_theme_constant_override("separation",6)
	result_panel.add_child(result_stack)
	center_label = _label("",29,GOLD)
	center_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	result_stack.add_child(center_label)
	var reveal := HBoxContainer.new()
	reveal.add_theme_constant_override("separation",18)
	result_stack.add_child(reveal)
	var showcase := VBoxContainer.new()
	showcase.custom_minimum_size.x = 400
	showcase.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	reveal.add_child(showcase)
	var display_surface := _panel(Color(0.025,0.055,0.09,0.92),GOLD)
	showcase.add_child(display_surface)
	var display_center := CenterContainer.new()
	display_center.custom_minimum_size.y = 246
	display_surface.add_child(display_center)
	var art_stack := Control.new()
	art_stack.custom_minimum_size = Vector2(415,244)
	art_stack.clip_contents = true
	display_center.add_child(art_stack)
	result_art = TextureRect.new()
	result_art.name = "ResultWeaponImage"
	result_art.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	result_art.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	result_art.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	art_stack.add_child(result_art)
	composite_preview = Control.new()
	composite_preview.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	art_stack.add_child(composite_preview)
	result_note = _label("",14,Color("#d7c9ac"))
	result_note.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	result_note.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	showcase.add_child(result_note)
	details = RichTextLabel.new()
	details.bbcode_enabled = true
	details.fit_content = true
	details.scroll_active = false
	details.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	details.custom_minimum_size = Vector2(370,160)
	reveal.add_child(details)
	var footer := HBoxContainer.new()
	footer.add_theme_constant_override("separation",12)
	content_root.add_child(footer)
	prev = Button.new()
	prev.text = "‹ PREVIOUS"
	prev.custom_minimum_size = Vector2(170,54)
	prev.pressed.connect(_previous)
	footer.add_child(prev)
	var spacer := Control.new()
	spacer.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	footer.add_child(spacer)
	action = Button.new()
	action.text = "NEXT ›"
	action.custom_minimum_size = Vector2(210,54)
	action.pressed.connect(_advance)
	footer.add_child(action)

func _refresh_steps() -> void:
	for child in step_line.get_children():
		step_line.remove_child(child)
		child.queue_free()
	for i in STEPS.size():
		var btn := Button.new()
		btn.text = "%d  %s" % [i+1, STEPS[i]]
		btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		btn.custom_minimum_size.y = 42
		btn.disabled = i > step and not _step_complete(i-1)
		if i == step:
			btn.add_theme_color_override("font_color",GOLD)
		var jump := i
		btn.pressed.connect(func(): _set_step(jump))
		step_line.add_child(btn)

func _step_complete(index: int) -> bool:
	if index < 0:
		return true
	for i in range(mini(index+1,4)):
		if choice[i] < 0:
			return false
	return true

func _options() -> Array:
	if step == 0:
		var list: Array = []
		for name in families:
			list.append({"name":name,"family":name})
		return list
	if step == 1 or step == 2:
		var group := "frameworks" if step == 1 else "strikers"
		var filtered: Array = []
		for item in catalog.get(group,[]):
			if str(item.get("family","")) == families[choice[0]]:
				filtered.append(item)
		return filtered
	if step == 3:
		return catalog.get("cores",[])
	return [{"name":"Standard","description":"A dependable regional forge."},{"name":"Mistvale","description":"An ancient forge with stronger craftsmanship."},{"name":"Sands","description":"The highest forge tier of this test catalog."}]

func _set_step(index: int) -> void:
	step = clampi(index,0,4)
	selection_view.visible = true
	result_view.visible = false
	_refresh_steps()
	stage_heading.text = "STAGE %d — %s" % [step+1,STEPS[step]]
	stage_description.text = [
		"Choose a weapon family to determine the valid framework and striker inventory.",
		"Select the weapon's chassis. Its handling and durability shape the assembly.",
		"Choose a striking head or blade. This defines physical damage and tactical traits.",
		"Set the elemental core. Browse all sixty cores and their abilities.",
		"Choose the forge tier. Start Craft to reveal the completed test weapon."
	][step]
	_rebuild_inventory()
	_refresh_slots()
	assembly_row.visible = true
	prev.disabled = step == 0
	action.text = "START CRAFT" if step == 4 else "NEXT STAGE ›"
	action.disabled = choice[step] < 0

func _icon(item: Dictionary) -> Texture2D:
	var path := str(item.get("icon",""))
	return load(path) if path != "" and ResourceLoader.exists(path) else null

func _rebuild_inventory() -> void:
	for old in cards.get_children():
		cards.remove_child(old)
		old.queue_free()
	var options := _options()
	cards.columns = mini(4, maxi(1, options.size()))
	for i in options.size():
		var item: Dictionary = options[i]
		var tile := Button.new()
		tile.custom_minimum_size = Vector2(205,184) if options.size() <= 6 else Vector2(175,158)
		tile.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		tile.clip_contents = true
		var chosen: bool = i == choice[step]
		var skin := StyleBoxFlat.new()
		skin.bg_color = Color("#324b50") if chosen else Color("#142b3a")
		skin.border_color = GOLD if chosen else Color("#566777")
		skin.set_border_width_all(3 if chosen else 1)
		skin.set_corner_radius_all(6)
		tile.add_theme_stylebox_override("normal",skin)
		var box := VBoxContainer.new()
		box.mouse_filter = Control.MOUSE_FILTER_IGNORE
		box.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
		var pic := TextureRect.new()
		pic.mouse_filter = Control.MOUSE_FILTER_IGNORE
		pic.custom_minimum_size.y = 108 if options.size() <= 6 else 91
		pic.size_flags_vertical = Control.SIZE_EXPAND_FILL
		pic.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		pic.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		pic.texture = _icon(item)
		box.add_child(pic)
		var name := _label(str(item.get("name","Unknown")),16,GOLD if chosen else Color("#f7efde"))
		name.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		name.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		name.mouse_filter = Control.MOUSE_FILTER_IGNORE
		box.add_child(name)
		var item_detail := ""
		if step == 1:
			item_detail = "TIER %s  •  DUR %s" % [item.get("tier",0),item.get("durability",0)]
		elif step == 2:
			item_detail = str(item.get("physical",""))
		elif step == 3:
			item_detail = str(item.get("elemental",""))
		elif step == 4:
			item_detail = str(item.get("description",""))
		if item.get("art_status", "") == "placeholder_existing_family_component":
			item_detail += "  •  TEMP ART"
		var sub := _label(item_detail,12,Color("#d7c9ac"))
		sub.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		sub.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		sub.mouse_filter = Control.MOUSE_FILTER_IGNORE
		box.add_child(sub)
		tile.add_child(box)
		var pick := i
		tile.pressed.connect(func(): _choose(pick))
		cards.add_child(tile)

func _choose(index: int) -> void:
	if step == 0 and choice[0] != index:
		choice[1] = -1
		choice[2] = -1
	choice[step] = index
	_refresh_slots()
	_rebuild_inventory()
	action.disabled = false
	_refresh_steps()

func _refresh_slots() -> void:
	for i in range(3):
		var option_idx: int = int(choice[i+1])
		if option_idx < 0 or choice[0] < 0:
			slot_pictures[i].texture = null
			slot_names[i].text = "Empty"
			continue
		var options := _options_for_part(i)
		if option_idx >= options.size():
			slot_names[i].text = "Empty"
			continue
		var item: Dictionary = options[option_idx]
		slot_pictures[i].texture = _icon(item)
		slot_names[i].text = str(item.get("name","Unknown"))

func _options_for_part(index: int) -> Array:
	if index == 2:
		return catalog.get("cores",[])
	var list: Array = []
	var group := "frameworks" if index == 0 else "strikers"
	for item in catalog.get(group,[]):
		if str(item.get("family","")) == families[choice[0]]:
			list.append(item)
	return list

func _previous() -> void:
	if result_view.visible:
		_set_step(4)
	else:
		_set_step(step-1)

func _advance() -> void:
	if choice[step] < 0:
		return
	if step < 4:
		_set_step(step+1)
	else:
		_show_result()

func _show_result() -> void:
	var a: Dictionary = _options_for_part(0)[choice[1]]
	var b: Dictionary = _options_for_part(1)[choice[2]]
	var c: Dictionary = _options_for_part(2)[choice[3]]
	var result: Dictionary = {}
	for recipe in catalog.get("recipes",[]):
		if recipe["framework"] == a["name"] and recipe["striker"] == b["name"] and recipe["core"] == c["name"]:
			result = recipe
			break
	selection_view.visible = false
	result_view.visible = true
	assembly_row.visible = false
	stage_heading.text = "CRAFTING COMPLETE — PRACTICE RESULT"
	stage_description.text = "Hammer timing will be added here later. No items, gold or campaign progress are consumed."
	center_label.text = str(result.get("name","UNCHARTED ASSEMBLY"))
	result_art.texture = null
	for child in composite_preview.get_children():
		composite_preview.remove_child(child)
		child.queue_free()
	var finished_texture := _icon(result) if not result.is_empty() else null
	if families[int(choice[0])] == "Sword" and not sword_snap.is_empty() and _show_sword_snap(a,b):
		result_note.text = "SWORD SNAP TEST — socket join with slight overlap; core effects pending"
	elif finished_texture != null:
		result_art.texture = finished_texture
		result_note.text = "NAMED RECIPE ARTWORK — catalog concept"
	else:
		result_note.text = "UNNAMED ASSEMBLY — component concept preview (final assembled art pending)"
		_add_composite_component(a,Vector2(36,8),Vector2(296,224))
		_add_composite_component(b,Vector2(180,21),Vector2(210,188))
		_add_composite_component(c,Vector2(325,158),Vector2(78,72))
	var stat := "[b]Weapon family:[/b] %s\n[b]Framework:[/b] %s\n[b]Striker:[/b] %s\n[b]Entropic core:[/b] %s\n[b]Forge:[/b] %s\n" % [
		families[choice[0]],a["name"],b["name"],c["name"],["Standard","Mistvale","Sands"][choice[4]]]
	stat += "\n[b]Handling:[/b] %s\n[b]Striker trait:[/b] %s\n[b]Core effect:[/b] %s\n" % [a.get("handling",""),b.get("trait",""),c.get("effect","")]
	if result.is_empty():
		stat += "\n[i]Legal family assembly. Final combat stats require the production forging formula; no values invented.[/i]"
	else:
		var attacks := str(result.get("attack","")).split(" → ")
		stat += "\n[b]Named discovery![/b]\n[b]Physical / elemental:[/b] %s\n[b]Masterwork durability:[/b] %s\n[b]Seconds per action:[/b] %s" % [
			attacks[mini(choice[4],attacks.size()-1)],result.get("durability",""),result.get("interval","")]
	details.text = stat
	prev.disabled = false
	prev.text = "‹ CHANGE PARTS"
	action.disabled = false
	action.text = "CRAFT AGAIN"
	action.pressed.disconnect(_advance)
	action.pressed.connect(_craft_again)

func _craft_again() -> void:
	action.pressed.disconnect(_craft_again)
	action.pressed.connect(_advance)
	prev.text = "‹ PREVIOUS"
	_set_step(0)

func _add_composite_component(item: Dictionary, origin: Vector2, dimensions: Vector2) -> void:
	var texture := _icon(item)
	if texture == null:
		return
	var layer := TextureRect.new()
	layer.texture = texture
	layer.position = origin
	layer.size = dimensions
	layer.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	layer.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	layer.mouse_filter = Control.MOUSE_FILTER_IGNORE
	composite_preview.add_child(layer)


func _show_sword_snap(frame_part: Dictionary, blade_part: Dictionary) -> bool:
	var point_path := "res://data/entropic_forge/sword_attachment_points.json"
	var calibration: Dictionary = JSON.parse_string(FileAccess.get_file_as_string(point_path))
	var assets: Dictionary = sword_snap.get("assets", {})
	var frame_record: Dictionary = {}
	var blade_record: Dictionary = {}
	for entry in assets.get("frameworks", []):
		if str(entry.get("name", "")) == str(frame_part.get("name", "")):
			frame_record = entry.duplicate(true)
	for entry in assets.get("strikers", []):
		if str(entry.get("name", "")) == str(blade_part.get("name", "")):
			blade_record = entry.duplicate(true)
	var frame_points: Dictionary = calibration.get("frameworks", {}).get(frame_part.get("name", ""), {})
	var blade_points: Dictionary = calibration.get("strikers", {}).get(blade_part.get("name", ""), {})
	if frame_record.is_empty() or blade_record.is_empty() or frame_points.is_empty() or blade_points.is_empty():
		return false
	frame_record.merge(frame_points, true)
	blade_record.merge(blade_points, true)
	var preview := preload("res://scripts/weapon_snap_preview.gd").new()
	if not preview.configure(frame_record, blade_record, float(calibration.get("overlap_px", 5.0))):
		preview.free()
		return false
	preview.name = "SocketAlignedSword"
	preview.padding_px = float(calibration.get("canvas_padding_px", 18.0))
	preview.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	composite_preview.add_child(preview)
	return true
