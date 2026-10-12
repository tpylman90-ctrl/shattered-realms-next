# Expanded component refinement — 2026-10-11

Update 2026-10-12: six additional Sword blade images installed (14 total, 176 pending). All 15 families now use catalog-art socket assembly. The historical details below describe the initial pass; see `weapon-family-assembly.md` for the current renderer.

## Completed

- Refined all 100 added frameworks and 90 added strikers using original family speed/attack scales and defined numerical trade-offs.
- Replaced undefined stability/weight and ambiguous control bonuses with explicit accuracy, durability, speed, elemental, reach or bounded status effects.
- Preserved all original 140 physical component records, all 60 cores, all 180 named discoveries, and existing Sword snap images/logic.
- Generated eight individual transparent inventory icons using built-in image_gen; normalized them to 512 × 512 PNG.
- Replaced the generic concept marker with TEMP ART only on the 182 entries still using shared imagery.

## New tab artwork

- Ravenwood Thornhook
- Ashen Emberguard
- Icehelm Splitguard
- Harbor Basket Hilt
- Mirebone Fanggrip
- Stormcrown Coil Hilt
- Ironhold Bastion Grip
- Volcanic Furnace Tang

## Remaining work

The image service returned usage_limit_reached. 182 icons remain: 92 frameworks and 90 strikers. Do not call the full art set complete. Exact prompts and paths are persisted in `data/entropic_forge/component_art_jobs.json`. The CLI image-generation fallback requires explicit user choice and an API key; it was not used.

## Design and integration boundaries

The new numeric values are balance proposals, not playtested results. Expanded records now include structured mechanics alongside display descriptions, but production forging/combat formulas are still unconnected for unnamed assemblies. The physical/elemental traits use the installed core; a regional name or visual material does not force the weapon element.

Inventory illustrations are not automatically reusable snap sprites. No component socket, assembly crop or result-screen join has been changed. Original selection art remains attached to original items. Each completed replacement has a unique path; the existing artwork ZIP cannot overwrite it.

To apply later approved icons, add their PNGs at the queue paths and rerun `python tools/refine_expanded_components.py --allow-pending-art`. Omit the flag when all 190 images exist to require completeness. Then run `python tools/verify_forge_art.py` after restoring the original artwork pack.
