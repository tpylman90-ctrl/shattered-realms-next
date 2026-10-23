# Entropic Forge — component and weapon catalog

**Balance draft 0.1.0 — designer spoilers. These values are proposed and have not been playtested.**

200 components: 50 frameworks, 90 strikers, 60 cores. 36 gathering stocks support component shaping. 15 families allow 18,000 legal assemblies; the 180 named recipes below are discoveries within that space, not the only allowed combinations.

Gold appraisal is not guaranteed merchant availability. A dash in buy price means not sold. Hidden strike contributions and recipe contents belong in the ancient book only when their pages are earned. Full sources, shaping quantities, effect definitions and every forging state are included in the JSON data.

## Sword components

Hands: 1. Tags: Vanguard, Guardian. Elemental coefficient: 1.0. Base reach: 1.5 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Watchman’s Leather Grip | 1 | 45 / 45 / 11 | 1 | 55 | 1.8 s | +5 accuracy points. |
| Duelist’s Tideguard | 3 | 180 / 180 / 45 | 2 | 70 | 1.636 s | +10% action speed; -2 accuracy; -10% durability. |
| Sentinel’s Ironbark Hilt | 4 | 360 / — / 90 | 3 | 85 | 1.895 s | +25% durability; -5% action speed. |
| Sunbound Filigree Hilt | 5 | 660 / — / 165 | 3 | 100 | 1.8 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Plainsteel Straight Blade | 1 | 55 / 55 / 14 | 1 | 20 slash | 20 | +3 accuracy points. |
| Serrated Fang Blade | 2 | 100 / 100 / 25 | 2 | 27 slash | 24 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Tidebronze Saber Blade | 3 | 190 / 190 / 48 | 2 | 35 slash | 30 | +8% physical attack; -0.2 m reach. |
| Webglass Needle Blade | 3 | 220 / 220 / 55 | 3 | 33 slash | 18 | +6 critical chance points; -8% physical attack. |
| Scaleiron Falchion Blade | 4 | 390 / — / 98 | 3 | 46 slash | 38 | Ignore 10% of physical armor for this hit. |
| Veil-Silver Channel Blade | 5 | 700 / — / 175 | 4 | 58 slash | 28 | +12% elemental attack; -6% physical attack. |

## Greatsword components

Hands: 2. Tags: Heavy, Vanguard. Elemental coefficient: 1.5. Base reach: 2.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Militia Longgrip | 1 | 45 / 45 / 11 | 1 | 55 | 3.333 s | +8 accuracy; +10% durability; -10% action speed. |
| Drakespine Wargrip | 3 | 180 / 180 / 45 | 2 | 70 | 3.158 s | +0.4 m reach; -3 accuracy; -5% action speed. |
| Black Anvil Twohander | 4 | 360 / — / 90 | 3 | 85 | 3.0 s | +22% elemental attack; -4 accuracy; -20% durability; no hidden-life hint. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Broad Militia Blade | 1 | 55 / 55 / 14 | 1 | 34 slash | 20 | +3 accuracy points. |
| Notched Siege Blade | 2 | 100 / 100 / 25 | 2 | 46 slash | 24 | +25% direct damage against barriers only. |
| Drakebone Cleaver | 3 | 190 / 190 / 48 | 2 | 60 slash | 30 | One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc. |
| Basalt Execution Blade | 3 | 220 / 220 / 55 | 3 | 56 slash | 18 | 15% chance to remove 6 ATB points; once per target action. |
| Froststeel Flamberge | 4 | 390 / — / 98 | 3 | 78 slash | 38 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Null-Edge Colossus Blade | 5 | 700 / — / 175 | 4 | 99 slash | 28 | Physical attack -12%; elemental attack +20%. |

## Dagger components

Hands: 1. Tags: Skirmisher, Precision. Elemental coefficient: 0.6. Base reach: 0.9 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Poacher’s Thumbgrip | 1 | 45 / 45 / 11 | 1 | 55 | 1.05 s | +5 accuracy points. |
| Websilk Loop Grip | 3 | 180 / 180 / 45 | 2 | 70 | 0.955 s | +10% action speed; -2 accuracy; -10% durability. |
| Mirage Balanced Tang | 4 | 360 / — / 90 | 3 | 85 | 1.05 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Watchman’s Point | 1 | 55 / 55 / 14 | 1 | 12 pierce | 20 | +3 accuracy points. |
| Hollow Adder Fang | 2 | 100 / 100 / 25 | 2 | 17 pierce | 24 | Physical attack -12%; elemental attack +20%. |
| Glasswind Stiletto | 3 | 190 / 190 / 48 | 2 | 22 pierce | 30 | +6 critical chance points; -8% physical attack. |
| Barbed Webglass Point | 3 | 220 / 220 / 55 | 3 | 20 pierce | 18 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Belliron Ritual Blade | 4 | 390 / — / 98 | 3 | 29 pierce | 38 | +20% physical damage against undead; no effect on other targets. |
| Star-Slate Crescent | 5 | 700 / — / 175 | 4 | 36 pierce | 28 | +12% elemental attack; -6% physical attack. |

## Spear components

Hands: 2. Tags: Guardian, Precision. Elemental coefficient: 1.05. Base reach: 3.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Ranger’s Ash Haft | 1 | 45 / 45 / 11 | 1 | 55 | 2.316 s | +0.4 m reach; -3 accuracy; -5% action speed. |
| Rimepine Lance Shaft | 3 | 180 / 180 / 45 | 2 | 70 | 2.316 s | +25% durability; -5% action speed. |
| Stormkeeper Spear Haft | 4 | 360 / — / 90 | 3 | 85 | 2.2 s | +15% elemental attack; -15% durability. |
| Oathroot Longshaft | 5 | 660 / — / 165 | 3 | 100 | 2.444 s | +8 accuracy; +10% durability; -10% action speed. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Iron Leaf Spearhead | 1 | 55 / 55 / 14 | 1 | 24 pierce | 20 | +3 accuracy points. |
| Wyrmtooth Pikehead | 2 | 100 / 100 / 25 | 2 | 32 pierce | 24 | Ignore 10% of physical armor for this hit. |
| Sunbronze Winged Head | 3 | 190 / 190 / 48 | 2 | 42 pierce | 30 | +6 critical chance points; -8% physical attack. |
| Stormsteel Fork | 3 | 220 / 220 / 55 | 3 | 40 pierce | 18 | +12% elemental attack; -6% physical attack. |
| Froststeel Lance Tip | 4 | 390 / — / 98 | 3 | 55 pierce | 38 | +25% direct damage against barriers only. |
| Hollow Veil-Silver Point | 5 | 700 / — / 175 | 4 | 70 pierce | 28 | Physical attack -12%; elemental attack +20%. |

## Axe components

Hands: 1. Tags: Vanguard, Heavy. Elemental coefficient: 1.0. Base reach: 1.4 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Woodcutter’s Haft | 1 | 45 / 45 / 11 | 1 | 55 | 2.211 s | +25% durability; -5% action speed. |
| Corsair’s Hook Haft | 3 | 180 / 180 / 45 | 2 | 70 | 1.909 s | +10% action speed; -2 accuracy; -10% durability. |
| Cinderbrace Split Haft | 4 | 360 / — / 90 | 3 | 85 | 2.1 s | +22% elemental attack; -4 accuracy; -20% durability; no hidden-life hint. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Forester’s Axe Bit | 1 | 55 / 55 / 14 | 1 | 24 slash | 20 | +3 accuracy points. |
| Raider’s Hook Bit | 2 | 100 / 100 / 25 | 2 | 32 slash | 24 | One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc. |
| Drakeglass Bearded Edge | 3 | 190 / 190 / 48 | 2 | 41 slash | 30 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Bog-Iron Hewing Head | 3 | 220 / 220 / 55 | 3 | 39 slash | 18 | Ignore 10% of physical armor for this hit. |
| Basalt Double Bit | 4 | 390 / — / 98 | 3 | 54 slash | 38 | 15% chance to remove 6 ATB points; once per target action. |
| Star-Slate Crescent Bit | 5 | 700 / — / 175 | 4 | 68 slash | 28 | +6 critical chance points; -8% physical attack. |

## Hammer components

Hands: 2. Tags: Heavy, Control. Elemental coefficient: 1.5. Base reach: 1.7 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Quarryman’s Haft | 1 | 45 / 45 / 11 | 1 | 55 | 3.556 s | +8 accuracy; +10% durability; -10% action speed. |
| Siegebreaker Shock Haft | 3 | 180 / 180 / 45 | 2 | 70 | 3.368 s | +25% durability; -5% action speed. |
| Thunderbrow Pattern Haft | 4 | 360 / — / 90 | 3 | 85 | 3.2 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Quarry Iron Block | 1 | 55 / 55 / 14 | 1 | 37 blunt | 20 | +3 accuracy points. |
| Siege Ram Head | 2 | 100 / 100 / 25 | 2 | 50 blunt | 24 | +25% direct damage against barriers only. |
| Resonant Belliron Head | 3 | 190 / 190 / 48 | 2 | 65 blunt | 30 | 15% chance to remove 6 ATB points; once per target action. |
| Basalt Furnace Head | 3 | 220 / 220 / 55 | 3 | 61 blunt | 18 | Physical attack -12%; elemental attack +20%. |
| Scaleiron Shatter Head | 4 | 390 / — / 98 | 3 | 85 blunt | 38 | Ignore 10% of physical armor for this hit. |
| Singing-Quartz Impact Head | 5 | 700 / — / 175 | 4 | 107 blunt | 28 | +12% elemental attack; -6% physical attack. |

## Mace components

Hands: 1. Tags: Guardian, Control. Elemental coefficient: 1.0. Base reach: 1.3 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Gateward Handle | 1 | 45 / 45 / 11 | 1 | 55 | 2.05 s | +5 accuracy points. |
| Reedbound Cudgel Haft | 3 | 180 / 180 / 45 | 2 | 70 | 2.158 s | +25% durability; -5% action speed. |
| Lanternkeeper Flanged Grip | 4 | 360 / — / 90 | 3 | 85 | 2.05 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Gatewatch Iron Ball | 1 | 55 / 55 / 14 | 1 | 22 blunt | 20 | +3 accuracy points. |
| Thorn-Cage Head | 2 | 100 / 100 / 25 | 2 | 30 blunt | 24 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Sunbronze Flanged Head | 3 | 190 / 190 / 48 | 2 | 39 blunt | 30 | Ignore 10% of physical armor for this hit. |
| Hexstone Knob | 3 | 220 / 220 / 55 | 3 | 37 blunt | 18 | +20% physical damage against undead; no effect on other targets. |
| Froststeel Crown | 4 | 390 / — / 98 | 3 | 52 blunt | 38 | 15% chance to remove 6 ATB points; once per target action. |
| Veil-Silver Lantern Cage | 5 | 700 / — / 175 | 4 | 65 blunt | 28 | +12% elemental attack; -6% physical attack. |

## Staff components

