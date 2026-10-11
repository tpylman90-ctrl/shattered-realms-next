# Forge artwork integration status

## Actual installed content
- 512 catalog records and 180 named combinations are committed in `data/entropic_forge/forge_test_catalog.json`.
- `scripts/forge_lab.gd` resolves `icon` fields for 512 individual PNG paths. It shows the illustrated forge room at `res://assets/forge/forge_room.png` when present; otherwise a lightweight procedural workshop.
- Android APK CI is active on this branch.

## Outstanding upload
The generated binary art pack has been assembled and checked locally in the conversation artifact **shattered_realms_complete_forge_art_overlay.zip**, but **it is not part of the GitHub branch**. Extract and commit the pack at repository root to enable the illustrated room and PNG previews in GitHub Actions APK builds. The ZIP includes 512 individual 256×256 transparent icons; 312 were cropped from later concept atlases and are *representative artwork*, not guaranteed recipe-specific rendered assemblies.

The icon path contract is `assets/entropic_forge/icons/{frameworks,strikers,cores,stocks,salvage,recipes}/<slug>.png`. A validator and manifest are included in the archive.

## Test criteria
1. Godot imports full artwork and loads the test lab with no script errors.
2. Pick components across all 15 families and confirm exact named recipes are recognized.
3. Catalog inspector can browse all six classes and all 512 entries.
4. Five-strike trial produces rough/serviceable/masterwork and appends history without changing campaign save.
5. Android artifact `ShatteredRealmsNext-Android` is produced.

## Safe asset-only ZIP (recommended)
Use `shattered_realms_forge_assets_only.zip` instead of the original overlay, because the original ZIP also contains an older copy of `scripts/forge_lab.gd`. The asset-only ZIP contains precisely 512 item PNG files plus `assets/forge/forge_room.png`, without scripts, data or Git metadata. Extract its `assets/` directory into the root of this feature branch, then commit and push. CI runs `python3 tools/verify_forge_art.py`, validates the Godot project and builds the Android APK.
