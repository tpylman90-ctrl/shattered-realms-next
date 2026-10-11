extends SceneTree
var failures: Array[String] = []
var city: Control

func _initialize() -> void:
	call_deferred("run")

func check(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)
		push_error(message)

func settle() -> void:
	for frame in range(4):
		await process_frame

func choose_action(npc_id: String, node_id: String, action: String) -> void:
	city.talk(npc_id, node_id)
	for option in city.npcs[npc_id].nodes[node_id].choices:
		if option.get("action", "") == action:
			city.choose(npc_id, option)
			return
	check(false, "Missing action " + action)

func run() -> void:
	var app = load("res://scenes/front_end.tscn").instantiate()
	app.persistent_city_progress = false
	root.add_child(app)
	await settle()
	app.motion_enabled = false
	app.start_campaign()
	app.open_location("blackthorn")
	await settle()
	city = app.page.get_node("Blackthorn")
	check(city.rooms.size() == 8, "Eight Blackthorn locations are required")
	check(city.npcs.size() == 6, "Six local NPCs are required")
	# Every room is reachable from the entrance using actual exits.
	var reached: Array[String] = ["courtyard"]
	var pending: Array[String] = ["courtyard"]
	while not pending.is_empty():
		var id := pending.pop_back() as String
		city.enter_room(id)
		await settle()
		check(city.canvas.texture != null, "Missing room art " + id)
		for hotspot in city.rooms[id].hotspots:
			if hotspot.kind == "exit":
				check(city.rooms.has(hotspot.target), "Dangling room exit " + id)
				city.activate_hotspot(hotspot)
				check(city.room_id == hotspot.target, "Exit must navigate from " + id)
				city.enter_room(id)
				if not reached.has(hotspot.target):
					reached.append(hotspot.target)
					pending.append(hotspot.target)
			elif hotspot.kind == "npc":
				check(city.npcs.has(hotspot.target), "Missing NPC " + hotspot.target)
			elif hotspot.kind in ["inspect", "rest"]:
				city.activate_hotspot(hotspot)
				check(is_instance_valid(city.modal), "Inspection must show text")
				city.close_modal()
		if id != "courtyard":
			city.handle_back()
			check(city.room_id == city.rooms[id].parent, "Back must reach room parent")
	check(reached.size() == city.rooms.size(), "Every room must be connected")
	# Every conversation node displays a portrait and links only to real nodes.
	for npc_id in city.npcs:
		var npc: Dictionary = city.npcs[npc_id]
		check(npc.portrait >= 0 and npc.portrait < 6, "Valid portrait tile required")
		for node_id in npc.nodes:
			city.talk(npc_id, node_id)
			await settle()
			check(city.find_child("NPCPortrait", true, false) != null, "Portrait missing for " + npc_id)
			check(city.find_child("DialogueText", true, false).text == npc.nodes[node_id].text, "Dialogue text mismatch")
			for option in npc.nodes[node_id].get("choices", []):
				check(npc.nodes.has(option.next), "Dangling dialogue branch")
		city.close_modal()
	# Errand must be gated, consumable once, and persistent without touching player saves.
	city.state.flags.clear()
	city.state.apply_action("collect_bandages")
	check(not city.state.has_flag("carrying_bandages"), "Cannot collect before accepting errand")
	choose_action("tamsin", "request", "accept_bandages")
	check(city.state.has_flag("bandages_requested"), "Accept must activate errand")
	choose_action("nell", "greeting", "collect_bandages")
	check(city.state.has_flag("carrying_bandages"), "Nell must give the bundle")
	choose_action("tamsin", "greeting", "deliver_bandages")
	check(city.state.has_flag("bandages_delivered") and not city.state.has_flag("carrying_bandages"), "Delivery must consume bundle and complete errand")
	city.state.apply_action("collect_bandages")
	check(not city.state.has_flag("carrying_bandages"), "Cannot duplicate completed errand supplies")
	city.state.persistent = true
	city.state.save_path = "user://blackthorn_test_progress.cfg"
	city.state.save_progress()
	var restored = load("res://scripts/blackthorn_state.gd").new()
	restored.save_path = city.state.save_path
	restored.load_progress()
	check(restored.has_flag("bandages_delivered"), "Errand completion must survive reload")
	check(restored.visited.size() == 8, "Visited rooms must survive reload")
	DirAccess.remove_absolute(restored.save_path)
	city.state.persistent = false
	city.close_modal()
	city.enter_room("captains_tent")
	city.talk("rowan")
	app.go_back()
	check(not is_instance_valid(city.modal) and city.room_id == "captains_tent", "Back closes conversation before leaving room")
	app.go_back()
	check(city.room_id == "militia_yard", "Back leaves tent for yard")
	app.go_back()
	check(city.room_id == "courtyard", "Back leaves yard for courtyard")
	app.go_back()
	check(app.screen == "atlas", "Back at gate returns to atlas")
	if failures.is_empty():
		print("BLACKTHORN PASS: 8 connected rooms, 6 portrait NPCs, all dialogue nodes, errand gating, save/reload, nested back")
	quit(0 if failures.is_empty() else 1)