Hands: 2. Tags: Caster, Control. Elemental coefficient: 1.7. Base reach: 2.2 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Herbalist’s Bogroot Staff | 1 | 45 / 45 / 11 | 1 | 55 | 2.632 s | +25% durability; -5% action speed. |
| Gloamwood Channel Staff | 3 | 180 / 180 / 45 | 2 | 70 | 2.5 s | +15% elemental attack; -15% durability. |
| Veil-Silver Casting Shaft | 4 | 360 / — / 90 | 3 | 85 | 2.273 s | +10% action speed; -2 accuracy; -10% durability. |
| Astral Spiral Staff | 5 | 660 / — / 165 | 3 | 100 | 2.5 s | +22% elemental attack; -4 accuracy; -20% durability; no hidden-life hint. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Carved Root Crown | 1 | 55 / 55 / 14 | 1 | 12 blunt | 20 | +3 accuracy points. |
| Marsh-Bone Focus | 2 | 100 / 100 / 25 | 2 | 17 blunt | 24 | Physical attack -12%; elemental attack +20%. |
| Storm Fork Crown | 3 | 190 / 190 / 48 | 2 | 22 blunt | 30 | +12% elemental attack; -6% physical attack. |
| Moon Lens Cradle | 3 | 220 / 220 / 55 | 3 | 20 blunt | 18 | +6 critical chance points; -8% physical attack. |
| Hexstone Ritual Cage | 4 | 390 / — / 98 | 3 | 29 blunt | 38 | +20% physical damage against undead; no effect on other targets. |
| Prismatic Silver Crown | 5 | 700 / — / 175 | 4 | 36 blunt | 28 | +25% direct damage against barriers only. |

## Wand components

Hands: 1. Tags: Caster, Precision. Elemental coefficient: 1.15. Base reach: 6.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Apprentice’s Yew Handle | 1 | 45 / 45 / 11 | 1 | 55 | 1.5 s | +5 accuracy points. |
| Crystal-Focus Wand Grip | 3 | 180 / 180 / 45 | 2 | 70 | 1.5 s | +15% elemental attack; -15% durability. |
| Dawnweaver Conductor | 4 | 360 / — / 90 | 3 | 85 | 1.364 s | +10% action speed; -2 accuracy; -10% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Copper Casting Tip | 1 | 55 / 55 / 14 | 1 | 6 blunt | 20 | +3 accuracy points. |
| Adder-Fang Focus | 2 | 100 / 100 / 25 | 2 | 9 blunt | 24 | Physical attack -12%; elemental attack +20%. |
| Frostglass Prism | 3 | 190 / 190 / 48 | 2 | 11 blunt | 30 | +12% elemental attack; -6% physical attack. |
| Sunbronze Aperture | 3 | 220 / 220 / 55 | 3 | 11 blunt | 18 | +6 critical chance points; -8% physical attack. |
| Webglass Needle Focus | 4 | 390 / — / 98 | 3 | 15 blunt | 38 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Star-Slate Lens | 5 | 700 / — / 175 | 4 | 19 blunt | 28 | +25% direct damage against barriers only. |

## Bow components

Hands: 2. Tags: Ranger, Precision. Elemental coefficient: 1.1. Base reach: 14.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Scout’s Ironbark Riser | 1 | 45 / 45 / 11 | 1 | 55 | 2.2 s | +5 accuracy points. |
| Recurve Sinew Riser | 3 | 180 / 180 / 45 | 2 | 70 | 2.316 s | +25% durability; -5% action speed. |
| Moon-Yew Longbow Riser | 4 | 360 / — / 90 | 3 | 85 | 2.316 s | +0.4 m reach; -3 accuracy; -5% action speed. |
| Glasswind Split Riser | 5 | 660 / — / 165 | 3 | 100 | 2.0 s | +10% action speed; -2 accuracy; -10% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Plain Yew Limbs | 1 | 55 / 55 / 14 | 1 | 22 pierce | 20 | +3 accuracy points. |
| Recurved Drakebone Limbs | 2 | 100 / 100 / 25 | 2 | 30 pierce | 24 | Ignore 10% of physical armor for this hit. |
| Moon-Yew Long Limbs | 3 | 190 / 190 / 48 | 2 | 39 pierce | 30 | +2 m range; -5 accuracy points. |
| Websilk Composite Limbs | 3 | 220 / 220 / 55 | 3 | 36 pierce | 18 | +6 critical chance points; -8% physical attack. |
| Froststeel Spring Limbs | 4 | 390 / — / 98 | 3 | 51 pierce | 38 | 15% chance to remove 6 ATB points; once per target action. |
| Singing-Quartz Split Limbs | 5 | 700 / — / 175 | 4 | 64 pierce | 28 | +12% elemental attack; -6% physical attack. |

## Crossbow components

Hands: 2. Tags: Ranger, Heavy. Elemental coefficient: 1.35. Base reach: 12.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Militia Oak Stock | 1 | 45 / 45 / 11 | 1 | 55 | 3.222 s | +8 accuracy; +10% durability; -10% action speed. |
| Marine Ratchet Stock | 3 | 180 / 180 / 45 | 2 | 70 | 3.053 s | +25% durability; -5% action speed. |
| Cogspire Repeating Stock | 4 | 360 / — / 90 | 3 | 85 | 2.636 s | +10% action speed; -2 accuracy; -10% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Plainsteel Prod | 1 | 55 / 55 / 14 | 1 | 31 pierce | 20 | +3 accuracy points. |
| Drake-Sinew Compound Prod | 2 | 100 / 100 / 25 | 2 | 42 pierce | 24 | +6 critical chance points; -8% physical attack. |
| Marine Heavy Prod | 3 | 190 / 190 / 48 | 2 | 54 pierce | 30 | +2 m range; -5 accuracy points. |
| Springbrass Repeater Prod | 3 | 220 / 220 / 55 | 3 | 51 pierce | 18 | +8% physical attack; -0.2 m reach. |
| Froststeel Arbalest Prod | 4 | 390 / — / 98 | 3 | 71 pierce | 38 | Ignore 10% of physical armor for this hit. |
| Star-Slate Resonance Prod | 5 | 700 / — / 175 | 4 | 90 pierce | 28 | +12% elemental attack; -6% physical attack. |

## Whip components

Hands: 1. Tags: Skirmisher, Control. Elemental coefficient: 1.05. Base reach: 3.8 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Drover’s Wrapped Handle | 1 | 45 / 45 / 11 | 1 | 55 | 1.95 s | +5 accuracy points. |
| Stormtide Swivel Handle | 3 | 180 / 180 / 45 | 2 | 70 | 2.053 s | +0.4 m reach; -3 accuracy; -5% action speed. |
| Veilweave Lash Grip | 4 | 360 / — / 90 | 3 | 85 | 1.95 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Braided Oak Lash | 1 | 55 / 55 / 14 | 1 | 17 slash | 20 | +3 accuracy points. |
| Barbed Drake-Sinew Lash | 2 | 100 / 100 / 25 | 2 | 22 slash | 24 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Belliron Chain Lash | 3 | 190 / 190 / 48 | 2 | 29 slash | 30 | 15% chance to remove 6 ATB points; once per target action. |
| Websilk Razor Lash | 3 | 220 / 220 / 55 | 3 | 27 slash | 18 | +6 critical chance points; -8% physical attack. |
| Drakeglass Segmented Lash | 4 | 390 / — / 98 | 3 | 38 slash | 38 | One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc. |
| Veil-Silver Ribbon Lash | 5 | 700 / — / 175 | 4 | 48 slash | 28 | +12% elemental attack; -6% physical attack. |

## Scythe components

Hands: 2. Tags: Reaper, Control. Elemental coefficient: 1.4. Base reach: 2.6 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Reaper’s Farm Shaft | 1 | 45 / 45 / 11 | 1 | 55 | 2.947 s | +0.4 m reach; -3 accuracy; -5% action speed. |
| Gravewillow Crescent Haft | 3 | 180 / 180 / 45 | 2 | 70 | 2.8 s | +15% elemental attack; -15% durability. |
| Last-Lantern Balance Shaft | 4 | 360 / — / 90 | 3 | 85 | 2.947 s | +25% durability; -5% action speed. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Harvest Iron Crescent | 1 | 55 / 55 / 14 | 1 | 28 slash | 20 | +3 accuracy points. |
| Gravehook Crescent | 2 | 100 / 100 / 25 | 2 | 38 slash | 24 | Ignore 10% of physical armor for this hit. |
| Webglass Reaping Edge | 3 | 190 / 190 / 48 | 2 | 49 slash | 30 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Belliron Soul Crescent | 3 | 220 / 220 / 55 | 3 | 46 slash | 18 | +20% physical damage against undead; no effect on other targets. |
| Froststeel Sickle Arc | 4 | 390 / — / 98 | 3 | 64 slash | 38 | One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc. |
| Null Obsidian Reaping Arc | 5 | 700 / — / 175 | 4 | 81 slash | 28 | Physical attack -12%; elemental attack +20%. |

## Cannon components

Hands: 2. Tags: Artificer, Heavy. Elemental coefficient: 1.6. Base reach: 10.0 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Scrapper’s Shoulder Frame | 1 | 45 / 45 / 11 | 1 | 55 | 4.0 s | +8 accuracy; +10% durability; -10% action speed. |
| Rivetlock Recoil Cradle | 3 | 180 / 180 / 45 | 2 | 70 | 3.789 s | +25% durability; -5% action speed. |
| Brasswick Vented Cannon Frame | 4 | 360 / — / 90 | 3 | 85 | 3.6 s | +22% elemental attack; -4 accuracy; -20% durability; no hidden-life hint. |
| Sundial Artillery Frame | 5 | 660 / — / 165 | 3 | 100 | 3.6 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Riveted Iron Barrel | 1 | 55 / 55 / 14 | 1 | 38 pierce | 20 | +3 accuracy points. |
| Scatterbore Barrel | 2 | 100 / 100 / 25 | 2 | 51 pierce | 24 | One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc. |
| Tidebronze Longbore | 3 | 190 / 190 / 48 | 2 | 67 pierce | 30 | +2 m range; -5 accuracy points. |
| Springbrass Spiral Barrel | 3 | 220 / 220 / 55 | 3 | 63 pierce | 18 | +6 critical chance points; -8% physical attack. |
| Basalt Siege Barrel | 4 | 390 / — / 98 | 3 | 87 pierce | 38 | 15% chance to remove 6 ATB points; once per target action. |
| Prismatic Breach Barrel | 5 | 700 / — / 175 | 4 | 110 pierce | 28 | Physical attack -12%; elemental attack +20%. |

## Gauntlet components

Hands: 1. Tags: Brawler, Skirmisher. Elemental coefficient: 0.65. Base reach: 0.8 m.

| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |
|---|---:|---|---:|---:|---:|---|
| Pitfighter’s Wrist Brace | 1 | 45 / 45 / 11 | 1 | 55 | 1.091 s | +10% action speed; -2 accuracy; -10% durability. |
| Scale-Laced Knuckle Frame | 3 | 180 / 180 / 45 | 2 | 70 | 1.263 s | +25% durability; -5% action speed. |
| Springbrass Piston Brace | 4 | 360 / — / 90 | 3 | 85 | 1.2 s | +15% elemental attack; -15% durability. |

| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |
|---|---:|---|---:|---:|---:|---|
| Plainsteel Knuckle Plate | 1 | 55 / 55 / 14 | 1 | 14 blunt | 20 | +3 accuracy points. |
| Wyrmfang Knuckle Row | 2 | 100 / 100 / 25 | 2 | 18 blunt | 24 | 20% chance to bleed for 12% base physical per action, 2 actions; one stack. |
| Belliron Palm Plate | 3 | 190 / 190 / 48 | 2 | 24 blunt | 30 | 15% chance to remove 6 ATB points; once per target action. |
| Springbrass Ram Knuckle | 3 | 220 / 220 / 55 | 3 | 22 blunt | 18 | +8% physical attack; -0.2 m reach. |
| Froststeel Talon Plate | 4 | 390 / — / 98 | 3 | 31 blunt | 38 | +6 critical chance points; -8% physical attack. |
| Veil-Silver Channel Knuckle | 5 | 700 / — / 175 | 4 | 39 blunt | 28 | +12% elemental attack; -6% physical attack. |

## Entropic cores

Listed effect percentages use base elemental attack before forge multipliers. Core chance is rolled once per offensive action, on the first successful direct hit. Status effects refresh rather than accumulate. See effects.json for full proc rules.

### Ravenwood

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Thornseed Core | 2 | 110 / 110 / 28 | 0 | 12 verdant | 1 | 18% | Root for 1 action; boss substitute: -8% action speed. |
| Huntsman’s Echo Core | 3 | 260 / — / 65 | 1 | 21 spirit | 2 | 22% | Next allied hit gains +12% accuracy for 2 actions; mark consumed on hit. |
| Heart of the Old Grove Core | 4 | 510 / — / 128 | 2 | 32 verdant | 3 | 26% | Wielder gains a barrier equal to 12% of base physical + elemental attack for 2 actions. |
| Worldroot Seed Core | 5 | 1050 / — / 263 | 3 | 45 verdant | 4 | 30% | Root for 2 actions; boss substitute: -12% action speed for 2 actions. |

### Ashen Wastes

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Cinder Pearl Core | 2 | 110 / 110 / 28 | 0 | 12 fire | 1 | 18% | Burn deals 18% of base elemental attack per action for 2 actions. |
| Magma Heart Core | 3 | 260 / — / 65 | 1 | 21 magma | 2 | 22% | Leaves a 1.2 m pool for 2 actions, dealing 20% base elemental attack to all occupants each action. |
| Ashen Crown Core | 4 | 510 / — / 128 | 2 | 32 ash | 3 | 26% | Target loses 10 accuracy points for 2 actions. |
| First Furnace Ember Core | 5 | 1050 / — / 263 | 3 | 45 magma | 4 | 30% | Burn deals 22% base elemental magma damage per action for 3 actions. |

### Frostpeaks

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Rime Shard Core | 2 | 110 / 110 / 28 | 0 | 12 frost | 1 | 18% | Target action speed -12% for 2 actions. |
| Whiteout Eye Core | 3 | 260 / — / 65 | 1 | 21 frost | 2 | 22% | Target loses 15 accuracy points for 2 actions. |
| Glacial Heart Core | 4 | 510 / — / 128 | 2 | 32 frost | 3 | 26% | Wielder barrier = 15% base physical + elemental attack, lasting 2 actions. |
| Stillwinter Heart Core | 5 | 1050 / — / 263 | 3 | 45 frost | 4 | 30% | Target action speed -18% for 3 actions. |

### Drakeshard Range

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Drake Ember Core | 2 | 110 / 110 / 28 | 0 | 12 fire | 1 | 18% | Physical armor -8% for 2 actions. |
| Scale Resonance Core | 3 | 260 / — / 65 | 1 | 21 earth | 2 | 22% | Physical armor -12% for 2 actions. |
| Brood Oath Core | 4 | 510 / — / 128 | 2 | 32 spirit | 3 | 26% | Wielder takes 10% less physical damage until its next action. |

### Golden Expanse

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Sunwell Spark Core | 2 | 110 / 110 / 28 | 0 | 12 solar | 1 | 18% | Next allied hit adds 10% base elemental solar damage; mark consumed. |
| Mirage Eye Core | 3 | 260 / — / 65 | 1 | 21 mirage | 2 | 22% | Wielder gains 8 evasion points until its next action. |
| Buried Dawn Core | 4 | 510 / — / 128 | 2 | 32 solar | 3 | 26% | Remove 1 removable positive effect from the struck enemy. |
| Dawn Before Kings Core | 5 | 1050 / — / 263 | 3 | 45 solar | 4 | 30% | Remove up to 2 removable enemy positive effects. |

### Blighted Marsh

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Adder Bile Core | 2 | 110 / 110 / 28 | 0 | 12 venom | 1 | 18% | Poison deals 12% base elemental attack per action for 3 actions. |
| Mire Lantern Core | 3 | 260 / — / 65 | 1 | 21 verdant | 2 | 22% | Remove 1 poison stack from the wielder. |
| Rotmother Spore Core | 4 | 510 / — / 128 | 2 | 32 rot | 3 | 26% | Rot deals 18% base elemental per action for 2 actions; on death transfers remaining duration to 1 enemy within 2 m. |

### Cursed Mire

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Grave Ember Core | 2 | 110 / 110 / 28 | 0 | 12 spirit | 1 | 18% | Target receives 20% less healing for 2 actions. |
| Hexbound Tear Core | 3 | 260 / — / 65 | 1 | 21 curse | 2 | 22% | Target physical attack -10% for 2 actions. |
| Anchorless Soul Core | 4 | 510 / — / 128 | 2 | 32 spirit | 3 | 26% | Add spirit damage = 25% base elemental attack against undead only. |

### Shadowfen Forest

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Gloam Mote Core | 2 | 110 / 110 / 28 | 0 | 12 shadow | 1 | 18% | Target loses 10 evasion points for 2 actions. |
| Widow’s Knot Core | 3 | 260 / — / 65 | 1 | 21 shadow | 2 | 22% | Root for 1 action; boss substitute: -8% action speed. |
| Hollow Canopy Core | 4 | 510 / — / 128 | 2 | 32 rot | 3 | 26% | Target rot resistance -10 percentage points for 2 actions. |

### Iron Plains

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Marching Spark Core | 2 | 110 / 110 / 28 | 0 | 12 earth | 1 | 18% | Wielder gains 50% displacement resistance until its next action. |
| Warhorn Echo Core | 3 | 260 / — / 65 | 1 | 21 spirit | 2 | 22% | Wielder’s next direct hit gains 10% base physical damage; cannot stack. |
| Siegeheart Core | 4 | 510 / — / 128 | 2 | 32 earth | 3 | 26% | Deal an additional 30% base physical + elemental attack to barriers only. |

### Veiled Sea

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Salt Pearl Core | 2 | 110 / 110 / 28 | 0 | 12 tide | 1 | 18% | Physical armor -8% for 2 actions. |
| Undertow Knot Core | 3 | 260 / — / 65 | 1 | 21 tide | 2 | 22% | Pull target 1 m toward the wielder; immune targets take 10% base elemental tide damage instead. |
| Tempest Bottle Core | 4 | 510 / — / 128 | 2 | 32 storm | 3 | 26% | Deal 15% base elemental storm damage to 1 extra enemy within 2 m. |

### Ember Coast

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Coalglass Ember Core | 2 | 110 / 110 / 28 | 0 | 12 fire | 1 | 18% | Leave a 1 m trail at target for 2 actions, dealing 15% base elemental to all occupants each action. |
| Cinderwake Pearl Core | 3 | 260 / — / 65 | 1 | 21 magma | 2 | 22% | Leave a 1.5 m patch for 2 actions, dealing 25% base elemental to all occupants each action. |
| Dragon Pact Ember Core | 4 | 510 / — / 128 | 2 | 32 fire | 3 | 26% | Deal 25% base elemental fire damage to at most 2 extra enemies within 2 m. |

### Stormcrown Mountains

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Stormglass Spark Core | 2 | 110 / 110 / 28 | 0 | 12 storm | 1 | 18% | Remove 8 percentage points from target ATB; once per target action. |
| Thundercoil Core | 3 | 260 / — / 65 | 1 | 21 storm | 2 | 22% | Jump to at most 2 different enemies within 2 m for 20% base elemental storm damage each. |
| Skyward Seal Core | 4 | 510 / — / 128 | 2 | 32 storm | 3 | 26% | Wielder takes 12% less elemental damage until its next action. |

### Moonfall Highlands

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Moonlit Flake Core | 2 | 110 / 110 / 28 | 0 | 12 lunar | 1 | 18% | Target critical resistance -6 points for 2 actions. |
| Fallen Star Core | 3 | 260 / — / 65 | 1 | 21 astral | 2 | 22% | Add one astral pulse of 20% base elemental attack; pulse cannot trigger procs. |
| Observatory Heart Core | 4 | 510 / — / 128 | 2 | 32 astral | 3 | 26% | Pull struck target up to 1.5 m toward its nearest enemy ally; immune targets take 15% base elemental astral damage instead. |

### Copperfen Basin

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Clockwork Spark Core | 2 | 110 / 110 / 28 | 0 | 12 kinetic | 1 | 18% | Next direct physical hit gains 12% base physical damage; cannot stack. |
| Pressure Pearl Core | 3 | 260 / — / 65 | 1 | 21 kinetic | 2 | 22% | Push target 1 m away; immune targets take 10% base elemental kinetic damage instead. |
| Overload Governor Core | 4 | 510 / — / 128 | 2 | 32 storm | 3 | 26% | Deal 25% base elemental storm damage to 1 extra enemy within 2 m. Does not reveal cracked durability. |
| Prime Kettari Governor Core | 5 | 1050 / — / 263 | 3 | 45 kinetic | 4 | 30% | Push target 2 m; immune targets take 20% base elemental kinetic damage instead. No durability stabilization. |

### Glasswind Steppe

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Whisperglass Core | 2 | 110 / 110 / 28 | 0 | 12 wind | 1 | 18% | Add 15% base elemental wind damage ignoring 20% resistance for this pulse. |
| Sand-Singer Core | 3 | 260 / — / 65 | 1 | 21 wind | 2 | 22% | Target loses 12 accuracy points for 2 actions. |
| Horizon Prism Core | 4 | 510 / — / 128 | 2 | 32 mirage | 3 | 26% | Add 25% base elemental mirage damage to the first enemy behind the target, within 3 m. |

### Deadwind Hollow

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Bell-Wraith Ember Core | 2 | 110 / 110 / 28 | 0 | 12 spirit | 1 | 18% | Silence for 1 action; boss substitute: magic attack -8% for 1 action. |
| Lantern Soul Core | 3 | 260 / — / 65 | 1 | 21 spirit | 2 | 22% | Wielder gains 25 curse-resistance points until its next action. |
| Pale Procession Core | 4 | 510 / — / 128 | 2 | 32 curse | 3 | 26% | Target receives 25% less healing for 3 actions. |
| Unbound Funeral Star Core | 5 | 1050 / — / 263 | 3 | 45 spirit | 4 | 30% | Add 45% base elemental spirit damage against undead only. |

