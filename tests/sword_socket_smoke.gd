extends SceneTree
## Exercise every Sword pair and render a representative sheet when requested.
var errors: Array[String] = []

func _initialize() -> void:
	call_deferred("_run")

func _run() -> void:
	var catalog: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://data/entropic_forge/forge_test_catalog.json"))
	var points: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://data/entropic_forge/sword_attachment_points.json"))
	var frames: Array = catalog["frameworks"].filter(func(item: Dictionary) -> bool: return item["family"] == "Sword")
	var blades: Array = catalog["strikers"].filter(func(item: Dictionary) -> bool: return item["family"] == "Sword")
	var forge := preload("res://scripts/forge_lab_v2.gd").new()
	root.add_child(forge)
	for group in ["frameworks", "strikers"]:
		for item in catalog[group]:
			if item["family"] != "Sword":
				continue
			var record: Dictionary = forge._sword_record(item, group)
			if "res://" + str(record.get("file", "")) != item["icon"]:
				errors.append("Selected and assembled artwork differ: " + str(item["name"]))
			var checker := preload("res://scripts/weapon_snap_preview.gd").new()
			var prepared: Dictionary = checker._prepare_part(record)
			checker.free()
			var selected: Image = forge._icon(item).get_image()
			var r: Array = record["region_px"]
			var expected: Image = selected.get_region(Rect2i(r[0], r[1], r[2], r[3]))
			if prepared["texture"].get_image().get_data() != expected.get_data():
				errors.append("Assembly changed selected pixels: " + str(item["name"]))
	forge.queue_free()
	var count := 0
	for f in frames:
		for b in blades:
			var preview := preload("res://scripts/weapon_snap_preview.gd").new()
			var fr: Dictionary = f.duplicate(true)
			var br: Dictionary = b.duplicate(true)
			fr.merge(points["frameworks"][f["name"]], true)
			br.merge(points["strikers"][b["name"]], true)
			if not preview.configure(fr, br):
				errors.append("Could not configure " + str(f["name"]) + " / " + str(b["name"]))
			else:
				for canvas in [Vector2(415,244), Vector2(300,170), Vector2(720,300)]:
					var placed: Dictionary = preview.layout_for_canvas(canvas)
					var delta: Vector2 = placed["hilt_socket"] - placed["blade_socket"]
					if absf(delta.y) > 0.001 or absf(delta.x - 5.0 * float(placed["scale"])) > 0.001:
						errors.append("Socket overlap is not five scaled pixels")
					for key in ["frame", "blade"]:
						var rect: Rect2 = placed[key]
						if rect.position.x < 17.9 or rect.position.y < 17.9 or rect.end.x > canvas.x - 17.9 or rect.end.y > canvas.y - 17.9:
							errors.append("Assembly escapes preview: " + str(f["name"]))
			preview.free()
			count += 1
	print("Sword socket pairs: ", count, "; three viewport sizes; errors: ", errors.size())
	for error in errors:
		push_error(error)
	if "--capture" in OS.get_cmdline_user_args():
		root.size = Vector2i(1440, 840)
		var background := ColorRect.new()
		background.color = Color("18232b")
		background.size = Vector2(1440,840)
		root.add_child(background)
		for i in blades.size():
			var f: Dictionary = frames[i % frames.size()].duplicate(true)
			var b: Dictionary = blades[i].duplicate(true)
			f.merge(points["frameworks"][f["name"]], true)
			b.merge(points["strikers"][b["name"]], true)
			var preview := preload("res://scripts/weapon_snap_preview.gd").new()
			preview.position = Vector2((i % 4) * 360, (i / 4) * 280)
			preview.size = Vector2(360, 230)
			preview.configure(f, b)
			root.add_child(preview)
			var label := Label.new()
			label.text = str(f["name"]) + "\n" + str(b["name"])
			label.position = preview.position + Vector2(8, 232)
			label.add_theme_font_size_override("font_size", 13)
			root.add_child(label)
		for i in range(10):
			await process_frame
		await RenderingServer.frame_post_draw
		root.get_texture().get_image().save_png("res://build/sword-socket-review.png")
	quit(0 if errors.is_empty() else 1)
