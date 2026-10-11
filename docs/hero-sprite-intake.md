# Hero sprite pack installation

The **Hero Gallery** title-screen button uses the stable IDs in `scripts/hero_gallery.gd`.

1. Download `shattered_realms_26_hero_pack.zip` supplied with the 2026-10-11 artwork handoff.
2. Extract its `assets/` directory into this Godot repository root, preserving paths. It provides 26 transparent PNGs in `assets/runtime/characters/` and `assets/manifests/hero_sprites.json`.
3. Open the project in Godot and let the editor import the 26 image files.
4. Run the project (F5), select **Hero Gallery**, and select a territory using the dropdown.

The gallery degrades gracefully if the assets have not been installed. It is intentionally **a preview only**: no recruitment choice is made, and gameplay/avatar sprites, directional walk cycles, weapon sockets and battle animations are not yet implemented. The character art is single-pose source artwork and is not a movement sprite sheet.

The supplied artwork has been preserved at source resolution. The pack must be copied into the local Godot working tree and committed by a repo maintainer before its binaries are part of GitHub. Do not merge this change expecting the PNG files to materialize on their own.
