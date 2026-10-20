# Entropic Forge Blender render pipeline

The Blender workflow is a reproducible asset-production step for the Entropic Forge. It currently renders a small Axe-family study: a curved ashwood haft, a forged axe bit with an open socket ring, their assembled 3D preview, a `.blend` scene, and a render manifest. Blender's bundled Python and NumPy build the tapered haft geometry; system NumPy and Pillow verify the output PNGs in CI.

Run locally with Blender installed:

```sh
blender --background --python tools/blender/render_forge_components.py -- --output build/blender-forge
python3 tools/blender/validate_forge_renders.py build/blender-forge
```

GitHub Actions runs the same steps on changes under `tools/blender/` and uploads `EntropicForge-Blender-Axe-Study`. The artifact contains three 1024×1024 transparent PNGs, the source `.blend` scene, and `render_manifest.json`.

## Review gate

These first renders are a technical and visual proof, not catalog replacements. The existing game uses transparent 2D component sprites with per-image socket metadata, and the current Axe mounts use a 97-degree haft orientation, 90-degree striker orientation, 235/155 pixel display lengths, and 18 pixel overlap. Review silhouette, materials, scale, open socket, and attachment alignment before replacing any catalog image or mount record. This workflow does not edit the catalog, gameplay values, Sword calibration, or Android package.

Once the first study is accepted, the generator can expand to the remaining Axe pieces and then other weapon families while retaining a consistent camera, lighting setup, transparent output, and explicit mount points.
