#!/usr/bin/env blender --background --python
"""Render modular Entropic Forge axe parts; never composes a complete weapon.

The meshes are intentionally independent: three hafts, six heads, three cores,
and three effect-only overlays. NumPy creates the curved/tapered haft profiles.
"""
import argparse
import json
import math
import os
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector


SIZE = 512
ROOT = Path(__file__).resolve().parents[2]


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/blender-forge")
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    return parser.parse_args(argv)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves):
        for item in list(datablocks):
            if item.users == 0:
                datablocks.remove(item)


def material(name, color, metallic=0.0, roughness=0.45, emission=0.0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Metallic"].default_value = metallic
    bsdf.inputs["Roughness"].default_value = roughness
    if emission:
        bsdf.inputs["Emission Color"].default_value = (*color, 1.0)
        bsdf.inputs["Emission Strength"].default_value = emission
    return mat


WOOD = material("Material | Ashwood", (0.28, 0.105, 0.035), roughness=0.32)
WOOD_LIGHT = material("Material | Pale ash grain", (0.60, 0.30, 0.09), roughness=0.42)
IRON = material("Material | Forged iron", (0.105, 0.15, 0.19), metallic=0.82, roughness=0.28)
STEEL = material("Material | Honed steel", (0.48, 0.61, 0.65), metallic=0.9, roughness=0.2)
GOLD = material("Material | Brass fittings", (0.72, 0.39, 0.09), metallic=0.78, roughness=0.25)
LEATHER = material("Material | Wrapped leather", (0.11, 0.035, 0.025), roughness=0.58)
CORE_MATS = {
    "Cinder": material("Core | Cinder pearl", (1.0, 0.20, 0.025), metallic=0.18, roughness=0.22, emission=1.8),
    "Rime": material("Core | Rime shard", (0.15, 0.67, 1.0), metallic=0.25, roughness=0.16, emission=1.5),
    "Storm": material("Core | Stormglass", (0.52, 0.22, 1.0), metallic=0.2, roughness=0.2, emission=1.8),
}
EFFECT_MATS = {
    "Cinder": material("Effect | Ember glow", (1.0, 0.13, 0.015), emission=4.0),
    "Rime": material("Effect | Frost glow", (0.15, 0.68, 1.0), emission=3.5),
    "Storm": material("Effect | Arc glow", (0.63, 0.28, 1.0), emission=4.0),
}


def mesh_object(name, vertices, faces, mat, bevel=0.0):
    mesh = bpy.data.meshes.new(name + " Mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.materials.append(mat)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    if bevel:
        mod = obj.modifiers.new("Soft forged edges", "BEVEL")
        mod.width = bevel
        mod.segments = 3
        obj.modifiers.new("Weighted face normals", "WEIGHTED_NORMAL")
    return obj


def bevel_cube(name, location, scale, mat, bevel=0.035):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    mod = obj.modifiers.new("Rounded edges", "BEVEL")
    mod.width = bevel
    mod.segments = 3
    obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    return obj


def sphere(name, location, scale, mat, ico=False):
    if ico:
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=1, location=location)
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(mat)
    for p in obj.data.polygons:
        p.use_smooth = not ico
    return obj


def curve_mesh(name, points, radii, mat, sides=10):
    """Build a tube along a centerline using NumPy-generated rings."""
    pts = np.asarray(points, dtype=float)
    rad = np.asarray(radii, dtype=float)
    verts, faces = [], []
    for i, point in enumerate(pts):
        tangent = pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]
        tangent = tangent / (np.linalg.norm(tangent) + 1e-9)
        side = np.array([1.0, 0.0, 0.0])
        if abs(np.dot(tangent, side)) > 0.88:
            side = np.array([0.0, 0.0, 1.0])
        side -= tangent * np.dot(side, tangent)
        side /= np.linalg.norm(side) + 1e-9
        normal = np.cross(tangent, side)
        for j in range(sides):
            angle = (2 * math.pi * j) / sides
            v = point + rad[i] * (math.cos(angle) * side + math.sin(angle) * normal)
            verts.append(tuple(v))
    for i in range(len(pts) - 1):
        for j in range(sides):
            a = i * sides + j
            b = i * sides + (j + 1) % sides
            faces.append((a, b, b + sides, a + sides))
    faces.extend([tuple(range(sides - 1, -1, -1)), tuple((len(pts) - 1) * sides + j for j in range(sides))])
    return mesh_object(name, verts, faces, mat, bevel=0.012)


