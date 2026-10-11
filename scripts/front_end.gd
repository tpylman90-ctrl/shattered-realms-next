extends Control
## Temporary direct city entry. Board integration attaches at open_location().

const AtlasView = preload("res://scripts/atlas_view.gd")
const CITY_ART = preload("res://assets/art/blackthorn_arrival.png")
const TITLE_FONT = preload("res://assets/fonts/DejaVuSerif.ttf")
const GOLD := Color("e6c58b")
const INK := Color("0b151b")
const MUTED := Color("b3c1c0")

var screen := "title"
var selected_region := "ravenwood"
var regions: Array = []
var page: Control
var atlas: Control
var region_panel: PanelContainer
var region_picker: OptionButton
var last_zoom := 1.0
var last_pan := Vector2.ZERO
var settings_dialog: AcceptDialog
var motion_enabled := true


func _ready() -> void:
	get_tree().auto_accept_quit = false
	var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://data/campaign/atlas.json"))
	if not parsed is Dictionary or not parsed.get("regions") is Array:
		push_error("World atlas catalog is missing or invalid.")
		return
	regions = parsed.regions
	_install_theme()
	var preferences := ConfigFile.new()
	if preferences.load("user://preferences.cfg") == OK:
		motion_enabled = preferences.get_value("display", "motion", true)
	show_title()


func _install_theme() -> void:
	var skin := Theme.new()
	skin.default_font_size = 23
	skin.set_color("font_color", "Label", Color("f4ebd9"))
	skin.set_color("font_color", "Button", GOLD)
	skin.set_color("font_hover_color", "Button", Color("fff2ce"))
	skin.set_stylebox("normal", "Button", _box(Color("101d23"), Color("826e4c")))
	skin.set_stylebox("hover", "Button", _box(Color("25352f"), GOLD))
	skin.set_stylebox("pressed", "Button", _box(Color("354333"), GOLD))
	skin.set_stylebox("focus", "Button", _box(Color(0, 0, 0, 0), Color("ffe3a6"), 3))
	skin.set_stylebox("panel", "PanelContainer", _box(Color(0.035, 0.07, 0.09, 0.96), Color("766647")))
	skin.set_constant("separation", "VBoxContainer", 16)
	skin.set_constant("separation", "HBoxContainer", 12)
	theme = skin


func _box(fill: Color, border: Color, width := 1) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = fill
	style.border_color = border
	style.set_border_width_all(width)
	style.set_corner_radius_all(5)
	style.content_margin_left = 20
	style.content_margin_right = 20
	style.content_margin_top = 14
	style.content_margin_bottom = 14
	return style


func _new_page(id: String) -> void:
	if is_instance_valid(page):
		remove_child(page)
		page.queue_free()
	screen = id
	page = Control.new()
	page.name = id.capitalize()
	add_child(page)
	page.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	if motion_enabled:
		page.modulate.a = 0.0
		create_tween().tween_property(page, "modulate:a", 1.0, 0.25)


func _label(value: String, font_size := 23, color := Color("f4ebd9"), heading := false) -> Label:
	var label := Label.new()
	label.text = value
	label.add_theme_font_size_override("font_size", font_size)
	label.add_theme_color_override("font_color", color)
	if heading:
		label.add_theme_font_override("font", TITLE_FONT)
	return label


func _paragraph(value: String, font_size := 23) -> Label:
	var label := _label(value, font_size, MUTED)
	label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	return label


func _button(value: String, callback: Callable, minimum_width := 0.0) -> Button:
	var button := Button.new()
	button.text = value
	button.custom_minimum_size = Vector2(minimum_width, 60)
	button.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
	button.pressed.connect(callback)
	return button


func _art(parent: Control, darken := false) -> TextureRect:
	var picture := TextureRect.new()
	picture.texture = CITY_ART
	picture.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	picture.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	picture.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(picture)
	picture.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	if darken:
		var overlay := ColorRect.new()
		overlay.color = Color(0.01, 0.035, 0.055, 0.64)
		overlay.mouse_filter = Control.MOUSE_FILTER_IGNORE
		parent.add_child(overlay)
		overlay.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	return picture


