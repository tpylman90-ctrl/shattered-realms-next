#!/usr/bin/env python3
"""Validate modular transparent component renders using NumPy."""
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "build/blender-forge")
    manifest = json.loads((root / "render_manifest.json").read_text(encoding="utf-8"))
    assert manifest["review_only"] is True
    assert manifest["family"] == "Axe"
    assert manifest["assembled_weapon_rendered"] is False, "A complete weapon render is not allowed"
    components = manifest["components"]
    names = [item["file"] for item in components]
    assert len(names) == len(set(names)), "Component render names must be unique"
    assert manifest["renders"] == names
    counts = Counter(item["kind"] for item in components)
    assert counts == {"handle": 3, "blade": 6, "core": 3, "effect": 3}, f"Unexpected component mix: {counts}"
    for item in components:
        assert item["modular_only"] is True
        assert item["catalog_replacement"] is False
        path = root / item["file"]
        with Image.open(path) as image:
            assert image.format == "PNG", f"Not a PNG: {path}"
            assert image.mode == "RGBA", f"Expected RGBA: {path} ({image.mode})"
            assert image.size == (512, 512), f"Unexpected render size: {path} {image.size}"
            alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
            visible = alpha > 8
            coverage = float(visible.mean())
            assert 0.001 < coverage < 0.75, f"Suspicious alpha coverage {coverage:.3f}: {path}"
            ys, xs = np.nonzero(visible)
            pad = 4
            assert xs.size and ys.min() >= pad and xs.min() >= pad
            assert ys.max() < image.height - pad and xs.max() < image.width - pad
            anchor = item["anchor_px"]
            assert 0 <= anchor["x"] < image.width
            assert 0 <= anchor["y_from_top"] < image.height
            print(f"PASS {path.name}: {item['kind']} {image.width}x{image.height} RGBA, alpha {coverage:.1%}")
    blend = root / manifest["scene"]
    assert blend.is_file() and blend.stat().st_size > 1024, "Editable Blender component scene missing or empty"
    print(f"Validated {len(components)} standalone parts; NumPy {np.__version__}")


if __name__ == "__main__":
    main()
