# Axe component rebuild — October 14, 2026

The Axe art is rebuilt as independently selected haft and head components using the component fit and assembly approach used for Cannons and Crossbows. The previous mounted-art iteration remains in the repository as a rollback/reference; the catalog now selects the new component-only sprites.

## Rebuilt pieces

- Woodcutter’s Haft, Corsair’s Hook Haft and Cinderbrace Split Haft: horizontal standalone hafts with exposed right-side insertion ends.
- Forester’s Axe Bit, Raider’s Hook Bit, Drakeglass Bearded Edge, Bog-Iron Hewing Head, Basalt Double Bit and Star-Slate Crescent Bit: individual head components with calibrated eye/sleeve openings.
- Nine transparent 512×512 RGBA component files under `assets/entropic_forge/icons/`.

## Assembly and scope

- Catalog icon paths now point to the nine new components. Existing Axe overlap and draw order are unchanged.
- Contact-sheet review covers all 18 combinations from three hafts × six heads. Enlarged join details were checked across wood, corsair and cinder hafts.
- Gameplay fields, item statistics, core effects, Axe expansion-item references and Sword calibration/rendering are unchanged.
- `weapon_attachment_points.json` adds one full-source attachment record per new PNG; the assembled preview uses only the selected haft and head texture.
- Preview renders are independent raster compositions using the source regions, pivots, transforms, scales, overlap and draw order from `weapon_snap_preview.gd`. Godot was unavailable here, so this is not an in-engine or Android capture.

## Review images

- `axe-component-assembly-review-oct14.png` — all 18 legal combinations.
- `axe-component-join-detail-oct14.png` — three enlarged component joins.