def torus(name, loc, major, minor, mat):
    bpy.ops.mesh.primitive_torus_add(major_radius=major, minor_radius=minor, major_segments=36, minor_segments=10, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def make_handle(name, style):
    t = np.linspace(0.0, 1.0, 34)
    y = -1.72 + 2.74 * t
    if style == "Ashwood":
        x = 0.08 * np.sin(t * math.pi * 1.3) - 0.02 * t
        radius = 0.115 + 0.025 * np.sin(t * math.pi) + 0.035 * t
        wood, accent = WOOD, WOOD_LIGHT
    elif style == "Ironbound":
        x = 0.025 * np.sin(t * math.pi * 2.0)
        radius = 0.14 - 0.018 * t + 0.02 * np.sin(t * math.pi)
        wood, accent = IRON, STEEL
    else:  # Thornwood
        x = 0.08 * np.sin(t * math.pi * 2.0) + 0.04 * np.sin(t * math.pi * 5.0)
        radius = 0.12 + 0.028 * np.cos(t * math.pi * 2.0) ** 2
        wood, accent = material("Material | Dark thornwood", (0.16, 0.075, 0.035), roughness=0.4), GOLD
    curve_mesh(name + " | haft", np.column_stack((x, y, np.zeros_like(y))), radius, wood, 12)
    for idx, t_band in enumerate((0.08, 0.13, 0.80, 0.86)):
        yy = -1.72 + 2.74 * t_band
        xx = float(np.interp(t_band, t, x))
        torus(name + " | ferrule " + str(idx + 1), (xx, yy, 0), 0.128 if style != "Ironbound" else 0.145, 0.025, accent)
    # A restrained leather grip and contrasting wrap ribs.
    grip_y = np.linspace(-0.62, 0.24, 20)
    grip_x = np.interp((grip_y + 1.72) / 2.74, t, x)
    grip_r = np.interp((grip_y + 1.72) / 2.74, t, radius) * 1.08
    curve_mesh(name + " | leather grip", np.column_stack((grip_x, grip_y, np.full_like(grip_y, 0.005))), grip_r, LEATHER, 10)
    for yy in np.linspace(-0.55, 0.17, 7):
        xx = float(np.interp((yy + 1.72) / 2.74, t, x))
        torus(name + " | wrap", (xx, yy, 0.005), float(np.interp((yy + 1.72) / 2.74, t, radius)) * 1.07, 0.012, accent)
    sphere(name + " | pommel", (float(x[0]), -1.76, 0), (0.19, 0.17, 0.15), accent, ico=style == "Thornwood")
    sphere(name + " | socket collar", (float(x[-1]), 0.99, 0), (0.20, 0.12, 0.16), accent)


def extruded_profile(name, points, mat, depth=0.22, bevel=0.035):
    verts = [(x, y, z) for z in (-depth / 2, depth / 2) for x, y in points]
    n = len(points)
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, j + n, i + n))
    return mesh_object(name, verts, faces, mat, bevel)


