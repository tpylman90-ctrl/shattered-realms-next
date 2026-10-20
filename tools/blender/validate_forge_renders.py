#!/usr/bin/env python3
"""Check alpha sprites emitted by the Blender forge proof render."""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "build/blender-forge")
    manifest = json.loads((root / "render_manifest.json").read_text(encoding="utf-8"))
    assert manifest["review_only"] is True
    assert manifest["family"] == "Axe"
    for name in manifest["renders"]:
        path = root / name
        with Image.open(path) as image:
            assert image.format == "PNG", f"Not a PNG: {path}"
            assert image.mode == "RGBA", f"Expected RGBA: {path} ({image.mode})"
            assert image.size == (1024, 1024), f"Unexpected render size: {path} {image.size}"
            alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
            visible = alpha > 8
            coverage = float(visible.mean())
            assert 0.01 < coverage < 0.75, f"Suspicious alpha coverage {coverage:.3f}: {path}"
            ys, xs = np.nonzero(visible)
            assert xs.size and ys.min() > 0 and xs.min() > 0
            assert ys.max() < image.height - 1 and xs.max() < image.width - 1
            print(f"PASS {name}: {image.width}x{image.height} RGBA, alpha coverage {coverage:.1%}")
    print(f"Validated {len(manifest['renders'])} Blender renders; NumPy {np.__version__}")


if __name__ == "__main__":
    main()
