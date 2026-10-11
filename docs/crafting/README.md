# Entropic Forge design library

Balance draft 0.1.0. This is authored game design data, not a connected inventory or combat implementation. The hidden-strike concept and forge story come from the agreed design; specific component names, gold values, equations, effects and quest requirements are proposals for testing.

## Read the catalog

- [Full component and weapon catalog](CATALOG.md): every component, price, hidden strike contribution, trait, core effect and all 180 named assemblies.
- [Courier story](COURIER_STORY.md): 18 regional commissions, Mistvale restoration, the book awakening and the final desert investigations.
- [Component table](components.csv) and [weapon table](weapons.csv): flat exports for sorting and comparing.
- [Complete structured catalog](../../data/crafting/catalog.json): gathering sources, exact shaping quantities, page membership and six calculated outcomes per named weapon.
- [Combat effects](../../data/crafting/effects.json), [system rules](../../data/crafting/rules.json) and [quest gates](../../data/crafting/courier_story.json).

## The library's scope

| Content | Count | Purpose |
|---|---:|---|
| Frameworks | 50 | Class, rig, speed, handling, reach and base durability |
| Strikers | 90 | Physical attack, damage type, action weight and combat trait |
| Entropic cores | 60 | Element, effect, volatility and burst behavior |
| Salvage items | 96 | Sixty core shard identities and 36 degraded stock identities |
| Gathering stocks | 36 | Exact inputs for shaping frameworks and strikers |
| Weapon families | 15 | Sword, greatsword, dagger, spear, axe, hammer, mace, staff, wand, bow, crossbow, whip, scythe, cannon and gauntlet |
| Named discoveries | 180 | Twelve authored combinations per family |
| Legal assemblies | 18,000 | Every framework with six same-family strikers and any of 60 cores |

A player assembles one framework, one compatible striker and one core. A recipe's name is a memorable alias for its exact parts, not a fourth stat bonus. Experimentation works before its recipe is found. The book makes knowledge reliable and gives exploration a purpose.

All core types work in all families. A slow hammer can carry a healing effect, a bow can carry magma, and a dagger can carry a control effect. Family scaling and once-per-action effect rolls keep this freedom from making rapid multi-hit weapons automatically dominant. Part compatibility is explicit; a sword blade does not attach to a bow riser. Bow limbs, crossbow prods and cannon barrels occupy the striker slot.

The 18 source regions include atlas locations beyond the 13 hero groups. These do not add or alter hero assignments. Gathering sites and new courier contacts are proposed placements. Regional materials remain accessible with either hero choice.

## Reading the values

Physical and elemental attack are separate, pre-defense weapon contributions. They are not guaranteed enemy HP loss. Seconds/action is a balance interval for comparison and future combat integration; it does not settle the final animation or turn system. Attack budget/second excludes accuracy, critical hits, armor, area coverage and utility, so it is not a definitive weapon ranking. Reach is in world meters, with board-to-battle scale still to be fixed. Accuracy is a percentage; base critical chance is 5% and direct critical damage is 1.5×.

Gold appraisal communicates worth. Buy price exists only when a merchant can stock that component; a blank buy price means unavailable for purchase, not free. Sell prices are deliberately below acquisition costs. Components consume exactly one inventory item each when assembled. Raw stock, elemental core shards and degraded salvage are separate inventory categories.

Frameworks and strikers have explicit shaping recipes. Workshop rank 1 handles common/uncommon parts, rank 2 handles rare parts, rank 3 handles relic/exalted parts. Regional restoration and mastery unlock these facilities without requiring a particular hero. The book does not act as a permission lock. Blackthorn can have an ordinary workshop without granting access to an Entropic forge.

Common raw stocks can be bought when locally available; field collection saves gold. Rarer cores come from elites, recovered vaults and regional mastery. All have an eventual repeatable source so using a precious cracked weapon never permanently removes that build from a playthrough. Apex cores stay difficult to replace. The Unbound Funeral Star requires liberation of both Cursed Mire and Deadwind Hollow.

## Exact forge model

Let `P0` be striker attack after its physical trait, `E0` be core attack after family and component elemental factors, and `D0` be framework plus striker durability after the framework's durability trait. Let `L` be the hidden effective strike limit:

```
L = min(10, framework contribution + striker contribution + core contribution + skill bonus)
skill bonus = 0, 1, 2 or 3
curve = 2^((L - 2) / 8) - 1
standard perfect multiplier = 1.10 + 0.65 × curve
Mistvale perfect multiplier = standard perfect multiplier × 1.10
Sands perfect multiplier = 1.25 + 0.75 × curve
```

At `L = 10`, these give 175%, 192.5% and 200% total attack. Sands replaces the earlier curve; it does not multiply Mistvale's bonus. The improved starting point also ensures Sands is stronger at low limits. Integer output values round half-up only after calculation.

There is a universal 15-blow input maximum for every combination. A cap relative to the hidden limit would reveal the answer, so the interface must never stop at `L + some number`. There are no warning colors, sounds, meters or timing changes before crossing the limit. A discovered page can reveal its component's contribution; the player can then calculate the limit with their skill bonus. No UI may reveal another component's hidden contribution by inference from an unearned total.

### Under-struck

For `n < L`, `r = n / L`:

