# Campaign, hero pairs, and crafting — integration record

Recorded 2026-10-11 from the user's design discussion. This is a specification for future integration, not a claim that these systems are implemented. The existing playable Blackthorn rooms and dialogue are a separate content slice.

## Campaign opening and progression

Start Campaign plays an introduction about a peaceful realm now shattered beneath dark mist and monsters. The fate of its leaders and heroes remains the campaign mystery. “Could you be the one?” leads through a whiteout to preset male/female avatar selection and a basic starter discipline. Preset avatars keep rendering and asset costs controlled.

Ravenwood opens with a forest pan to the player's board piece. Movement instruction leads to a first-creature combat tutorial. Injured, the player follows the road to Blackthorn, a small timber-and-stone fort: dangerous woods outside, modest buildings, hopeful people inside. The local hero is not an early contact. An inn stay precedes an alpha wolf invading the fort; the player and one unit of men fight in the squad tutorial. The captain recognizes the player's leadership and recruits them, but remains a camp NPC and mission turn-in contact. Regional missions provide units, experience and loot. The hero recruitment climax and regional boss establish the player as a leader. After liberation the player chooses among connected territories to reunite the realm.

Each territory has at least five pre-boss quests, some more, from multiple sources. Later stories differ in structure and remain surprises for the player. Liberation ends in the hero and land pledging support. No forced linear territory order. The developer authors cities, dungeons and points of interest; the user authors large 3D territory boards with tile-by-tile pieces, multiple locations, monster spawns and hidden dungeons. Location scenes target painted 2D layers, matched 3D walkmeshes and foreground occlusion.

## Paired hero rule

Thirteen recruitment groups have two heroes each: 26 characters, at most 13 traveling recruits from these groups in one campaign. Mission choices determine which path reaches recruitment. The climax clearly signals commitment before the player chooses. Recruiting one permanently closes the other's recruitment path. The resident counterpart remains an interactive NPC with dialogue, local missions and a permanent territory-defense/recovery role. Both routes liberate the land and earn its allegiance.

Existing hero names are retained. The user supplied the following counterparts and recruitment stories as the working roster. New counterpart identities began as proposals; preserve them for integration without claiming existing character assets or implemented abilities. The 13 recruitment groups are not a claim that the expanded atlas contains only 13 maps. Hero assignments for other atlas lands remain unresolved. The earlier final-boss minimum of nine traveling heroes is not automatically changed by the expanded roster.

