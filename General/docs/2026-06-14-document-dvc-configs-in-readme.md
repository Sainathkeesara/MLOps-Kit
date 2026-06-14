# Document dvc/configs/ in README

The Repo Auditor flagged `dvc/configs/` as missing from the README. I checked the folder and it has `pipeline.yaml`, which is the DVC pipeline config for the prepare and train stages.

The README already had DVC in the Coverage table with Configs: 1, so that part was consistent. I added `dvc/configs/` under `dvc/` in the Layout section so the subfolder is visible instead of only the parent folder.

## Changes to Layout section

Added a nested line under `dvc/`:

```
- **`dvc/configs/`** — DVC pipeline YAML configuration
```

## Changes to Coverage table

Updated the General row to show Docs: 6:

```
| General | — | — | — | — | — | 6 | — |
```

The DVC row already shows Configs: 1, so that part stayed the same.

## Changes to Quick Links

Added the new layout note under Project:

```
- [dvc/configs/ Layout + Coverage doc](../General/docs/2026-06-14-document-dvc-configs-in-readme.md) — Documented dvc/configs/ in README Layout and Coverage sections
```

That's it: the folder is now visible in the README layout and the coverage row still matches the file count.