def make_blade(name, style):
    steel = STEEL if style in ("Crescent", "Broadhead", "Double") else IRON
    if style == "Battle":
        pts = [(-0.12, -0.58), (-0.50, -0.32), (-1.30, -0.20), (-1.55, 0.12), (-1.20, 0.72), (-0.48, 0.80), (-0.12, 0.56), (0.12, 0.56), (0.48, 0.80), (1.20, 0.72), (1.55, 0.12), (1.30, -0.20), (0.50, -0.32), (0.12, -0.58)]
    elif style == "Crescent":
        pts = [(-0.18, -0.63), (-0.63, -0.48), (-1.32, -0.08), (-1.58, 0.42), (-1.20, 0.98), (-0.91, 0.62), (-0.91, 0.22), (-0.56, -0.06), (-0.16, -0.12), (0.16, -0.12), (0.56, -0.06), (0.91, 0.22), (0.91, 0.62), (1.20, 0.98), (1.58, 0.42), (1.32, -0.08), (0.63, -0.48), (0.18, -0.63)]
    elif style == "Cleaver":
        pts = [(-0.16, -0.62), (-0.58, -0.38), (-1.22, -0.15), (-1.40, 0.12), (-1.37, 0.86), (-0.18, 0.72), (-0.12, 0.56), (0.12, 0.56), (0.18, 0.72), (1.37, 0.86), (1.40, 0.12), (1.22, -0.15), (0.58, -0.38), (0.16, -0.62)]
    elif style == "Hook":
        pts = [(-0.16, -0.62), (-0.55, -0.35), (-1.05, -0.10), (-1.35, 0.18), (-1.55, 0.78), (-1.06, 0.52), (-0.86, 0.19), (-0.40, -0.04), (-0.14, -0.11), (0.14, -0.11), (0.48, -0.03), (0.80, 0.14), (1.08, 0.47), (1.20, 0.91), (1.52, 0.83), (1.42, 0.25), (1.13, -0.12), (0.55, -0.42), (0.16, -0.62)]
    elif style == "Double":
        pts = [(-0.18, -0.60), (-0.66, -0.42), (-1.30, -0.08), (-1.58, 0.35), (-1.28, 0.84), (-0.52, 0.62), (-0.20, 0.47), (0.20, 0.47), (0.52, 0.62), (1.28, 0.84), (1.58, 0.35), (1.30, -0.08), (0.66, -0.42), (0.18, -0.60)]
    else:  # Broadhead
        pts = [(-0.16, -0.60), (-0.62, -0.37), (-1.42, -0.05), (-1.62, 0.30), (-1.48, 0.88), (-0.78, 0.78), (-0.42, 0.62), (-0.16, 0.50), (0.16, 0.50), (0.42, 0.62), (0.78, 0.78), (1.48, 0.88), (1.62, 0.30), (1.42, -0.05), (0.62, -0.37), (0.16, -0.60)]
    extruded_profile(name + " | head", pts, steel)
    # Central socket ring remains open so the handle and core can be selected independently.
    torus(name + " | empty socket lip", (0, -0.42, 0.13), 0.28, 0.075, GOLD if style in ("Battle", "Hook") else IRON)
    bevel_cube(name + " | socket bridge", (0, -0.54, 0.10), (0.36, 0.16, 0.17), steel, 0.045)
    # Sharpened edges are thin independent bevel strips on the outer silhouette.
    for side in (-1, 1):
        if style == "Crescent":
            line = [(side * 0.88, 0.56, 0.145), (side * 1.17, 0.83, 0.145), (side * 1.50, 0.42, 0.145)]
        elif style == "Cleaver":
            line = [(side * 0.18, 0.70, 0.145), (side * 1.32, 0.80, 0.145), (side * 1.37, 0.14, 0.145)]
        else:
            line = [(side * 0.50, 0.68, 0.145), (side * 1.30, 0.62, 0.145), (side * 1.48, 0.22, 0.145)]
        curve_mesh(name + " | edge glint " + str(side), line, [0.018] * 3, STEEL, 6)
    if style == "Hook":
        sphere(name + " | crown rivet", (0, 0.53, 0.17), (0.075, 0.075, 0.035), GOLD)


def make_core(name, element):
    mat = CORE_MATS[element]
    # A small, faceted crystal is the core asset; the surrounding effect is rendered separately.
    sphere(name + " | crystal", (0, 0, 0), (0.34, 0.43, 0.20), mat, ico=True)
    torus(name + " | brass cage", (0, 0, -0.04), 0.43, 0.055, GOLD)
    for x in (-0.36, 0.36):
        bevel_cube(name + " | clamp", (x, 0, 0), (0.12, 0.54, 0.12), GOLD, 0.04)


