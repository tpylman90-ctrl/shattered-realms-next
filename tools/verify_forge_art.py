#!/usr/bin/env python3
"""Validate the 702-entry catalog, completed replacement art and remaining placeholders."""
import hashlib, json, struct
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "data/entropic_forge/forge_test_catalog.json").read_text(encoding="utf-8"))
expected = {"frameworks": 150, "strikers": 180, "cores": 60, "stocks": 36, "salvage": 96, "recipes": 180}
paths = []
for category, count in expected.items():
    entries = catalog[category]
    assert len(entries) == count, f"{category}: got {len(entries)}, expected {count}"
    for entry in entries:
        icon = entry.get("icon")
        assert icon and icon.startswith("res://assets/entropic_forge/icons/"), entry
        paths.append(root / icon.removeprefix("res://"))
replacements = [e for category in ("frameworks", "strikers") for e in catalog[category] if e.get("art_status") == "distinct_inventory_component"]
pending = [e for category in ("frameworks", "strikers") for e in catalog[category] if e.get("art_status") == "placeholder_existing_family_component"]
assert len(replacements) + len(pending) == 190, "Every expansion entry must report its art state"
assert len(paths) == 702 and len(set(paths)) == 512 + len(replacements), "Only explicitly pending entries may reuse original art"
hashes = set()
for entry in replacements:
    path = root / entry["icon"].removeprefix("res://")
    payload = path.read_bytes()
    assert payload[:8] == b'\x89PNG\r\n\x1a\n', path
    assert struct.unpack('>II',payload[16:24]) == (512,512), path
    assert payload[25] in (4,6), f"Replacement must retain alpha: {path}"
    digest = hashlib.sha256(payload).hexdigest()
    assert digest not in hashes, f"Duplicate replacement image: {path}"
    hashes.add(digest)

room = root / "assets/forge/forge_room.png"
present = sum(path.is_file() for path in paths)
if present == 0 and not room.exists():
    print("Forge catalog verified: 702 indexed items. Original artwork overlay is absent; preview will use fallback.")
else:
    missing = [str(p.relative_to(root)) for p in set(paths) if not p.is_file()]
    if not room.exists():
        missing.append("assets/forge/forge_room.png")
    assert not missing, f"Partial artwork upload: {len(missing)} files missing, first: {missing[:8]}"
    print(f"Forge artwork verified: 512 original icons, {len(replacements)} distinct replacements, {len(pending)} placeholders pending, plus room.")
