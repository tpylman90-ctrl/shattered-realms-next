# Entropic Forge test lab — asset installation

The `FORGE LAB` title-screen button is wired on this branch and safely displays installation instructions when assets are absent.

The companion archive `shattered_realms_forge_test_pack.zip` contains:
- `scripts/forge_lab.gd` — interactive sandbox controls, previews and prototype strike timing
- `data/entropic_forge/forge_test_catalog.json` — 50 frameworks, 90 strikers, 60 cores, 180 catalog-discovered weapon recipes, 36 stocks and 96 salvage records
- `assets/entropic_forge/icons/` — 200 individual 256×256 RGBA PNG icons, one for each base assembly component

**Install:** Extract the ZIP **into the repository root**, merging `scripts/`, `data/` and `assets/` directories, then import in Godot. The ZIP does not contain a wrapper directory.

This branch deliberately **does not include binary icons**, because the current GitHub text-only write connector cannot upload the 200 PNG files. To merge fully, install the pack in a git checkout and commit the binaries and catalog, or push the pack contents to this branch through a Git-capable environment. The loader checks for the script/data and will not crash when absent.

**Scope:** 200 illustrated inventory icons. The 36 gathering stocks, 96 salvage entries and 180 finished recipe results are indexed but do not yet have unique illustrated images. All 180 named recipes show exact benchmark numbers from CATALOG.md by forge tier. Other valid assemblies show their real component traits but not fabricated final attack values; production forging formulas are required. The five-strike minigame is a UI experiment and does not consume inventory/gold or alter a campaign save. Godot runtime execution remains unverified.