def make_effect(name, element):
    mat = EFFECT_MATS[element]
    if element == "Cinder":
        for i, (x, y, r) in enumerate([(-0.34, -0.20, .075), (.28, -.08, .06), (-.18, .33, .05), (.38, .39, .045), (0, -.42, .045)]):
            sphere(name + " | ember " + str(i), (x, y, 0), (r, r * 1.35, r), mat, ico=True)
        for s in (-1, 1):
            curve_mesh(name + " | flame wisp " + str(s), [(s * .16, -.38, 0), (s * .30, -.10, 0), (s * .22, .12, 0), (s * .42, .40, 0)], [.055, .035, .045, .008], mat, 7)
    elif element == "Rime":
        for angle in np.linspace(0, 2 * math.pi, 6, endpoint=False):
            dx, dy = math.cos(angle), math.sin(angle)
            curve_mesh(name + " | frost ray", [(0, 0, 0), (dx * .27, dy * .27, 0), (dx * .47, dy * .47, 0)], [.035, .022, .008], mat, 6)
            bx, by = -dy, dx
            curve_mesh(name + " | frost fork", [(dx * .25, dy * .25, 0), (dx * .34 + bx * .12, dy * .34 + by * .12, 0)], [.022, .006], mat, 6)
    else:
        for points in ([(-.48, -.30, 0), (-.20, -.06, 0), (-.32, .16, 0), (0, .42, 0)], [(.48, .30, 0), (.20, .06, 0), (.32, -.16, 0), (0, -.42, 0)]):
            curve_mesh(name + " | lightning arc", points, [.05, .025, .04, .008], mat, 7)
        for x, y in [(-.34, .35), (.36, -.34), (.38, .32)]:
            sphere(name + " | spark", (x, y, 0), (.045, .045, .04), mat, ico=True)


def setup_camera_and_lights():
    bpy.ops.object.camera_add(location=(0, 0, 9))
    cam = bpy.context.object
    cam.name = "Render Camera | orthographic component view"
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 4.6
    bpy.context.scene.camera = cam
    for name, loc, power, size in [
        ("Key | warm softbox", (-3.4, 4.0, 5.0), 700, 4.0),
        ("Fill | cool softbox", (3.8, 0.4, 3.5), 500, 3.0),
        ("Rim | top strip", (0.0, -3.0, 3.5), 600, 2.5),
    ]:
        bpy.ops.object.light_add(type="AREA", location=loc)
        light = bpy.context.object
        light.name = name
        light.data.energy = power
        light.data.shape = "DISK"
        light.data.size = size
        light.rotation_euler = (Vector((0, 0, 0)) - light.location).to_track_quat("-Z", "Y").to_euler()
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 24
    scene.cycles.use_denoising = False
    scene.render.resolution_x = SIZE
    scene.render.resolution_y = SIZE
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "Medium High Contrast"
    scene.view_settings.exposure = 0
    scene.view_settings.gamma = 1
    if scene.world is None:
        scene.world = bpy.data.worlds.new("Forge | transparent render world")
    scene.world.color = (0.025, 0.025, 0.025)


