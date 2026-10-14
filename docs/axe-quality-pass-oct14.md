# Axe quality pass — October 14, 2026

The axe quality pass replaces the three original haft sprites and six original axe-head sprites with nine new transparent mounted sprites. The original source art remains in the local working tree; catalog entries now point to the new versioned `_mounted.png` files.

## Art and mount work

- Reworked Woodcutter’s, Corsair’s Hook, and Cinderbrace hafts with one shared camera, lighting direction, centered top tenons, and distinct wood, wrap, and fitting materials.
- Reworked Forester’s, Raider’s Hook, Drakeglass Bearded, Bog-Iron Hewing, Basalt Double Bit, and Star-Slate Crescent heads. Each has a calibrated hollow socket; the aperture reveals the selected haft underneath in the assembled result.
- Kept the Axe family overlap, draw order, and family settings unchanged. New pivots use the visible tenon/socket entrance. No gameplay values changed.
- Left expansion-item art statuses and icon references unchanged. This pass does not claim placeholder expansion items as unique finished art.

## Visual review and validation

- Inspected a rasterized contact sheet of the 18 combinations formed by the three original haft slots and six original head slots. Reviewed enlarged joins for three representative combinations after aligning the visible socket mouths.
- Validated all nine catalog paths, attachment records, 512×512 RGBA sprites, mount regions, socket pivots, transparent apertures, and file hashes. Compared the catalog with the prior commit: only the nine Axe icon paths changed; item attributes and gameplay fields are unchanged.
- Sword attachment metadata, Sword snap settings, and the snap renderer were not edited.
- The preview is an independent raster composition following `weapon_snap_preview.gd` source regions, transforms, pivots, overlap, and draw order. A Godot executable was unavailable in this environment, so this is not an in-engine or Android screenshot.

## Review images

- `axe-quality-assembly-preview-oct14.png` — all 18 legal base Axe combinations.
- `axe-quality-join-detail-oct14.jpg` — enlarged joins from three material pairings.

Prompts and source mappings are in `axe-quality-pass-prompts-oct14.json` and `axe-quality-manifest-oct14.json`.
