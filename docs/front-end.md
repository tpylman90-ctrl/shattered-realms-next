# First front-end slice

## Scope

Title → Start Campaign → World Atlas → Ravenwood → Blackthorn courtyard and connected rooms.

Blackthorn now supports point-and-click exploration and portrait dialogue. There is no invisible walking, dead joystick, or placeholder block character. A later movement slice will add the matched fixed camera, actual 3D walkmesh, avatar, and separate foreground masks. The opening cinematic and avatar selection are not implemented yet. See `blackthorn.md` for the room and interaction implementation.

## Board handoff

The user owns territory-board authoring in the separate builder. This repository owns cities, dungeons, points of interest and the front end. Territory boards will be large 3D spaces with pieces moving tile by tile, multiple locations, multiple monster spawn points and hidden dungeons. Explorable locations use painted layers with matched 3D movement and occlusion.

`open_location("blackthorn")` is the current direct-entry seam. When the Ravenwood board is ready, it can call this same location entry using a stable ID; no atlas screen coordinates should be used for world movement. `board_scene` is null in the territory definitions until a real board scene is supplied. No connections or new campaign unlock order have been invented.

## Atlas

`data/campaign/atlas.json` is presentation data: normalized polygons and markers on the approved map, descriptions and public settlement names. It includes 18 selectable lands, including the three approved additions and previously unlisted southern/endgame lands. Polygons are approximate selection areas, not exact borders, navigation meshes, or territorial ownership cells. Secret dungeon and ancient forge positions are not exposed.

`scripts/atlas_view.gd` uses one image rectangle for rendering and hit-testing at every zoom level. Zoom is focal-point anchored and limited to 1–3.5x. Panning is clamped to the image bounds. A pinch suppresses tap selection through the final finger release. Mouse-emulated touch is ignored in the atlas, while standard Godot buttons retain normal mobile input. The region picker is an accessible alternate selection path.

## Assets and provenance

- `assets/art/world_atlas.png`: user-approved revised world map generated in this conversation, 1536×1024. The embedded labels remain artwork; selecting a region displays live readable text. Enlarging the canvas does not imply new source detail.
- `assets/art/blackthorn_arrival.png`: generated with the built-in image tool for this slice. The same plate supports title and arrival views to avoid redundant texture memory. It is a new scene, not carried over from the legacy game.
- `assets/fonts/DejaVuSerif.ttf`: bundled with its license in `assets/fonts/LICENSE.txt`.

Blackthorn art prompt: a realistic pre-rendered JRPG background viewed just inside a small timber-and-stone frontier fort, threatening ancient woods beyond the palisade, modest timber keep, warm inn on the left, militia camp on the right, a clear central walking courtyard, fixed elevated perspective, detailed materials and grounded shadows; no text, UI, people, grand castle, lava, or low-poly placeholders.

The image files are runtime assets in the repository; they do not depend on temporary generated-image paths.

## Tests

`tests/front_end_smoke.gd` exercises actual scene navigation, every region's marker hit, transformed map selection, camera retention, invalid locations, single-touch and pinch-release behavior, viewport reflow, and settings close/back. CI also imports the project and smoke-starts the main scene. Android packaging and physical-device performance testing are not included in this slice.
