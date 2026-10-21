# Entropic Forge Blender component pipeline

The Blender workflow starts the Axe art rebuild as a modular component library. A selected handle and blade establish the weapon's silhouette, construction, and base materials. A selected core fits at their socket and adds a separate glow or effect layer. The build therefore renders individual parts only; it does not create or export a complete axe.

The first proof contains three standalone handles, six standalone blade heads, three elemental cores, and three effect-only overlays (Cinder, Rime, and Storm). The editable `.blend` source stages every component independently in a grid. Blender's bundled Python and NumPy generate the tapered/curved haft profiles; system NumPy and Pillow verify transparency, dimensions, coverage, anchors, and the component inventory in CI.

Run locally with Blender installed:

```sh
blender --background --python tools/blender/render_forge_components.py -- --output build/blender-forge
python3 tools/blender/validate_forge_renders.py build/blender-forge
```

GitHub Actions runs the same steps on changes under `tools/blender/` and uploads `EntropicForge-Blender-Axe-Components`. The artifact contains fifteen 512×512 transparent RGBA PNGs, the editable component-library `.blend`, and `render_manifest.json`.

## Review gate

These are visual studies, not catalog replacements. The existing game uses transparent 2D component sprites with per-image socket metadata. The current Axe mounts use a 97-degree handle orientation, 90-degree blade orientation, 235/155 pixel display lengths, and 18 pixel overlap. Manifest anchors are initial preview metadata and need calibration against the catalog sprites before integration. Review each silhouette, material, component scale, socket opening, and anchor alignment before replacing catalog images or mount records.

This workflow does not edit catalog entries, recipes, gameplay values, Sword calibration, or the Android package. Core and effect art stays independent of both handle and blade, so the chosen parts control the weapon's look while the core contributes its glow and effects.