| Recruitment group | Hero | Role, appearance and personality | Signature ability |
|---|---|---|---|
| Ravenwood / Blackthorn | Lyra Vane, the Shadow Stalker — female | Ranger/Assassin; dark leather, green hood, bow, paired daggers; quiet, observant, protective | Phantom Arrows strikes marked enemies through concealment |
| Ravenwood / Blackthorn | Garrick Thornward, the Briar Sentinel — male | Ranger/Guardian; broad woodland hunter, bark-patterned armor, patched cloak, spear, reinforced wooden shield; patient, dependable | Briar Stand intercepts attacks and punishes approaching enemies |
| Ashen Wastes / Ashenreach | Ignis, the Magma-Heart — male | Pyromancer/Juggernaut; massive volcanic build, ash-dark skin, blackened armor; direct, stubborn, loyal | Eruption Strike delivers a devastating crushing blow |
| Ashen Wastes / Ashenreach | Veyra Cindervein, the Crucible Keeper — female | Forge Warden/Battle Artificer; powerful basalt-toned figure, copper fittings, heavy smith apron, forge hammer, furnace shield | Crucible Guard absorbs punishment and releases a scorching counterattack |
| Frostpeaks / Icehelm | Vesper, the Frostbinder — female | Cryomancer/Warden; ice-blue armor, heavy fur, long frost staff; composed, exacting, dry humor | Glacial Bastion shelters allies behind ice defenses |
| Frostpeaks / Icehelm | Stellan Rimeborn, the White Wolf — male | Winter Tracker/Skirmisher; weathered face, braids, layered hides, hunting spear, crossbow; warm companion, relentless pursuer | Whiteout Hunt marks prey and enables rapid follow-up attacks |
| Blighted Marsh settlements | Morana, the Rot-Weaver — female | Plague Shaman/Witch; weathered robes, bone charms, medicinal herbs, twisted staff; unsettling, compassionate to outcasts | Venomous Miasma weakens clustered enemies |
| Blighted Marsh settlements | Odran Fenward, the Mire Shepherd — male | Marsh Warden/Restoration Shaman; reed cloak, scars, carved wooden mask, hooked polearm; gentle, practical, hard to frighten | Fen Sanctuary suppresses poison and restores allies within a protective zone |
| Veiled Sea / Silverkeep and Westhaven | Captain Jora Stormtide — female | Naval Commander/Swashbuckler; light pirate armor, single-ended whip-blade, repeater pistol, belt grenades, no shield; daring, irreverent | Tidal Blade sweeps through formations |
| Veiled Sea / Silverkeep and Westhaven | Captain Roran Deepwatch, the Breakwater — male | Marine Commander/Guardian; broad sailor, salt-worn coat, reinforced boarding armor, boarding pike, shield; steady, blunt, devoted to crews | Hold Fast resists displacement and concentrated attacks |
| Drakeshard Range / Ironhold | Dareth Scalebreaker — male | Dragon Slayer/Vanguard; battle scars, rugged scale armor, enormous cleaving blade; fearless, burdened by losses | Draconic Cleave breaks armored targets |
| Drakeshard Range / Ironhold | Kaela Wyrmbound, the Scale Oath — female | Drake Knight/Beast Warden; athletic, overlapping scale armor, lance, bonded drake in signature abilities; resolute, opposes indiscriminate dragon hunting | Wingguard calls her drake to intercept and retaliate |
| Iron Plains / Harrowstead | General Cedric Ironclad — male | Heavy Cavalry Commander; exceptionally broad, imposing chest armor, veteran bearing; disciplined, protective, distrusts shortcuts | Phalanx Charge coordinates a crushing advance |
| Iron Plains / Harrowstead | Marshal Adela Steelwind — female | Mobile Cavalry Commander/Tactician; tall, lean, riding armor, short cloak, cavalry saber, lance; decisive, adaptable | Wheeling Assault hits flanks and repositions allies |
| Ember Coast / Dragon's Rest | Ignacia, Flame of the Coast — female | Dragon Tamer/Sorceress; crimson clothes, dragon-scale chest armor, ornate staff; charismatic, proud, attached to her dragons | Dragon Breath unleashes a sweeping elemental attack |
| Ember Coast / Dragon's Rest | Tavian Ashsail, the Cinder Corsair — male | Coastal Skirmisher/Fire Alchemist; sun-weathered skin, dark curls, scorched captain coat, curved boarding blade, fire vessels; inventive, mischievous | Cinderwake lays a burning trail that disrupts movement |
| Stormcrown Mountains / Stormcrown Keep | Thorvald Thunderbrow, the Peak Sentinel — male | Tempest Warrior/Smith; heavy beard, formidable build, storm-forged armor, massive hammer; gruff, generous, devoted craftsman | Lightning Smash delivers a thunderous impact |
| Stormcrown Mountains / Stormcrown Keep | Eydis Stormweaver, the Sky Warden — female | Tempest Lancer/Runesmith; silver-dark braids, etched armor, metal-shod spear; thoughtful, ambitious, fascinated by ancient machinery | Storm Conduit links targets with successive lightning strikes |
| Ravenford and Eldergrove | Sir Alistair of Ravenford — male | Knight/Guardian; engraved steel chest armor, weathered heraldry, longsword, shield; principled, questions inherited authority | Oathkeeper's Stand draws pressure and protects wounded allies |
| Ravenford and Eldergrove | Dame Elowen Rootsworn — female | Grove Knight/Nature Warden; leaf-etched chest armor, practical green clothing, long glaive; candid, protective of woodland communities | Rootbound Aegis restrains attackers and strengthens nearby allies |
| Golden Expanse / Sunspire | Zephyr, the Mirage Blade — male | Desert Duelist/Illusionist; sand wraps, bronze armor, wind-worn scarf, paired curved blades; playful, elusive, secretly dutiful | Mirage Dance delivers repeated deceptive strikes |
| Golden Expanse / Sunspire | Samira Dawnwatch, the Sunshield — female | Desert Guardian/Solar Warden; bronze chest armor, indigo cloth, headscarf, spear, round shield; patient, commanding, protective of travelers | Dawnwall shields allies and counters hostile magic |
| Cursed Mire and Deadwind Hollow — two linked maps | Malakor, the Soul Reaper — male | Soul Knight/Reaper; aged black armor, tattered robes, long reaping weapon; grim, respectful of the dead | Soul Harvest converts defeated enemies' lingering essence into combat strength |
| Cursed Mire and Deadwind Hollow — two linked maps | Sereth Veilkeeper, the Last Lantern — female | Spirit Warden/Exorcist; pale travel robes, tarnished chest armor, funerary lantern, ritual sword; calm, compassionate, unyielding toward spirit enslavers | Last Light disrupts undead and wards allies against curses |
| Copperfen Basin / tinkerer homeland | Tessa Brasswick, the Shardshot — female, proposed name | Scrap Artificer/Cannon Specialist; adult auburn-haired woman, goggles, cropped leather workwear, shorts, tools, custom cannon; bold, witty, experimental | Fracture Salvo consumes a cracked weapon to fire a shot shaped by its properties |
| Copperfen Basin / tinkerer homeland | Tobin Rivetlock, the Patchwork Bastion — male | Combat Engineer/Construct Warden; stocky adult, untidy dark hair, brass spectacles, reinforced workwear, mechanical support harness; methodical, dry humor, protective | Last-Chance Payload consumes a cracked weapon in a single-use trap or defensive burst |

