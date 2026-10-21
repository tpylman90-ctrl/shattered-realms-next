# Entropic Forge Blender component pipeline

The Axe art pipeline uses **four reusable handle archetypes and four reusable head archetypes**. Existing Axe catalog pieces derive from those bases through small, controlled changes to material palette, width, fittings, engraved relief, and grip treatment. The four handle bases are split oak, iron bracing, furnace haft, and organic hook. The four head bases are bearded, crescent, double bit, and hooked.

This gives the catalog consistent construction and attachment proportions while keeping the editable Blender source manageable: the 10 hafts and 12 heads share only eight base mesh datablocks, with per-variant material overrides and small detail pieces. The current proof renders every original and expansion Axe catalog part. Cores and effect overlays remain independent assets: the selected handle and head define the weapon's shape; the core adds the elemental glow/effects. The generator never renders a complete axe.

The editable `.blend` contains the 28 standalone catalog parts arranged in a review grid. Blender's bundled Python and NumPy generate the curved/tapered haft meshes; raised ferrules now wrap the haft axis, with archetype-specific grip channels, braces, vents, grain crests, embossed grip badges, and organic ridges. Heads use a taller grouped profile, inset face plates, open socket sleeves, raised silhouette bindings, and distinct bearded, crescent, double-bit, and hooked relief. Forged metal, wood, and leather materials use procedural color and surface variation. The preview camera and softer AgX lighting reveal component depth while preserving transparent PNG output. System NumPy and Pillow verify transparency, dimensions, coverage, anchors, and archetype counts in CI, then create a labeled sheet of isolated parts.

Run locally with Blender installed:

```sh
blender --background --python-exit-code 1 --python tools/blender/render_forge_components.py -- --output build/blender-forge
python3 tools/blender/validate_forge_renders.py build/blender-forge
```

GitHub Actions runs the same steps on changes under `tools/blender/` and uploads `EntropicForge-Blender-Axe-Components`. The artifact contains 28 standalone 512×512 transparent RGBA PNGs (10 handles, 12 heads, 3 cores, and 3 effect overlays), a labeled contact sheet, the editable component-library `.blend`, and `render_manifest.json`.

## Review gate

These are visual studies, not catalog replacements. The latest pass fixes the haft ferrule orientation and increases raised sculptural detail, but still needs visual review against the attached reference art before any catalog replacement. The current game uses transparent 2D component sprites with per-image socket metadata. Existing Axe mounts use a 97-degree handle orientation, 90-degree head orientation, 235/155 pixel display lengths, and 18 pixel overlap. Manifest anchors reflect the current Blender sockets and still need in-engine calibration before integration. Review silhouette, detail readability at inventory size, socket fit, and consistency with the attached fantasy artwork before replacing catalog images or mount records.

This workflow does not edit catalog entries, recipes, gameplay values, Sword calibration, or the Android package. The four archetypes are a source-authoring and visual-consistency strategy; final PNG bytes still contribute to game size, so output dimensions and compression should be profiled before full catalog import.