### Mistvale

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Mist Dew Core | 2 | 110 / 110 / 28 | 0 | 12 mist | 1 | 18% | Wielder gains 6 evasion points until its next action. |
| Veilbound Star Core | 3 | 260 / — / 65 | 1 | 21 astral | 2 | 22% | Add one astral pulse of 25% base elemental attack; pulse cannot trigger procs. |
| Relic Memory Core | 4 | 510 / — / 128 | 2 | 32 astral | 3 | 26% | Target astral resistance -12 percentage points for 2 actions. |

### Devouring Deep

| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |
|---|---:|---|---:|---|---:|---:|---|
| Rift Cinder Core | 2 | 110 / 110 / 28 | 0 | 12 void | 1 | 18% | Add 35% base elemental void damage to barriers only. |
| Hunger Fragment Core | 3 | 260 / — / 65 | 1 | 21 void | 2 | 22% | Heal wielder for 8% of the direct elemental damage actually dealt; excludes bursts and shields. |
| Quiet Singularity Core | 4 | 510 / — / 128 | 2 | 32 void | 3 | 26% | Deal 30% base elemental void damage to at most 2 extra enemies within 2 m. |

## The 180 named discoveries

All results below use crafting skill +3 and a perfect forge. Attack is physical / elemental before enemy defenses. Standard → Mistvale → Sands columns show forge progression. Durability is Masterwork durability; cracked remaining durability is never player-visible. Named recipes are aliases for combinations and grant no hidden fourth-part bonus.

### Sword recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Briar Oath | Watchman’s Leather Grip + Plainsteel Straight Blade + Thornseed Core | 5 | 26/16 → 28/17 → 29/18 | 75 | 1.8 | 63 / 74 g |
| Cinder Vow | Duelist’s Tideguard + Serrated Fang Blade + Cinder Pearl Core | 7 | 39/17 → 43/19 → 45/20 | 85 | 1.718 | 108 / 137 g |
| White Mercy | Sentinel’s Ironbark Hilt + Tidebronze Saber Blade + Rime Shard Core | 8 | 58/19 → 64/20 → 67/21 | 144 | 2.047 | 175 / 231 g |
| Scale Promise | Sunbound Filigree Hilt + Webglass Needle Blade + Drake Ember Core | 9 | 50/23 → 55/25 → 57/26 | 100 | 1.692 | 258 / 347 g |
| Sunlit Verdict | Watchman’s Leather Grip + Scaleiron Falchion Blade + Sunwell Spark Core | 7 | 67/17 → 73/19 → 76/20 | 93 | 2.052 | 146 / 191 g |
| Adder’s Courtesy | Duelist’s Tideguard + Veil-Silver Channel Blade + Adder Bile Core | 9 | 90/22 → 98/24 → 102/25 | 88 | 1.8 | 258 / 347 g |
| Gravewarden | Sentinel’s Ironbark Hilt + Plainsteel Straight Blade + Grave Ember Core | 7 | 29/17 → 32/19 → 33/20 | 131 | 1.895 | 141 / 184 g |
| Widow’s Answer | Sunbound Filigree Hilt + Serrated Fang Blade + Gloam Mote Core | 8 | 42/21 → 46/23 → 48/24 | 105 | 1.89 | 228 / 305 g |
| Marchkeeper | Watchman’s Leather Grip + Tidebronze Saber Blade + Marching Spark Core | 6 | 52/16 → 57/18 → 59/19 | 85 | 1.944 | 96 / 121 g |
| Salt Testament | Duelist’s Tideguard + Webglass Needle Blade + Salt Pearl Core | 8 | 47/19 → 52/20 → 53/21 | 79 | 1.538 | 138 / 179 g |
| Ashwake Saber | Sentinel’s Ironbark Hilt + Scaleiron Falchion Blade + Coalglass Ember Core | 9 | 76/20 → 83/22 → 86/23 | 154 | 2.16 | 225 / 301 g |
| Stormlit Promise | Sunbound Filigree Hilt + Veil-Silver Channel Blade + Stormglass Spark Core | 10 | 95/27 → 105/30 → 109/31 | 109 | 1.98 | 378 / 515 g |

### Greatsword recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Winter’s Debt | Militia Longgrip + Broad Militia Blade + Rime Shard Core | 5 | 44/23 → 48/26 → 50/27 | 83 | 3.333 | 63 / 74 g |
| Wyrm’s Reproach | Drakespine Wargrip + Notched Siege Blade + Drake Ember Core | 7 | 67/26 → 73/29 → 76/30 | 94 | 3.316 | 108 / 137 g |
| Dawn Divider | Black Anvil Twohander + Drakebone Cleaver + Sunwell Spark Core | 8 | 93/34 → 102/37 → 106/39 | 92 | 3.24 | 175 / 231 g |
| Bog King’s Fall | Militia Longgrip + Basalt Execution Blade + Adder Bile Core | 7 | 81/26 → 89/29 → 93/30 | 80 | 3.133 | 104 / 131 g |
| Cursebreaker’s Burden | Drakespine Wargrip + Froststeel Flamberge + Grave Ember Core | 8 | 120/28 → 132/31 → 137/32 | 108 | 3.6 | 180 / 238 g |
| Canopy Reaver | Black Anvil Twohander + Null-Edge Colossus Blade + Gloam Mote Core | 10 | 152/46 → 168/51 → 174/53 | 90 | 3.3 | 303 / 410 g |
| Last Battle Line | Militia Longgrip + Broad Militia Blade + Marching Spark Core | 5 | 44/23 → 48/26 → 50/27 | 83 | 3.333 | 63 / 74 g |
| Breakwater Blade | Drakespine Wargrip + Notched Siege Blade + Salt Pearl Core | 7 | 67/26 → 73/29 → 76/30 | 94 | 3.316 | 108 / 137 g |
| Nestkeeper’s Fury | Black Anvil Twohander + Drakebone Cleaver + Coalglass Ember Core | 8 | 93/34 → 102/37 → 106/39 | 92 | 3.24 | 175 / 231 g |
| Summit Judgment | Militia Longgrip + Basalt Execution Blade + Stormglass Spark Core | 7 | 81/26 → 89/29 → 93/30 | 80 | 3.133 | 104 / 131 g |
| Moonfall Monument | Drakespine Wargrip + Froststeel Flamberge + Moonlit Flake Core | 8 | 120/28 → 132/31 → 137/32 | 108 | 3.6 | 180 / 238 g |
| Foundry Requiem | Black Anvil Twohander + Null-Edge Colossus Blade + Clockwork Spark Core | 10 | 152/46 → 168/51 → 174/53 | 90 | 3.3 | 303 / 410 g |

### Dagger recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Salt Whisper | Poacher’s Thumbgrip + Watchman’s Point + Salt Pearl Core | 5 | 16/9 → 17/10 → 18/11 | 75 | 1.05 | 63 / 74 g |
| Ember Needle | Websilk Loop Grip + Hollow Adder Fang + Coalglass Ember Core | 7 | 22/13 → 24/14 → 25/14 | 85 | 1.003 | 108 / 137 g |
| Thunder’s Wink | Mirage Balanced Tang + Glasswind Stiletto + Stormglass Spark Core | 8 | 31/13 → 34/14 → 36/15 | 98 | 1.134 | 175 / 231 g |
| Moonless Kiss | Poacher’s Thumbgrip + Barbed Webglass Point + Moonlit Flake Core | 7 | 29/10 → 32/12 → 33/12 | 73 | 0.987 | 104 / 131 g |
| Clockwork Stiletto | Websilk Loop Grip + Belliron Ritual Blade + Clockwork Spark Core | 8 | 45/11 → 49/12 → 51/13 | 97 | 1.089 | 180 / 238 g |
| Glasswind Secret | Mirage Balanced Tang + Star-Slate Crescent + Whisperglass Core | 10 | 59/16 → 65/18 → 68/19 | 96 | 1.155 | 303 / 410 g |
| Bellringer’s Debt | Poacher’s Thumbgrip + Watchman’s Point + Bell-Wraith Ember Core | 5 | 16/9 → 17/10 → 18/11 | 75 | 1.05 | 63 / 74 g |
| Mist Thief | Websilk Loop Grip + Hollow Adder Fang + Mist Dew Core | 7 | 22/13 → 24/14 → 25/14 | 85 | 1.003 | 108 / 137 g |
| Hunger’s Point | Mirage Balanced Tang + Glasswind Stiletto + Rift Cinder Core | 8 | 31/13 → 34/14 → 36/15 | 98 | 1.134 | 175 / 231 g |
| Root Assassin | Poacher’s Thumbgrip + Barbed Webglass Point + Worldroot Seed Core | 10 | 35/47 → 39/52 → 40/54 | 73 | 0.987 | 339 / 460 g |
| Furnace Splinter | Websilk Loop Grip + Belliron Ritual Blade + First Furnace Ember Core | 10 | 51/47 → 56/52 → 58/54 | 97 | 1.089 | 415 / 567 g |
| Winter Widow | Mirage Balanced Tang + Star-Slate Crescent + Stillwinter Heart Core | 10 | 59/61 → 65/67 → 68/70 | 96 | 1.155 | 538 / 739 g |

### Spear recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Moonwarden’s Reach | Ranger’s Ash Haft + Iron Leaf Spearhead + Moonlit Flake Core | 5 | 31/16 → 34/18 → 35/19 | 75 | 2.316 | 63 / 74 g |
| Pressure Lance | Rimepine Lance Shaft + Wyrmtooth Pikehead + Clockwork Spark Core | 7 | 46/18 → 51/20 → 53/21 | 118 | 2.432 | 108 / 137 g |
| Horizon Harpoon | Stormkeeper Spear Haft + Sunbronze Winged Head + Whisperglass Core | 8 | 60/22 → 66/25 → 68/26 | 98 | 2.376 | 175 / 231 g |
| Funeral Standard | Oathroot Longshaft + Stormsteel Fork + Bell-Wraith Ember Core | 9 | 62/23 → 68/25 → 71/26 | 130 | 2.297 | 258 / 347 g |
| Veilpiercer | Ranger’s Ash Haft + Froststeel Lance Tip + Mist Dew Core | 7 | 80/18 → 88/20 → 91/21 | 93 | 2.64 | 146 / 191 g |
| Rift Skewer | Rimepine Lance Shaft + Hollow Veil-Silver Point + Rift Cinder Core | 9 | 101/25 → 111/27 → 116/28 | 123 | 2.548 | 258 / 347 g |
| Rootbound Watch | Stormkeeper Spear Haft + Iron Leaf Spearhead + Worldroot Seed Core | 10 | 42/95 → 46/105 → 48/109 | 89 | 2.2 | 376 / 513 g |
| First Flame Pike | Oathroot Longshaft + Wyrmtooth Pikehead + First Furnace Ember Core | 10 | 56/83 → 62/91 → 64/95 | 136 | 2.566 | 463 / 634 g |
| Stillwinter Thorn | Ranger’s Ash Haft + Sunbronze Winged Head + Stillwinter Heart Core | 9 | 63/78 → 70/85 → 72/89 | 85 | 2.501 | 331 / 450 g |
| Pale Sentinel | Rimepine Lance Shaft + Stormsteel Fork + Unbound Funeral Star Core | 10 | 66/93 → 72/102 → 75/106 | 110 | 2.177 | 373 / 507 g |
| Governor’s Reach | Stormkeeper Spear Haft + Froststeel Lance Tip + Prime Kettari Governor Core | 10 | 96/95 → 106/105 → 110/109 | 105 | 2.508 | 460 / 630 g |
| Dawnwatch Lance | Oathroot Longshaft + Hollow Veil-Silver Point + Dawn Before Kings Core | 10 | 108/99 → 119/109 → 123/113 | 141 | 2.688 | 613 / 844 g |

