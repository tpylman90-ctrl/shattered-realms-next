# Shattered Realms

A clean Godot rebuild of Shattered Realms. The first front-end slice now connects the title screen, approved world atlas, Ravenwood location selection, and Blackthorn arrival preview.

## Project direction

Shattered Realms is a connected-territory fantasy campaign. The player explores a 3D world map, enters detailed territory boards, visits cities built as pre-rendered 2.5D rooms, fights turn-based battles, and discovers separate dungeons.

The campaign begins in Ravenwood, with Blackthorn as the first settlement. The full story opening, character selection, tutorial encounters and playable city walkmesh are subsequent slices. During board development Ravenwood provides direct access to Blackthorn. Ravenford remains a world capital, not the opening city.

## Start

Open `project.godot` in Godot 4.7.2 and run the project (F6 runs only the current scene; use F5 for the complete flow).

1. Choose **Start Campaign** to open the atlas with Ravenwood selected.
2. Select **Blackthorn** to view the arrival scene.
3. Use **Ravenwood**, **World Atlas**, Escape, or Android Back to return.

The atlas supports touch selection, one-finger dragging, pinch zoom, mouse wheel zoom, and visible zoom/fit buttons. The territory dropdown makes every region accessible without precisely tapping the artwork. Other lands show their names and settlements but cannot yet be entered. Settings includes a persistent screen-transition toggle.

This build is a menu and location-access slice, not a playable campaign. Blackthorn is an arrival preview without movement or shop entrances. No board, battle, save-game, or crafting implementation is implied by these screens. The original boot-check scene is retained as a content diagnostic.

## Validation

```sh
godot --headless --editor --path . --quit
godot --headless --path . --script res://tests/front_end_smoke.gd
```

See `docs/front-end.md` for atlas coordinates, asset provenance, and the future board-entry contract.

## Repository rules

- Keep the standalone map builder in its own repository.
- Keep only approved runtime assets here. Source renders, provider payloads, temporary exports, and experiments stay outside the game repository.
- Treat territory, hero, item, encounter, and city definitions as data. Scenes consume stable IDs instead of embedding campaign facts in scripts.
- Make every feature part of the same route: world map → territory → city/dungeon → battle → rewards → campaign state.
- Validate Godot import and headless startup in CI. Add signed Android exports after the first vertical slice is stable.