def render_assets(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    clear_scene()
    setup_camera_and_lights()
    components = []
    specs = [
        ("handle", "ashwood", "Ashwood", lambda: make_handle("Handle | Ashwood", "Ashwood"), (247, 143)),
        ("handle", "ironbound", "Ironbound", lambda: make_handle("Handle | Ironbound", "Ironbound"), (256, 143)),
        ("handle", "thornwood", "Thornwood", lambda: make_handle("Handle | Thornwood", "Thornwood"), (256, 143)),
        ("blade", "battle", "Battle", lambda: make_blade("Blade | Battle", "Battle"), (256, 303)),
        ("blade", "crescent", "Crescent", lambda: make_blade("Blade | Crescent", "Crescent"), (256, 303)),
        ("blade", "cleaver", "Cleaver", lambda: make_blade("Blade | Cleaver", "Cleaver"), (256, 303)),
        ("blade", "hook", "Hook", lambda: make_blade("Blade | Hook", "Hook"), (256, 303)),
        ("blade", "double", "Double", lambda: make_blade("Blade | Double", "Double"), (256, 303)),
        ("blade", "broadhead", "Broadhead", lambda: make_blade("Blade | Broadhead", "Broadhead"), (256, 303)),
        ("core", "cinder_pearl", "Cinder Pearl", lambda: make_core("Core | Cinder Pearl", "Cinder"), (256, 256)),
        ("core", "rime_shard", "Rime Shard", lambda: make_core("Core | Rime Shard", "Rime"), (256, 256)),
        ("core", "stormglass", "Stormglass", lambda: make_core("Core | Stormglass", "Storm"), (256, 256)),
        ("effect", "cinder_glow", "Cinder glow", lambda: make_effect("Effect | Cinder Glow", "Cinder"), (256, 256)),
        ("effect", "rime_burst", "Rime burst", lambda: make_effect("Effect | Rime Burst", "Rime"), (256, 256)),
        ("effect", "storm_arcs", "Storm arcs", lambda: make_effect("Effect | Storm Arcs", "Storm"), (256, 256)),
    ]
    for kind, slug, label, build, anchor in specs:
        # Isolate each part in the saved master scene and in its own transparent render.
        for obj in list(bpy.context.scene.objects):
            if obj.type in {"MESH", "CURVE"}:
                bpy.data.objects.remove(obj, do_unlink=True)
        build()
        asset_objects = [obj for obj in bpy.context.scene.objects if obj.type in {"MESH", "CURVE"}]
        for obj in bpy.context.scene.objects:
            obj.hide_render = obj.type in {"MESH", "CURVE"} and obj not in asset_objects
        name = f"axe_{kind}_{slug}.png"
        bpy.context.scene.render.filepath = str(out_dir / name)
        bpy.ops.render.render(write_still=True)
        components.append({
            "file": name,
            "kind": kind,
            "name": label,
            "size": [SIZE, SIZE],
            "anchor_px": {"x": anchor[0], "y_from_top": anchor[1]},
            "display_rotation_degrees": {"handle": 97, "blade": 90, "core": 0, "effect": 0}[kind],
            "catalog_replacement": False,
            "modular_only": True,
        })
        # Remove this part before creating the next; camera and lights stay editable.
        for obj in asset_objects:
            bpy.data.objects.remove(obj, do_unlink=True)
    # Separate review scene includes all component objects in collections, but no assembled axe.
    # Rebuild all parts in a staging layout so artists can inspect/edit the source blend.
    for index, (kind, slug, label, build, anchor) in enumerate(specs):
        before = set(bpy.context.scene.objects[:])
        build()
        new_objects = set(bpy.context.scene.objects[:]) - before
        column, row = index % 5, index // 5
        offset_x, offset_y = (column - 2) * 3.5, (1 - row) * 3.5
        for obj in new_objects:
            obj.name = f"{kind.upper()} | {label} | {obj.name}"
            obj.location.x += offset_x
            obj.location.y += offset_y
    bpy.context.scene.camera.data.ortho_scale = 17.5
    blend_path = out_dir / "axe_modular_components.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    manifest = {
        "family": "Axe",
        "review_only": True,
        "assembled_weapon_rendered": False,
        "component_model": "selected handle and blade define shape; core adds separate glow/effects",
        "dimensions_px": [SIZE, SIZE],
        "components": components,
        "renders": [c["file"] for c in components],
        "scene": blend_path.name,
        "notes": [
            "Each PNG contains one component category item only; no handle-plus-blade composition is rendered.",
            "Core inserts and their effect overlays are separate assets.",
            "Socket anchors are preview metadata and must be calibrated against catalog sprites before integration.",
            "Source scene is an editable library of standalone components, not a composed weapon.",
        ],
    }
    (out_dir / "render_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {len(components)} standalone components to {out_dir}")


if __name__ == "__main__":
    render_assets(Path(args().output).resolve())