### Axe recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Lantern Hew | Woodcutter’s Haft + Forester’s Axe Bit + Bell-Wraith Ember Core | 5 | 31/16 → 34/17 → 35/18 | 94 | 2.211 | 63 / 74 g |
| Mistfall Hatchet | Corsair’s Hook Haft + Raider’s Hook Bit + Mist Dew Core | 7 | 46/17 → 51/19 → 53/20 | 85 | 2.004 | 108 / 137 g |
| Hunger Hewn | Cinderbrace Split Haft + Drakeglass Bearded Edge + Rift Cinder Core | 8 | 63/23 → 70/25 → 72/26 | 92 | 2.268 | 175 / 231 g |
| Worldroot Splitter | Woodcutter’s Haft + Bog-Iron Hewing Head + Worldroot Seed Core | 10 | 68/79 → 75/87 → 78/90 | 91 | 2.078 | 339 / 460 g |
| First Furnace Bite | Corsair’s Hook Haft + Basalt Double Bit + First Furnace Ember Core | 10 | 95/79 → 104/87 → 108/90 | 97 | 2.176 | 415 / 567 g |
| Stillwinter Hook | Cinderbrace Split Haft + Star-Slate Crescent Bit + Stillwinter Heart Core | 10 | 109/96 → 120/106 → 125/110 | 90 | 2.31 | 538 / 739 g |
| Funeral Crescent | Woodcutter’s Haft + Forester’s Axe Bit + Unbound Funeral Star Core | 8 | 37/69 → 41/76 → 42/79 | 94 | 2.211 | 298 / 403 g |
| Clockwork Woodsman | Corsair’s Hook Haft + Raider’s Hook Bit + Prime Kettari Governor Core | 10 | 56/79 → 62/87 → 64/90 | 85 | 2.004 | 343 / 465 g |
| Dawncleaver | Cinderbrace Split Haft + Drakeglass Bearded Edge + Dawn Before Kings Core | 10 | 72/96 → 79/106 → 82/110 | 92 | 2.268 | 410 / 560 g |
| Briar Butcher | Woodcutter’s Haft + Bog-Iron Hewing Head + Thornseed Core | 7 | 57/17 → 62/19 → 65/20 | 91 | 2.078 | 104 / 131 g |
| Ashkeeper’s Hook | Corsair’s Hook Haft + Basalt Double Bit + Cinder Pearl Core | 8 | 83/19 → 92/20 → 95/21 | 97 | 2.176 | 180 / 238 g |
| White Pass Reaver | Cinderbrace Split Haft + Star-Slate Crescent Bit + Rime Shard Core | 10 | 109/26 → 120/28 → 125/29 | 90 | 2.31 | 303 / 410 g |

### Hammer recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Gatebreaker | Quarryman’s Haft + Quarry Iron Block + Huntsman’s Echo Core | 6 | 51/43 → 56/47 → 58/49 | 83 | 3.556 | 100 / 126 g |
| Ember Bell | Siegebreaker Shock Haft + Siege Ram Head + Magma Heart Core | 8 | 77/49 → 85/53 → 88/55 | 118 | 3.536 | 145 / 189 g |
| Rime Knell | Thunderbrow Pattern Haft + Resonant Belliron Head + Whiteout Eye Core | 9 | 107/59 → 117/65 → 122/68 | 98 | 3.456 | 213 / 284 g |
| Drakefall | Quarryman’s Haft + Basalt Furnace Head + Scale Resonance Core | 8 | 83/58 → 91/64 → 95/67 | 80 | 3.343 | 141 / 184 g |
| Dawn Ram | Siegebreaker Shock Haft + Scaleiron Shatter Head + Mirage Eye Core | 9 | 140/52 → 154/57 → 159/59 | 135 | 3.84 | 218 / 291 g |
| Mirebound Mallet | Thunderbrow Pattern Haft + Singing-Quartz Impact Head + Mire Lantern Core | 10 | 176/71 → 194/78 → 201/81 | 96 | 3.52 | 340 / 462 g |
| Curse Anchor | Quarryman’s Haft + Quarry Iron Block + Hexbound Tear Core | 6 | 51/43 → 56/47 → 58/49 | 83 | 3.556 | 100 / 126 g |
| Webbreaker | Siegebreaker Shock Haft + Siege Ram Head + Widow’s Knot Core | 8 | 77/49 → 85/53 → 88/55 | 118 | 3.536 | 145 / 189 g |
| Siege Psalm | Thunderbrow Pattern Haft + Resonant Belliron Head + Warhorn Echo Core | 9 | 107/59 → 117/65 → 122/68 | 98 | 3.456 | 213 / 284 g |
| Tidehammer | Quarryman’s Haft + Basalt Furnace Head + Undertow Knot Core | 8 | 83/58 → 91/64 → 95/67 | 80 | 3.343 | 141 / 184 g |
| Cinderquake | Siegebreaker Shock Haft + Scaleiron Shatter Head + Cinderwake Pearl Core | 9 | 140/52 → 154/57 → 159/59 | 135 | 3.84 | 218 / 291 g |
| Storm Anvil | Thunderbrow Pattern Haft + Singing-Quartz Impact Head + Thundercoil Core | 10 | 176/71 → 194/78 → 201/81 | 96 | 3.52 | 340 / 462 g |

### Mace recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Winter Crown | Gateward Handle + Gatewatch Iron Ball + Whiteout Eye Core | 6 | 30/29 → 33/32 → 34/33 | 75 | 2.05 | 100 / 126 g |
| Broodkeeper | Reedbound Cudgel Haft + Thorn-Cage Head + Scale Resonance Core | 8 | 46/32 → 51/36 → 53/37 | 118 | 2.266 | 145 / 189 g |
| Sunlit Rebuke | Lanternkeeper Flanged Grip + Sunbronze Flanged Head + Mirage Eye Core | 9 | 64/40 → 70/44 → 73/45 | 98 | 2.214 | 213 / 284 g |
| Reedwarden | Gateward Handle + Hexstone Knob + Mire Lantern Core | 8 | 57/32 → 63/36 → 65/37 | 73 | 1.927 | 141 / 184 g |
| Grave Lantern | Reedbound Cudgel Haft + Froststeel Crown + Hexbound Tear Core | 9 | 85/34 → 94/38 → 98/39 | 135 | 2.46 | 218 / 291 g |
| Gloam Cudgel | Lanternkeeper Flanged Grip + Veil-Silver Lantern Cage + Widow’s Knot Core | 10 | 107/47 → 118/52 → 122/54 | 96 | 2.255 | 340 / 462 g |
| Marching Bell | Gateward Handle + Gatewatch Iron Ball + Warhorn Echo Core | 6 | 30/29 → 33/32 → 34/33 | 75 | 2.05 | 100 / 126 g |
| Saltwarden | Reedbound Cudgel Haft + Thorn-Cage Head + Undertow Knot Core | 8 | 46/32 → 51/36 → 53/37 | 118 | 2.266 | 145 / 189 g |
| Hearthguard | Lanternkeeper Flanged Grip + Sunbronze Flanged Head + Cinderwake Pearl Core | 9 | 64/40 → 70/44 → 73/45 | 98 | 2.214 | 213 / 284 g |
| Thunder Chapel | Gateward Handle + Hexstone Knob + Thundercoil Core | 8 | 57/32 → 63/36 → 65/37 | 73 | 1.927 | 141 / 184 g |
| Moonward | Reedbound Cudgel Haft + Froststeel Crown + Fallen Star Core | 9 | 85/34 → 94/38 → 98/39 | 135 | 2.46 | 218 / 291 g |
| Pressure Saint | Lanternkeeper Flanged Grip + Veil-Silver Lantern Cage + Pressure Pearl Core | 10 | 107/47 → 118/52 → 122/54 | 96 | 2.255 | 340 / 462 g |

### Staff recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Tidal Testament | Herbalist’s Bogroot Staff + Carved Root Crown + Undertow Knot Core | 6 | 16/49 → 18/54 → 19/56 | 94 | 2.632 | 100 / 126 g |
| Cinder Shepherd | Gloamwood Channel Staff + Marsh-Bone Focus + Cinderwake Pearl Core | 8 | 23/76 → 25/84 → 26/87 | 80 | 2.625 | 145 / 189 g |
| Stormbranch | Veil-Silver Casting Shaft + Storm Fork Crown + Thundercoil Core | 9 | 34/66 → 37/72 → 39/75 | 104 | 2.455 | 213 / 284 g |
| Moon Observatory | Astral Spiral Staff + Moon Lens Cradle + Fallen Star Core | 10 | 32/76 → 35/84 → 37/87 | 94 | 2.35 | 295 / 399 g |
| Clockmaker’s Crook | Herbalist’s Bogroot Staff + Hexstone Ritual Cage + Pressure Pearl Core | 8 | 45/55 → 49/61 → 51/63 | 116 | 3.0 | 184 / 243 g |
| Windglass Pilgrim | Gloamwood Channel Staff + Prismatic Silver Crown + Sand-Singer Core | 10 | 63/72 → 69/79 → 72/82 | 83 | 2.75 | 295 / 399 g |
| Last Procession | Veil-Silver Casting Shaft + Carved Root Crown + Lantern Soul Core | 8 | 19/55 → 20/61 → 21/63 | 95 | 2.273 | 179 / 236 g |
| Mistvale Memory | Astral Spiral Staff + Marsh-Bone Focus + Veilbound Star Core | 9 | 25/86 → 27/94 → 28/98 | 99 | 2.625 | 265 / 357 g |
| Rift Interpreter | Herbalist’s Bogroot Staff + Storm Fork Crown + Hunger Fragment Core | 7 | 30/58 → 33/64 → 34/66 | 106 | 2.843 | 134 / 173 g |
| Worldroot Cantor | Gloamwood Channel Staff + Moon Lens Cradle + Worldroot Seed Core | 10 | 32/154 → 35/169 → 37/176 | 75 | 2.35 | 373 / 507 g |
| First Furnace Oracle | Veil-Silver Casting Shaft + Hexstone Ritual Cage + First Furnace Ember Core | 10 | 51/134 → 56/147 → 58/153 | 111 | 2.591 | 460 / 630 g |
| Stillwinter Scribe | Astral Spiral Staff + Prismatic Silver Crown + Stillwinter Heart Core | 10 | 63/163 → 69/180 → 72/187 | 102 | 2.75 | 613 / 844 g |

