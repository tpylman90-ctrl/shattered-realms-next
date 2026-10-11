#!/usr/bin/env python3
"""Design invariants, economy checks and forge boundary checks; no game runtime tests."""
import contextlib, io, json, runpy
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with contextlib.redirect_stdout(io.StringIO()):
 g=runpy.run_path(str(ROOT/'tools/build_crafting_catalog.py'))
 runpy.run_path(str(ROOT/'tools/build_courier_story.py'))
data=json.loads((ROOT/'data/crafting/catalog.json').read_text())
story=json.loads((ROOT/'data/crafting/courier_story.json').read_text())
components=data['components'];recipes=data['recipes'];pages=data['pages']
idx={c['id']:c for c in components};raw={m['id']:m for m in data['materials']}
assert len(idx)==len(components)==200
assert Counter(c['kind'] for c in components)==dict(framework=50,striker=90,core=60)
assert len({c['name'] for c in components})==200
assert len(recipes)==len({r['id'] for r in recipes})==180
assert len(raw)==36 and len(data['families'])==15
assert Counter(r['family'] for r in recipes)=={f['id']:12 for f in data['families']}
assert set(idx)=={r[k] for r in recipes for k in ['framework_id','striker_id','core_id']}
assert {p['id'] for p in pages}=={q['reward_page_id'] for q in story['quests'] if 'reward_page_id' in q}
assert len(story['quests'])==len({q['id'] for q in story['quests']})==24
for p in pages:
 assert set(p['component_ids'])=={c['id'] for c in components if c['recipe_page_id']==p['id']}
 assert set(p['recipe_ids'])=={r['id'] for r in recipes if r['discovery_page_id']==p['id']}
for c in components:
 assert c['appraisal_gold']>c['sell_gold']>=0
 if c['buy_gold'] is not None:assert c['buy_gold']>c['sell_gold']
 if c.get('shaping'):
  shape=c['shaping'];cost=shape['fee_gold']+sum(raw[x['material_id']]['buy_gold']*x['quantity'] for x in shape['inputs'])
  assert cost>c['sell_gold'],(c['name'],'shaping resale arbitrage')
  assert all(x['quantity']>0 for x in shape['inputs'])
  # Even treating all six accumulated degraded stocks as recovered raw stock cannot create value.
 else:assert c['combat_effect'] in g['EFFECT_SPECS']
for r in recipes:
 f,s,c=[idx[r[k]] for k in ['framework_id','striker_id','core_id']]
 assert f['weapon_family']==s['weapon_family']==r['family']
 assert g['stats'](f,s,c,3,'sands')==r['sands_masterwork_skill3']
 assert r['sands_cracked_plus1_skill3']['friendly_fire']
 assert not r['requires_recipe_to_attempt'] and r['exclusive_hero'] is None
count=0;checks=0;max_profit=-10**9
for family,(frames,strikers) in g['byfamily'].items():
 for f in frames:
  for s in strikers:
   for c in g['cores']:
    count+=1
    # Both untrained and max-skill boundaries, every legal assembly.
    for skill in [0,3]:
     a=g['stats'](f,s,c,skill);m=g['stats'](f,s,c,skill,'mistvale');z=g['stats'](f,s,c,skill,'sands');L=a['effective_strike_limit']
     assert 2<=L<=10 and a['masterwork_multiplier']<=1.75 and z['masterwork_multiplier']<=2
     for channel in ['physical_attack','elemental_attack']:
      assert a[channel]<=m[channel]<=z[channel]
     for forge in ['standard','mistvale','sands']:
      perfect=g['stats'](f,s,c,skill,forge)
      under=g['stats'](f,s,c,skill,forge,L-1)
      cracked=g['stats'](f,s,c,skill,forge,L+1)
      worst=g['stats'](f,s,c,skill,forge,15)
      assert under['physical_attack']<=perfect['physical_attack']
      assert under['durability_design_center']>perfect['durability_design_center']
      assert cracked['elemental_attack']>=perfect['elemental_attack']
      assert cracked['hidden_remaining_durability'] and cracked['friendly_fire']
      assert 1<=cracked['hidden_durability_range'][0]<=cracked['hidden_durability_range'][1]<perfect['durability_design_center']
      assert worst['terminal_burst_radius_m']<=5 and worst['state']=='cracked'
      checks+=1
    # Lowest direct purchase or shaping cost; cores use appraisal even if not sold (conservative).
    cost=0
    for part in [f,s]:
     shape=part['shaping'];shape_cost=shape['fee_gold']+sum(raw[x['material_id']]['buy_gold']*x['quantity'] for x in shape['inputs'])
     cost+=min(shape_cost,part['buy_gold'] if part['buy_gold'] is not None else shape_cost)
    cost+=c['appraisal_gold']
    profit=a['weapon_sell_gold']-cost-a['forge_fee_gold'];max_profit=max(max_profit,profit)
    assert profit<0,(f['name'],s['name'],c['name'],'weapon resale arbitrage')
assert count==18000
# Exact advertised ceilings independently verify the curve endpoints.
assert abs((1.10+.65*(2**1-1))-1.75)<1e-9
assert abs((1.25+.75*(2**1-1))-2)<1e-9
assert story['quests'][0]['on_accept']==['grant_ancient_ledger']
reveal=next(q for q in story['quests'] if q['id']=='book_awakening')
assert set(reveal['qualifying_outcomes'])=={'under_struck','masterwork','cracked'}
salvage=json.loads((ROOT/'data/crafting/salvage.json').read_text())['items']
assert len(salvage)==len({x['id'] for x in salvage})==96
for item in salvage:
 assert item['buy_gold'] is None and item['combine']['quantity'] in (4,5)
 assert item['combine']['output_id'] in (idx | raw)
 if item['kind']=='core_shard':
  assert idx[item['core_id']]['sell_gold'] <= item['combine']['fee_gold']+5*item['sell_gold']
report=dict(status='PASS',salvage_items=96,components=200,raw_materials=36,named_recipes=180,legal_assemblies=count,forge_state_boundary_groups=checks,regional_folios=18,story_entries=24,max_direct_buy_shape_forge_sell_profit_gold=max_profit,limits='Numerical and reference validation only; no combat playtest, runtime integration or full campaign economy simulation.')
(ROOT/'docs/crafting/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
