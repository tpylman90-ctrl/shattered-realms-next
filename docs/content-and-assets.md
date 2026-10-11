# Content and asset rules

## Source of truth

Every runtime object has a stable ID and one authored definition. Scenes render data; they do not own duplicated campaign facts.

- Territory catalogs define connections, level ranges, city, dungeon, and regional theme.
- Board definitions drive both terrain visuals and traversable cells.
- Hero definitions own progression, role tags, signature ability, and traits.
- Equipment definitions own slots, base effect, and tag-based synergies.
- Encounter definitions own roster, threat band, terrain hooks, and rewards.

## Asset intake

Only reviewed, optimized, game-ready assets enter runtime folders. Keep source renders and experiments outside the game repository.

Each admitted asset gets a manifest entry with a stable asset ID and path, content type and target scene, dimensions or mesh format, license/source note, import settings, and intended scale.

Use clear folders: assets/runtime/{boards,cities,battle,characters,ui,audio} and assets/manifests. Never store base64 chunks, duplicate exports, test captures, editor caches, or build outputs under runtime assets.

## Art acceptance

- **City plates:** path composition is designed before adding walkmesh points. Foreground masks and depth cards are separate layers.
- **Characters:** feet touch the walk surface; apparent height follows camera depth.
- **Boards:** soil, sand, snow, lava, rock, and vegetation have distinct shape and surface response, not color-only variants.
- **Props:** silhouettes read at normal zoom; added detail remains useful at close zoom and does not change traversal unless authored in board data.