func _margin(parent: Control, amount := 28) -> MarginContainer:
	var margin := MarginContainer.new()
	for side in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + side, amount)
	parent.add_child(margin)
	margin.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	return margin


func show_title() -> void:
	_new_page("title")
	_art(page, true)
	var center := CenterContainer.new()
	page.add_child(center)
	center.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var stack := VBoxContainer.new()
	stack.custom_minimum_size.x = 620
	stack.add_theme_constant_override("separation", 24)
	center.add_child(stack)
	var eyebrow := _label("A REALM DIVIDED. A HOPE UNBROKEN.", 19, GOLD)
	eyebrow.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	stack.add_child(eyebrow)
	var title := _label("SHATTERED\nREALMS", 78, Color("f3dfb6"), true)
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	stack.add_child(title)
	var subtitle := _label("Your journey begins in Ravenwood.", 24, MUTED)
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	stack.add_child(subtitle)
	var start := _button("START CAMPAIGN", start_campaign)
	start.name = "StartCampaign"
	stack.add_child(start)
	stack.add_child(_button("SETTINGS", show_settings))
	var note := _label("THE BLACKTHORN CHAPTER", 17, GOLD)
	note.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	stack.add_child(note)
	start.grab_focus()


func start_campaign() -> void:
	selected_region = "ravenwood"
	last_zoom = 1.0
	last_pan = Vector2.ZERO
	show_atlas()


func show_atlas() -> void:
	_new_page("atlas")
	var background := ColorRect.new()
	background.color = INK
	page.add_child(background)
	background.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var column := VBoxContainer.new()
	_margin(page, 18).add_child(column)
	var top := HBoxContainer.new()
	column.add_child(top)
	top.add_child(_button("‹  TITLE", show_title, 145))
	var title := _label("WORLD ATLAS", 30, GOLD, true)
	title.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(title)
	region_picker = OptionButton.new()
	region_picker.name = "TerritorySelector"
	region_picker.custom_minimum_size = Vector2(310, 60)
	for region in regions:
		region_picker.add_item(region.name)
	region_picker.item_selected.connect(func(index: int): atlas.select_region(str(regions[index].id)))
	top.add_child(region_picker)
	var body := HBoxContainer.new()
	body.size_flags_vertical = Control.SIZE_EXPAND_FILL
	column.add_child(body)
	atlas = AtlasView.new()
	atlas.name = "Atlas"
	atlas.regions = regions
	atlas.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	atlas.size_flags_vertical = Control.SIZE_EXPAND_FILL
	body.add_child(atlas)
	atlas.region_selected.connect(_show_region)
	region_panel = PanelContainer.new()
	region_panel.custom_minimum_size.x = 370
	body.add_child(region_panel)
	var bottom := HBoxContainer.new()
	column.add_child(bottom)
	var hint := _label("Select a land  ·  Drag to pan  ·  Pinch or scroll to zoom", 20, MUTED)
	hint.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	bottom.add_child(hint)
	bottom.add_child(_button("−", func(): atlas.change_zoom(1.0 / 1.3), 64))
	bottom.add_child(_button("+", func(): atlas.change_zoom(1.3), 64))
	bottom.add_child(_button("FIT MAP", func(): atlas.reset_view(), 140))
	atlas.zoom = last_zoom
	atlas.pan = last_pan
	atlas.select_region(selected_region)


