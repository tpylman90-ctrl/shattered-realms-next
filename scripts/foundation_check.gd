extends Control

const CATALOGS := {
	"territories": ["res://data/campaign/territories.json", "territories"],
	"cities": ["res://data/cities/cities.json", "cities"],
	"dungeons": ["res://data/dungeons/dungeons.json", "dungeons"],
	"heroes": ["res://data/heroes/heroes.json", "heroes"]
}


func _ready() -> void:
	var issues: Array[String] = []
	var entries: Dictionary = {}
	var ids: Dictionary = {}
	for catalog_name in CATALOGS:
		var definition: Array = CATALOGS[catalog_name]
		entries[catalog_name] = _load_entries(str(definition[0]), str(definition[1]), issues)
		ids[catalog_name] = _index_ids(entries[catalog_name], str(catalog_name), issues)

	var territory_ids: Dictionary = ids.get("territories", {})
	var city_ids: Dictionary = ids.get("cities", {})
	var dungeon_ids: Dictionary = ids.get("dungeons", {})
	for territory in entries.get("territories", []):
		for neighbor in territory.get("connects_to", []):
			if not territory_ids.has(str(neighbor)):
				issues.append("Unknown connected territory: %s" % str(neighbor))
		var city_id: Variant = territory.get("city_id")
		if city_id != null and not city_ids.has(str(city_id)):
			issues.append("Unknown city: %s" % str(city_id))
		var dungeon_id := str(territory.get("dungeon_id", ""))
		if not dungeon_ids.has(dungeon_id):
			issues.append("Unknown dungeon: %s" % dungeon_id)
	for hero in entries.get("heroes", []):
		if not territory_ids.has(str(hero.get("territory_id", ""))):
			issues.append("Unknown hero territory: %s" % str(hero.get("territory_id", "")))

	var status := "FOUNDATION READY" if issues.is_empty() else "CONTENT CHECK FAILED"
	var detail := "%d territories, %d cities, %d dungeons, and %d named heroes loaded." % [
		entries.get("territories", []).size(),
		entries.get("cities", []).size(),
		entries.get("dungeons", []).size(),
		entries.get("heroes", []).size()
	]
	if not issues.is_empty():
		detail = "\n".join(issues)
	_build_screen(status, detail)


func _load_entries(path: String, key: String, issues: Array[String]) -> Array:
	if not FileAccess.file_exists(path):
		issues.append("Missing catalog: %s" % path)
		return []
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		issues.append("Could not open catalog: %s" % path)
		return []
	var parsed: Variant = JSON.parse_string(file.get_as_text())
	if not parsed is Dictionary or not parsed.get(key, null) is Array:
		issues.append("Invalid catalog structure: %s" % path)
		return []
	return parsed.get(key, [])


func _index_ids(items: Array, catalog_name: String, issues: Array[String]) -> Dictionary:
	var result: Dictionary = {}
	for item in items:
		if not item is Dictionary:
			issues.append("Invalid %s entry." % catalog_name)
			continue
		var id := str(item.get("id", ""))
		if id.is_empty() or result.has(id):
			issues.append("Missing or duplicate %s ID: %s" % [catalog_name, id])
			continue
		result[id] = true
	return result


func _build_screen(status: String, detail: String) -> void:
	var background := ColorRect.new()
	background.color = Color("080d13")
	background.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(background)

	var center := CenterContainer.new()
	center.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	add_child(center)

	var stack := VBoxContainer.new()
	stack.alignment = BoxContainer.ALIGNMENT_CENTER
	stack.add_theme_constant_override("separation", 14)
	center.add_child(stack)

	var title := Label.new()
	title.text = "SHATTERED REALMS"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 34)
	title.add_theme_color_override("font_color", Color("e9d6b4"))
	stack.add_child(title)

	var subtitle := Label.new()
	subtitle.text = "A connected world. A shared campaign."
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	subtitle.add_theme_font_size_override("font_size", 18)
	subtitle.add_theme_color_override("font_color", Color("9ca9ae"))
	stack.add_child(subtitle)

	var state := Label.new()
	state.text = status
	state.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	state.add_theme_font_size_override("font_size", 16)
	state.add_theme_color_override("font_color", Color("d6a85f") if status == "FOUNDATION READY" else Color("e07c68"))
	stack.add_child(state)

	var message := Label.new()
	message.text = detail
	message.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	message.add_theme_font_size_override("font_size", 14)
	message.add_theme_color_override("font_color", Color("c3c9c6"))
	stack.add_child(message)
