#!/usr/bin/env python3
"""One-time, reproducible polish of the 190 expanded component records.

Original components, cores, named recipes, snap-manifest assets and saved IDs stay intact.
By default every replacement PNG must exist; --allow-pending-art retains clearly marked placeholders. Values remain sandbox balance proposals.
"""
import argparse, json, math, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'data/entropic_forge/forge_test_catalog.json'
def slug(s): return re.sub('[^a-z0-9]+','_',s.lower()).strip('_')
def rounded(x): return math.floor(x+.5)
BASE_INTERVAL={'Sword':1.8,'Greatsword':3.0,'Dagger':1.05,'Spear':2.2,'Axe':2.1,'Hammer':3.2,'Mace':2.05,'Staff':2.5,'Wand':1.5,'Bow':2.2,'Crossbow':2.9,'Whip':1.95,'Scythe':2.8,'Cannon':3.6,'Gauntlet':1.2}
# Effects use the same concrete vocabulary as the original components.
FRAME_ROLES={
 'braced':dict(label='Braced housing',speed_pct=-5,accuracy_points=0,durability_pct=20,elemental_pct=0,reach_m=0,description='+20% durability; -5% action speed.'),
 'quick':dict(label='Light counterbalance',speed_pct=8,accuracy_points=-2,durability_pct=-10,elemental_pct=0,reach_m=0,description='+8% action speed; -2 accuracy points; -10% durability.'),
 'conductive':dict(label='Insulated conduit',speed_pct=0,accuracy_points=-2,durability_pct=-10,elemental_pct=12,reach_m=0,description='+12% elemental attack; -2 accuracy points; -10% durability.'),
 'guarded':dict(label='Guarded grip',speed_pct=-3,accuracy_points=5,durability_pct=10,elemental_pct=0,reach_m=0,description='+5 accuracy points; +10% durability; -3% action speed.'),
 'extended':dict(label='Extended leverage',speed_pct=-5,accuracy_points=-3,durability_pct=0,elemental_pct=0,reach_m=.3,description='+0.3 m reach; -3 accuracy points; -5% action speed.'),
 'precise':dict(label='Indexed grip',speed_pct=0,accuracy_points=7,durability_pct=-8,elemental_pct=0,reach_m=0,description='+7 accuracy points; -8% durability.'),
 'vented':dict(label='Vented core seat',speed_pct=-4,accuracy_points=0,durability_pct=-15,elemental_pct=18,reach_m=0,description='+18% elemental attack; -4% action speed; -15% durability. Does not stabilize a cracked weapon.'),
}
STRIKER_ROLES={
 'puncture':dict(label='Armor seam',description='Ignore 8% of target physical armor for the direct hit; -3 accuracy points.',physical_pct=0,accuracy_points=-3,armor_ignore_pct=8),
 'bleed':dict(label='Raking edge',description='18% chance to bleed for 12% base physical attack per target action, 2 actions; one stack; -4% direct physical attack.',physical_pct=-4,bleed_chance_pct=18,bleed_base_physical_pct=12,duration_actions=2,max_stacks=1),
 'precision':dict(label='Fine point',description='+5 critical chance points; -8% physical attack. Direct hits only.',physical_pct=-8,critical_chance_points=5),
 'cleave':dict(label='Sweeping face',description='One extra enemy within 1 m takes 15% base physical attack; -5% primary physical attack; no recursive procs.',physical_pct=-5,secondary_target_limit=1,secondary_radius_m=1,secondary_base_physical_pct=15),
 'concussive':dict(label='Impact shoulder',description='15% chance to remove 5 ATB points from the direct target; once per target action. Control-immune targets instead take 5% extra base physical attack.',physical_pct=0,atb_chance_pct=15,atb_points=5,immune_substitute_physical_pct=5),
 'channel':dict(label='Core channel',description='+15% elemental attack; -8% physical attack. Preserves the installed core element.',physical_pct=-8,elemental_pct=15),
 'barrier':dict(label='Breaching face',description='+20% direct physical damage against barriers; -3 accuracy points. No bonus against ordinary armor.',physical_pct=0,barrier_damage_pct=20,accuracy_points=-3),
}
def frame_role(name,family,index):
 n=name.lower()
 if any(w in n for w in ['heatvent','furnace','volcanic','cinder','flameglass']):return 'vented'
 if any(w in n for w in ['coil','conduit','conductor','dynamo','capacitor','voltage','silver','glassrod']):return 'conductive'
 if any(w in n for w in ['braced','bastion','siege','juggernaut','anchor','stonewall','foundry','casing']):return 'braced'
 if any(w in n for w in ['basket','guard','cuff','brace','command']):return 'guarded'
 if any(w in n for w in ['silent','frostneedle','hunter','reverse','ritual']):return 'precise'
 if any(w in n for w in ['giant','longhook','pole','shaft','dual','reaver','harvest']):return 'extended'
 if any(w in n for w in ['quick','flexible','silk','prowler','corsair','curved','finger']):return 'quick'
 return ['guarded','braced','precise','quick','extended','conductive','vented'][index%7]