```
P = P0 × (0.35 + 0.65r) × under-forge factor
E = E0 × (0.50 + 0.50r) × under-forge factor
durability = D0 + round((perfect P - P) × 0.80)
under-forge factor = 1.00 standard, 1.10 Mistvale, 1.15 Sands
```

Unrealized physical attack becomes durability. Elemental attack also falls, but does not separately create more durability. This makes stopping early a deliberate endurance build rather than a failed Masterwork. Conversion strength is a tuning parameter; dungeon-length testing must determine whether it offers enough value.

### Masterwork

At exactly `n = L`, multiply both attack channels by the forge's perfect multiplier and retain `D0`. Skill changes the hidden target and its reward; more crafting skill does not add a visible warning. Skill and forge are frozen into the created item so a later respec cannot alter it.

### Cracked

Let `o = n - L` and core volatility `v` range from 1 to 4:

```
physical = perfect P × 0.80
elemental = perfect E × (1 + (0.35 + 0.05(v - 1)) × o)
hidden durability center = round(D0 × max(0.05, 0.28 × 0.62^(o - 1)))
```

On finalization, hidden durability is sampled uniformly between floor(60%) and ceil(140%) of that center, with a minimum of one. Each offensive weapon action consumes 1–3 hidden points. The item breaks when remaining durability reaches or crosses zero. This prevents exact hit counting from becoming a substitute durability meter. Save/load retains the roll and RNG progression. The range exists only in designer data, never in the player's item view.

An intact weapon consumes one durability per offensive weapon action. Multi-hit abilities pay once per action; healing, guarding and unrelated magic do not spend weapon durability. An intact weapon exhausted in combat becomes unusable until repaired and does not explode. Proposed intact repair price: 20% of component appraisal times the fraction missing, rounded up to at least one gold when damage exists. Cracked weapons cannot be repaired or restored to an intact state.

Crossing the limit may change the finished weapon's appearance, but further wear has no escalating crack animation, glow, sound or countdown. The inventory says **Cracked — unstable** and shows its offensive properties, never current or maximum remaining durability. Its core effect chance gains four percentage points per excess strike, capped at 50%; effect magnitude does not scale again.

### Terminal burst and tinkerer payloads

```
burst attack budget = (P0 + E0) × perfect multiplier × (2 + 0.4o) × (1 + 0.08(v - 1))
burst radius = min(5, 2.5 + 0.3o + core radius bonus) meters
```

The triggering attack resolves, then the weapon is consumed and the burst resolves once. Everyone in range, including the wielder and allies, can be hit. Armor/resistance integration will determine final damage. Burst and secondary effects cannot recursively roll weapon effects or cause duplicate explosions.

Tessa's learned cannon ability and Tobin's learned device ability consume one cracked weapon as their entire payload. They use the same terminal budget, regardless of how much hidden life remained. Proposed costs are one full action and 14/18 MP respectively; these are balance proposals, not a new combat-system commitment. Tobin may deploy one device at a time. Payload is removed before its effect resolves. Normal cannon attacks do not automatically consume a second weapon.

Destroying a weapon leaves two same-core shards and two degraded stocks. A payload leaves one shard and two degraded stocks. Five shards plus 25% of the core's appraisal fuse into the same discovered core. Four degraded pieces of one raw material plus five gold recover one raw stock. Salvage must be recovered at the aftermath site. Nothing returns all three original parts.

## Discovery and visual progression

The first courier assignment grants the ancient ledger on acceptance. Eighteen regional folios gradually disclose sources, hidden contributions and the named recipes. Commissions include gathering across multiple regions, rescues, repairs, recovery, escorts and delivery. They are permanent and optional, without expiration. The player chooses among accessible regions; the questline never forces a linear main campaign.

Mistvale's restored relic stands outside the city and feels like the story's final reward. Its first completed craft triggers the book's response and reveals the map into the sands. Any finalized state qualifies; opening a preview or cancelling does not. The secret chapter must not appear as a locked quest, map silhouette or missing completion entry beforehand.

The final forge restructures the metal into a smooth, hard finish: silver, gold and bright yellow static. The original core effect remains legible. A magma weapon still carries magma; an ancient finish never silently changes it to lightning. Cracked ancient weapons preserve their dangerous leakage and friendly-fire risk.

## Integration and remaining balance work

The catalog supplies stable IDs and data, not 18,000 meshes. Each family uses shared rigs and base geometry, striker variants define silhouettes, and component materials/core effects provide visual variety. Attach the assembled weapon at one skeletal socket. Cities and dungeons retain the agreed layered 2D scenery with depth-aware occlusion; the catalog does not replace that direction with fully modeled rooms.

Before production integration, test encounter damage, defenses, resistances, animation timing, inventory limits, elemental identities and MP costs. Run short and long dungeon trials with endurance, Masterwork and cracked builds. Preserve found and purchased weapons with their own identities and useful benefits. Core control effects need boss substitutes and immunity rules. The 332 inventory definitions comprise 200 assembly parts, 36 gathering stocks and 96 salvage identities; courier-only quest objects are outside this inventory catalog. Economy checks cover direct buy/shape/sell and salvage loops, not a simulated campaign economy.

Rebuild with `python tools/build_crafting_catalog.py` then `python tools/build_courier_story.py`. Validate with `python tools/validate_crafting_catalog.py`. These scripts must stay outside player-facing data-loading paths: the designer files intentionally contain hidden values and story spoilers.
