#!/usr/bin/env python3
"""Render a Blender-made axe component proof sheet for Entropic Forge.

The generated PNGs are review assets. They do not replace catalog art or change
gameplay data until their sockets and in-game appearance have been approved.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector


def cli_args() -> argparse.Namespace:
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/blender-forge")
    return parser.parse_args(argv)


def material(name: str, color: tuple[float, float, float, float], metallic: float, roughness: float) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = True
    principled = mat.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = color
    principled.inputs["Metallic"].default_value = metallic
    principled.inputs["Roughness"].default_value = roughness
    return mat


def aim(obj: bpy.types.Object, point: tuple[float, float, float]) -> None:
    obj.rotation_euler = (Vector(point) - obj.location).to_track_quat("-Z", "Y").to_euler()


def create_mesh(name: str, vertices: list[tuple[float, float, float]], faces: list[tuple[int, ...]], mat: bpy.types.Material) -> bpy.types.Object:
    mesh = bpy.data.meshes.new(name + "Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.materials.append(mat)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    return obj


def bevel(obj: bpy.types.Object, width: float = 0.035, segments: int = 3) -> None:
    mod = obj.modifiers.new("Crisp crafted edges", "BEVEL")
    mod.width = width
    mod.segments = segments


def cylinder_between(name: str, a: tuple[float, float, float], b: tuple[float, float, float], radius: float,
                     mat: bpy.types.Material, vertices: int = 16) -> bpy.types.Object:
    start, end = Vector(a), Vector(b)
    direction = end - start
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=direction.length,
                                        location=(start + end) * 0.5)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(mat)
    bevel(obj, min(radius * 0.2, 0.025), 2)
    return obj


def create_haft(wood: bpy.types.Material, dark_wood: bpy.types.Material, brass: bpy.types.Material,
                leather: bpy.types.Material) -> list[bpy.types.Object]:
    # NumPy generates a gently curved, tapered octagonal haft with a reinforced tenon.
    z = np.linspace(-2.34, 2.28, 46, dtype=np.float64)
    angles = np.linspace(0.0, 2.0 * math.pi, 9, endpoint=False)
    radius = 0.105 + 0.035 * np.exp(-((z + 0.25) / 1.4) ** 2)
    radius += 0.018 * (z < -1.75)
    center_x = 0.055 * np.sin(z * 1.15)
    vertices: list[tuple[float, float, float]] = []
    for zi, ri, xi in zip(z, radius, center_x):
        for angle in angles:
            vertices.append((float(xi + ri * math.cos(angle)), float(ri * math.sin(angle)), float(zi)))
    faces: list[tuple[int, ...]] = []
    for row in range(len(z) - 1):
        for col in range(len(angles)):
            nxt = (col + 1) % len(angles)
            faces.append((row * len(angles) + col, row * len(angles) + nxt,
                          (row + 1) * len(angles) + nxt, (row + 1) * len(angles) + col))
    faces.append(tuple(range(len(angles) - 1, -1, -1)))
    faces.append(tuple((len(z) - 1) * len(angles) + i for i in range(len(angles))))
    haft = create_mesh("Woodcutter haft | curved ashwood", vertices, faces, wood)
    bevel(haft, 0.018, 2)

    objects = [haft]
    # Separate wrap collars and metal fittings add readable dimensional details.
    for index, (height, mat) in enumerate([
        (-1.72, brass), (-1.48, leather), (-1.35, leather),
        (-1.22, leather), (1.92, brass), (2.08, dark_wood),
    ]):
        bpy.ops.mesh.primitive_torus_add(major_radius=0.112 if height < 1.5 else 0.145,
                                         minor_radius=0.026, major_segments=24, minor_segments=8,
                                         location=(0.055 * math.sin(height * 1.15), 0, height))
        ring = bpy.context.object
        ring.name = f"Haft fitting {index + 1:02d}"
        ring.data.materials.append(mat)
        objects.append(ring)
    cylinder_between("Head tenon", (0.055 * math.sin(2.15 * 1.15), 0, 1.98),
                     (0.055 * math.sin(2.15 * 1.15), 0, 2.39), 0.095, dark_wood, 12)
    objects.append(bpy.context.object)
    return objects


def create_axe_head(steel: bpy.types.Material, edge_mat: bpy.types.Material, brass: bpy.types.Material) -> list[bpy.types.Object]:
    # The head wraps around the tenon; its open ring leaves the selected haft visible.
    profile = [(-1.48, 2.70), (-1.35, 2.42), (-1.12, 2.12), (-0.90, 1.83),
               (-0.52, 1.80), (-0.32, 1.94), (-0.30, 2.39), (-0.48, 2.54),
               (-0.83, 2.62), (-1.22, 2.66)]
    thickness = 0.19
    vertices = [(x, y, z) for y in (-thickness, thickness) for x, z in profile]
    count = len(profile)
    faces = [tuple(range(count)), tuple(range(count, count * 2))]
    faces += [(i, (i + 1) % count, (i + 1) % count + count, i + count) for i in range(count)]
    blade = create_mesh("Forester axe bit | forged wedge", vertices, faces, steel)
    bevel(blade, 0.055, 4)

    # A bright bevel ribbon follows the cutting edge and makes the silhouette legible at icon scale.
    edge_points = [(-1.48, -0.214, 2.70), (-1.35, -0.214, 2.42), (-1.12, -0.214, 2.12), (-0.90, -0.214, 1.83)]
    curve = bpy.data.curves.new("Sharpened edge", "CURVE")
    curve.dimensions = "3D"
    curve.bevel_depth = 0.028
    curve.bevel_resolution = 3
    spline = curve.splines.new("POLY")
    spline.points.add(len(edge_points) - 1)
    for point, coord in zip(spline.points, edge_points):
        point.co = (*coord, 1.0)
    edge = bpy.data.objects.new("Continuous polished cutting bevel", curve)
    bpy.context.collection.objects.link(edge)
    edge.data.materials.append(edge_mat)

    # The toroidal socket is a real open ring, not a painted oval.
    bpy.ops.mesh.primitive_torus_add(major_radius=0.205, minor_radius=0.075,
                                     major_segments=40, minor_segments=12,
                                     location=(0.0, 0, 2.12))
    eye = bpy.context.object
    eye.name = "Open haft eye | forged socket rim"
    eye.scale = (1.0, 0.76, 1.0)
    eye.data.materials.append(brass)
    return [blade, edge, eye]


def prepare_scene() -> tuple[bpy.types.Scene, bpy.types.Object]:
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 32
    # Ubuntu's repository Blender build may omit OpenImageDenoiser (OIDN).
    # Keep the headless CPU pipeline portable across runners.
    scene.cycles.use_denoising = False
    scene.render.resolution_x = 1024
    scene.render.resolution_y = 1024
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = True
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.view_transform = "AgX"
    scene.world.color = (0.16, 0.16, 0.16)

    bpy.ops.object.camera_add(location=(0.0, -10.0, 3.1))
    camera = bpy.context.object
    camera.name = "Forge icon orthographic camera"
    aim(camera, (0.0, 0.0, 0.0))
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = 5.85
    scene.camera = camera

    for name, location, power, size, color in [
        ("Warm key", (-4.5, -5.0, 6.5), 950, 4.0, (1.0, 0.78, 0.54)),
        ("Cool fill", (4.0, -3.0, 2.0), 620, 3.5, (0.48, 0.68, 1.0)),
        ("Rim light", (0.5, 3.0, 5.0), 1200, 3.0, (1.0, 0.47, 0.18)),
    ]:
        bpy.ops.object.light_add(type="AREA", location=location)
        lamp = bpy.context.object
        lamp.name = name
        lamp.data.energy = power
        lamp.data.shape = "DISK"
        lamp.data.size = size
        lamp.data.color = color
        aim(lamp, (0, 0, 0.4))
    return scene, camera


def render_group(scene: bpy.types.Scene, objects: list[bpy.types.Object], path: Path) -> None:
    for obj in bpy.data.objects:
        obj.hide_render = obj not in objects and obj.type not in {"CAMERA", "LIGHT"}
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def main() -> None:
    args = cli_args()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

    scene, camera = prepare_scene()
    wood = material("Ashwood | satin grain", (0.25, 0.095, 0.032, 1), 0.05, 0.32)
    dark_wood = material("Dark end grain", (0.075, 0.027, 0.013, 1), 0.08, 0.38)
    leather = material("Ox-blood leather wrap", (0.19, 0.025, 0.018, 1), 0.0, 0.46)
    brass = material("Aged forge brass", (0.50, 0.25, 0.065, 1), 0.72, 0.24)
    steel = material("Tempered steel", (0.17, 0.23, 0.28, 1), 0.86, 0.22)
    edge_mat = material("Polished cutting edge", (0.72, 0.82, 0.88, 1), 0.92, 0.14)

    haft = create_haft(wood, dark_wood, brass, leather)
    head = create_axe_head(steel, edge_mat, brass)
    for obj in bpy.data.objects:
        obj.hide_render = obj.type in {"CAMERA", "LIGHT"}

    render_group(scene, haft, output / "woodcutters_haft_blender_test.png")
    render_group(scene, head, output / "foresters_axe_bit_blender_test.png")
    render_group(scene, haft + head, output / "axe_assembled_blender_test.png")

    scene.render.filepath = str(output / "axe_assembled_blender_test.png")
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.wm.save_as_mainfile(filepath=str(output / "entropic_forge_axe_study.blend"))
    metadata = {
        "generator": "render_forge_components.py",
        "blender": bpy.app.version_string,
        "numpy": np.__version__,
        "family": "Axe",
        "review_only": True,
        "component_names": ["Woodcutter haft", "Forester axe bit"],
        "renders": [
            "woodcutters_haft_blender_test.png",
            "foresters_axe_bit_blender_test.png",
            "axe_assembled_blender_test.png",
        ],
        "mount_note": "Prototype socket and tenon require visual review before catalog attachment metadata is authored.",
    }
    (output / "render_manifest.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
