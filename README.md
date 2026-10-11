# Shattered Realms

A clean Godot foundation for Shattered Realms. This repository starts with the agreed architecture and content rules, then grows through small, playable vertical slices.

## Project direction

Shattered Realms is a connected-territory fantasy campaign. The player explores a 3D world map, enters detailed territory boards, visits cities built as pre-rendered 2.5D rooms, fights turn-based battles, and discovers separate dungeons.

The opening campaign direction is Ravenford as the home city and Ravenwood as the first expedition. Ashenreach remains the current visual pilot for the volcanic city method. The Ashenreach work is a reference and style test, not a reason to make the campaign order linear.

## Start

Open this folder in Godot 4.7.2 or newer. The first project scene is an intentionally small boot check; it verifies that the content manifest loads before the first playable slice is built.

## Repository rules

- Keep the standalone map builder in its own repository.
- Keep only approved runtime assets here. Source renders, provider payloads, temporary exports, and experiments stay outside the game repository.
- Treat territory, hero, item, encounter, and city definitions as data. Scenes consume stable IDs instead of embedding campaign facts in scripts.
- Make every feature part of the same route: world map → territory → city/dungeon → battle → rewards → campaign state.
- Validate Godot import and headless startup in CI. Add signed Android exports after the first vertical slice is stable.