### Wand recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Moon Needle | Apprentice’s Yew Handle + Copper Casting Tip + Fallen Star Core | 6 | 8/33 → 9/36 → 9/38 | 75 | 1.5 | 100 / 126 g |
| Pressure Pointer | Crystal-Focus Wand Grip + Adder-Fang Focus + Pressure Pearl Core | 8 | 12/51 → 13/57 → 14/59 | 80 | 1.575 | 145 / 189 g |
| Horizon Quill | Dawnweaver Conductor + Frostglass Prism + Sand-Singer Core | 9 | 17/44 → 19/49 → 19/51 | 104 | 1.473 | 213 / 284 g |
| Pale Bell | Apprentice’s Yew Handle + Sunbronze Aperture + Lantern Soul Core | 8 | 16/37 → 17/41 → 18/43 | 73 | 1.41 | 141 / 184 g |
| Veil Signature | Crystal-Focus Wand Grip + Webglass Needle Focus + Veilbound Star Core | 9 | 25/46 → 27/50 → 28/52 | 92 | 1.71 | 218 / 291 g |
| Null Stylus | Dawnweaver Conductor + Star-Slate Lens + Hunger Fragment Core | 10 | 33/42 → 37/46 → 38/48 | 102 | 1.5 | 340 / 462 g |
| Grove Script | Apprentice’s Yew Handle + Copper Casting Tip + Worldroot Seed Core | 8 | 9/80 → 10/88 → 11/91 | 75 | 1.5 | 298 / 403 g |
| Furnace Whisper | Crystal-Focus Wand Grip + Adder-Fang Focus + First Furnace Ember Core | 10 | 14/125 → 15/137 → 16/143 | 80 | 1.575 | 343 / 465 g |
| Winter Cipher | Dawnweaver Conductor + Frostglass Prism + Stillwinter Heart Core | 10 | 18/101 → 20/112 → 21/116 | 104 | 1.473 | 410 / 560 g |
| Funeral Reed | Apprentice’s Yew Handle + Sunbronze Aperture + Unbound Funeral Star Core | 10 | 18/91 → 19/100 → 20/103 | 73 | 1.41 | 339 / 460 g |
| Prime Conductor | Crystal-Focus Wand Grip + Webglass Needle Focus + Prime Kettari Governor Core | 10 | 26/104 → 29/115 → 30/119 | 92 | 1.71 | 415 / 567 g |
| First Dawn Quill | Dawnweaver Conductor + Star-Slate Lens + Dawn Before Kings Core | 10 | 33/91 → 37/100 → 38/103 | 102 | 1.5 | 538 / 739 g |

### Bow recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Last Lantern Bow | Scout’s Ironbark Riser + Plain Yew Limbs + Lantern Soul Core | 6 | 30/32 → 33/35 → 34/36 | 75 | 2.2 | 100 / 126 g |
| Veilstrung | Recurve Sinew Riser + Recurved Drakebone Limbs + Veilbound Star Core | 8 | 46/36 → 51/39 → 53/41 | 118 | 2.432 | 145 / 189 g |
| Hunger at Distance | Moon-Yew Longbow Riser + Moon-Yew Long Limbs + Hunger Fragment Core | 9 | 64/38 → 70/42 → 73/43 | 115 | 2.501 | 213 / 284 g |
| Worldroot Vigil | Glasswind Split Riser + Websilk Composite Limbs + Worldroot Seed Core | 10 | 58/87 → 64/95 → 66/99 | 106 | 1.88 | 493 / 676 g |
| Furnace Recurve | Scout’s Ironbark Riser + Froststeel Spring Limbs + First Furnace Ember Core | 10 | 89/87 → 98/95 → 102/99 | 93 | 2.508 | 381 / 520 g |
| Stillwinter Longbow | Recurve Sinew Riser + Singing-Quartz Split Limbs + Stillwinter Heart Core | 10 | 105/97 → 116/107 → 120/111 | 123 | 2.548 | 493 / 676 g |
| Funeral Archer | Moon-Yew Longbow Riser + Plain Yew Limbs + Unbound Funeral Star Core | 10 | 39/87 → 42/95 → 44/99 | 105 | 2.316 | 376 / 513 g |
| Clockwork Canopy | Glasswind Split Riser + Recurved Drakebone Limbs + Prime Kettari Governor Core | 10 | 53/87 → 58/95 → 60/99 | 112 | 2.1 | 463 / 634 g |
| Dawn Horizon | Scout’s Ironbark Riser + Moon-Yew Long Limbs + Dawn Before Kings Core | 9 | 64/81 → 70/89 → 73/93 | 85 | 2.376 | 331 / 450 g |
| Briar Whisper | Recurve Sinew Riser + Websilk Composite Limbs + Huntsman’s Echo Core | 9 | 54/38 → 60/42 → 62/43 | 110 | 2.177 | 175 / 231 g |
| Ashwind | Moon-Yew Longbow Riser + Froststeel Spring Limbs + Magma Heart Core | 10 | 89/40 → 98/44 → 102/46 | 123 | 2.64 | 263 / 354 g |
| White Hunter | Glasswind Split Riser + Singing-Quartz Split Limbs + Whiteout Eye Core | 10 | 105/45 → 116/50 → 120/52 | 115 | 2.2 | 415 / 567 g |

### Crossbow recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Watchman’s Promise | Militia Oak Stock + Plainsteel Prod + Heart of the Old Grove Core | 7 | 45/63 → 50/69 → 51/72 | 83 | 3.222 | 163 / 214 g |
| Cinder Bolt | Marine Ratchet Stock + Drake-Sinew Compound Prod + Ashen Crown Core | 9 | 63/71 → 70/78 → 72/81 | 118 | 3.206 | 208 / 277 g |
| Icebound Warrant | Cogspire Repeating Stock + Marine Heavy Prod + Glacial Heart Core | 10 | 95/76 → 104/83 → 108/86 | 104 | 2.847 | 275 / 371 g |
| Wyrm Marshal | Militia Oak Stock + Springbrass Repeater Prod + Brood Oath Core | 9 | 90/71 → 99/78 → 103/81 | 80 | 3.029 | 204 / 271 g |
| Dawn Mechanism | Marine Ratchet Stock + Froststeel Arbalest Prod + Buried Dawn Core | 10 | 124/76 → 137/83 → 142/86 | 135 | 3.48 | 280 / 378 g |
| Adder’s Writ | Cogspire Repeating Stock + Star-Slate Resonance Prod + Rotmother Spore Core | 10 | 148/85 → 163/93 → 169/97 | 102 | 2.9 | 403 / 550 g |
| Grave Arbiter | Militia Oak Stock + Plainsteel Prod + Anchorless Soul Core | 7 | 45/63 → 50/69 → 51/72 | 83 | 3.222 | 163 / 214 g |
| Webline | Marine Ratchet Stock + Drake-Sinew Compound Prod + Hollow Canopy Core | 9 | 63/71 → 70/78 → 72/81 | 118 | 3.206 | 208 / 277 g |
| Siege Witness | Cogspire Repeating Stock + Marine Heavy Prod + Siegeheart Core | 10 | 95/76 → 104/83 → 108/86 | 104 | 2.847 | 275 / 371 g |
| Marine’s Return | Militia Oak Stock + Springbrass Repeater Prod + Tempest Bottle Core | 9 | 90/71 → 99/78 → 103/81 | 80 | 3.029 | 204 / 271 g |
| Rookery Guard | Marine Ratchet Stock + Froststeel Arbalest Prod + Dragon Pact Ember Core | 10 | 124/76 → 137/83 → 142/86 | 135 | 3.48 | 280 / 378 g |
| Storm Ratchet | Cogspire Repeating Stock + Star-Slate Resonance Prod + Skyward Seal Core | 10 | 148/85 → 163/93 → 169/97 | 102 | 2.9 | 403 / 550 g |

### Whip recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Winter Lash | Drover’s Wrapped Handle + Braided Oak Lash + Glacial Heart Core | 7 | 25/49 → 27/54 → 28/56 | 75 | 1.95 | 163 / 214 g |
| Broodbinder | Stormtide Swivel Handle + Barbed Drake-Sinew Lash + Brood Oath Core | 9 | 36/55 → 40/61 → 41/63 | 94 | 2.156 | 208 / 277 g |
| Suncoil | Veilweave Lash Grip + Belliron Chain Lash + Buried Dawn Core | 10 | 51/68 → 56/74 → 58/77 | 98 | 2.106 | 275 / 371 g |
| Fen Shepherd | Drover’s Wrapped Handle + Websilk Razor Lash + Rotmother Spore Core | 9 | 41/55 → 45/61 → 47/63 | 73 | 1.833 | 204 / 271 g |
| Gravechain | Stormtide Swivel Handle + Drakeglass Segmented Lash + Anchorless Soul Core | 10 | 67/59 → 73/65 → 76/67 | 108 | 2.34 | 280 / 378 g |
| Widow’s Thread | Veilweave Lash Grip + Veil-Silver Ribbon Lash + Hollow Canopy Core | 10 | 79/76 → 87/83 → 90/87 | 96 | 2.145 | 403 / 550 g |
| Iron Reins | Drover’s Wrapped Handle + Braided Oak Lash + Siegeheart Core | 7 | 25/49 → 27/54 → 28/56 | 75 | 1.95 | 163 / 214 g |
| Undertow Lash | Stormtide Swivel Handle + Barbed Drake-Sinew Lash + Tempest Bottle Core | 9 | 36/55 → 40/61 → 41/63 | 94 | 2.156 | 208 / 277 g |
| Cinder Ribbon | Veilweave Lash Grip + Belliron Chain Lash + Dragon Pact Ember Core | 10 | 51/68 → 56/74 → 58/77 | 98 | 2.106 | 275 / 371 g |
| Skyline Lash | Drover’s Wrapped Handle + Websilk Razor Lash + Skyward Seal Core | 9 | 41/55 → 45/61 → 47/63 | 73 | 1.833 | 204 / 271 g |
| Mooncord | Stormtide Swivel Handle + Drakeglass Segmented Lash + Observatory Heart Core | 10 | 67/59 → 73/65 → 76/67 | 108 | 2.34 | 280 / 378 g |
| Pressure Serpent | Veilweave Lash Grip + Veil-Silver Ribbon Lash + Overload Governor Core | 10 | 79/76 → 87/83 → 90/87 | 96 | 2.145 | 403 / 550 g |