func _show_region(id: String) -> void:
	selected_region = id
	var region: Dictionary = {}
	for index in range(regions.size()):
		if str(regions[index].id) == id:
			region = regions[index]
			region_picker.select(index)
			break
	if region.is_empty():
		return
	for child in region_panel.get_children():
		region_panel.remove_child(child)
		child.queue_free()
	var scroll := ScrollContainer.new()
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	region_panel.add_child(scroll)
	var stack := VBoxContainer.new()
	stack.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	scroll.add_child(stack)
	stack.add_child(_label("SELECTED TERRITORY", 16, GOLD))
	var title := _label(str(region.name), 32, Color("f4ebd9"), true)
	title.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	stack.add_child(title)
	stack.add_child(_paragraph(str(region.description)))
	stack.add_child(HSeparator.new())
	stack.add_child(_label("LOCATIONS", 17, GOLD))
	if id == "ravenwood":
		var thumbnail := TextureRect.new()
		thumbnail.texture = CITY_ART
		thumbnail.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		thumbnail.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		thumbnail.custom_minimum_size.y = 155
		stack.add_child(thumbnail)
		var enter := _button("BLACKTHORN  ›", func(): open_location("blackthorn"))
		enter.name = "EnterBlackthorn"
		stack.add_child(enter)
		stack.add_child(_paragraph("A timber-and-stone refuge beneath the ancient trees. Beyond its walls, the forest grows restless.", 21))
	else:
		for settlement in region.settlements:
			stack.add_child(_label(str(settlement), 24, Color("f4ebd9"), true))
		stack.add_child(_paragraph("This land is not yet available to enter.", 20))


func open_location(id: String) -> void:
	if id != "blackthorn":
		return
	if is_instance_valid(atlas) and screen == "atlas":
		last_zoom = atlas.zoom
		last_pan = atlas.pan
	show_blackthorn()


func show_blackthorn() -> void:
	_new_page("blackthorn")
	_art(page)
	var layout := VBoxContainer.new()
	_margin(page).add_child(layout)
	var header := PanelContainer.new()
	layout.add_child(header)
	var row := HBoxContainer.new()
	header.add_child(row)
	row.add_child(_button("‹  RAVENWOOD", show_atlas, 220))
	var names := VBoxContainer.new()
	names.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	names.add_theme_constant_override("separation", 3)
	row.add_child(names)
	names.add_child(_label("BLACKTHORN", 31, GOLD, true))
	names.add_child(_label("RAVENWOOD  /  INSIDE THE GATES", 16, MUTED))
	row.add_child(_button("WORLD ATLAS", show_atlas, 195))
	var spacer := Control.new()
	spacer.size_flags_vertical = Control.SIZE_EXPAND_FILL
	layout.add_child(spacer)
	var footer := PanelContainer.new()
	layout.add_child(footer)
	var story := VBoxContainer.new()
	story.add_theme_constant_override("separation", 8)
	footer.add_child(story)
	story.add_child(_label("A LIGHT IN THE WOODS", 25, GOLD, true))
	story.add_child(_paragraph("Beyond the palisade, Ravenwood stirs in the dark. Here, hearths still burn. Somewhere behind these walls, a warm bed waits.", 23))
	story.add_child(_label("ARRIVAL PREVIEW", 15, MUTED))


func show_settings() -> void:
	settings_dialog = AcceptDialog.new()
	settings_dialog.title = "Settings"
	settings_dialog.dialog_text = ""
	settings_dialog.min_size = Vector2i(600, 300)
	var stack := VBoxContainer.new()
	settings_dialog.add_child(stack)
	var motion := CheckButton.new()
	motion.text = "Screen transitions"
	motion.button_pressed = motion_enabled
	motion.custom_minimum_size.y = 64
	stack.add_child(motion)
	motion.toggled.connect(func(enabled: bool):
		motion_enabled = enabled
		var preferences := ConfigFile.new()
		preferences.set_value("display", "motion", enabled)
		preferences.save("user://preferences.cfg")
	)
	stack.add_child(_label("Map: drag to pan; pinch / scroll to zoom.", 22, MUTED))
	stack.add_child(_label("Escape / Back returns to the previous screen.", 22, MUTED))
	add_child(settings_dialog)
	settings_dialog.close_requested.connect(settings_dialog.queue_free)
	settings_dialog.confirmed.connect(settings_dialog.queue_free)
	settings_dialog.popup_centered()


func go_back() -> void:
	if is_instance_valid(settings_dialog):
		settings_dialog.queue_free()
		return
	if screen == "blackthorn":
		show_atlas()
	elif screen == "atlas":
		show_title()


func _unhandled_key_input(event: InputEvent) -> void:
	if event.is_action_pressed("ui_cancel"):
		go_back()
		get_viewport().set_input_as_handled()


func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_GO_BACK_REQUEST:
		go_back()
	elif what == NOTIFICATION_WM_CLOSE_REQUEST:
		get_tree().quit()
