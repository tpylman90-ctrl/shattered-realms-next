extends Control
signal exited

const State = preload("res://scripts/blackthorn_state.gd")
const RoomCanvas = preload("res://scripts/room_canvas.gd")
const GOLD := Color("e6c58b")
const PALE := Color("f4ebd9")
const MUTED := Color("b3c1c0")

var state = State.new()
var rooms: Dictionary = {}
var npcs: Dictionary = {}
var room_id := "courtyard"
var canvas: Control
var heading: Label
var description: Label
var route_picker: OptionButton
var modal: Control
var dialogue_npc := ""
var dialogue_node := ""
var markers := true
var portrait_sheet: Texture2D

func _ready() -> void:
	var catalog: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://data/cities/blackthorn.json"))
	rooms = catalog.rooms
	npcs = catalog.npcs
	portrait_sheet = load("res://assets/art/blackthorn/npc_portraits.png")
	state.load_progress()
	_build()
	enter_room(state.current_room if rooms.has(state.current_room) else "courtyard")

func _label(text: String, size := 22, color := PALE) -> Label:
	var label := Label.new()
	label.text = text
	label.add_theme_font_size_override("font_size", size)
	label.add_theme_color_override("font_color", color)
	return label

func _button(text: String, action: Callable) -> Button:
	var button := Button.new()
	button.text = text
	button.custom_minimum_size.y = 56
	button.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
	button.pressed.connect(action)
	return button

func _build() -> void:
	var backdrop := ColorRect.new()
	backdrop.color = Color("091218")
	backdrop.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(backdrop)
	backdrop.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var margin := MarginContainer.new()
	add_child(margin)
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	for side in ["top", "bottom", "left", "right"]:
		margin.add_theme_constant_override("margin_" + side, 16)
	var column := VBoxContainer.new()
	margin.add_child(column)
	var bar := HBoxContainer.new()
	column.add_child(bar)
	bar.add_child(_button("‹ ATLAS", func(): exited.emit()))
	var titles := VBoxContainer.new()
	titles.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	titles.add_theme_constant_override("separation", 1)
	bar.add_child(titles)
	titles.add_child(_label("BLACKTHORN / RAVENWOOD", 15, GOLD))
	heading = _label("", 28, PALE)
	titles.add_child(heading)
	route_picker = OptionButton.new()
	route_picker.custom_minimum_size = Vector2(265, 56)
	route_picker.item_selected.connect(_route_selected)
	bar.add_child(route_picker)
	bar.add_child(_button("JOURNAL", show_journal))
	var toggle := _button("MARKERS", func():
		markers = not markers
		canvas.set_markers(markers)
	)
	toggle.toggle_mode = true
	toggle.button_pressed = true
	bar.add_child(toggle)
	canvas = RoomCanvas.new()
	canvas.name = "RoomCanvas"
	canvas.size_flags_vertical = Control.SIZE_EXPAND_FILL
	column.add_child(canvas)
	canvas.hotspot_activated.connect(activate_hotspot)
	var footer := PanelContainer.new()
	column.add_child(footer)
	description = _label("", 21, MUTED)
	description.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	footer.add_child(description)

func enter_room(id: String) -> void:
	if not rooms.has(id):
		return
	close_modal()
	room_id = id
	state.visit(id)
	var room: Dictionary = rooms[id]
	heading.text = room.name
	description.text = room.description
	canvas.show_room(room)
	canvas.set_markers(markers)
	route_picker.clear()
	route_picker.add_item("GO TO…")
	route_picker.set_item_disabled(0, true)
	for hotspot in room.hotspots:
		if hotspot.kind == "exit":
			route_picker.add_item(str(hotspot.label))
			route_picker.set_item_metadata(route_picker.item_count - 1, hotspot.target)
	route_picker.select(0)

func _route_selected(index: int) -> void:
	if index > 0:
		enter_room(str(route_picker.get_item_metadata(index)))

