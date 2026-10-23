extends RefCounted
## Small local exploration save; deliberately separate from future combat/campaign saves.
const SAVE_PATH := "user://blackthorn_exploration.cfg"
var flags: Dictionary = {}
var visited: Array[String] = []
var current_room := "courtyard"
var persistent := true
var save_path := SAVE_PATH

func load_progress() -> void:
	if not persistent:
		return
	var file := ConfigFile.new()
	if file.load(save_path) != OK:
		return
	var stored: Variant = file.get_value("exploration", "flags", {})
	if stored is Dictionary:
		flags = stored
	var rooms: Variant = file.get_value("exploration", "visited", [])
	if rooms is Array:
		for room in rooms:
			visited.append(str(room))
	current_room = str(file.get_value("exploration", "room", "courtyard"))

func save_progress() -> void:
	if not persistent:
		return
	var file := ConfigFile.new()
	file.set_value("exploration", "flags", flags)
	file.set_value("exploration", "visited", visited)
	file.set_value("exploration", "room", current_room)
	var error := file.save(save_path)
	if error != OK:
		push_warning("Blackthorn exploration could not be saved: %s" % error)

func visit(room: String) -> void:
	current_room = room
	if not visited.has(room):
		visited.append(room)
	save_progress()

func has_flag(id: String) -> bool:
	return bool(flags.get(id, false))

func permits(choice: Dictionary) -> bool:
	for id in choice.get("requires", []):
		if not has_flag(str(id)):
			return false
	for id in choice.get("unless", []):
		if has_flag(str(id)):
			return false
	return true

func apply_action(id: String) -> void:
	match id:
		"accept_bandages":
			if not has_flag("bandages_delivered"):
				flags["bandages_requested"] = true
		"collect_bandages":
			if has_flag("bandages_requested") and not has_flag("bandages_delivered"):
				flags["carrying_bandages"] = true
		"deliver_bandages":
			if has_flag("carrying_bandages") and not has_flag("bandages_delivered"):
				flags["carrying_bandages"] = false
				flags["bandages_delivered"] = true
		"rest":
			flags["rested"] = true
	save_progress()

func journal() -> String:
	if has_flag("bandages_delivered"):
		return "A small kindness — complete. Tamsin received Nell’s clean bandages."
	if has_flag("carrying_bandages"):
		return "A small kindness — bring the bandage bundle to Tamsin in the infirmary."
	if has_flag("bandages_requested"):
		return "A small kindness — ask Nell in the barracks for clean bandages."
	return "Get to know Blackthorn. The inn, camp and village workshops are open to you."
