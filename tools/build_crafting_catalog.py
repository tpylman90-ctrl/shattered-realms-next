#!/usr/bin/env python3
"""Authoritative authoring inputs and reproducible balance-v1 catalog export.
Design data only: this is not connected to the Godot inventory or combat runtime.
"""
import csv, json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data/crafting'; DOC=ROOT/'docs/crafting'
OUT.mkdir(parents=True,exist_ok=True); DOC.mkdir(parents=True,exist_ok=True)
def slug(s): return re.sub(r'[^a-z0-9]+','_',s.lower()).strip('_')
def dump(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def rnd(x): return math.floor(x+0.5)
# id, label, soft stock, hard stock, harvest site, second site
REGIONS=[
('ravenwood','Ravenwood','Ironbark Heartwood','Blackthorn Iron','Old Watch Trail','Rootbound Quarry'),
('ashen_wastes','Ashen Wastes','Cinderwood','Basalt Iron','Cinder Terraces','Cooling Galleries'),
('frostpeaks','Frostpeaks','Rimepine','Froststeel Ore','White Pass','Blue Ice Galleries'),
('drakeshard_range','Drakeshard Range','Drake Sinew','Scaleiron','Broodfall Ledges','Highland Scree'),
('golden_expanse','Golden Expanse','Dunepalm Heartwood','Sunbronze','Buried Caravan Wells','Sunken Foundry'),
('blighted_marsh','Blighted Marsh','Bogroot Fiber','Mire Iron','Reedkeeper Pools','Drowned Kilns'),
('cursed_mire','Cursed Mire','Gravewillow','Hexstone','Bound Marsh','Curse Anchor Ruins'),
('shadowfen_forest','Shadowfen Forest','Gloamwood','Webglass','Silent Canopy','Spider Reliquary'),
('iron_plains','Iron Plains','Warhorse Sinew','Tempered Plainsteel','Remount Fields','Abandoned Siegeworks'),
('veiled_sea','Veiled Sea','Saltbound Oak','Tidebronze','Shipwright Strand','Wreck Shoals'),
('ember_coast','Ember Coast','Ashsail Cord','Drakeglass','Scorched Rookery','Obsidian Tidepools'),
('stormcrown_keep','Stormcrown Mountains','Storm Cedar','Thundersteel','Split Summit','Wardkeeper Mines'),
('moonfall_highlands','Moonfall Highlands','Moon Yew','Star Slate','Observatory Orchard','Fallen Lens Crater'),
('copperfen_basin','Copperfen Basin','Oiled Reed Cord','Springbrass','Canal Reeds','Collapsed Pumpworks'),
('glasswind_steppe','Glasswind Steppe','Windreed','Singing Quartz','Whistling Flats','Glass Ridge'),
('deadwind_hollow','Deadwind Hollow','Shroud Thread','Belliron','Silent Cloister','Broken Belfry'),
('mistvale','Mistvale','Mist Silk','Veil Silver','Cloud Orchard','Forgotten Aqueduct'),
('devouring_deep','Devouring Deep','Rift Tendon','Null Obsidian','Outer Fracture','Drowned Watch Ruins'),
]
# family, hands, interval seconds, physical coefficient, elemental coefficient, reach m, accuracy %, tags
FAMILY_SPECS=[
('sword',1,1.8,1.0,1.0,1.5,94,['Vanguard','Guardian']),
('greatsword',2,3.0,1.7,1.5,2.0,89,['Heavy','Vanguard']),
('dagger',1,1.05,.62,.60,.9,97,['Skirmisher','Precision']),
('spear',2,2.2,1.2,1.05,3.0,95,['Guardian','Precision']),
('axe',1,2.1,1.18,1.0,1.4,89,['Vanguard','Heavy']),
('hammer',2,3.2,1.85,1.5,1.7,85,['Heavy','Control']),
('mace',1,2.05,1.12,1.0,1.3,92,['Guardian','Control']),
('staff',2,2.5,.62,1.7,2.2,93,['Caster','Control']),
('wand',1,1.5,.32,1.15,6.0,96,['Caster','Precision']),
('bow',2,2.2,1.10,1.10,14.0,92,['Ranger','Precision']),
('crossbow',2,2.9,1.55,1.35,12.0,95,['Ranger','Heavy']),
('whip',1,1.95,.83,1.05,3.8,90,['Skirmisher','Control']),
('scythe',2,2.8,1.4,1.4,2.6,87,['Reaper','Control']),
('cannon',2,3.6,1.9,1.6,10.0,84,['Artificer','Heavy']),
('gauntlet',1,1.2,.68,.65,.8,96,['Brawler','Skirmisher']),
]
FRAME_NAMES={
'sword':['Watchman’s Leather Grip','Duelist’s Tideguard','Sentinel’s Ironbark Hilt','Sunbound Filigree Hilt'],
'greatsword':['Militia Longgrip','Drakespine Wargrip','Black Anvil Twohander'],
'dagger':['Poacher’s Thumbgrip','Websilk Loop Grip','Mirage Balanced Tang'],
'spear':['Ranger’s Ash Haft','Rimepine Lance Shaft','Stormkeeper Spear Haft','Oathroot Longshaft'],
'axe':['Woodcutter’s Haft','Corsair’s Hook Haft','Cinderbrace Split Haft'],
'hammer':['Quarryman’s Haft','Siegebreaker Shock Haft','Thunderbrow Pattern Haft'],
'mace':['Gateward Handle','Reedbound Cudgel Haft','Lanternkeeper Flanged Grip'],
'staff':['Herbalist’s Bogroot Staff','Gloamwood Channel Staff','Veil-Silver Casting Shaft','Astral Spiral Staff'],
'wand':['Apprentice’s Yew Handle','Crystal-Focus Wand Grip','Dawnweaver Conductor'],
'bow':['Scout’s Ironbark Riser','Recurve Sinew Riser','Moon-Yew Longbow Riser','Glasswind Split Riser'],
'crossbow':['Militia Oak Stock','Marine Ratchet Stock','Cogspire Repeating Stock'],
'whip':['Drover’s Wrapped Handle','Stormtide Swivel Handle','Veilweave Lash Grip'],
'scythe':['Reaper’s Farm Shaft','Gravewillow Crescent Haft','Last-Lantern Balance Shaft'],
'cannon':['Scrapper’s Shoulder Frame','Rivetlock Recoil Cradle','Brasswick Vented Cannon Frame','Sundial Artillery Frame'],
'gauntlet':['Pitfighter’s Wrist Brace','Scale-Laced Knuckle Frame','Springbrass Piston Brace'],
}
# Six physically distinct compatible strikers per family; string/list ids follow family conventions.
STRIKER_NAMES={
'sword':['Plainsteel Straight Blade','Serrated Fang Blade','Tidebronze Saber Blade','Webglass Needle Blade','Scaleiron Falchion Blade','Veil-Silver Channel Blade'],
'greatsword':['Broad Militia Blade','Notched Siege Blade','Drakebone Cleaver','Basalt Execution Blade','Froststeel Flamberge','Null-Edge Colossus Blade'],
'dagger':['Watchman’s Point','Hollow Adder Fang','Glasswind Stiletto','Barbed Webglass Point','Belliron Ritual Blade','Star-Slate Crescent'],
'spear':['Iron Leaf Spearhead','Wyrmtooth Pikehead','Sunbronze Winged Head','Stormsteel Fork','Froststeel Lance Tip','Hollow Veil-Silver Point'],
'axe':['Forester’s Axe Bit','Raider’s Hook Bit','Drakeglass Bearded Edge','Bog-Iron Hewing Head','Basalt Double Bit','Star-Slate Crescent Bit'],
'hammer':['Quarry Iron Block','Siege Ram Head','Resonant Belliron Head','Basalt Furnace Head','Scaleiron Shatter Head','Singing-Quartz Impact Head'],
'mace':['Gatewatch Iron Ball','Thorn-Cage Head','Sunbronze Flanged Head','Hexstone Knob','Froststeel Crown','Veil-Silver Lantern Cage'],
'staff':['Carved Root Crown','Marsh-Bone Focus','Storm Fork Crown','Moon Lens Cradle','Hexstone Ritual Cage','Prismatic Silver Crown'],
'wand':['Copper Casting Tip','Adder-Fang Focus','Frostglass Prism','Sunbronze Aperture','Webglass Needle Focus','Star-Slate Lens'],
'bow':['Plain Yew Limbs','Recurved Drakebone Limbs','Moon-Yew Long Limbs','Websilk Composite Limbs','Froststeel Spring Limbs','Singing-Quartz Split Limbs'],
'crossbow':['Plainsteel Prod','Drake-Sinew Compound Prod','Marine Heavy Prod','Springbrass Repeater Prod','Froststeel Arbalest Prod','Star-Slate Resonance Prod'],
'whip':['Braided Oak Lash','Barbed Drake-Sinew Lash','Belliron Chain Lash','Websilk Razor Lash','Drakeglass Segmented Lash','Veil-Silver Ribbon Lash'],
'scythe':['Harvest Iron Crescent','Gravehook Crescent','Webglass Reaping Edge','Belliron Soul Crescent','Froststeel Sickle Arc','Null Obsidian Reaping Arc'],
'cannon':['Riveted Iron Barrel','Scatterbore Barrel','Tidebronze Longbore','Springbrass Spiral Barrel','Basalt Siege Barrel','Prismatic Breach Barrel'],
'gauntlet':['Plainsteel Knuckle Plate','Wyrmfang Knuckle Row','Belliron Palm Plate','Springbrass Ram Knuckle','Froststeel Talon Plate','Veil-Silver Channel Knuckle'],
}
# Unique region cores: element, core-specific behavior id, short name.
CORE_GROUPS=[
[('Thornseed','verdant','thorn_bind'),('Huntsman’s Echo','spirit','hunters_mark'),('Heart of the Old Grove','verdant','grove_guard')],
[('Cinder Pearl','fire','ignite'),('Magma Heart','magma','magma_pool'),('Ashen Crown','ash','ash_blind')],
[('Rime Shard','frost','chill'),('Whiteout Eye','frost','whiteout'),('Glacial Heart','frost','frost_guard')],
[('Drake Ember','fire','drake_scorch'),('Scale Resonance','earth','scale_break'),('Brood Oath','spirit','brood_guard')],
[('Sunwell Spark','solar','solar_mark'),('Mirage Eye','mirage','mirage_feint'),('Buried Dawn','solar','solar_purge')],
[('Adder Bile','venom','poison'),('Mire Lantern','verdant','cleanse_guard'),('Rotmother Spore','rot','rot_spread')],
[('Grave Ember','spirit','soul_scar'),('Hexbound Tear','curse','hex_weaken'),('Anchorless Soul','spirit','spirit_release')],
[('Gloam Mote','shadow','gloam_expose'),('Widow’s Knot','shadow','web_tether'),('Hollow Canopy','rot','canopy_decay')],
[('Marching Spark','earth','steadfast'),('Warhorn Echo','spirit','rally'),('Siegeheart','earth','siege_break')],
[('Salt Pearl','tide','salt_erosion'),('Undertow Knot','tide','undertow'),('Tempest Bottle','storm','squall')],
[('Coalglass Ember','fire','ember_trail'),('Cinderwake Pearl','magma','cinderwake'),('Dragon Pact Ember','fire','dragon_flare')],
[('Stormglass Spark','storm','shock'),('Thundercoil','storm','chain_arc'),('Skyward Seal','storm','ward_charge')],
[('Moonlit Flake','lunar','moon_expose'),('Fallen Star','astral','star_echo'),('Observatory Heart','astral','gravity_well')],
[('Clockwork Spark','kinetic','recoil_charge'),('Pressure Pearl','kinetic','pressure_pulse'),('Overload Governor','storm','governed_overload')],
[('Whisperglass','wind','wind_cut'),('Sand-Singer','wind','sand_shear'),('Horizon Prism','mirage','horizon_pierce')],
[('Bell-Wraith Ember','spirit','bell_silence'),('Lantern Soul','spirit','lantern_ward'),('Pale Procession','curse','procession')],
[('Mist Dew','mist','mist_veil'),('Veilbound Star','astral','veil_echo'),('Relic Memory','astral','relic_release')],
[('Rift Cinder','void','rift_cut'),('Hunger Fragment','void','hunger'),('Quiet Singularity','void','singularity')],
]
APEX=[('Worldroot Seed','ravenwood','verdant','worldroot'),('First Furnace Ember','ashen_wastes','magma','first_furnace'),('Stillwinter Heart','frostpeaks','frost','stillwinter'),('Unbound Funeral Star','deadwind_hollow','spirit','funeral_star'),('Prime Kettari Governor','copperfen_basin','kinetic','prime_governor'),('Dawn Before Kings','golden_expanse','solar','first_dawn')]
# Shared proc rules below give these concise behaviors exact numerical meaning.
EFFECT_SPECS={
 'thorn_bind':('root',1,0,'Root for 1 action; boss substitute: -8% action speed.'),
 'hunters_mark':('marked',2,12,'Next allied hit gains +12% accuracy for 2 actions; mark consumed on hit.'),
 'grove_guard':('barrier',2,12,'Wielder gains a barrier equal to 12% of base physical + elemental attack for 2 actions.'),
 'ignite':('burn',2,18,'Burn deals 18% of base elemental attack per action for 2 actions.'),
 'magma_pool':('ground_damage',2,20,'Leaves a 1.2 m pool for 2 actions, dealing 20% base elemental attack to all occupants each action.'),
 'ash_blind':('accuracy_down',2,10,'Target loses 10 accuracy points for 2 actions.'),
 'chill':('speed_down',2,12,'Target action speed -12% for 2 actions.'),
 'whiteout':('accuracy_down',2,15,'Target loses 15 accuracy points for 2 actions.'),
 'frost_guard':('barrier',2,15,'Wielder barrier = 15% base physical + elemental attack, lasting 2 actions.'),
 'drake_scorch':('armor_down',2,8,'Physical armor -8% for 2 actions.'),
 'scale_break':('armor_down',2,12,'Physical armor -12% for 2 actions.'),
 'brood_guard':('guard',1,10,'Wielder takes 10% less physical damage until its next action.'),
 'solar_mark':('marked',2,10,'Next allied hit adds 10% base elemental solar damage; mark consumed.'),
 'mirage_feint':('evasion',1,8,'Wielder gains 8 evasion points until its next action.'),
 'solar_purge':('dispel',0,1,'Remove 1 removable positive effect from the struck enemy.'),
 'poison':('poison',3,12,'Poison deals 12% base elemental attack per action for 3 actions.'),
 'cleanse_guard':('cleanse',0,1,'Remove 1 poison stack from the wielder.'),
 'rot_spread':('rot',2,18,'Rot deals 18% base elemental per action for 2 actions; on death transfers remaining duration to 1 enemy within 2 m.'),
 'soul_scar':('healing_down',2,20,'Target receives 20% less healing for 2 actions.'),
 'hex_weaken':('attack_down',2,10,'Target physical attack -10% for 2 actions.'),
 'spirit_release':('undead_damage',0,25,'Add spirit damage = 25% base elemental attack against undead only.'),
 'gloam_expose':('evasion_down',2,10,'Target loses 10 evasion points for 2 actions.'),
 'web_tether':('root',1,0,'Root for 1 action; boss substitute: -8% action speed.'),
 'canopy_decay':('resistance_down',2,10,'Target rot resistance -10 percentage points for 2 actions.'),
 'steadfast':('displacement_resist',1,50,'Wielder gains 50% displacement resistance until its next action.'),
 'rally':('next_hit',1,10,'Wielder’s next direct hit gains 10% base physical damage; cannot stack.'),
 'siege_break':('barrier_damage',0,30,'Deal an additional 30% base physical + elemental attack to barriers only.'),
 'salt_erosion':('armor_down',2,8,'Physical armor -8% for 2 actions.'),
 'undertow':('pull',0,1,'Pull target 1 m toward the wielder; immune targets take 10% base elemental tide damage instead.'),
 'squall':('splash',0,15,'Deal 15% base elemental storm damage to 1 extra enemy within 2 m.'),
 'ember_trail':('ground_damage',2,15,'Leave a 1 m trail at target for 2 actions, dealing 15% base elemental to all occupants each action.'),
 'cinderwake':('ground_damage',2,25,'Leave a 1.5 m patch for 2 actions, dealing 25% base elemental to all occupants each action.'),
 'dragon_flare':('splash',0,25,'Deal 25% base elemental fire damage to at most 2 extra enemies within 2 m.'),
 'shock':('atb_delay',0,8,'Remove 8 percentage points from target ATB; once per target action.'),
 'chain_arc':('chain',0,20,'Jump to at most 2 different enemies within 2 m for 20% base elemental storm damage each.'),
 'ward_charge':('magic_guard',1,12,'Wielder takes 12% less elemental damage until its next action.'),
 'moon_expose':('critical_resist_down',2,6,'Target critical resistance -6 points for 2 actions.'),
 'star_echo':('echo',0,20,'Add one astral pulse of 20% base elemental attack; pulse cannot trigger procs.'),
 'gravity_well':('pull',0,1.5,'Pull struck target up to 1.5 m toward its nearest enemy ally; immune targets take 15% base elemental astral damage instead.'),
 'recoil_charge':('next_hit',1,12,'Next direct physical hit gains 12% base physical damage; cannot stack.'),
 'pressure_pulse':('push',0,1,'Push target 1 m away; immune targets take 10% base elemental kinetic damage instead.'),
 'governed_overload':('splash',0,25,'Deal 25% base elemental storm damage to 1 extra enemy within 2 m. Does not reveal cracked durability.'),
 'wind_cut':('armor_pierce_pulse',0,15,'Add 15% base elemental wind damage ignoring 20% resistance for this pulse.'),
 'sand_shear':('accuracy_down',2,12,'Target loses 12 accuracy points for 2 actions.'),
 'horizon_pierce':('line_pulse',0,25,'Add 25% base elemental mirage damage to the first enemy behind the target, within 3 m.'),
 'bell_silence':('silence',1,0,'Silence for 1 action; boss substitute: magic attack -8% for 1 action.'),
 'lantern_ward':('curse_guard',1,25,'Wielder gains 25 curse-resistance points until its next action.'),
 'procession':('healing_down',3,25,'Target receives 25% less healing for 3 actions.'),
 'mist_veil':('evasion',1,6,'Wielder gains 6 evasion points until its next action.'),
 'veil_echo':('echo',0,25,'Add one astral pulse of 25% base elemental attack; pulse cannot trigger procs.'),
 'relic_release':('resistance_down',2,12,'Target astral resistance -12 percentage points for 2 actions.'),
 'rift_cut':('barrier_damage',0,35,'Add 35% base elemental void damage to barriers only.'),
 'hunger':('drain',0,8,'Heal wielder for 8% of the direct elemental damage actually dealt; excludes bursts and shields.'),
 'singularity':('splash',0,30,'Deal 30% base elemental void damage to at most 2 extra enemies within 2 m.'),
 'worldroot':('root',2,0,'Root for 2 actions; boss substitute: -12% action speed for 2 actions.'),
 'first_furnace':('burn',3,22,'Burn deals 22% base elemental magma damage per action for 3 actions.'),
 'stillwinter':('speed_down',3,18,'Target action speed -18% for 3 actions.'),
 'funeral_star':('undead_damage',0,45,'Add 45% base elemental spirit damage against undead only.'),
 'prime_governor':('push',0,2,'Push target 2 m; immune targets take 20% base elemental kinetic damage instead. No durability stabilization.'),
 'first_dawn':('dispel',0,2,'Remove up to 2 removable enemy positive effects.'),
}
# Framework traits are baseline numeric modifiers; striker traits are combat passives.
FRAME_TRAITS={
'sure_grip':dict(accuracy=5,durability_pct=0,speed_pct=0,description='+5 accuracy points.'),
'quick_recovery':dict(accuracy=-2,durability_pct=-10,speed_pct=10,description='+10% action speed; -2 accuracy; -10% durability.'),
'enduring':dict(accuracy=0,durability_pct=25,speed_pct=-5,description='+25% durability; -5% action speed.'),
'extended':dict(accuracy=-3,durability_pct=0,speed_pct=-5,reach_m=.4,description='+0.4 m reach; -3 accuracy; -5% action speed.'),
'channelled':dict(accuracy=0,durability_pct=-15,speed_pct=0,element_pct=15,description='+15% elemental attack; -15% durability.'),
'braced':dict(accuracy=8,durability_pct=10,speed_pct=-10,description='+8 accuracy; +10% durability; -10% action speed.'),
'volatile_conduit':dict(accuracy=-4,durability_pct=-20,speed_pct=0,element_pct=22,description='+22% elemental attack; -4 accuracy; -20% durability; no hidden-life hint.'),
}
STRIKER_TRAITS={
'balanced_edge':dict(trigger='direct_hit',description='+3 accuracy points.',accuracy=3),
'armor_teeth':dict(trigger='direct_hit',description='Ignore 10% of physical armor for this hit.',armor_ignore_pct=10),
'hollow_channel':dict(trigger='direct_hit',description='Physical attack -12%; elemental attack +20%.',physical_pct=-12,element_pct=20),
'serrated':dict(trigger='first_direct_hit_per_action',description='20% chance to bleed for 12% base physical per action, 2 actions; one stack.',chance_pct=20,bleed_pct=12,duration_actions=2),
'concussive':dict(trigger='first_direct_hit_per_action',description='15% chance to remove 6 ATB points; once per target action.',chance_pct=15,atb_delay_points=6),
'wardbreaker':dict(trigger='direct_hit',description='+25% direct damage against barriers only.',barrier_damage_pct=25),
'farshot':dict(trigger='base_stats',description='+2 m range; -5 accuracy points.',reach_m=2,accuracy=-5),
'close_quarters':dict(trigger='base_stats',description='+8% physical attack; -0.2 m reach.',physical_pct=8,reach_m=-.2),
'precision':dict(trigger='direct_hit',description='+6 critical chance points; -8% physical attack.',crit_points=6,physical_pct=-8),
'cleaving':dict(trigger='first_direct_hit_per_action',description='One extra enemy within 1 m of target takes 18% base physical damage; no recursive proc.',splash_pct=18,max_extra_targets=1),
'conductive':dict(trigger='base_stats',description='+12% elemental attack; -6% physical attack.',element_pct=12,physical_pct=-6),
'soul_notch':dict(trigger='direct_hit',description='+20% physical damage against undead; no effect on other targets.',undead_physical_pct=20),
}
# Author-selected regional sources and handling styles, not random item rolls.
FRAME_REGIONS={
'sword':[8,9,0,4],'greatsword':[8,3,1],'dagger':[0,7,4],'spear':[0,2,11,0],
'axe':[0,10,1],'hammer':[8,3,11],'mace':[8,5,15],'staff':[5,7,16,12],
'wand':[12,14,4],'bow':[0,3,12,14],'crossbow':[8,9,13],'whip':[9,11,16],
'scythe':[8,6,15],'cannon':[13,13,13,4],'gauntlet':[8,3,13]}
FRAME_STYLES={
'sword':['sure_grip','quick_recovery','enduring','channelled'],'greatsword':['braced','extended','volatile_conduit'],
'dagger':['sure_grip','quick_recovery','channelled'],'spear':['extended','enduring','channelled','braced'],
'axe':['enduring','quick_recovery','volatile_conduit'],'hammer':['braced','enduring','channelled'],
'mace':['sure_grip','enduring','channelled'],'staff':['enduring','channelled','quick_recovery','volatile_conduit'],
'wand':['sure_grip','channelled','quick_recovery'],'bow':['sure_grip','enduring','extended','quick_recovery'],
'crossbow':['braced','enduring','quick_recovery'],'whip':['sure_grip','extended','channelled'],
'scythe':['extended','channelled','enduring'],'cannon':['braced','enduring','volatile_conduit','channelled'],
'gauntlet':['quick_recovery','enduring','channelled']}
STRIKER_REGIONS={
'sword':[8,3,9,7,3,16],'greatsword':[8,8,3,1,2,17],'dagger':[8,5,14,7,15,12],
'spear':[8,3,4,11,2,16],'axe':[8,9,10,5,1,12],'hammer':[8,8,15,1,3,14],
'mace':[8,0,4,6,2,16],'staff':[0,5,11,12,6,16],'wand':[13,5,2,4,7,12],
'bow':[0,3,12,7,2,14],'crossbow':[8,3,9,13,2,12],'whip':[9,3,15,7,10,16],
'scythe':[8,6,7,15,2,17],'cannon':[13,13,9,13,1,16],'gauntlet':[8,3,15,13,2,16]}
STRIKER_STYLES={
'sword':['balanced_edge','serrated','close_quarters','precision','armor_teeth','conductive'],
'greatsword':['balanced_edge','wardbreaker','cleaving','concussive','serrated','hollow_channel'],
'dagger':['balanced_edge','hollow_channel','precision','serrated','soul_notch','conductive'],
'spear':['balanced_edge','armor_teeth','precision','conductive','wardbreaker','hollow_channel'],
'axe':['balanced_edge','cleaving','serrated','armor_teeth','concussive','precision'],
'hammer':['balanced_edge','wardbreaker','concussive','hollow_channel','armor_teeth','conductive'],
'mace':['balanced_edge','serrated','armor_teeth','soul_notch','concussive','conductive'],
'staff':['balanced_edge','hollow_channel','conductive','precision','soul_notch','wardbreaker'],
'wand':['balanced_edge','hollow_channel','conductive','precision','serrated','wardbreaker'],
'bow':['balanced_edge','armor_teeth','farshot','precision','concussive','conductive'],
'crossbow':['balanced_edge','precision','farshot','close_quarters','armor_teeth','conductive'],
'whip':['balanced_edge','serrated','concussive','precision','cleaving','conductive'],
'scythe':['balanced_edge','armor_teeth','serrated','soul_notch','cleaving','hollow_channel'],
'cannon':['balanced_edge','cleaving','farshot','precision','concussive','hollow_channel'],
'gauntlet':['balanced_edge','serrated','concussive','close_quarters','precision','conductive']}
RARITY={1:'common',2:'uncommon',3:'rare',4:'relic',5:'exalted'}
materials=[]
for ri,(rid,label,soft,hard,site,other) in enumerate(REGIONS):
 for j,name in enumerate([soft,hard]):
  materials.append(dict(id='mat_'+slug(name),name=name,territory_id=rid,category='flexible_stock' if j==0 else 'rigid_stock',buy_gold=8+ri*2+j*6,sell_gold=rnd((8+ri*2+j*6)*.25),stack_limit=99,source=dict(site=site if j==0 else other,method='harvest',status='proposed_spawn_site_not_implemented'),renewable=True))
components=[];families=[];byfamily={}
for fi,(family,hands,interval,power,element,reach,accuracy,tags) in enumerate(FAMILY_SPECS):
 families.append(dict(id=family,name=family.title(),hands=hands,slots=['right_hand','left_hand'] if hands==2 else ['right_hand_or_left_hand'],base_interval_seconds=interval,physical_factor=power,elemental_factor=element,base_reach_m=reach,base_accuracy_pct=accuracy,tags=tags,rig_id='rig_'+family,ammo_note='Striker means paired limbs/prod; ordinary ammunition abstracted into action cost in this draft.' if family in ['bow','crossbow'] else 'Cannon barrel is the striker; cracked-weapon ordnance is a separate learned ability.' if family=='cannon' else 'No sidearm slot. TwoHanded-in-one-hand remains a hero trait exception.'))
 frames=[];strikers=[]
 for i,name in enumerate(FRAME_NAMES[family]):
  tier=[1,3,4,5][i];ri=FRAME_REGIONS[family][i]; rid,label,soft,hard,site,other=REGIONS[ri]
  style=FRAME_STYLES[family][i];tr=FRAME_TRAITS[style]
  obj=dict(id='frame_'+slug(name),name=name,kind='framework',weapon_family=family,compatible_families=[family],tier=tier,rarity=RARITY[tier],territory_id=rid,buy_gold=[45,0,0,0][i] if i==0 else [0,0,0,0][i],sell_gold=0,appraisal_gold=[45,180,360,660][i],weight_kg=round((.35+.12*i)*(1.5 if hands==2 else 1),2),base_durability=55+15*i,hidden_strike_contribution=[1,2,3,3][i],action_interval_seconds=round(interval/(1+tr['speed_pct']/100),3),handling_trait=style,source=dict(method='shape',site=site,entity=soft+' stock',status='proposed_spawn_site_not_implemented'),shaping=dict(inputs=[dict(material_id='mat_'+slug(soft),quantity=2+i),dict(material_id='mat_'+slug(hard),quantity=1)],fee_gold=[8,30,90,170][i],output_quantity=1),merchant_stock='regular' if i==0 else 'rotating_after_local_quest' if i==1 else 'none',recipe_page_id=None)
  obj['buy_gold']=obj['appraisal_gold'] if i<2 else None;obj['sell_gold']=rnd(obj['appraisal_gold']*.25)
  components.append(obj);frames.append(obj)
 for i,name in enumerate(STRIKER_NAMES[family]):
  tier=[1,2,3,3,4,5][i];ri=STRIKER_REGIONS[family][i];rid,label,soft,hard,site,other=REGIONS[ri]
  dtype='pierce' if family in ['dagger','spear','bow','crossbow','cannon'] else 'blunt' if family in ['hammer','mace','staff','wand','gauntlet'] else 'slash'
  stock=soft if family=='bow' or (family=='whip' and i<2) else hard
  obj=dict(id='striker_'+slug(name),name=name,kind='striker',weapon_family=family,compatible_families=[family],tier=tier,rarity=RARITY[tier],territory_id=rid,appraisal_gold=[55,100,190,220,390,700][i],buy_gold=[55,100,190,220,None,None][i],sell_gold=rnd([55,100,190,220,390,700][i]*.25),weight_kg=round((.25+.1*i)*(2 if hands==2 else 1),2),physical_attack=rnd([20,27,35,33,46,58][i]*power),damage_type=dtype,durability_bonus=[20,24,30,18,38,28][i],hidden_strike_contribution=[1,2,2,3,3,4][i],mass_interval_factor=[1,1.05,1.08,.94,1.14,1.10][i],combat_trait=STRIKER_STYLES[family][i],source=dict(method='shape',site=other,entity=stock+' stock',status='proposed_spawn_site_not_implemented'),shaping=dict(inputs=[dict(material_id='mat_'+slug(stock),quantity=2+i),dict(material_id='mat_'+slug(soft if stock==hard else hard),quantity=1)],fee_gold=[10,20,50,65,120,210][i],output_quantity=1),merchant_stock='regular' if i<2 else 'rotating_after_local_quest' if i<4 else 'none',recipe_page_id=None)
  components.append(obj);strikers.append(obj)
 byfamily[family]=(frames,strikers)
cores=[]
for ri,group in enumerate(CORE_GROUPS):
 for i,(name,element,effect) in enumerate(group):
  rid,label,soft,hard,site,other=REGIONS[ri]; tier=i+2
  core=dict(id='core_'+slug(name),name=name+' Core',kind='core',compatible_families=[x[0] for x in FAMILY_SPECS],tier=tier,rarity=RARITY[tier],territory_id=rid,appraisal_gold=[110,260,510][i],buy_gold=110 if i==0 else None,sell_gold=rnd([110,260,510][i]*.25),weight_kg=[.08,.12,.18][i],element=element,elemental_attack=[12,21,32][i],hidden_strike_contribution=[0,1,2][i],volatility=[1,2,3][i],combat_effect=effect,proc_chance_pct=[18,22,26][i],burst_radius_bonus_m=[0,.2,.4][i],source=dict(method=['harvest','elite_drop','dungeon_recovery'][i],site=[site,other,other+' lower vault'][i],entity=[name+' deposit',name+'-bearing regional guardian',name+' sealed reliquary'][i],status='proposed_spawn_site_not_implemented'),merchant_stock='rare_caravan' if i==0 else 'none',renewable=True,renewal='Regenerating deposits / repeatable local encounters after discovery; never exclusive to one hero route.',shaping=None,recipe_page_id=None)
  if rid=='devouring_deep':core['source']['site']='Outer Fracture expedition area';core['source']['availability']='Reachable before the final boss; not a post-victory-only reward.'
  components.append(core);cores.append(core)
for name,rid,element,effect in APEX:
 core=dict(id='core_'+slug(name),name=name+' Core',kind='core',compatible_families=[x[0] for x in FAMILY_SPECS],tier=5,rarity='exalted',territory_id=rid,appraisal_gold=1050,buy_gold=None,sell_gold=263,weight_kg=.24,element=element,elemental_attack=45,hidden_strike_contribution=3,volatility=4,combat_effect=effect,proc_chance_pct=30,burst_radius_bonus_m=.5,source=dict(method='regional_mastery_quest',site=dict(ravenwood='Old Grove Heart',ashen_wastes='First Furnace Ruin',frostpeaks='Stillwinter Vault',deadwind_hollow='Quiet Belfry',copperfen_basin='Prime Pump Chamber',golden_expanse='Dawnwell Ruins')[rid],entity=name+' mastery cache',status='proposed_spawn_site_not_implemented'),merchant_stock='none',renewable=True,renewal='First copy from regional mastery; later copies from a difficult repeatable recovery expedition. Both hero routes have access.',shaping=None,recipe_page_id=None)
 if rid=='deadwind_hollow':core['source']['requires_both_liberated']=['cursed_mire','deadwind_hollow']
 components.append(core);cores.append(core)
for part in components:
 if part['kind']!='core':
  part['shaping']['workshop_rank']=1 if part['tier']<=2 else 2 if part['tier']==3 else 3
  part['shaping']['rank_note']='Ranks 2/3 unlocked through regional smith restoration/mastery, available to either hero route; book knowledge is not a crafting gate.'
# Every page supplies exact designer-hidden contributions for its components once discovered.
pages=[]
for ri,(rid,label,*_) in enumerate(REGIONS):
 ids=[c['id'] for c in components if c['territory_id']==rid]
 page_id='page_'+rid
 pages.append(dict(id=page_id,title=label+' Working Leaves',component_ids=ids,reveals=['hidden_strike_contribution','source_site','source_entity','shaping_inputs'],reward_channel='courier_story',early_sources_visible_without_page=False))
 for c in components:
  if c['id'] in ids:c['recipe_page_id']=page_id
# Named authored recipe titles: 12 per family. Ingredients are visible in the exported cookbook.
RECIPE_NAMES={
'sword':['Briar Oath','Cinder Vow','White Mercy','Scale Promise','Sunlit Verdict','Adder’s Courtesy','Gravewarden','Widow’s Answer','Marchkeeper','Salt Testament','Ashwake Saber','Stormlit Promise'],
'greatsword':['Winter’s Debt','Wyrm’s Reproach','Dawn Divider','Bog King’s Fall','Cursebreaker’s Burden','Canopy Reaver','Last Battle Line','Breakwater Blade','Nestkeeper’s Fury','Summit Judgment','Moonfall Monument','Foundry Requiem'],
'dagger':['Salt Whisper','Ember Needle','Thunder’s Wink','Moonless Kiss','Clockwork Stiletto','Glasswind Secret','Bellringer’s Debt','Mist Thief','Hunger’s Point','Root Assassin','Furnace Splinter','Winter Widow'],
'spear':['Moonwarden’s Reach','Pressure Lance','Horizon Harpoon','Funeral Standard','Veilpiercer','Rift Skewer','Rootbound Watch','First Flame Pike','Stillwinter Thorn','Pale Sentinel','Governor’s Reach','Dawnwatch Lance'],
'axe':['Lantern Hew','Mistfall Hatchet','Hunger Hewn','Worldroot Splitter','First Furnace Bite','Stillwinter Hook','Funeral Crescent','Clockwork Woodsman','Dawncleaver','Briar Butcher','Ashkeeper’s Hook','White Pass Reaver'],
'hammer':['Gatebreaker','Ember Bell','Rime Knell','Drakefall','Dawn Ram','Mirebound Mallet','Curse Anchor','Webbreaker','Siege Psalm','Tidehammer','Cinderquake','Storm Anvil'],
'mace':['Winter Crown','Broodkeeper','Sunlit Rebuke','Reedwarden','Grave Lantern','Gloam Cudgel','Marching Bell','Saltwarden','Hearthguard','Thunder Chapel','Moonward','Pressure Saint'],
'staff':['Tidal Testament','Cinder Shepherd','Stormbranch','Moon Observatory','Clockmaker’s Crook','Windglass Pilgrim','Last Procession','Mistvale Memory','Rift Interpreter','Worldroot Cantor','First Furnace Oracle','Stillwinter Scribe'],
'wand':['Moon Needle','Pressure Pointer','Horizon Quill','Pale Bell','Veil Signature','Null Stylus','Grove Script','Furnace Whisper','Winter Cipher','Funeral Reed','Prime Conductor','First Dawn Quill'],
'bow':['Last Lantern Bow','Veilstrung','Hunger at Distance','Worldroot Vigil','Furnace Recurve','Stillwinter Longbow','Funeral Archer','Clockwork Canopy','Dawn Horizon','Briar Whisper','Ashwind','White Hunter'],
'crossbow':['Watchman’s Promise','Cinder Bolt','Icebound Warrant','Wyrm Marshal','Dawn Mechanism','Adder’s Writ','Grave Arbiter','Webline','Siege Witness','Marine’s Return','Rookery Guard','Storm Ratchet'],
'whip':['Winter Lash','Broodbinder','Suncoil','Fen Shepherd','Gravechain','Widow’s Thread','Iron Reins','Undertow Lash','Cinder Ribbon','Skyline Lash','Mooncord','Pressure Serpent'],
'scythe':['Tide Reaper','Ash Harvest','Storm Crescent','Moon’s Toll','Clockwork Harvest','Glasswind Requiem','Pale Procession Scythe','Mist Mourner','Hunger’s Harvest','Worldroot Reclaimer','First Furnace Reaper','Stillwinter Requiem'],
'cannon':['Moonshot','Pressure Sermon','Horizon Breaker','Funeral Broadside','Veil Breach','Null Battery','Worldroot Salvo','First Furnace Mortar','Stillwinter Battery','Lantern Thunder','Prime Shardcaster','First Dawn Artillery'],
'gauntlet':['Lantern Fist','Mist Palm','Hunger Knuckle','Worldroot Grasp','Furnace Piston','Winter Claw','Funeral Hand','Prime Impact','Dawnbringer’s Grip','Briar Knuckle','Ashboxer','Whiteclaw'],
}
def stats(f,s,c,skill=0,forge='standard',strikes=None):
 fam=next(x for x in families if x['id']==f['weapon_family']);ft=FRAME_TRAITS[f['handling_trait']];st=STRIKER_TRAITS[s['combat_trait']]
 base_limit=f['hidden_strike_contribution']+s['hidden_strike_contribution']+c['hidden_strike_contribution'];limit=min(10,base_limit+skill)
 n=limit if strikes is None else strikes
 if forge not in ('standard','mistvale','sands') or f['weapon_family']!=s['weapon_family']:raise ValueError('Invalid forge or incompatible parts')
 if not (0<=skill<=3 and 1<=n<=15):raise ValueError('Invalid skill or strike count')
 p=s['physical_attack']*(1+st.get('physical_pct',0)/100)
 e=c['elemental_attack']*fam['elemental_factor']*(1+ft.get('element_pct',0)/100)*(1+st.get('element_pct',0)/100)
 dur=rnd((f['base_durability']+s['durability_bonus'])*(1+ft.get('durability_pct',0)/100))
 curve=(2**((limit-2)/8)-1)
 mult=(1.25+.75*curve) if forge=='sands' else (1.10+.65*curve)
 aura=1.10 if forge=='mistvale' else 1.0
 pp=p*mult*aura;ee=e*mult*aura
 over=max(0,n-limit);ratio=n/limit
 if n<limit:
  under_aura=1.15 if forge=='sands' else aura
  physical=p*(.35+.65*ratio)*under_aura;elemental=e*(.5+.5*ratio)*under_aura;durability=dur+rnd((pp-physical)*.8);state='under_struck'
 elif n==limit:
  physical=pp;elemental=ee;durability=dur;state='masterwork'
 else:
  physical=pp*.8;elemental=ee*(1+(.35+.05*(c['volatility']-1))*over);durability=max(1,rnd(dur*max(.05,.28*(.62**(over-1)))));state='cracked'
 interval=round(f['action_interval_seconds']*s['mass_interval_factor'],3)
 total=f['appraisal_gold']+s['appraisal_gold']+c['appraisal_gold']
 result=dict(state=state,base_strike_limit=base_limit,effective_strike_limit=limit,strikes=n,physical_attack=rnd(physical),elemental_attack=rnd(elemental),element=c['element'],action_interval_seconds=interval,attack_budget_per_second=round((physical+elemental)/interval,2),accuracy_pct=max(60,min(99,fam['base_accuracy_pct']+ft.get('accuracy',0)+st.get('accuracy',0))),critical_chance_pct=5+st.get('crit_points',0),reach_m=round(max(.5,fam['base_reach_m']+ft.get('reach_m',0)+st.get('reach_m',0)),2),durability_design_center=durability,component_appraisal_gold=total,forge_fee_gold=rnd(10+total*dict(standard=.12,mistvale=.18,sands=.25)[forge]),weapon_sell_gold=rnd(total*(.08 if state=='cracked' else .35 if state=='masterwork' else .30*(.5+.5*ratio))),masterwork_multiplier=round(mult*aura,4),hidden_remaining_durability=state=='cracked')
 if state=='cracked':
  result.update(hidden_durability_range=[max(1,math.floor(durability*.6)),max(1,math.ceil(durability*1.4))],terminal_burst_attack=rnd((p+e)*mult*aura*(2+.4*over)*(1+.08*(c['volatility']-1))),terminal_burst_radius_m=round(min(5,2.5+.3*over+c['burst_radius_bonus_m']),2),durability_cost_per_offensive_action=[1,3],friendly_fire=True)
 return result
CORE_ROUTES=[list(range(0,36,3)),list(range(6,42,3)),[27,30,33,36,39,42,45,48,51,54,55,56],[36,39,42,45,48,51,54,55,56,57,58,59],[45,48,51,54,55,56,57,58,59,0,3,6]]
recipes=[]
for fi,fam in enumerate(families):
 frames,strikers=byfamily[fam['id']]
 for j,name in enumerate(RECIPE_NAMES[fam['id']]):
  f=frames[j%len(frames)];s=strikers[j%6];core_index=CORE_ROUTES[fi%5][j];c=cores[core_index+(fi//5 if core_index<54 else 0)]
  recipes.append(dict(id='recipe_'+slug(name),name=name,family=fam['id'],framework_id=f['id'],striker_id=s['id'],core_id=c['id'],ingredients=[dict(component_id=x['id'],quantity=1) for x in [f,s,c]],archetype_tags=fam['tags'],exclusive_hero=None,minimum_forge='standard',requires_recipe_to_attempt=False,discovery_page_id=c['recipe_page_id'],intended_use=' / '.join([FRAME_TRAITS[f['handling_trait']]['description'],STRIKER_TRAITS[s['combat_trait']]['description'],EFFECT_SPECS[c['combat_effect']][3]]),standard_masterwork_skill0=stats(f,s,c),standard_masterwork_skill3=stats(f,s,c,3),mistvale_masterwork_skill3=stats(f,s,c,3,'mistvale'),sands_masterwork_skill3=stats(f,s,c,3,'sands'),sands_understrike_one_short_skill3=stats(f,s,c,3,'sands',min(10,f['hidden_strike_contribution']+s['hidden_strike_contribution']+c['hidden_strike_contribution']+3)-1),sands_cracked_plus1_skill3=stats(f,s,c,3,'sands',min(10,f['hidden_strike_contribution']+s['hidden_strike_contribution']+c['hidden_strike_contribution']+3)+1)))
# Ensure names describe evocative discoveries, not hidden unique bonuses: exact components own all stats.
for page in pages:page['recipe_ids']=[r['id'] for r in recipes if r['discovery_page_id']==page['id']]
metadata=dict(version='0.1.0',status='proposed_balance_not_playtested',components=200,frameworks=50,strikers=90,cores=60,raw_materials=36,named_recipes=180,compatible_assemblies=18000,designer_spoilers=True,game_runtime_integrated=False)
dump('catalog.json',dict(metadata=metadata,families=families,materials=materials,components=components,pages=pages,recipes=recipes))
dump('effects.json',dict(framework_traits=FRAME_TRAITS,striker_traits=STRIKER_TRAITS,core_effects={k:dict(status=v[0],duration_actions=v[1],magnitude=v[2],description=v[3]) for k,v in EFFECT_SPECS.items()},proc_rules=dict(roll='Once on the first successful direct target per offensive action; listed core chance.',source_values='Base P0/E0 after component passives, before forging state and forge multipliers. Prevents recursive scaling.',stacking='Same named status refreshes duration, never stacks; different sources use strongest magnitude.',duration='Target completed actions, not seconds. Wielder effects use wielder actions.',limits='Hard-control immune bosses receive listed substitutes; all effects respect immunity flags.',secondary_hits='DoTs, echoes, splashes, bursts and shatter cannot roll weapon procs.',cracked='Core proc chance gains 4 percentage points per excess forge strike, capped at 50%; effect magnitude unchanged.',friendly_fire='All persistent ground damage and terminal/ordnance bursts affect both sides. Other listed extra-enemy effects target enemies only.',critical='Direct hits only; critical damage 1.5x before defense; proc damage and terminal bursts cannot crit.',armor='Attack values are pre-defense weapon contribution, not promised final HP damage. Combat integration determines defense formula.')))
# Structured economic/salvage rules and exact crafting evaluator proposal.
dump('rules.json',dict(version='0.1.0',status='balance_proposal',compatibility='One framework + one matching-family striker + any one core. No fourth equipment part.',skill_bonus=[0,1,2,3],limit='min(10, framework.strikes + striker.strikes + core.strikes + skill_bonus)',snapshot='Skill bonus and forge are frozen at craft creation; later respec cannot retroactively change an item.',strike_cap='Universal maximum 15 blows for every combination. Never stop at a limit-relative count: that would disclose the hidden limit. Excess blows continue scaling elemental leakage; durability floors at 5% of base before its hidden random roll.',cancel='Until the first blow, cancellation returns all components. After a blow, stopping finalizes the current item; no material refunds.',critical_note='175% and 200% mean 1.75x and 2.00x total attack, not +175%/+200%.',forge_locations=dict(standard=['ashenreach','stormcrown_keep','ironhold','dragons_rest'],mistvale='relic outside Mistvale city, unlocked through courier story',sands='secret Golden Expanse forge, revealed only after first completed Mistvale craft'),mistvale_bonus='1.10x final physical and elemental weapon attack; does not stack with sands forge bonus.',sands_bonus='Perfect curve is 1.25 + 0.75*(2**((L-2)/8)-1), reaching 2.00x. Under-struck attack uses 1.15x base-state output. Neither stacks with Mistvale; Sands is stronger at every limit.',formula_source='tools/build_crafting_catalog.py: stats() is the exact balance reference, not game runtime.',salvage=dict(shatter_shards=2,tinkerer_payload_shards=1,fusion_shards=5,fusion_fee='25% of that core appraisal, rounded half-up; restore the SAME core id.',degraded_stock='One degraded framework stock and one degraded striker stock; four same-material degraded pieces + 5 gold recover one original raw stock.',intact_disassembly='At a suitable workshop, consumes weapon and returns 1 core shard plus 2 degraded stocks. Never returns original parts.',cracked_repair='Cannot repair, stabilize, dismantle safely into original parts, or reveal remaining durability.',ordnance_recovery='Survive battle and recover salvage at impact/device site; no automatic remote salvage.',fusion_gate='Must previously discover the whole core; neither fusion nor salvage unlocks an undiscovered core.'),anti_exploit=dict(terminal='Remove weapon/ordnance from inventory before damage event; one unique detonation id prevents duplicate bursts.',ordnance='Tessa: 1 full action + 14 MP. Tobin: 1 full action + 18 MP; device arms at end of his action, max 1 deployed. Proposed costs.',payload='Use the same pre-defense terminal budget and radius as that cracked weapon. Remaining hidden durability never increases payload strength.',self_feed='Firing a cracked cannon does not recursively consume loaded cracked ordnance. One payload item and one detonation event.',staff='Every offensive weapon-channeling action consumes durability; healing, guard and non-weapon spells do not. Multi-hit actions pay once.',hidden_life='On crack: hidden starting durability sampled uniformly from integer range shown in designer data. Each offensive action spends 1–3 hidden points uniformly. Item RNG state persists through save/load.',reload='Outcome and RNG progression committed with item/action transaction; reloading cannot reroll a completed forge or hit.',no_danger_meter=True),ledger=dict(acquired='On accepting the first courier mission.',ordinary_recipes='Knowledge aids experimentation; discovered parts may be combined before their recipe page is owned.',hidden_values='Component strike contributions only revealed by acquired pages; other hidden values never appear in ordinary equipment UI.',secret_reveal='First finalized Mistvale forge use after restoration triggers the book and new sand map once. Under-struck, Masterwork and cracked outcomes all qualify; preview/cancel does not.'),purchased_equipment='Existing loot/shop items keep independent identities and benefits; do not automatically replace them with generated catalog recipes.'))
# Salvage inventory definitions are separate from the 200 assembly components.
salvage=[]
for c in cores:
 salvage.append(dict(id='shard_'+c['id'],name=c['name'].removesuffix(' Core')+' Core Shard',kind='core_shard',core_id=c['id'],appraisal_gold=rnd(c['appraisal_gold']/5),buy_gold=None,sell_gold=max(1,rnd(c['appraisal_gold']*.02)),stack_limit=99,combine=dict(quantity=5,fee_gold=rnd(c['appraisal_gold']*.25),output_id=c['id'],requires_whole_core_discovered=True)))
for m in materials:
 salvage.append(dict(id='degraded_'+m['id'],name='Degraded '+m['name'],kind='degraded_stock',material_id=m['id'],appraisal_gold=max(1,rnd(m['buy_gold']/4)),buy_gold=None,sell_gold=max(0,math.floor(m['buy_gold']*.03)),stack_limit=99,combine=dict(quantity=4,fee_gold=5,output_id=m['id'])))
dump('salvage.json',dict(items=salvage,rules='Salvage is recovered after combat. Each destroyed item drops one degraded unit of the framework primary shaping stock and one of the striker primary shaping stock; identical stocks stack. Ordinary shatter gives two same-core shards; tinkerer payload gives one. Intact disassembly gives one shard and the same two stocks.'))
# Flat human-readable spreadsheets, intentionally CSV without a workbook dependency.
fields=['id','name','kind','weapon_family','tier','rarity','territory_id','appraisal_gold','buy_gold','sell_gold','weight_kg','hidden_strike_contribution','physical_attack','elemental_attack','element','base_durability','durability_bonus','action_interval_seconds','volatility','handling_trait','combat_trait','combat_effect','recipe_page_id']
with (DOC/'components.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(components)
with (DOC/'weapons.csv').open('w',newline='') as f:
 fields=['name','family','framework','striker','core','base_strike_limit','masterwork_limit_skill3','physical_standard','elemental_standard','physical_mistvale','elemental_mistvale','physical_sands','elemental_sands','sands_durability','interval_seconds','accuracy_pct','reach_m','component_appraisal_gold','standard_fee_gold','sands_fee_gold','sands_sell_gold','cracked_plus1_elemental','cracked_plus1_burst','cracked_plus1_radius_m','recipe_page']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();idx={c['id']:c for c in components}
 for r in recipes:
  a=r['standard_masterwork_skill3'];m=r['mistvale_masterwork_skill3'];s=r['sands_masterwork_skill3'];c=r['sands_cracked_plus1_skill3']
  w.writerow(dict(name=r['name'],family=r['family'],framework=idx[r['framework_id']]['name'],striker=idx[r['striker_id']]['name'],core=idx[r['core_id']]['name'],base_strike_limit=a['base_strike_limit'],masterwork_limit_skill3=a['effective_strike_limit'],physical_standard=a['physical_attack'],elemental_standard=a['elemental_attack'],physical_mistvale=m['physical_attack'],elemental_mistvale=m['elemental_attack'],physical_sands=s['physical_attack'],elemental_sands=s['elemental_attack'],sands_durability=s['durability_design_center'],interval_seconds=s['action_interval_seconds'],accuracy_pct=s['accuracy_pct'],reach_m=s['reach_m'],component_appraisal_gold=s['component_appraisal_gold'],standard_fee_gold=a['forge_fee_gold'],sands_fee_gold=s['forge_fee_gold'],sands_sell_gold=s['weapon_sell_gold'],cracked_plus1_elemental=c['elemental_attack'],cracked_plus1_burst=c['terminal_burst_attack'],cracked_plus1_radius_m=c['terminal_burst_radius_m'],recipe_page=r['discovery_page_id']))
# Full readable catalog with BOTH ingredients and numeric attributes, not just names.
lines=['# Entropic Forge — component and weapon catalog','', '**Balance draft 0.1.0 — designer spoilers. These values are proposed and have not been playtested.**','', '200 components: 50 frameworks, 90 strikers, 60 cores. 36 gathering stocks support component shaping. 15 families allow 18,000 legal assemblies; the 180 named recipes below are discoveries within that space, not the only allowed combinations.','', 'Gold appraisal is not guaranteed merchant availability. A dash in buy price means not sold. Hidden strike contributions and recipe contents belong in the ancient book only when their pages are earned. Full sources, shaping quantities, effect definitions and every forging state are included in the JSON data.','']
for fam in families:
 frames,strikers=byfamily[fam['id']];lines += ['## '+fam['name']+' components','',f"Hands: {fam['hands']}. Tags: {', '.join(fam['tags'])}. Elemental coefficient: {fam['elemental_factor']}. Base reach: {fam['base_reach_m']} m.",'','| Framework | Tier | Value / buy / sell gold | Hidden strikes | Durability | Action interval | Handling |','|---|---:|---|---:|---:|---:|---|']
 for c in frames:lines.append(f"| {c['name']} | {c['tier']} | {c['appraisal_gold']} / {c['buy_gold'] if c['buy_gold'] is not None else '—'} / {c['sell_gold']} | {c['hidden_strike_contribution']} | {c['base_durability']} | {c['action_interval_seconds']} s | {FRAME_TRAITS[c['handling_trait']]['description']} |")
 lines += ['','| Striker | Tier | Value / buy / sell gold | Hidden strikes | Physical | Durability added | Trait |','|---|---:|---|---:|---:|---:|---|']
 for c in strikers:lines.append(f"| {c['name']} | {c['tier']} | {c['appraisal_gold']} / {c['buy_gold'] if c['buy_gold'] is not None else '—'} / {c['sell_gold']} | {c['hidden_strike_contribution']} | {c['physical_attack']} {c['damage_type']} | {c['durability_bonus']} | {STRIKER_TRAITS[c['combat_trait']]['description']} |")
 lines += ['']
lines += ['## Entropic cores','','Listed effect percentages use base elemental attack before forge multipliers. Core chance is rolled once per offensive action, on the first successful direct hit. Status effects refresh rather than accumulate. See effects.json for full proc rules.','']
for rid,label,*_ in REGIONS:
 lines += ['### '+label,'','| Core | Tier | Value / buy / sell gold | Hidden strikes | Elemental | Volatility | Chance | Effect |','|---|---:|---|---:|---|---:|---:|---|']
 for c in cores:
  if c['territory_id']==rid:lines.append(f"| {c['name']} | {c['tier']} | {c['appraisal_gold']} / {c['buy_gold'] if c['buy_gold'] is not None else '—'} / {c['sell_gold']} | {c['hidden_strike_contribution']} | {c['elemental_attack']} {c['element']} | {c['volatility']} | {c['proc_chance_pct']}% | {EFFECT_SPECS[c['combat_effect']][3]} |")
 lines += ['']
lines += ['## The 180 named discoveries','','All results below use crafting skill +3 and a perfect forge. Attack is physical / elemental before enemy defenses. Standard → Mistvale → Sands columns show forge progression. Durability is Masterwork durability; cracked remaining durability is never player-visible. Named recipes are aliases for combinations and grant no hidden fourth-part bonus.','']
idx={c['id']:c for c in components}
for fam in families:
 lines += ['### '+fam['name']+' recipes','', '| Weapon | Framework + striker + core | Limit | Attack: standard → Mistvale → Sands | Durability | Seconds/action | Sands fee / resale |','|---|---|---:|---|---:|---:|---|']
 for r in recipes:
  if r['family']!=fam['id']:continue
  a=r['standard_masterwork_skill3'];m=r['mistvale_masterwork_skill3'];s=r['sands_masterwork_skill3']
  parts=' + '.join(idx[r[k]]['name'] for k in ['framework_id','striker_id','core_id'])
  lines.append(f"| {r['name']} | {parts} | {s['effective_strike_limit']} | {a['physical_attack']}/{a['elemental_attack']} → {m['physical_attack']}/{m['elemental_attack']} → {s['physical_attack']}/{s['elemental_attack']} | {s['durability_design_center']} | {s['action_interval_seconds']} | {s['forge_fee_gold']} / {s['weapon_sell_gold']} g |")
 lines += ['']
lines += ['## Gathering stocks','','These exact stock quantities feed the shaping recipes in catalog.json. Sites are newly authored proposals, not existing placed game objects.','', '| Stock | Territory | Harvest site | Buy / sell gold |','|---|---|---|---|']
for m in materials:lines.append(f"| {m['name']} | {m['territory_id']} | {m['source']['site']} | {m['buy_gold']} / {m['sell_gold']} |")
lines += ['','## Salvage items and recombination','','These 96 salvage items are additional to the 200 assembly components and 36 gathering stocks. Salvage cannot be bought. Values are appraisal / merchant buyback.','', '| Salvage item | Value / sell gold | Combine |','|---|---|---|']
all_names={x['id']:x['name'] for x in components+materials}
for item in salvage:
 recipe=item['combine'];lines.append(f"| {item['name']} | {item['appraisal_gold']} / {item['sell_gold']} | {recipe['quantity']} pieces + {recipe['fee_gold']} gold → {all_names[recipe['output_id']]} |")
(DOC/'CATALOG.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(metadata,indent=2))