### Scythe recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Tide Reaper | Reaper’s Farm Shaft + Harvest Iron Crescent + Tempest Bottle Core | 7 | 41/65 → 45/72 → 46/74 | 75 | 2.947 | 163 / 214 g |
| Ash Harvest | Gravewillow Crescent Haft + Gravehook Crescent + Dragon Pact Ember Core | 9 | 62/85 → 69/93 → 71/97 | 80 | 2.94 | 208 / 277 g |
| Storm Crescent | Last-Lantern Balance Shaft + Webglass Reaping Edge + Skyward Seal Core | 10 | 86/78 → 94/86 → 98/90 | 144 | 3.183 | 275 / 371 g |
| Moon’s Toll | Reaper’s Farm Shaft + Belliron Soul Crescent + Observatory Heart Core | 9 | 76/74 → 83/81 → 86/84 | 73 | 2.77 | 204 / 271 g |
| Clockwork Harvest | Gravewillow Crescent Haft + Froststeel Sickle Arc + Overload Governor Core | 10 | 112/90 → 123/99 → 128/103 | 92 | 3.192 | 280 / 378 g |
| Glasswind Requiem | Last-Lantern Balance Shaft + Null Obsidian Reaping Arc + Horizon Prism Core | 10 | 125/94 → 137/103 → 143/108 | 141 | 3.242 | 403 / 550 g |
| Pale Procession Scythe | Reaper’s Farm Shaft + Harvest Iron Crescent + Pale Procession Core | 7 | 41/65 → 45/72 → 46/74 | 75 | 2.947 | 163 / 214 g |
| Mist Mourner | Gravewillow Crescent Haft + Gravehook Crescent + Relic Memory Core | 9 | 62/85 → 69/93 → 71/97 | 80 | 2.94 | 208 / 277 g |
| Hunger’s Harvest | Last-Lantern Balance Shaft + Webglass Reaping Edge + Quiet Singularity Core | 10 | 86/78 → 94/86 → 98/90 | 144 | 3.183 | 275 / 371 g |
| Worldroot Reclaimer | Reaper’s Farm Shaft + Belliron Soul Crescent + Worldroot Seed Core | 10 | 81/110 → 89/121 → 92/126 | 73 | 2.77 | 339 / 460 g |
| First Furnace Reaper | Gravewillow Crescent Haft + Froststeel Sickle Arc + First Furnace Ember Core | 10 | 112/127 → 123/139 → 128/145 | 92 | 3.192 | 415 / 567 g |
| Stillwinter Requiem | Last-Lantern Balance Shaft + Null Obsidian Reaping Arc + Stillwinter Heart Core | 10 | 125/132 → 137/146 → 143/151 | 141 | 3.242 | 538 / 739 g |

### Cannon recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Moonshot | Scrapper’s Shoulder Frame + Riveted Iron Barrel + Observatory Heart Core | 7 | 55/74 → 61/82 → 63/85 | 83 | 4.0 | 163 / 214 g |
| Pressure Sermon | Rivetlock Recoil Cradle + Scatterbore Barrel + Overload Governor Core | 9 | 84/84 → 92/92 → 96/96 | 118 | 3.978 | 208 / 277 g |
| Horizon Breaker | Brasswick Vented Cannon Frame + Tidebronze Longbore + Horizon Prism Core | 10 | 117/109 → 129/120 → 134/125 | 92 | 3.888 | 275 / 371 g |
| Funeral Broadside | Sundial Artillery Frame + Springbrass Spiral Barrel + Pale Procession Core | 10 | 101/103 → 112/113 → 116/118 | 100 | 3.384 | 358 / 486 g |
| Veil Breach | Scrapper’s Shoulder Frame + Basalt Siege Barrel + Relic Memory Core | 9 | 143/84 → 157/92 → 163/96 | 102 | 4.56 | 246 / 331 g |
| Null Battery | Rivetlock Recoil Cradle + Prismatic Breach Barrel + Quiet Singularity Core | 10 | 169/108 → 186/118 → 194/123 | 123 | 4.168 | 358 / 486 g |
| Worldroot Salvo | Brasswick Vented Cannon Frame + Riveted Iron Barrel + Worldroot Seed Core | 10 | 67/154 → 73/169 → 76/176 | 84 | 3.6 | 376 / 513 g |
| First Furnace Mortar | Sundial Artillery Frame + Scatterbore Barrel + First Furnace Ember Core | 10 | 89/145 → 98/159 → 102/166 | 105 | 3.78 | 463 / 634 g |
| Stillwinter Battery | Scrapper’s Shoulder Frame + Tidebronze Longbore + Stillwinter Heart Core | 9 | 110/118 → 121/130 → 126/135 | 94 | 4.32 | 331 / 450 g |
| Lantern Thunder | Rivetlock Recoil Cradle + Springbrass Spiral Barrel + Unbound Funeral Star Core | 10 | 101/126 → 112/139 → 116/144 | 110 | 3.562 | 373 / 507 g |
| Prime Shardcaster | Brasswick Vented Cannon Frame + Basalt Siege Barrel + Prime Kettari Governor Core | 10 | 152/154 → 167/169 → 174/176 | 98 | 4.104 | 460 / 630 g |
| First Dawn Artillery | Sundial Artillery Frame + Prismatic Breach Barrel + Dawn Before Kings Core | 10 | 169/174 → 186/191 → 194/199 | 109 | 3.96 | 613 / 844 g |

### Gauntlet recipes

| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |
|---|---|---:|---|---:|---:|---|
| Lantern Fist | Pitfighter’s Wrist Brace + Plainsteel Knuckle Plate + Pale Procession Core | 7 | 20/30 → 22/33 → 23/34 | 68 | 1.091 | 163 / 214 g |
| Mist Palm | Scale-Laced Knuckle Frame + Wyrmfang Knuckle Row + Relic Memory Core | 9 | 30/34 → 33/38 → 34/39 | 118 | 1.326 | 208 / 277 g |
| Hunger Knuckle | Springbrass Piston Brace + Belliron Palm Plate + Quiet Singularity Core | 10 | 42/42 → 46/46 → 48/48 | 98 | 1.296 | 275 / 371 g |
| Worldroot Grasp | Pitfighter’s Wrist Brace + Springbrass Ram Knuckle + Worldroot Seed Core | 10 | 42/51 → 46/56 → 48/59 | 66 | 1.026 | 339 / 460 g |
| Furnace Piston | Scale-Laced Knuckle Frame + Froststeel Talon Plate + First Furnace Ember Core | 10 | 50/51 → 55/56 → 57/59 | 135 | 1.44 | 415 / 567 g |
| Winter Claw | Springbrass Piston Brace + Veil-Silver Channel Knuckle + Stillwinter Heart Core | 10 | 64/66 → 71/73 → 73/75 | 96 | 1.32 | 538 / 739 g |
| Funeral Hand | Pitfighter’s Wrist Brace + Plainsteel Knuckle Plate + Unbound Funeral Star Core | 8 | 22/45 → 24/50 → 25/52 | 68 | 1.091 | 298 / 403 g |
| Prime Impact | Scale-Laced Knuckle Frame + Wyrmfang Knuckle Row + Prime Kettari Governor Core | 10 | 32/51 → 35/56 → 36/59 | 118 | 1.326 | 343 / 465 g |
| Dawnbringer’s Grip | Springbrass Piston Brace + Belliron Palm Plate + Dawn Before Kings Core | 10 | 42/59 → 46/65 → 48/67 | 98 | 1.296 | 410 / 560 g |
| Briar Knuckle | Pitfighter’s Wrist Brace + Springbrass Ram Knuckle + Heart of the Old Grove Core | 9 | 39/34 → 43/38 → 45/39 | 66 | 1.026 | 204 / 271 g |
| Ashboxer | Scale-Laced Knuckle Frame + Froststeel Talon Plate + Ashen Crown Core | 10 | 50/36 → 55/40 → 57/42 | 135 | 1.44 | 280 / 378 g |
| Whiteclaw | Springbrass Piston Brace + Veil-Silver Channel Knuckle + Glacial Heart Core | 10 | 64/47 → 71/52 → 73/54 | 96 | 1.32 | 403 / 550 g |

## Gathering stocks

These exact stock quantities feed the shaping recipes in catalog.json. Sites are newly authored proposals, not existing placed game objects.

| Stock | Territory | Harvest site | Buy / sell gold |
|---|---|---|---|
| Ironbark Heartwood | ravenwood | Old Watch Trail | 8 / 2 |
| Blackthorn Iron | ravenwood | Rootbound Quarry | 14 / 4 |
| Cinderwood | ashen_wastes | Cinder Terraces | 10 / 3 |
| Basalt Iron | ashen_wastes | Cooling Galleries | 16 / 4 |
| Rimepine | frostpeaks | White Pass | 12 / 3 |
| Froststeel Ore | frostpeaks | Blue Ice Galleries | 18 / 5 |
| Drake Sinew | drakeshard_range | Broodfall Ledges | 14 / 4 |
| Scaleiron | drakeshard_range | Highland Scree | 20 / 5 |
| Dunepalm Heartwood | golden_expanse | Buried Caravan Wells | 16 / 4 |
| Sunbronze | golden_expanse | Sunken Foundry | 22 / 6 |
| Bogroot Fiber | blighted_marsh | Reedkeeper Pools | 18 / 5 |
| Mire Iron | blighted_marsh | Drowned Kilns | 24 / 6 |
| Gravewillow | cursed_mire | Bound Marsh | 20 / 5 |
| Hexstone | cursed_mire | Curse Anchor Ruins | 26 / 7 |
| Gloamwood | shadowfen_forest | Silent Canopy | 22 / 6 |
| Webglass | shadowfen_forest | Spider Reliquary | 28 / 7 |
| Warhorse Sinew | iron_plains | Remount Fields | 24 / 6 |
| Tempered Plainsteel | iron_plains | Abandoned Siegeworks | 30 / 8 |
| Saltbound Oak | veiled_sea | Shipwright Strand | 26 / 7 |
| Tidebronze | veiled_sea | Wreck Shoals | 32 / 8 |
| Ashsail Cord | ember_coast | Scorched Rookery | 28 / 7 |
| Drakeglass | ember_coast | Obsidian Tidepools | 34 / 9 |
| Storm Cedar | stormcrown_keep | Split Summit | 30 / 8 |
| Thundersteel | stormcrown_keep | Wardkeeper Mines | 36 / 9 |
| Moon Yew | moonfall_highlands | Observatory Orchard | 32 / 8 |
| Star Slate | moonfall_highlands | Fallen Lens Crater | 38 / 10 |
| Oiled Reed Cord | copperfen_basin | Canal Reeds | 34 / 9 |
| Springbrass | copperfen_basin | Collapsed Pumpworks | 40 / 10 |
| Windreed | glasswind_steppe | Whistling Flats | 36 / 9 |
| Singing Quartz | glasswind_steppe | Glass Ridge | 42 / 11 |
| Shroud Thread | deadwind_hollow | Silent Cloister | 38 / 10 |
| Belliron | deadwind_hollow | Broken Belfry | 44 / 11 |
| Mist Silk | mistvale | Cloud Orchard | 40 / 10 |
| Veil Silver | mistvale | Forgotten Aqueduct | 46 / 12 |
| Rift Tendon | devouring_deep | Outer Fracture | 42 / 11 |
| Null Obsidian | devouring_deep | Drowned Watch Ruins | 48 / 12 |

