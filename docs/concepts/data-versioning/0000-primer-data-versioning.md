---
last_verified: 2026-07-25
tool_version: n/a
sources: []
---

# Data Versioning — quick primer

> First-day notes on Data Versioning. What it is, why it matters, and the key ideas to know.

## What is it?

I just learned that data versioning is the practice of taking snapshots of datasets so you can re-create any past state. Git tracks code changes, but it doesn't track data — and in ML, the data is just as important as the code. Tools like DVC (Data Version Control) solve this by storing lightweight pointers in git that point to the actual data stored elsewhere (like S3 or a local cache). When the data changes, the pointer changes, and every version is tracked.

The analogy that clicked for me is this: git is to code what DVC is to data. You commit, tag versions, and can roll back to any point in history. But instead of tracking source files, you're tracking datasets, feature tables, or model artifacts.

## Why does it matter for MLOps?

Reproducibility is the core promise of MLOps — I should be able to re-run a training job from three months ago and get the same results. That's impossible if the data keeps changing without versioning. Here's why I need it as an MLOps practitioner:

- It pins exactly which dataset a model was trained on, so audits and debug work are grounded in real data, not guesses.
- It makes rollbacks possible: if I discover a data quality bug in the current dataset, I can revert training to the last clean version.
- Multiple team members can experiment with data transformations without stepping on each other — each person works on their own data branch.
- It enables data pipelines where each stage reads a versioned input and writes a versioned output, so the whole pipeline is traceable.

## Key terminology

- **Data version** — A snapshot of a dataset at a point in time, identified by a hash or tag. Example: `raw_data_v3` tracked by its MD5 hash `a1b2c3...`.
- **Pointer file** — A small file git tracks instead of the full dataset. It contains the hash pointing to the actual data. Example: `data/raw_sales.csv.dvc` is a pointer — git stores only this tiny file, not the megabytes of CSV data.
- **PUSH** — Upload the current dataset snapshot to remote storage so it's backed up and available to the team. Example: `dvc push` sends cached data to S3.
- **PULL** — Download a dataset snapshot matching the pointer file. Example: `dvc pull` restores `data/raw_sales.csv` from the hash stored in the pointer file.
- **Pipeline (data)** — A directed acyclic graph of data stages where each stage reads a versioned input and writes a versioned output. Example: raw → clean → features → training_data.
- **Cache** — A local directory where DVC stores downloaded data snapshots so it doesn't re-download them every time. Example: `.dvc/cache/` on disk.
- **Branch (data)** — Like a git branch for data — you can experiment with different data transformations on your own copy without affecting the main dataset.

## A concrete example

Here's a minimal data versioning workflow using DVC-style commands:

```bash
dvc init                            # start tracking data in this repo
dvc add data/raw_sales.csv          # hash the file, create a pointer
git add data/raw_sales.csv.dvc .dvc # commit the pointer to git
git commit -m "add raw sales v1"
dvc push                            # upload the actual data to remote storage
```

The heavy data never goes into git — only the pointer file does. Later, `dvc pull` restores the exact bytes from the stored hash. This way, anyone on the team can re-create the exact dataset I trained on.

## How this connects to what's next

Data versioning pairs naturally with experiment tracking (every training run records which data version it used) and pipeline orchestration (each pipeline step reads a versioned input and writes a versioned output). Next I'll want to practice versioning a dataset, training a model against a specific data version, and reproducing the results by checking out an older data snapshot.