def striker_role(name,family,index):
 n=name.lower()
 if any(w in n for w in ['breaker','breach','siege','ironwall','bastion']):return 'barrier'
 if any(w in n for w in ['rapier','needle','dirk','point','pike','harpoon','lance']):return 'puncture'
 if any(w in n for w in ['claw','talon','thorn','rake','hook','reaper','fang','bramble']):return 'bleed' if family not in ['Staff','Wand'] else 'channel'
 if any(w in n for w in ['coil','conduct','thunder','lightning','spark','tesla','arc','prism','focus','orb','eye','pearl','lens','halo','crown']):return 'channel'
 if any(w in n for w in ['maul','block','impact','globe','ram','fist','loghead']):return 'concussive'
 if any(w in n for w in ['cleav','falchion','cutter','surfline','broadside','crescent']):return 'cleave'
 return ['precision','channel','cleave','puncture','concussive','bleed'][index%6]

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--allow-pending-art',action='store_true');args=parser.parse_args()
 c=json.loads(PATH.read_text());changes=[];missing=[]
 for category,original_count in [('frameworks',50),('strikers',90)]:
  originals=c[category][:original_count]
  local_indices={}
  for item in c[category][original_count:]:
   family=item['family'];i=local_indices.get(family,0);local_indices[family]=i+1
   asset='assets/entropic_forge/icons/'+category+'/'+slug(item['name'])+'.png'
   if not (ROOT/asset).is_file():missing.append(asset)
   original_family=[x for x in originals if x['family']==family]
   # New choices span uncommon through exalted with distinctive trade-offs.
   tier=[2,3,3,4,4,5,3][i];item['tier']=tier
   if category=='frameworks':
    role=frame_role(item['name'],family,i);effect=FRAME_ROLES[role]
    base_dur={2:62,3:72,4:86,5:98}[tier]
    # Display base durability, consistent with the original catalog convention.
    item.update(value={2:'110 / 110 / 28',3:'205 / 205 / 51',4:'390 / — / 98',5:'650 / — / 163'}[tier],hidden_strikes={2:1,3:2,4:3,5:3}[tier],durability=base_dur,interval=f"{BASE_INTERVAL[family]/(1+effect['speed_pct']/100):.3f} s",handling=effect['description'],mechanics=dict(effect,role_id=role,interval_includes_speed_modifier=True,durability_includes_modifier=False))
   else:
    role=striker_role(item['name'],family,i);effect=STRIKER_ROLES[role]
    template=next(x for x in original_family if x['tier']==tier)
    base_attack=int(template['physical'].split()[0]);damage_type=template['physical'].split()[1]
    # Do not apply trait multipliers twice: physical is the raw component value.
    attack=rounded(base_attack*[.98,1.02,.96,1.00,1.03,.98][i])
    if family in ['Sword','Dagger','Greatsword'] and any(w in item['name'].lower() for w in ['rapier','needle','dirk']):damage_type='pierce'
    item.update(value={2:'120 / 120 / 30',3:'215 / 215 / 54',4:'410 / — / 103',5:'690 / — / 173'}[tier],hidden_strikes={2:2,3:2 if i%2==0 else 3,4:3,5:4}[tier],physical=f'{attack} {damage_type}',durability={2:24,3:29,4:37,5:29}[tier],trait=effect['description'],mechanics=dict(effect,role_id=role,physical_includes_modifier=False))
   item.update(icon='res://'+asset if (ROOT/asset).is_file() else item['icon'],art_status='distinct_inventory_component' if (ROOT/asset).is_file() else 'placeholder_existing_family_component',silhouette=item['name']+' — '+effect['label'],art_scope='Inventory icon only; existing Sword assembly cutouts and anchors remain separate.',balance_status='proposed_unplaytested_expansion_refinement')
   changes.append(dict(name=item['name'],family=family,category=category,icon=item['icon'],role=effect['label'],trait=effect['description'],art_status=item['art_status']))
 if missing and not args.allow_pending_art:raise SystemExit(f'Refusing incomplete art integration: {len(missing)} missing; first: {missing[:5]}')
 c['version']=4
 c['expansion_note']='190 expanded components have family-scaled balance proposals. Art status is recorded per item; placeholders remain until a distinct icon is supplied. Original 140 physical components and 180 discoveries unchanged. Sword result snap sprites remain separate. Production combat integration remains pending.'
 PATH.write_text(json.dumps(c,indent=2,ensure_ascii=False)+'\n')
 (ROOT/'data/entropic_forge/expanded_component_art.json').write_text(json.dumps(dict(version=1,scope='190 replacement inventory icons; no snap-asset replacement',items=changes),indent=2,ensure_ascii=False)+'\n')
 print(f'Refined {len(changes)} components; {len(changes)-len(missing)} distinct icons, {len(missing)} placeholders pending.')
if __name__=='__main__':main()