## Salvage items and recombination

These 96 salvage items are additional to the 200 assembly components and 36 gathering stocks. Salvage cannot be bought. Values are appraisal / merchant buyback.

| Salvage item | Value / sell gold | Combine |
|---|---|---|
| Thornseed Core Shard | 22 / 2 | 5 pieces + 28 gold → Thornseed Core |
| Huntsman’s Echo Core Shard | 52 / 5 | 5 pieces + 65 gold → Huntsman’s Echo Core |
| Heart of the Old Grove Core Shard | 102 / 10 | 5 pieces + 128 gold → Heart of the Old Grove Core |
| Cinder Pearl Core Shard | 22 / 2 | 5 pieces + 28 gold → Cinder Pearl Core |
| Magma Heart Core Shard | 52 / 5 | 5 pieces + 65 gold → Magma Heart Core |
| Ashen Crown Core Shard | 102 / 10 | 5 pieces + 128 gold → Ashen Crown Core |
| Rime Shard Core Shard | 22 / 2 | 5 pieces + 28 gold → Rime Shard Core |
| Whiteout Eye Core Shard | 52 / 5 | 5 pieces + 65 gold → Whiteout Eye Core |
| Glacial Heart Core Shard | 102 / 10 | 5 pieces + 128 gold → Glacial Heart Core |
| Drake Ember Core Shard | 22 / 2 | 5 pieces + 28 gold → Drake Ember Core |
| Scale Resonance Core Shard | 52 / 5 | 5 pieces + 65 gold → Scale Resonance Core |
| Brood Oath Core Shard | 102 / 10 | 5 pieces + 128 gold → Brood Oath Core |
| Sunwell Spark Core Shard | 22 / 2 | 5 pieces + 28 gold → Sunwell Spark Core |
| Mirage Eye Core Shard | 52 / 5 | 5 pieces + 65 gold → Mirage Eye Core |
| Buried Dawn Core Shard | 102 / 10 | 5 pieces + 128 gold → Buried Dawn Core |
| Adder Bile Core Shard | 22 / 2 | 5 pieces + 28 gold → Adder Bile Core |
| Mire Lantern Core Shard | 52 / 5 | 5 pieces + 65 gold → Mire Lantern Core |
| Rotmother Spore Core Shard | 102 / 10 | 5 pieces + 128 gold → Rotmother Spore Core |
| Grave Ember Core Shard | 22 / 2 | 5 pieces + 28 gold → Grave Ember Core |
| Hexbound Tear Core Shard | 52 / 5 | 5 pieces + 65 gold → Hexbound Tear Core |
| Anchorless Soul Core Shard | 102 / 10 | 5 pieces + 128 gold → Anchorless Soul Core |
| Gloam Mote Core Shard | 22 / 2 | 5 pieces + 28 gold → Gloam Mote Core |
| Widow’s Knot Core Shard | 52 / 5 | 5 pieces + 65 gold → Widow’s Knot Core |
| Hollow Canopy Core Shard | 102 / 10 | 5 pieces + 128 gold → Hollow Canopy Core |
| Marching Spark Core Shard | 22 / 2 | 5 pieces + 28 gold → Marching Spark Core |
| Warhorn Echo Core Shard | 52 / 5 | 5 pieces + 65 gold → Warhorn Echo Core |
| Siegeheart Core Shard | 102 / 10 | 5 pieces + 128 gold → Siegeheart Core |
| Salt Pearl Core Shard | 22 / 2 | 5 pieces + 28 gold → Salt Pearl Core |
| Undertow Knot Core Shard | 52 / 5 | 5 pieces + 65 gold → Undertow Knot Core |
| Tempest Bottle Core Shard | 102 / 10 | 5 pieces + 128 gold → Tempest Bottle Core |
| Coalglass Ember Core Shard | 22 / 2 | 5 pieces + 28 gold → Coalglass Ember Core |
| Cinderwake Pearl Core Shard | 52 / 5 | 5 pieces + 65 gold → Cinderwake Pearl Core |
| Dragon Pact Ember Core Shard | 102 / 10 | 5 pieces + 128 gold → Dragon Pact Ember Core |
| Stormglass Spark Core Shard | 22 / 2 | 5 pieces + 28 gold → Stormglass Spark Core |
| Thundercoil Core Shard | 52 / 5 | 5 pieces + 65 gold → Thundercoil Core |
| Skyward Seal Core Shard | 102 / 10 | 5 pieces + 128 gold → Skyward Seal Core |
| Moonlit Flake Core Shard | 22 / 2 | 5 pieces + 28 gold → Moonlit Flake Core |
| Fallen Star Core Shard | 52 / 5 | 5 pieces + 65 gold → Fallen Star Core |
| Observatory Heart Core Shard | 102 / 10 | 5 pieces + 128 gold → Observatory Heart Core |
| Clockwork Spark Core Shard | 22 / 2 | 5 pieces + 28 gold → Clockwork Spark Core |
| Pressure Pearl Core Shard | 52 / 5 | 5 pieces + 65 gold → Pressure Pearl Core |
| Overload Governor Core Shard | 102 / 10 | 5 pieces + 128 gold → Overload Governor Core |
| Whisperglass Core Shard | 22 / 2 | 5 pieces + 28 gold → Whisperglass Core |
| Sand-Singer Core Shard | 52 / 5 | 5 pieces + 65 gold → Sand-Singer Core |
| Horizon Prism Core Shard | 102 / 10 | 5 pieces + 128 gold → Horizon Prism Core |
| Bell-Wraith Ember Core Shard | 22 / 2 | 5 pieces + 28 gold → Bell-Wraith Ember Core |
| Lantern Soul Core Shard | 52 / 5 | 5 pieces + 65 gold → Lantern Soul Core |
| Pale Procession Core Shard | 102 / 10 | 5 pieces + 128 gold → Pale Procession Core |
| Mist Dew Core Shard | 22 / 2 | 5 pieces + 28 gold → Mist Dew Core |
| Veilbound Star Core Shard | 52 / 5 | 5 pieces + 65 gold → Veilbound Star Core |
| Relic Memory Core Shard | 102 / 10 | 5 pieces + 128 gold → Relic Memory Core |
| Rift Cinder Core Shard | 22 / 2 | 5 pieces + 28 gold → Rift Cinder Core |
| Hunger Fragment Core Shard | 52 / 5 | 5 pieces + 65 gold → Hunger Fragment Core |
| Quiet Singularity Core Shard | 102 / 10 | 5 pieces + 128 gold → Quiet Singularity Core |
| Worldroot Seed Core Shard | 210 / 21 | 5 pieces + 263 gold → Worldroot Seed Core |
| First Furnace Ember Core Shard | 210 / 21 | 5 pieces + 263 gold → First Furnace Ember Core |
| Stillwinter Heart Core Shard | 210 / 21 | 5 pieces + 263 gold → Stillwinter Heart Core |
| Unbound Funeral Star Core Shard | 210 / 21 | 5 pieces + 263 gold → Unbound Funeral Star Core |
| Prime Kettari Governor Core Shard | 210 / 21 | 5 pieces + 263 gold → Prime Kettari Governor Core |
| Dawn Before Kings Core Shard | 210 / 21 | 5 pieces + 263 gold → Dawn Before Kings Core |
| Degraded Ironbark Heartwood | 2 / 0 | 4 pieces + 5 gold → Ironbark Heartwood |
| Degraded Blackthorn Iron | 4 / 0 | 4 pieces + 5 gold → Blackthorn Iron |
| Degraded Cinderwood | 3 / 0 | 4 pieces + 5 gold → Cinderwood |
| Degraded Basalt Iron | 4 / 0 | 4 pieces + 5 gold → Basalt Iron |
| Degraded Rimepine | 3 / 0 | 4 pieces + 5 gold → Rimepine |
| Degraded Froststeel Ore | 5 / 0 | 4 pieces + 5 gold → Froststeel Ore |
| Degraded Drake Sinew | 4 / 0 | 4 pieces + 5 gold → Drake Sinew |
| Degraded Scaleiron | 5 / 0 | 4 pieces + 5 gold → Scaleiron |
| Degraded Dunepalm Heartwood | 4 / 0 | 4 pieces + 5 gold → Dunepalm Heartwood |
| Degraded Sunbronze | 6 / 0 | 4 pieces + 5 gold → Sunbronze |
| Degraded Bogroot Fiber | 5 / 0 | 4 pieces + 5 gold → Bogroot Fiber |
| Degraded Mire Iron | 6 / 0 | 4 pieces + 5 gold → Mire Iron |
| Degraded Gravewillow | 5 / 0 | 4 pieces + 5 gold → Gravewillow |
| Degraded Hexstone | 7 / 0 | 4 pieces + 5 gold → Hexstone |
| Degraded Gloamwood | 6 / 0 | 4 pieces + 5 gold → Gloamwood |
| Degraded Webglass | 7 / 0 | 4 pieces + 5 gold → Webglass |
| Degraded Warhorse Sinew | 6 / 0 | 4 pieces + 5 gold → Warhorse Sinew |
| Degraded Tempered Plainsteel | 8 / 0 | 4 pieces + 5 gold → Tempered Plainsteel |
| Degraded Saltbound Oak | 7 / 0 | 4 pieces + 5 gold → Saltbound Oak |
| Degraded Tidebronze | 8 / 0 | 4 pieces + 5 gold → Tidebronze |
| Degraded Ashsail Cord | 7 / 0 | 4 pieces + 5 gold → Ashsail Cord |
| Degraded Drakeglass | 9 / 1 | 4 pieces + 5 gold → Drakeglass |
| Degraded Storm Cedar | 8 / 0 | 4 pieces + 5 gold → Storm Cedar |
| Degraded Thundersteel | 9 / 1 | 4 pieces + 5 gold → Thundersteel |
| Degraded Moon Yew | 8 / 0 | 4 pieces + 5 gold → Moon Yew |
| Degraded Star Slate | 10 / 1 | 4 pieces + 5 gold → Star Slate |
| Degraded Oiled Reed Cord | 9 / 1 | 4 pieces + 5 gold → Oiled Reed Cord |
| Degraded Springbrass | 10 / 1 | 4 pieces + 5 gold → Springbrass |
| Degraded Windreed | 9 / 1 | 4 pieces + 5 gold → Windreed |
| Degraded Singing Quartz | 11 / 1 | 4 pieces + 5 gold → Singing Quartz |
| Degraded Shroud Thread | 10 / 1 | 4 pieces + 5 gold → Shroud Thread |
| Degraded Belliron | 11 / 1 | 4 pieces + 5 gold → Belliron |
| Degraded Mist Silk | 10 / 1 | 4 pieces + 5 gold → Mist Silk |
| Degraded Veil Silver | 12 / 1 | 4 pieces + 5 gold → Veil Silver |
| Degraded Rift Tendon | 11 / 1 | 4 pieces + 5 gold → Rift Tendon |
| Degraded Null Obsidian | 12 / 1 | 4 pieces + 5 gold → Null Obsidian |
