# Weapon mounting refinement — October 14, 2026

The old universal centre socket could not assemble bows correctly, and the original cannon/crossbow sheets mixed projections. Several greatsword bases also ended in a broad flat cut instead of a tang.

Changes:

- Bow risers now have two source-pixel receiving ports. Each selected limb pair supplies two independently positioned pieces, preserving the complete original limb roots. The renderer fits the combined three-piece bounds once.
- All ten risers and twelve limb sets have calibrated ports/regions. Horizontal result presentation is retained.
- Six original axe head anchors now sit at the handle collar openings. Insertion overlap is deeper, older head scale is moderated, and adjacent sprite-sheet scraps are excluded where identified.
- Three original greatsword grip angles and sockets are corrected. Six original blades have replacement artwork with tapered shoulders and a narrow tang; excess hidden tang length is excluded by the authored region.
- Four cannon frames and six barrels now use a shared side view, horizontal bore and receiving sleeve. Three crossbow stocks and six prods now use a top-down view with a transverse front bracket and string.
- The 25 replacement images are RGBA 512×512 sprites named `*_mounted.png`. Original archive assets remain intact. Catalog references and existing expansion-placeholder references point to the corresponding replacement. This pass does not claim those expansion placeholders as unique art.
- Inventory icons use the calibrated region and exclusions, cached by path. Result assembly still uses the selected source images. Existing Sword calibration remains separate.

The component contract is visual: frame ports identify the actual receiving hardware; striker sockets identify the tang, collar opening, barrel shank or crossbow bracket. Future assets must use the same projection before socket calibration. A socket offset cannot repair incompatible perspective.

Validation includes all 1,800 family-legal pairs at three canvas sizes, both bow root-to-stud joins, live result width, the separate 120-pair Sword regression, catalog integrity and unchanged non-art catalog fields. Contact-sheet inspection uses textures and transforms exported by the Godot preview through an independent raster composition; it is not an Android screenshot. Device visual review remains useful for final aesthetic refinements.

Generation: built-in image_gen. Prompts are in `mount-art-prompts-oct14.json`; installed file mappings and attachment metadata are in `mount-art-manifest-oct14.json`. No gameplay values changed.
