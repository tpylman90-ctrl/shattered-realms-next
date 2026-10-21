#!/usr/bin/env python3
"""Validate modular transparent component renders using NumPy."""
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


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
    assert counts == {"handle": 10, "blade": 12, "core": 3, "effect": 3}, f"Unexpected component mix: {counts}"
    for kind in ("handle", "blade"):
        archetypes = {item["base_archetype"] for item in components if item["kind"] == kind}
        assert len(archetypes) == 4, f"Expected four reusable {kind} archetypes, got {sorted(archetypes)}"
    images = []
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
            images.append((item, image.copy()))
            print(f"PASS {path.name}: {item['kind']} {image.width}x{image.height} RGBA, alpha {coverage:.1%}")
    blend = root / manifest["scene"]
    assert blend.is_file() and blend.stat().st_size > 1024, "Editable Blender component scene missing or empty"
    assert manifest["base_archetypes"]["handles"] == ["furnace_haft", "iron_braced", "organic_hook", "split_oak"]
    assert manifest["base_archetypes"]["blades"] == ["bearded", "crescent", "double", "hooked"]
    # A grid of isolated thumbnails is review-friendly while preserving part boundaries.
    cell_w, cell_h, columns = 172, 200, 5
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (33, 37, 43))
    draw = ImageDraw.Draw(sheet)
    for index, (item, rgba) in enumerate(images):
        thumb = rgba.copy()
        thumb.thumbnail((148, 150), Image.Resampling.LANCZOS)
        x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
        x, y = x0 + (cell_w - thumb.width) // 2, y0 + 4
        sheet.paste(thumb, (x, y), thumb)
        draw.text((x0 + 6, y0 + 166), f"{item['kind']}: {item['name']}", fill=(236, 238, 241))
    sheet.save(root / "axe_component_contact_sheet.png")
    print(f"Validated {len(components)} standalone parts; NumPy {np.__version__}")


if __name__ == "__main__":
    main()
