# Sword preview attachment points

The catalog icon is the authoritative Sword component image. Both selection tabs and assembled results use the exact same PNG. The old Sword ZIP contains different prototype artwork and is no longer used by the active renderer. This fixes cases such as Icehelm Splitguard changing from silver to a red hilt, and Ashen Magma Edge changing from a serrated blade to a broad hooked head.

`data/entropic_forge/sword_attachment_points.json` contains each of the ten hilts and twelve blades' expected catalog path, complete opaque bounds, source-pixel socket, rotation in degrees, and display length. Cropping removes transparent margins only; it preserves each component silhouette. The source images and inventory paths are unchanged. If a catalog icon changes, its calibration must be reviewed; `_sword_record` rejects a path mismatch instead of silently using unrelated art.

`scripts/weapon_snap_preview.gd` rotates the source texture around its measured socket, inserts the blade five preview-space pixels behind the hilt collar, and draws the hilt over the seam. It fits the rotated bounds of the entire assembly into the panel with 18px padding and one uniform scale. This supports both angled original hilts and newer horizontal hilts without replacing their art.

`tests/sword_socket_smoke.gd` checks the actual catalog-to-renderer paths and compares prepared texture bytes against selected icon pixels for all 22 parts. It checks all 120 pairs at three panel sizes for overlap and containment. The Android workflow runs this test. The optional `--capture` renders a twelve-example sheet when a graphics display is available.

Validation for this change: Godot 4.7.2 headless import, all socket/identity assertions, Foundry inventory smoke, and a visual review of independent reference compositions using the same coordinates. The reference compositions are not gameplay screenshots.

Some expanded blades still share placeholder catalog art. Their selections and results now consistently show that same placeholder; this fix does not create distinct replacement artwork. Core effects and gameplay forging formulas are unchanged.
