# Shattered Realms

A clean Godot rebuild of Shattered Realms. The title screen and approved world atlas lead through Ravenwood to eight connected Blackthorn locations with portrait conversations and a local errand.

## Project direction

Shattered Realms is a connected-territory fantasy campaign. The player explores a 3D world map, enters detailed territory boards, visits cities built as pre-rendered 2.5D rooms, fights turn-based battles, and discovers separate dungeons.

The campaign begins in Ravenwood, with Blackthorn as the first settlement. The full story opening, character selection, tutorial encounters and playable city walkmesh are subsequent slices. During board development Ravenwood provides direct access to Blackthorn. Ravenford remains a world capital, not the opening city.

## Start

Open `project.godot` in Godot 4.7.2 and run the project (F6 runs only the current scene; use F5 for the complete flow).

1. Choose **Start Campaign** to open the atlas with Ravenwood selected.
2. Select **Blackthorn** to enter the fort courtyard.
3. Tap named doors to explore the inn, guest room, militia yard, barracks, captain’s tent, smithy and infirmary. The **Go to…** menu lists each room's exits.
4. Tap a named NPC to talk. A portrait appears beside the text, with selectable conversation topics. Tamsin and Nell offer a small optional bandage-delivery errand.
5. **Journal** tracks the errand and visited rooms. **Markers** hides or shows interaction labels. Escape / Android Back first closes dialogue, then returns to the parent room, then the atlas.

The atlas supports touch selection, one-finger dragging, pinch zoom, mouse wheel zoom, and visible zoom/fit buttons. The territory dropdown makes every region accessible without precisely tapping the artwork. Other lands show their names and settlements but cannot yet be entered. Settings includes a persistent screen-transition toggle.

Blackthorn currently uses point-and-click room exploration. It has real room transitions, branching conversations, inspections, and a small persistent exploration save. Avatar walking, matched 3D walkmeshes, separated foreground occlusion layers, battles, shop transactions and Entropic crafting are not implemented yet. Resting in the guest room is a short pause, not the overnight event that triggers the planned alpha-wolf tutorial. The original boot-check scene remains as a content diagnostic.

## Validation

```sh
godot --headless --editor --path . --quit
godot --headless --path . --script res://tests/front_end_smoke.gd
godot --headless --path . --script res://tests/blackthorn_smoke.gd
```

See `docs/front-end.md` for atlas coordinates, asset provenance, and the future board-entry contract.

## Repository rules

- Keep the standalone map builder in its own repository.
- Keep only approved runtime assets here. Source renders, provider payloads, temporary exports, and experiments stay outside the game repository.
- Treat territory, hero, item, encounter, and city definitions as data. Scenes consume stable IDs instead of embedding campaign facts in scripts.
- Make every feature part of the same route: world map → territory → city/dungeon → battle → rewards → campaign state.
- Validate Godot import and headless startup in CI. Add signed Android exports after the first vertical slice is stable.
