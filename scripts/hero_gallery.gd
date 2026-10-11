extends Control
## Runtime-ready hero pair preview. Artwork paths are supplied by the companion asset pack.
signal return_requested

const PAIRS := [
	["Golden Expanse", "zephyr", "samira"],
	["Blighted Marsh", "morana", "odran"],
	["Ember Coast", "ignacia", "tavian"],
	["Cursed Mire / Deadwind Hollow", "malakor", "sereth"],
	["Copperfen Basin", "tessa", "tobin"],
	["Stormcrown", "thorvald", "eydis"],
	["Ravenford / Eldergrove", "alistair", "elowen"],
	["Veiled Sea", "jora", "roran"],
	["Drakeshard Range", "dareth", "kaela"],
	["Iron Plains", "cedric", "adela"],
	["Ravenwood", "lyra", "garrick"],
	["Ashen Wastes", "ignis", "veyra"],
	["Frostpeaks", "vesper", "stellan"]
]
const NAMES := {
	"zephyr": "Zephyr", "samira": "Samira Dawnwatch",
	"morana": "Morana", "odran": "Odran Fenward",
	"ignacia": "Ignacia", "tavian": "Tavian Ashsail",
	"malakor": "Malakor", "sereth": "Sereth Veilkeeper",
	"tessa": "Tessa Brasswick", "tobin": "Tobin Rivetlock",
	"thorvald": "Thorvald Thunderbrow", "eydis": "Eydis Stormweaver",
	"alistair": "Sir Alistair", "elowen": "Dame Elowen",
	"jora": "Captain Jora Stormtide", "roran": "Captain Roran Deepwatch",
	"dareth": "Dareth Scalebreaker", "kaela": "Kaela Wyrmbound",
	"cedric": "General Cedric Ironclad", "adela": "Marshal Adela Steelwind",
	"lyra": "Lyra Vane", "garrick": "Garrick Thornward",
	"ignis": "Ignis", "veyra": "Veyra Cindervein",
	"vesper": "Vesper", "stellan": "Stellan Rimeborn"
}
var portrait_a: TextureRect
var portrait_b: TextureRect
var name_a: Label
var name_b: Label
var info: Label

func _ready() -> void:
	set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var panel := VBoxContainer.new()
	panel.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	panel.add_theme_constant_override("separation", 8)
	add_child(panel)
	var bar := HBoxContainer.new()
	panel.add_child(bar)
	var back := Button.new()
	back.text = "‹ BACK TO TITLE"
	back.pressed.connect(func(): return_requested.emit())
	bar.add_child(back)
	var header := Label.new()
	header.text = "HEROES OF THE SHATTERED REALMS"
	header.add_theme_font_size_override("font_size", 27)
	header.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	header.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	bar.add_child(header)
	var picker := OptionButton.new()
	picker.custom_minimum_size.x = 300
	for pair in PAIRS:
		picker.add_item(pair[0])
	bar.add_child(picker)
	var portraits := HBoxContainer.new()
	portraits.size_flags_vertical = Control.SIZE_EXPAND_FILL
	portraits.add_theme_constant_override("separation", 12)
	panel.add_child(portraits)
	var first := _portrait_column(portraits)
	name_a = first[0]
	portrait_a = first[1]
	var second := _portrait_column(portraits)
	name_b = second[0]
	portrait_b = second[1]
	info = Label.new()
	info.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	info.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	panel.add_child(info)
	picker.item_selected.connect(_show_pair)
	_show_pair(0)

func _portrait_column(parent: BoxContainer) -> Array:
	var box := VBoxContainer.new()
	box.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	box.size_flags_vertical = Control.SIZE_EXPAND_FILL
	parent.add_child(box)
	var name_label := Label.new()
	name_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	name_label.add_theme_font_size_override("font_size", 23)
	box.add_child(name_label)
	var art := TextureRect.new()
	art.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	art.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	art.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	art.size_flags_vertical = Control.SIZE_EXPAND_FILL
	box.add_child(art)
	return [name_label, art]

func _show_pair(index: int) -> void:
	var pair: Array = PAIRS[index]
	name_a.text = NAMES[pair[1]]
	name_b.text = NAMES[pair[2]]
	portrait_a.texture = _texture(pair[1])
	portrait_b.texture = _texture(pair[2])
	info.text = "Choose one hero to recruit; the other remains to protect the territory. Recruitment choices are not active in this preview."
	if portrait_a.texture == null or portrait_b.texture == null:
		info.text = "Sprite files not installed. Extract the 26-hero asset pack into the project root."

func _texture(hero_id: String) -> Texture2D:
	var path := "res://assets/runtime/characters/%s.png" % hero_id
	if ResourceLoader.exists(path):
		return load(path) as Texture2D
	return null
