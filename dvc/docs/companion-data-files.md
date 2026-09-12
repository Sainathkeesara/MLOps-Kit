---
last_verified: 2026-09-12
tool_version: "3.67.1"
sources:
  - https://github.com/iterative/dvc/releases/tag/3.67.1
---

# DVC companion data files

> Data files referenced by DVC notes and primer.

## Files

| File | Description |
|------|-------------|
| `train.csv` | Iris dataset (150 samples, 5 columns) used in DVC tracking examples |
| `train.csv.dvc` | DVC pointer file for `train.csv` — tracks the hash so `dvc checkout` can restore it |
| `sample.csv` | Small 9-row subset of the Iris dataset for quick DVC demos |
| `sample.csv.dvc` | DVC pointer file for `sample.csv` |

## Usage

These files are companions to the DVC notes. The notes reference `dvc add data/train.csv` and `dvc add data/sample.csv` — these are the actual data files those commands operate on.

```bash
dvc add data/train.csv     # creates data/train.csv.dvc
dvc add data/sample.csv    # creates data/sample.csv.dvc
```

The `.dvc` files store the MD5 hash and file size so DVC can detect changes and restore the correct version from cache.
