#!/usr/bin/env python3
"""Validate committed forge artwork and the 512-entry item/path contract."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "data/entropic_forge/forge_test_catalog.json").read_text(encoding="utf-8"))
expected = {"frameworks": 50, "strikers": 90, "cores": 60, "stocks": 36, "salvage": 96, "recipes": 180}
paths = []
for category, count in expected.items():
    entries = catalog[category]
    assert len(entries) == count, f"{category}: got {len(entries)}, expected {count}"
    for entry in entries:
        icon = entry.get("icon")
        assert icon and icon.startswith("res://assets/entropic_forge/icons/"), entry
        paths.append(root / icon.removeprefix("res://"))
assert len(paths) == 512 and len(set(paths)) == 512, "Expected 512 unique icon paths"

room = root / "assets/forge/forge_room.png"
present = sum(path.is_file() for path in paths)
if present == 0 and not room.exists():
    print("Forge catalog verified: 512 indexed items. Artwork overlay not yet committed; preview will use fallback.")
else:
    missing = [str(p.relative_to(root)) for p in paths if not p.is_file()]
    if not room.exists():
        missing.append("assets/forge/forge_room.png")
    assert not missing, f"Partial artwork upload: {len(missing)} files missing, first: {missing[:8]}"
    print("Forge artwork complete: 512 icons and illustrated room.")
