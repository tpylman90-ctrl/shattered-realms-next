# Blackthorn rooms and conversations

## Connected locations

The courtyard connects to the Lantern Inn common room, militia yard, Bram's smithy and Tamsin's infirmary. The inn connects to its upstairs guest room. The militia yard connects to the barracks/supply counter and captain's tent. Every exit has a return route. Escape / Android Back closes the current conversation before leaving a room, then follows the room parent toward the courtyard and atlas.

Six ordinary local NPCs have distinct portrait tiles and branching conversations: Mara (innkeeper), Rowan (captain), Tamsin (healer), Bram (repair smith), Nell (quartermaster), and Eren (gate watch). These are new supporting character names; they do not replace the Ravenwood hero. The captain remains at camp. There is no hero encounter or recruitment in this implementation.

## Interaction and state

`data/cities/blackthorn.json` owns room art, image-relative hotspot positions, exits, inspection text, NPC identities, portrait indices and dialogue graphs. `room_canvas.gd` fits the whole painting without cropping and applies the same transform to hotspots. Doors, NPCs and inspection points can be tapped. The exit dropdown offers an alternate way to travel if markers are hidden.

`blackthorn.gd` presents the room, portrait dialogue, branching choice buttons, journal and nested Back behavior. Portraits are runtime AtlasTexture regions in one six-person sheet, not separate copies of the source texture. Room art is loaded on entry rather than preloading every room.

`blackthorn_state.gd` stores current room, visited rooms, a short-rest flag and errand flags in `user://blackthorn_exploration.cfg`. This is a deliberately small exploration save, separate from the future campaign/combat save. Returning through the atlas resumes the most recent room. The title's Start Campaign button currently enters this prototype; it does not erase exploration progress.

Optional errand: Tamsin asks for a clean bandage bundle. Accepting unlocks Nell's collection dialogue in the barracks. Delivery consumes the bundle and completes the journal entry. Collection and delivery are guarded against duplication. No unimplemented currency, healing or combat reward is claimed. The guest-room rest does not advance the overnight story or trigger the alpha-wolf tutorial.

## Visual scope and provenance

Seven new fixed-perspective room paintings and a six-NPC portrait sheet were created with the built-in image-generation tool. The approved courtyard served as the architecture, material and lighting reference for each room: modest timber, rough stone, warm lantern light, cool ancient forest, no grand castle. The inn and bedroom are warm refuges; the yard, barracks and tent are practical militia spaces; the smithy is an ordinary repair workshop, not an Entropic Forge; the infirmary uses simple cots and herbs. The portraits depict six distinct adult villagers/militia in practical clothes, arranged in a regular 3×2 grid for runtime use.

The room paintings are 1672×941, the portrait sheet 1536×1024. All runtime images are bundled under `assets/art/blackthorn/`. The current implementation is point-and-click; it does not yet implement a walking character, a true 3D walkmesh, or independently occluding painted layers. Those remain the intended city rendering method, not a claim about this room-content slice.

## Validation

The automated Blackthorn check traverses every room exit, checks all dialogue targets and portraits, exercises inspections, completes the errand, verifies collection/delivery guards and tests save/reload without writing the player's actual save. It also checks Back through dialogue → tent → yard → courtyard → atlas. Front-end tests still cover map and touch behavior. Actual Godot-rendered courtyard, inn conversation, captain conversation and healer conversation were visually inspected at 1280×720. Physical Android-device testing and APK packaging remain outside this change.
