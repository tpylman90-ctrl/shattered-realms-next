# Sword preview attachment points

The Sword preview now joins a hilt's forward socket to a blade's root, with five preview-space pixels of insertion. The blade draws first and the hilt collar covers the seam. This replaces arbitrary image-box positioning and universal percentage cropping.

`data/entropic_forge/sword_attachment_points.json` supplies an individual crop rectangle and source-pixel socket for all ten hilts and twelve blades. Coordinates refer to the original 512px cutouts from the existing Sword ZIP. Hilt rotation is counterclockwise; blade rotation is clockwise. The renderer transforms each socket alongside its pixels. Crops exclude baked blade handles and adjacent fragments in the three contaminated sheet cutouts. The original PNGs and inventory icon paths are unchanged.

`scripts/weapon_snap_preview.gd` prepares the parts at consistent hilt/blade lengths, then fits their combined bounds into the available panel with 18px padding. Both axes use the same scale factor. Resize redraws the complete assembly; neither part is independently stretched to fit the panel. Preview clipping is an additional guard, not the layout mechanism.

The 120 possible Sword pairs are checked at three preview sizes in `tests/sword_socket_smoke.gd`. Assertions cover socket overlap and both part bounds. The Android pipeline runs this check after extracting the Sword ZIP. The optional `--capture` argument creates a twelve-example visual review sheet under `build/` when a rendering display is available.

These are preview attachment points, not character hand sockets or a change to forging stats. Some source cutouts remain rough prototype art; per-part coordinates can be refined independently without changing the renderer.
