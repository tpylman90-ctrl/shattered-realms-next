#!/usr/bin/env blender --background --python
"""Render modular Entropic Forge axe parts; never composes a complete weapon.

The meshes are intentionally independent: catalog variants derive from four
haft and four head archetypes, while cores/effects remain their own layers.
NumPy creates the curved/tapered haft profiles.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector


SIZE = 512
MATERIAL_CACHE = {}
MESH_CACHE = {}


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
    if name in MATERIAL_CACHE:
        return MATERIAL_CACHE[name]
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
    if not emission:
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        texcoord = nodes.new("ShaderNodeTexCoord")
        noise = nodes.new("ShaderNodeTexNoise")
        noise.inputs["Scale"].default_value = 34.0 if metallic > 0.5 else 6.0
        noise.inputs["Detail"].default_value = 4.0
        noise.inputs["Roughness"].default_value = 0.72
        bump = nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = 0.20 if metallic > 0.5 else 0.24
        bump.inputs["Distance"].default_value = 0.026 if metallic > 0.5 else 0.04
        ramp = nodes.new("ShaderNodeValToRGB")
        ramp.color_ramp.elements[0].position = 0.25
        ramp.color_ramp.elements[0].color = (*(c * 0.52 for c in color), 1.0)
        ramp.color_ramp.elements[1].position = 0.76
        ramp.color_ramp.elements[1].color = (*(min(1.0, c * 1.18 + 0.015) for c in color), 1.0)
        links.new(texcoord.outputs["Generated"], noise.inputs["Vector"])
        links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
        links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
        links.new(noise.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    MATERIAL_CACHE[name] = mat
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


def mesh_object(name, vertices, faces, mat, bevel=0.0, cache_key=None):
    shared = cache_key is not None and cache_key in MESH_CACHE
    if shared:
        mesh = MESH_CACHE[cache_key]
    else:
        mesh = bpy.data.meshes.new(name + " Mesh")
        mesh.from_pydata(vertices, [], faces)
        mesh.materials.append(mat)
        mesh.update()
        if cache_key:
            MESH_CACHE[cache_key] = mesh
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    if shared and obj.material_slots:
        obj.material_slots[0].link = "OBJECT"
        obj.material_slots[0].material = mat
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


def curve_mesh(name, points, radii, mat, sides=10, cache_key=None):
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
    return mesh_object(name, verts, faces, mat, bevel=0.012, cache_key=cache_key)


def torus(name, loc, major, minor, mat, axis="Z"):
    bpy.ops.mesh.primitive_torus_add(major_radius=major, minor_radius=minor, major_segments=36, minor_segments=10, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    if axis == "Y":
        # Haft shafts run along Y, so their ferrules must wrap that axis.
        obj.rotation_euler.x = math.pi / 2
    return obj


def shaft_cuff(name, x, y, radius, mat, detail):
    """A raised, sculpted ferrule wrapped around a Y-axis haft."""
    torus(name + " | outer bead", (x, y, 0), radius * 1.035, 0.052, mat, axis="Y")
    torus(name + " | inner bead", (x, y, 0), radius * 0.91, 0.024, detail, axis="Y")
    torus(name + " | cuff edge", (x, y - 0.065, 0), radius * 0.99, 0.018, detail, axis="Y")
    for side in (-1, 1):
        sphere(name + " | rivet", (x + side * radius * 0.55, y, radius * 0.78),
               (0.042, 0.042, 0.034), detail, ico=True)


def make_handle(name, variant):
    """Build a catalog haft from one of four shared geometric archetypes."""
    style = variant["base"]
    slug = variant["slug"]
    wood = material(f"Haft | {slug} | body", variant["body"], roughness=0.36)
    accent = material(f"Haft | {slug} | fittings", variant["metal"], metallic=0.8, roughness=0.27)
    leather = material(f"Haft | {slug} | wrap", variant["wrap"], roughness=0.6)
    detail = material(f"Haft | {slug} | carved detail", variant["detail"], metallic=0.45, roughness=0.34)
    t = np.linspace(0.0, 1.0, 34)
    y = -1.72 + 2.74 * t
    if style == "split_oak":
        x = 0.08 * np.sin(t * math.pi * 1.3) - 0.02 * t
        radius = 0.115 + 0.025 * np.sin(t * math.pi) + 0.035 * t
    elif style == "iron_braced":
        x = 0.025 * np.sin(t * math.pi * 2.0)
        radius = 0.14 - 0.018 * t + 0.02 * np.sin(t * math.pi)
    elif style == "furnace_haft":
        x = 0.035 * np.sin(t * math.pi * 1.4)
        radius = 0.15 + 0.025 * np.sin(t * math.pi) - 0.02 * t
    else:  # organic_hook
        x = 0.10 * np.sin(t * math.pi * 1.7) + 0.018 * np.sin(t * math.pi * 5.0)
        radius = 0.12 + 0.025 * np.cos(t * math.pi * 2.0) ** 2
    radius *= 1.12
    curve_mesh(name + " | haft", np.column_stack((x, y, np.zeros_like(y))), radius, wood, 12, cache_key="haft:" + style)
    # Heavy socket and butt ferrules give every haft a readable connection point.
    for idx, t_band in enumerate((0.055, 0.105, 0.80, 0.855, 0.91)):
        yy = -1.72 + 2.74 * t_band
        xx = float(np.interp(t_band, t, x))
        rr = float(np.interp(t_band, t, radius))
        shaft_cuff(name + " | ferrule " + str(idx + 1), xx, yy, rr, accent, detail)
        if idx in (0, 4):
            torus(name + " | terminal rim", (xx, yy, 0), rr * 1.14, 0.018, detail, axis="Y")
    # Wrapped center grip with diagonal ribs and a carved secondary inlay.
    grip_y = np.linspace(-0.72, 0.28, 22)
    grip_x = np.interp((grip_y + 1.72) / 2.74, t, x)
    grip_r = np.interp((grip_y + 1.72) / 2.74, t, radius) * 1.10
    curve_mesh(name + " | leather grip", np.column_stack((grip_x, grip_y, np.full_like(grip_y, 0.01))), grip_r, leather, 12)
    for index, yy in enumerate(np.linspace(-0.66, 0.22, 9)):
        xx = float(np.interp((yy + 1.72) / 2.74, t, x))
        rr = float(np.interp((yy + 1.72) / 2.74, t, radius))
        torus(name + " | wrap stitch", (xx, yy, 0.01), rr * 1.08, 0.012, detail if index % 2 == 0 else accent, axis="Y")
    wrap_t = np.linspace(0.0, 1.0, 96)
    wrap_y = -0.68 + 0.88 * wrap_t
    wrap_center_x = np.interp((wrap_y + 1.72) / 2.74, t, x)
    wrap_radius = np.interp((wrap_y + 1.72) / 2.74, t, radius) * 1.11
    wrap_angle = wrap_t * math.pi * 14.0
    wrap_points = np.column_stack((wrap_center_x + wrap_radius * np.cos(wrap_angle), wrap_y,
                                   0.01 + wrap_radius * np.sin(wrap_angle)))
    curve_mesh(name + " | braided grip cord", wrap_points, np.full_like(wrap_t, 0.024), detail, 8)
    # Carved grip medallion and side rivets are individual relief details.
    sphere(name + " | grip medallion", (float(np.interp(0.0, y, x)), -0.18, 0.145), (0.13, 0.17, 0.045), accent, ico=True)
    sphere(name + " | inset mark", (float(np.interp(0.0, y, x)), -0.18, 0.185), (0.07, 0.10, 0.025), detail, ico=True)
    medallion_x = float(np.interp(0.0, y, x))
    crest = extruded_profile(name + " | raised grip crest",
                             [(-.105, -.13), (0, -.20), (.105, -.13),
                              (.105, .02), (0, .13), (-.105, .02)],
                             accent, depth=.045, bevel=.018)
    crest.location = (medallion_x, -.18, .19)
    sphere(name + " | crest stud", (medallion_x, -.18, .23),
           (.043, .055, .025), detail, ico=True)
    sphere(name + " | pommel", (float(x[0]), -1.76, 0), (0.19, 0.17, 0.15), accent, ico=style == "organic_hook")
    if style in {"split_oak", "iron_braced"}:
        for side in (-1, 1):
            channel_points = []
            for yy in np.linspace(-0.54, 0.12, 8):
                tt = (yy + 1.72) / 2.74
                cx = float(np.interp(tt, t, x)) + side * float(np.interp(tt, t, radius)) * 0.72
                channel_points.append((cx, float(yy), 0.105))
            curve_mesh(name + " | grip channel", channel_points,
                       np.linspace(0.018, 0.009, len(channel_points)), detail, 6)
    if style == "split_oak":
        for side in (-1, 1):
            curve_mesh(name + " | split grain crest",
                       [(0, 0.38, 0.09), (side * 0.07, 0.56, 0.10),
                        (side * 0.11, 0.74, 0.095), (side * 0.08, 0.91, 0.07)],
                       [0.035, 0.025, 0.017, 0.005], WOOD_LIGHT, 7)
    elif style == "iron_braced":
        for yy in (-1.05, 0.48):
            for side in (-1, 1):
                curve_mesh(name + " | diagonal brace",
                           [(side * .10, yy - .12, .10), (0, yy, .16), (-side * .10, yy + .12, .10)],
                           [.028, .035, .02], accent, 7)
    elif style == "furnace_haft":
        for yy in (-1.32, -1.12, 0.56, 0.76):
            xx = float(np.interp((yy + 1.72) / 2.74, t, x))
            rr = float(np.interp((yy + 1.72) / 2.74, t, radius))
            bevel_cube(name + " | vent plate", (xx, yy, rr * .72), (rr * 1.12, .075, .045), accent, .025)
    else:
        for side in (-1, 1):
            for yy in (-1.30, -0.98, 0.48, 0.78):
                xx = float(np.interp((yy + 1.72) / 2.74, t, x))
                rr = float(np.interp((yy + 1.72) / 2.74, t, radius))
                sphere(name + " | organic ridge", (xx + side * rr * .70, yy, rr * .28),
                       (.055, .13, .07), detail, ico=True)
    torus(name + " | socket collar", (float(x[-1]), 1.02, 0), float(radius[-1]) * 1.07, 0.035, accent, axis="Y")
    if style == "organic_hook":
        curve_mesh(name + " | hooked butt", [(float(x[0]), -1.72, 0), (float(x[0]) + 0.18, -1.91, 0), (float(x[0]) + 0.34, -1.84, 0), (float(x[0]) + 0.28, -1.65, 0)], [0.11, 0.085, 0.055, 0.012], detail, 9)
    elif variant.get("inlay"):
        # Thin non-emissive inlay keeps elemental color reserved for the core layer.
        for side in (-1, 1):
            curve_mesh(name + " | etched inlay", [(side * 0.06, -0.54, 0.11), (side * 0.07, -0.10, 0.12), (side * 0.04, 0.38, 0.11)], [0.012, 0.015, 0.006], detail, 6)


def extruded_profile(name, points, mat, depth=0.22, bevel=0.035, cache_key=None):
    verts = [(x, y, z) for z in (-depth / 2, depth / 2) for x, y in points]
    n = len(points)
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, j + n, i + n))
    return mesh_object(name, verts, faces, mat, bevel, cache_key=cache_key)


def make_blade(name, style, variant):
    """Build a head variant from one of four shared silhouette families."""
    before = set(bpy.context.scene.objects[:])
    slug = variant["slug"]
    steel = material(f"Head | {slug} | forged body", variant["steel"], metallic=0.82, roughness=0.26)
    edge = material(f"Head | {slug} | honed edge", variant["edge"], metallic=0.91, roughness=0.19)
    accent = material(f"Head | {slug} | fittings", variant["metal"], metallic=0.8, roughness=0.24)
    relief = material(f"Head | {slug} | relief", variant["detail"], metallic=0.65, roughness=0.3)
    if style == "Crescent":
        pts = [(-0.18, -0.63), (-0.63, -0.48), (-1.32, -0.08), (-1.58, 0.42), (-1.20, 0.98), (-0.91, 0.62), (-0.91, 0.22), (-0.56, -0.06), (-0.16, -0.12), (0.16, -0.12), (0.56, -0.06), (0.91, 0.22), (0.91, 0.62), (1.20, 0.98), (1.58, 0.42), (1.32, -0.08), (0.63, -0.48), (0.18, -0.63)]
    elif style == "Hook":
        pts = [(-0.16, -0.62), (-0.55, -0.35), (-1.05, -0.10), (-1.35, 0.18), (-1.55, 0.78), (-1.06, 0.52), (-0.86, 0.19), (-0.40, -0.04), (-0.14, -0.11), (0.14, -0.11), (0.48, -0.03), (0.80, 0.14), (1.08, 0.47), (1.20, 0.91), (1.52, 0.83), (1.42, 0.25), (1.13, -0.12), (0.55, -0.42), (0.16, -0.62)]
    elif style == "Double":
        pts = [(-0.18, -0.60), (-0.66, -0.42), (-1.30, -0.08), (-1.58, 0.35), (-1.28, 0.84), (-0.52, 0.62), (-0.20, 0.47), (0.20, 0.47), (0.52, 0.62), (1.28, 0.84), (1.58, 0.35), (1.30, -0.08), (0.66, -0.42), (0.18, -0.60)]
    else:  # shared single-bit bearded head base
        pts = [(0.13, -0.62), (-0.24, -0.43), (-0.78, -0.31), (-1.35, -0.12), (-1.58, 0.12), (-1.50, 0.42), (-1.22, 0.78), (-0.74, 0.82), (-0.25, 0.58), (0.12, 0.42), (0.42, 0.60), (0.62, 0.40), (0.43, 0.08), (0.48, -0.31), (0.15, -0.62)]
    width = variant.get("width", 1.0)
    head = extruded_profile(name + " | head", pts, steel, depth=0.25, bevel=0.045, cache_key="head:" + variant["base"])
    head.scale.x = width
    # An inset face plate and tapered spine give the blade a forged, sculpted profile.
    panel_pts = [(x * 0.84, y * 0.82 + 0.05) for x, y in pts]
    plate_color = tuple(min(0.66, channel * 1.18 + 0.025) for channel in variant["steel"])
    plate = material(f"Head | {slug} | inset plate", plate_color, metallic=0.88, roughness=0.25)
    panel = extruded_profile(name + " | inset face plate", panel_pts, plate, depth=0.055, bevel=0.022)
    panel.scale.x = width
    panel.location.z = 0.16
    # A fine raised metal border catches the key light around the whole forged profile.
    trim = [(x * width, y, .215) for x, y in pts]
    trim.append(trim[0])
    curve_mesh(name + " | perimeter binding", trim, [.018] * len(trim), accent, 7)
    ridge_points = [(0, -0.30), (-0.16, -0.04), (-0.12, 0.36), (0, 0.67), (0.12, 0.36), (0.16, -0.04)]
    ridge = extruded_profile(name + " | central ridge", ridge_points, plate, depth=0.045, bevel=0.018)
    ridge.location.z = 0.205
    # Central socket ring remains open so the handle and core can be selected independently.
    torus(name + " | socket mouth", (0, -0.43, 0.14), 0.30, 0.052, accent)
    torus(name + " | socket lower lip", (0, -0.66, 0.12), 0.24, 0.032, accent)
    torus(name + " | socket inner rim", (0, -0.43, 0.17), 0.215, 0.018, plate)
    # Two rails make a hollow sleeve; the opening stays clear for the chosen haft/core.
    for side in (-1, 1):
        curve_mesh(name + " | socket sleeve rail", [(side * .25, -.44, .10), (side * .27, -.54, .10), (side * .25, -.66, .10)], [.07, .065, .06], accent, 8)
    # Raised spine, hammered face lines, and fasteners provide relief at icon scale.
    for side in (-1, 1):
        sphere(name + " | socket rivet", (side * 0.33, -0.15, 0.22), (0.055, 0.055, 0.035), accent, ico=True)
        sphere(name + " | face rivet", (side * 0.55 * width, 0.34, 0.22), (0.04, 0.04, 0.025), relief, ico=True)
    # Sharpened edges are thin independent bevel strips on the outer silhouette.
    if style == "Battle":
        curve_mesh(name + " | honed bearded edge", [(-.36, .62, .17), (-.82, .78, .17), (-1.24, .72, .17), (-1.49, .42, .17)], [.022, .028, .028, .008], edge, 6)
        curve_mesh(name + " | poll edge", [(.31, .47, .17), (.50, .45, .17), (.58, .27, .17)], [.018, .016, .006], edge, 6)
    else:
        for side in (-1, 1):
            if style == "Crescent":
                line = [(side * 0.88 * width, 0.56, 0.17), (side * 1.17 * width, 0.83, 0.17), (side * 1.50 * width, 0.42, 0.17)]
            elif style == "Hook":
                line = [(side * .82 * width, .18, .17), (side * 1.10 * width, .52, .17), (side * 1.38 * width, .76, .17)]
            else:  # double bit
                line = [(side * 0.50 * width, 0.60, 0.17), (side * 1.20 * width, 0.71, 0.17), (side * 1.50 * width, 0.37, 0.17)]
            curve_mesh(name + " | edge glint " + str(side), line, [0.026] * 3, edge, 6)
    if style == "Battle":
        for side in (-1, 1):
            curve_mesh(name + " | bearded leaf filigree",
                       [(side * .30, .00, .215), (side * .50, .16, .215),
                        (side * .74, .28, .215), (side * 1.02, .35, .205)],
                       [.030, .022, .014, .004], relief, 7)
            curve_mesh(name + " | leaf vein",
                       [(side * .53, .17, .225), (side * .48, .31, .225),
                        (side * .44, .39, .22)], [.018, .010, .003], accent, 6)
    elif style == "Crescent":
        for side in (-1, 1):
            curve_mesh(name + " | crescent rib",
                       [(side * .28, .16, .215), (side * .56, .34, .22),
                        (side * .83, .54, .215), (side * 1.12, .66, .205)],
                       [.032, .027, .019, .005], relief, 7)
            sphere(name + " | crescent jewel seat", (side * .61, .30, .225),
                   (.085, .11, .035), accent, ico=True)
    elif style == "Double":
        for side in (-1, 1):
            curve_mesh(name + " | twin blade spine",
                       [(side * .22, .44, .215), (side * .48, .51, .22),
                        (side * .84, .58, .215), (side * 1.18, .56, .205)],
                       [.034, .026, .018, .005], relief, 7)
        extruded_profile(name + " | central crest",
                         [(-.20, .16), (0, .40), (.20, .16), (0, -.08)],
                         accent, depth=.035, bevel=.012).location.z = .23
    else:
        for side in (-1, 1):
            curve_mesh(name + " | hooked spine ridge",
                       [(side * .25, .08, .215), (side * .48, .22, .22),
                        (side * .71, .42, .215), (side * 1.00, .57, .205)],
                       [.035, .026, .016, .005], relief, 7)
    if style == "Hook":
        sphere(name + " | crown rivet", (0, 0.53, 0.19), (0.075, 0.075, 0.035), accent)
    # Region motifs are shallow non-emissive relief; elemental glow belongs to the core overlay.
    motif = variant.get("motif", "rivet")
    if motif == "leaf":
        for side in (-1, 1):
            curve_mesh(name + " | leaf etch", [(side * .22, -.10, .19), (side * .35, .05, .19), (side * .22, .20, .19)], [.022, .012, .004], relief, 6)
    elif motif == "scale":
        for row, yy in enumerate((0.05, 0.22, 0.39)):
            for side in (-1, 1):
                sphere(name + " | scale stud", (side * (0.43 + row * .13) * width, yy, .155), (.045, .055, .025), relief, ico=True)
    elif motif == "anchor":
        curve_mesh(name + " | anchor mark", [(0, .55, .19), (0, .30, .19), (-.12, .19, .19), (0, .11, .19), (.12, .19, .19)], [.025, .022, .02, .018, .014], relief, 6)
    elif motif == "storm":
        curve_mesh(name + " | storm etch", [(-.28, .36, .19), (-.08, .17, .19), (-.20, .01, .19), (.12, -.12, .19)], [.025, .02, .014, .006], relief, 6)
    # Raise the head's blade-to-socket proportion without scaling the mount parts
    # independently. One parent keeps every engraving, edge, and sleeve detail aligned.
    new_objects = set(bpy.context.scene.objects[:]) - before
    root = bpy.data.objects.new(name + " | sculpted head group", None)
    bpy.context.collection.objects.link(root)
    for obj in new_objects:
        obj.parent = root
    root.scale.y = 1.35


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


HANDLE_CATALOG = [
    {"slug":"woodcutters_haft", "name":"Woodcutter's Haft", "base":"split_oak", "body":(.30,.13,.045), "metal":(.52,.34,.15), "wrap":(.15,.045,.025), "detail":(.72,.48,.20), "motif":"leaf"},
    {"slug":"corsairs_hook_haft", "name":"Corsair's Hook Haft", "base":"organic_hook", "body":(.20,.12,.065), "metal":(.40,.29,.12), "wrap":(.055,.16,.16), "detail":(.70,.45,.18), "motif":"rope"},
    {"slug":"cinderbrace_split_haft", "name":"Cinderbrace Split Haft", "base":"furnace_haft", "body":(.12,.075,.065), "metal":(.33,.20,.12), "wrap":(.20,.035,.025), "detail":(.63,.24,.09), "motif":"inlay", "inlay":True},
    {"slug":"ravenwood_split_oak_haft", "name":"Ravenwood Split Oak Haft", "base":"split_oak", "body":(.20,.095,.035), "metal":(.19,.16,.12), "wrap":(.08,.12,.055), "detail":(.32,.23,.10), "motif":"leaf"},
    {"slug":"ironhold_cleaver_handle", "name":"Ironhold Cleaver Handle", "base":"iron_braced", "body":(.10,.13,.15), "metal":(.36,.41,.43), "wrap":(.07,.045,.035), "detail":(.62,.43,.19), "motif":"rivets"},
    {"slug":"blazebound_furnace_haft", "name":"Blazebound Furnace Haft", "base":"furnace_haft", "body":(.095,.055,.04), "metal":(.39,.20,.085), "wrap":(.17,.045,.035), "detail":(.55,.20,.07), "motif":"inlay", "inlay":True},
    {"slug":"frostline_hook_grip", "name":"Frostline Hook Grip", "base":"organic_hook", "body":(.20,.25,.27), "metal":(.46,.59,.62), "wrap":(.77,.79,.75), "detail":(.58,.74,.80), "motif":"ice"},
    {"slug":"harbor_boarding_handle", "name":"Harbor Boarding Handle", "base":"organic_hook", "body":(.18,.10,.045), "metal":(.40,.27,.10), "wrap":(.035,.15,.16), "detail":(.58,.40,.18), "motif":"rope"},
    {"slug":"thunderhead_coil_haft", "name":"Thunderhead Coil Haft", "base":"iron_braced", "body":(.075,.09,.13), "metal":(.43,.29,.12), "wrap":(.035,.07,.12), "detail":(.22,.44,.67), "motif":"inlay", "inlay":True},
    {"slug":"harrowstead_dual_grip", "name":"Harrowstead Dual Grip", "base":"split_oak", "body":(.17,.07,.03), "metal":(.27,.20,.12), "wrap":(.08,.035,.025), "detail":(.51,.32,.13), "motif":"rivets"},
]

BLADE_CATALOG = [
    {"slug":"foresters_axe_bit", "name":"Forester's Axe Bit", "base":"bearded", "profile":"Battle", "steel":(.22,.26,.28), "edge":(.70,.76,.77), "metal":(.52,.34,.14), "detail":(.60,.42,.20), "width":1.0, "motif":"leaf"},
    {"slug":"raiders_hook_bit", "name":"Raider's Hook Bit", "base":"hooked", "profile":"Hook", "steel":(.19,.14,.11), "edge":(.67,.57,.43), "metal":(.48,.24,.09), "detail":(.57,.32,.13), "width":1.0, "motif":"rivet"},
    {"slug":"drakeglass_bearded_edge", "name":"Drakeglass Bearded Edge", "base":"bearded", "profile":"Battle", "steel":(.16,.11,.10), "edge":(.73,.54,.39), "metal":(.43,.18,.11), "detail":(.67,.26,.12), "width":1.04, "motif":"scale"},
    {"slug":"bog_iron_hewing_head", "name":"Bog-Iron Hewing Head", "base":"bearded", "profile":"Battle", "steel":(.13,.16,.14), "edge":(.54,.63,.57), "metal":(.32,.29,.16), "detail":(.37,.44,.30), "width":1.02, "motif":"rivet"},
    {"slug":"basalt_double_bit", "name":"Basalt Double Bit", "base":"double", "profile":"Double", "steel":(.15,.16,.18), "edge":(.63,.67,.70), "metal":(.30,.27,.22), "detail":(.56,.43,.28), "width":1.0, "motif":"rivet"},
    {"slug":"star_slate_crescent_bit", "name":"Star-Slate Crescent Bit", "base":"crescent", "profile":"Crescent", "steel":(.14,.17,.24), "edge":(.65,.72,.83), "metal":(.42,.35,.20), "detail":(.29,.49,.72), "width":1.0, "motif":"storm"},
    {"slug":"ashen_obsidian_beak", "name":"Ashen Obsidian Beak", "base":"hooked", "profile":"Hook", "steel":(.095,.075,.07), "edge":(.42,.33,.29), "metal":(.28,.16,.09), "detail":(.64,.24,.10), "width":.90, "motif":"rivet"},
    {"slug":"icehelm_avalanche_bit", "name":"Icehelm Avalanche Bit", "base":"bearded", "profile":"Battle", "steel":(.32,.40,.47), "edge":(.81,.87,.90), "metal":(.51,.62,.68), "detail":(.54,.76,.86), "width":1.06, "motif":"storm"},
    {"slug":"drakeshard_twin_drake_axehead", "name":"Drakeshard Twin-Drake Axehead", "base":"double", "profile":"Double", "steel":(.18,.10,.08), "edge":(.70,.48,.34), "metal":(.52,.22,.12), "detail":(.65,.28,.13), "width":1.08, "motif":"scale"},
    {"slug":"ravenwood_thorn_cleaver", "name":"Ravenwood Thorn Cleaver", "base":"bearded", "profile":"Battle", "steel":(.15,.18,.13), "edge":(.62,.69,.56), "metal":(.30,.22,.12), "detail":(.32,.42,.20), "width":1.04, "motif":"leaf"},
    {"slug":"stormcrown_thunderhead", "name":"Stormcrown Thunderhead", "base":"crescent", "profile":"Crescent", "steel":(.14,.16,.20), "edge":(.70,.76,.84), "metal":(.44,.31,.13), "detail":(.33,.58,.79), "width":1.04, "motif":"storm"},
    {"slug":"veiled_sea_anchor_cutter", "name":"Veiled Sea Anchor Cutter", "base":"hooked", "profile":"Hook", "steel":(.17,.21,.20), "edge":(.68,.67,.59), "metal":(.46,.32,.14), "detail":(.29,.51,.53), "width":1.02, "motif":"anchor"},
]


def setup_camera_and_lights():
    bpy.ops.object.camera_add(location=(0.3, -0.2, 9.0))
    cam = bpy.context.object
    cam.name = "Render Camera | orthographic component view"
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 4.6
    bpy.context.scene.camera = cam
    for name, loc, power, size in [
        ("Key | warm softbox", (-3.4, 4.0, 5.0), 250, 4.0),
        ("Fill | cool softbox", (3.8, 0.4, 3.5), 140, 3.0),
        ("Rim | top strip", (0.0, -3.0, 3.5), 190, 2.5),
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
    scene.cycles.samples = 32
    scene.cycles.use_denoising = False
    scene.render.resolution_x = SIZE
    scene.render.resolution_y = SIZE
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.view_transform = "AgX"
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.view_settings.exposure = -0.35
    scene.view_settings.gamma = 1
    if scene.world is None:
        scene.world = bpy.data.worlds.new("Forge | transparent render world")
    scene.world.color = (0.025, 0.025, 0.025)


def render_assets(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    clear_scene()
    setup_camera_and_lights()
    components = []
    specs = []
    for variant in HANDLE_CATALOG:
        specs.append(("handle", variant["slug"], variant["name"],
                      lambda v=variant: make_handle("Haft | " + v["name"], v),
                      (256, 132), variant["base"], variant["motif"]))
    for variant in BLADE_CATALOG:
        specs.append(("blade", variant["slug"], variant["name"],
                      lambda v=variant: make_blade("Head | " + v["name"], v["profile"], v),
                      (256, 314), variant["base"], variant["motif"]))
    for slug, label, element in (
        ("cinder_pearl", "Cinder Pearl", "Cinder"),
        ("rime_shard", "Rime Shard", "Rime"),
        ("stormglass", "Stormglass", "Storm"),
    ):
        specs.append(("core", slug, label, lambda e=element, n=label: make_core("Core | " + n, e), (256, 256), "core_crystal", element.lower()))
        specs.append(("effect", slug + "_effect", label + " effect", lambda e=element, n=label: make_effect("Effect | " + n, e), (256, 256), "effect_overlay", element.lower()))
    for kind, slug, label, build, anchor, base_id, variant_id in specs:
        # Isolate each part in the saved master scene and in its own transparent render.
        for obj in list(bpy.context.scene.objects):
            if obj.type in {"MESH", "CURVE"}:
                bpy.data.objects.remove(obj, do_unlink=True)
        build()
        asset_objects = [obj for obj in bpy.context.scene.objects if obj.type in {"MESH", "CURVE"}]
        for obj in bpy.context.scene.objects:
            obj.hide_render = obj.type in {"MESH", "CURVE"} and obj not in asset_objects
        name = f"axe_{kind}_{slug}.png"
        bpy.context.scene.camera.data.ortho_scale = {"handle": 3.9, "blade": 4.5, "core": 4.6, "effect": 4.6}[kind]
        bpy.context.scene.render.filepath = str(out_dir / name)
        bpy.ops.render.render(write_still=True)
        components.append({
            "file": name,
            "kind": kind,
            "name": label,
            "base_archetype": base_id,
            "variant_detail": variant_id,
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
    for index, (kind, slug, label, build, anchor, base_id, variant_id) in enumerate(specs):
        before = set(bpy.context.scene.objects[:])
        build()
        new_objects = set(bpy.context.scene.objects[:]) - before
        column, row = index % 5, index // 5
        offset_x, offset_y = (column - 2) * 3.5, (2.5 - row) * 3.5
        for obj in new_objects:
            obj.name = f"{kind.upper()} | {label} | {obj.name}"
        for obj in new_objects:
            # Move a grouped head once through its root, not once per child mesh.
            if obj.parent not in new_objects:
                obj.location.x += offset_x
                obj.location.y += offset_y
    bpy.context.scene.camera.data.ortho_scale = 22.5
    blend_path = out_dir / "axe_archetype_library.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
    manifest = {
        "family": "Axe",
        "review_only": True,
        "assembled_weapon_rendered": False,
        "component_model": "four shared haft archetypes and four shared head archetypes; catalog variants add restrained fittings and surface treatment; cores remain separate",
        "base_archetypes": {
            "handles": sorted({v["base"] for v in HANDLE_CATALOG}),
            "blades": sorted({v["base"] for v in BLADE_CATALOG}),
        },
        "shared_mesh_base_count": len(MESH_CACHE),
        "shared_mesh_bases": sorted(MESH_CACHE.keys()),
        "dimensions_px": [SIZE, SIZE],
        "components": components,
        "renders": [c["file"] for c in components],
        "scene": blend_path.name,
        "notes": [
            "Each PNG contains one component category item only; no handle-plus-blade composition is rendered.",
            "Axe heads and hafts are catalog variants derived from four reusable archetype silhouettes per category.",
            "Core inserts and their effect overlays are separate assets.",
            "Socket anchors are preview metadata and must be calibrated against catalog sprites before integration.",
            "Source scene is an editable library of standalone components, not a composed weapon.",
        ],
    }
    (out_dir / "render_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {len(components)} standalone components to {out_dir}")


if __name__ == "__main__":
    render_assets(Path(args().output).resolve())
