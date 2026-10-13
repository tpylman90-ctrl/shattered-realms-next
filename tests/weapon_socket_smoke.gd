extends SceneTree

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var errors: Array[String] = []
	var forge := preload("res://scripts/forge_lab_v2.gd").new()
	root.add_child(forge)
	var count := 0
	for family in forge.families:
		var settings: Dictionary = forge.sword_points if family == "Sword" else forge.weapon_points["families"][family]
		var overlap := float(settings.get("overlap_px", 5))
		for f in forge.catalog["frameworks"]:
			if f["family"] != family:
				continue
			for b in forge.catalog["strikers"]:
				if b["family"] != family:
					continue
				var fr: Dictionary = forge._weapon_record(f, "frameworks")
				var br: Dictionary = forge._weapon_record(b, "strikers")
				if fr.get("file", "") != str(f["icon"]).trim_prefix("res://") or br.get("file", "") != str(b["icon"]).trim_prefix("res://"):
					errors.append("Selected art mismatch: " + str(f["name"]))
				var preview := preload("res://scripts/weapon_snap_preview.gd").new()
				if not preview.configure(fr, br, overlap):
					errors.append("Missing socket: " + str(f["name"]) + " / " + str(b["name"]))
				else:
					for canvas in [Vector2(300,170),Vector2(415,244),Vector2(720,300)]:
						var layout: Dictionary = preview.layout_for_canvas(canvas)
						var delta: Vector2 = layout["hilt_socket"] - layout["blade_socket"]
						if absf(delta.y) > 0.01 or absf(delta.x - overlap * float(layout["scale"])) > 0.01:
							errors.append("Socket join error: " + family)
						for key in ["frame", "blade"]:
							var rect: Rect2 = layout[key]
							if not rect.position.is_finite() or rect.position.x < 17.9 or rect.position.y < 17.9 or rect.end.x > canvas.x-17.9 or rect.end.y > canvas.y-17.9:
								errors.append("Out of bounds: " + family)
				preview.free()
				count += 1
		# Exercise the live result builder, not only the layout helper.
		forge.choice = [forge.families.find(family),0,0,0,0]
		forge._show_result()
		await process_frame
		await process_frame
		var surface: Control = forge.composite_preview.get_parent().get_parent()
		if absf(forge.composite_preview.size.x - surface.size.x) > 1.0:
			errors.append("Preview does not fill result surface: " + family)
		if not forge.composite_preview.has_node("SocketAlignedWeapon"):
			errors.append("Live result did not mount parts: " + family)
		forge._craft_again()
	print("Weapon sockets: ", count, " pairs in ", forge.families.size(), " families, three sizes; errors: ", errors.size())
	for error in errors:
		push_error(error)
	forge.queue_free()
	quit(0 if errors.is_empty() and count == 1800 else 1)
