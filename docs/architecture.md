# Architecture and shared direction

## Player journey

The complete campaign uses one consistent route:

1. **World map:** connected territories, campaign pressure, army movement, fog, and unlock state.
2. **Territory board:** detailed regional terrain with one authoritative board definition driving both rendering and movement rules.
3. **City or dungeon:** cities are compact 2.5D rooms; dungeons are separate exploration spaces.
4. **Battle:** turn-based ATB combat, then rewards and campaign-state updates.

The world map, territory board, and city/dungeon scenes are distinct views of the same campaign state. They do not maintain parallel copies of progress.

## Visual methods

- **World map:** readable sculpted overview with subtle POI markers and labels shown on selection.
- **Territory boards:** large detailed 3D game boards, with characters represented by 3D pieces moving tile by tile. Board data owns cells, elevations, terrain, hazards, obstacles, roads, rivers, bridges, cliffs, connections, several locations, monster spawn points, and hidden dungeons. The user authors boards in the separate builder.
- **Cities:** fixed camera matched to hand-painted backgrounds. Use 2D painted plates, a true 3D walkmesh, perspective-scaled characters, and separate foreground occlusion layers. Ashenreach is the current method pilot: obsidian basalt, black iron, lava light, and one room at a time.
- **Battles:** high-resolution region-specific painted arenas with 3D combatants and clear ground contact.

## Campaign and combat rules

- The campaign opens in Ravenwood and teaches board movement and the first creature encounter before arrival in Blackthorn. An inn stay precedes the alpha-wolf squad tutorial. The captain stays at camp as the mission contact; the regional hero joins at the boss stage. Later connected territories can be approached in different orders; do not force a linear campaign.
- Only author a territory edge when its connection is established. The current scaffold intentionally leaves undocumented route edges unmapped. Reconnecting a territory opens neighboring routes. Enemy pressure can reclaim unsecured territory; garrisons protect holdings.
- Encounters scale with party progress while retaining regional level floors, elites, and apex threats.
- A battle party consists of the hero and up to four army units. Command position is front, middle, or rear. Only the active unit shows a hollow selection ring.
- The final Devouring Deep encounter is a three-stage fight that asks the player to field at least nine heroes, three per stage.
- Equipment has a base effect plus tag-based archetype, elemental, tactical, and optional signature-hero synergies. Equipment is not hero-locked. Weapons occupy right- and left-hand slots; a one-hand-two-handed exception is a data-driven hero trait.

## First vertical slice

Build one thin, fully connected experience before broad content production:

- Boot and campaign state load from validated catalogs.
- Reach a territory from the world map.
- Explore a small Ravenwood territory board and reveal a landmark.
- Enter a short Blackthorn city room with a real walkmesh.
- Trigger one encounter, complete the battle, receive a reward, and save it.
- Return to the world map with territory and inventory state intact.

Ashenreach remains the current city-art pilot; it is not a forced first stop in the story.