### Recruitment paths and resident duties

1. Ravenwood: Lyra pursues enemy scouts and their commander; Garrick rescues isolated families and breaks the siege. The resident commands woodland defenses. Both paths must respect the controlled opening/tutorial sequence and late hero introduction.
2. Ashen Wastes: Ignis destroys the attack source; Veyra restores foundries and defends evacuation routes. The resident protects people and industry.
3. Frostpeaks: Vesper seals an ancient breach beneath Icehelm; Stellan recovers missing patrols in blizzards and kills their pursuer. The resident guards the passes.
4. Blighted Marsh: Morana turns corruption against its creators; Odran cleanses water and recovers endangered settlements. The resident maintains safe marsh routes.
5. Veiled Sea: Jora seizes the enemy flagship; Roran escorts refugees and breaks the blockade. The resident commands coastal defense.
6. Drakeshard: Dareth hunts a corrupted elder drake; Kaela destroys what drives the brood mad. The resident safeguards Ironhold and its approaches.
7. Iron Plains: Cedric holds the main battle line and defeats the invading army; Adela frees villages and cuts its supplies. The resident commands Harrowstead's army.
8. Ember Coast: Ignacia protects nesting grounds and restores the dragon pact; Tavian destroys raiders and recovers stolen eggs. The resident protects Dragon's Rest and the coast.
9. Stormcrown: Thorvald reclaims the ancestral forge; Eydis restores failing storm wards. The resident maintains keep, forge and defenses.
10. Ravenford/Eldergrove: Alistair exposes betrayal and restores city defenses; Elowen saves sacred sites and reconciles divided protectors. The resident safeguards the reunited territory.
11. Golden Expanse: Zephyr infiltrates Sunspire's exploitative rulers; Samira restores wells and defends caravans. The resident secures city and crossings.
12. Linked curse: Malakor seizes and destroys the necromancer's instruments; Sereth releases the bound dead and consecrates burials. The resident guards both lands against the curse's return.
13. Copperfen: Tessa recovers stolen experiments and dismantles saboteurs; Tobin rebuilds defenses and withstands their assault. The resident becomes chief defensive engineer. Copperfen settlements: Cogspire and Rivetbank; proposed race name Kettari.

## Cursed Mire / Deadwind Hollow: confirmed shared liberation

These remain TWO SEPARATE MAPS. An ancient curse already held them before the rise of the great beast. Its newer darkness feeds on and strengthens that older curse. The story progressively reveals why defeating present-day servants alone cannot free the lands.

Investigation and missions move between the two maps: discovering the curse's origins, breaking its anchors, and learning how the lands sustain each other's suffering. Local progress weakens the darkness, but neither map can count as fully liberated until BOTH are freed. They share a liberation climax and Malakor/Sereth recruitment decision. The remaining hero watches over both. Do not collapse their map IDs or prematurely grant one a final liberated state. Exact curse origin, quest details, anchors and final encounter remain to be authored; do not reveal future surprises prematurely.

## Entropic Forge: confirmed system direction

### Three-part assembly

- Framework (grip/haft): weapon class, animation rig, attack speed and handling.
- Striker (blade/head): physical geometry, physical damage and slash/pierce/blunt type.
- Entropic Core (catalyst): territory-sourced elemental power and environmental effects (magma, void, ash, etc.), with correct scene depth/occlusion.
- Components assemble into one localized object attached to a 3D skeletal socket. Reuse base meshes and dynamic albedo/normal materials for memory efficiency.