func activate_hotspot(hotspot: Dictionary) -> void:
	if is_instance_valid(modal):
		return
	match str(hotspot.kind):
		"exit": enter_room(str(hotspot.target))
		"npc": talk(str(hotspot.target))
		"inspect": show_message(str(hotspot.label), str(hotspot.text))
		"rest":
			state.apply_action("rest")
			show_message("A moment of quiet", "You sit on the edge of the bed and let the sounds of the fort settle around you. For a little while, the forest feels far away.")

func _modal_panel() -> VBoxContainer:
	close_modal()
	modal = Control.new()
	modal.name = "ConversationOverlay"
	add_child(modal)
	modal.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var shade := ColorRect.new()
	shade.color = Color(0.0, 0.015, 0.025, 0.40)
	modal.add_child(shade)
	shade.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var margin := MarginContainer.new()
	modal.add_child(margin)
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	for side in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + side, 32)
	var align := VBoxContainer.new()
	align.alignment = BoxContainer.ALIGNMENT_END
	margin.add_child(align)
	var panel := PanelContainer.new()
	panel.name = "DialoguePanel"
	align.add_child(panel)
	var content := VBoxContainer.new()
	panel.add_child(content)
	return content

func close_modal() -> void:
	if is_instance_valid(modal):
		remove_child(modal)
		modal.queue_free()
	modal = null

func portrait(index: int) -> AtlasTexture:
	var image := AtlasTexture.new()
	image.atlas = portrait_sheet
	var tile := portrait_sheet.get_size() / Vector2(3, 2)
	image.region = Rect2(Vector2(index % 3, index / 3) * tile, tile)
	return image

func talk(npc_id: String, node_id := "greeting") -> void:
	if not npcs.has(npc_id) or not npcs[npc_id].nodes.has(node_id):
		return
	dialogue_npc = npc_id
	dialogue_node = node_id
	var npc: Dictionary = npcs[npc_id]
	var node: Dictionary = npc.nodes[node_id]
	var content := _modal_panel()
	var row := HBoxContainer.new()
	row.add_theme_constant_override("separation", 24)
	content.add_child(row)
	var photo := TextureRect.new()
	photo.name = "NPCPortrait"
	photo.texture = portrait(int(npc.portrait))
	photo.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	photo.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	photo.custom_minimum_size = Vector2(210, 210)
	row.add_child(photo)
	var words := VBoxContainer.new()
	words.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.add_child(words)
	words.add_child(_label(str(npc.name), 30, GOLD))
	words.add_child(_label(str(npc.role), 17, MUTED))
	var body := _label(str(node.text), 25)
	body.name = "DialogueText"
	body.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	words.add_child(body)
	var choices := HFlowContainer.new()
	choices.add_theme_constant_override("h_separation", 10)
	choices.add_theme_constant_override("v_separation", 8)
	content.add_child(choices)
	for choice in node.get("choices", []):
		if state.permits(choice):
			var option: Dictionary = choice
			var button := _button(str(option.text), func(): choose(npc_id, option))
			button.add_theme_font_size_override("font_size", 20)
			choices.add_child(button)
	var leave := _button("End conversation", close_modal)
	leave.add_theme_font_size_override("font_size", 20)
	choices.add_child(leave)
	if choices.get_child_count() > 0:
		choices.get_child(0).grab_focus()

func choose(npc_id: String, choice: Dictionary) -> void:
	if not state.permits(choice):
		return
	state.apply_action(str(choice.get("action", "")))
	talk(npc_id, str(choice.get("next", "greeting")))

func show_message(title: String, text: String) -> void:
	var panel := _modal_panel()
	panel.add_child(_label(title, 30, GOLD))
	var body := _label(text, 25)
	body.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	panel.add_child(body)
	panel.add_child(_button("Close", close_modal))

func show_journal() -> void:
	show_message("BLACKTHORN JOURNAL", state.journal() + "\n\nLocations visited: %d / %d" % [state.visited.size(), rooms.size()])

func handle_back() -> bool:
	if is_instance_valid(modal):
		close_modal()
		return true
	if room_id != "courtyard":
		enter_room(str(rooms[room_id].parent))
		return true
	return false