### Hidden strikes

Every material combination has a hidden Strike Limit. Under-striking produces less physical attack and converts unused potential into extra durability. Exact striking produces a Masterwork with exponential attack multipliers, reaching 175% in the volatile ten-strike case. Over-striking creates a Cracked weapon: greatly reduced durability but increasing elemental leakage/effects per extra strike. Three crafting skill tiers add +1, +2, +3 to the hidden base limit; exact cap interaction and formulas still need definition.

There are no UI or sensory warnings before crossing the breaking point. Cracks become visible only after over-striking. Cracked weapons show no remaining durability number or bar, and no escalating countdown cues to predict their terminal attack. Uncracked durability presentation is not otherwise specified. Whether ordinary strike count is shown has not been explicitly settled.

A cracked weapon reaching zero durability during an offensive attack creates a massive elemental terminal burst that damages enemies AND the player's party. Hidden remaining life prevents reliable timing of the final ordinary attack. Destroyed weapons leave Core Shards (fusable into whole cores) and degraded base materials such as Warped Metal and Charred Wood. Exact damage, durability, salvage and fusion formulas remain open.

Tinkerers learn specialized ways to consume cracked weapons as one-use ordnance. Tessa's cannon launches the weapon and detonates it at impact; Tobin uses a deployable trap/defensive device. The weapon is permanently consumed, retains its elemental identity, and remains dangerous to nearby allies. Exact scaling, resource costs and salvage eligibility for launched weapons/devices remain open. Learned abilities/personal quests should support this specialization.

### Forge geography and optional crafting questline

Entropic Forges exist only where culture and industry justify them, not in every settlement. Ashenreach, Stormcrown, Ironhold and Dragon's Rest were proposed normal forge locations. Blackthorn has an ordinary repair smith, not an Entropic Forge.

Mistvale has an ancient relic forge OUTSIDE its city. An optional crafting-focused discovery/restoration quest unlocks it and adds 10% damage to weapons built there. Its clues lead through more quests to the last and greatest forge, hidden in the Golden Expanse's sands. That forge raises the maximum Masterwork multiplier from 175% to 200%; its ancient benefit replaces rather than stacks with Mistvale's bonus. Correct components and perfect striking remain necessary. Exact reference value/order of operations for Mistvale's 10% needs balancing.

Ancient energy restructures the weapon at an atomic level, as pressure creates a diamond. It transforms odd dark metal with blue energy into a smooth, hard, clean silver-and-gold finish with bright yellow static bolts. Core elemental effects remain. This is material transformation, not a cosmetic coating. A fractured perfected weapon leaks exceptionally concentrated power and is powerful, dangerous and deadly; hidden durability still applies. Visual progression should communicate forge origin and cracked state without giving pre-crack warnings or a remaining-life countdown.

### Discovery and recipes

An empty crafting ledger is acquired early. Permanent long-haul delivery side quests between cities reward recipe pages. Pages reveal hidden strike capacities and specific material harvest locations. Unknown values can be deduced through experimentation. The system must support organic exploration, player knowledge and travel rather than exposing all secrets in the crafting UI.

## New crafting requirement, 2026-10-11

Create a LARGE library of discoverable components, supporting many new craftable weapons beyond the existing weapons available as loot or purchases. Preserve found and purchased equipment as valid parts of the game. Component counts, compatible families, specific catalog entries, rarity distribution, economy, blueprints and balance are the next design discussion; do not treat proposed numbers as approved implementation.


## Crafting catalog and courier continuation — 2026-10-11

The user confirmed that the optional courier storyline unlocks the great forges. It includes gathering across the world before delivery and other mission types, rather than only point-to-point deliveries. The ancient recipe book is received on accepting the first assignment; permanent commissions progressively supply its missing pages. Mistvale should feel like the final discovery. Only its first completed forge use makes the book respond to the relic magic and reveal a new map, beginning the journey into the sands. Do not expose the desert chapter earlier in a player-facing quest list.

The requested extensive crafting list is now authored as a balance proposal in [the crafting design library](../crafting/README.md): 200 assembly components, 36 gathering stocks, 96 salvage definitions and 180 named recipes across 15 families. Exact formulas, values, quests and new names remain proposed until playtested; this does not retroactively mark previously open numerical choices as user-confirmed. The reference evaluator and structured data are not integrated into game inventory or combat.
