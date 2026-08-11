---
last_verified: 2026-08-11
tool_version: n/a
sources:
  - https://tildalice.io/dvc-basics-track-ml-dataset-3-commands/
  - https://doc.dvc.org/user-guide/troubleshooting
---

# Snapshot-based vs diff-based versioning for ML datasets

> Two approaches to tracking dataset changes. Snapshot-based versioning stores a
> complete copy at each version (DVC's model); diff-based versioning stores only
> what changed. The choice depends on data size, change frequency, and format.

## Purpose

When a dataset changes, versioning systems must decide how much to store.
Snapshot-based systems capture the whole file whenever it changes — the approach
DVC uses, where each `dvc add` writes the full file to a cache and a pointer to
Git [source: https://tildalice.io/dvc-basics-track-ml-dataset-3-commands/].
Diff-based systems record only the differences between versions, the approach
Git itself takes with text files and what tools like Delta Lake or LakeFS build
for data tables.

This document compares the two along the dimensions that matter most for ML
work: storage cost, restore speed, format compatibility, and reproducibility
guarantees.

## Snapshot-based versioning

### How it works

Each version is an independent, complete copy of the dataset. The system
computes a content hash (e.g. sha256) and stores the full file in a cache, then
writes a small pointer — hash, path, size — that version control tracks instead
of the data. To restore, the system reads the pointer and fetches the cached
bytes.

DVC follows this model: `dvc add data.csv` hashes the file, stores it in
`.dvc/cache/`, and writes `data.csv.dvc` (the pointer) for Git to commit
[source: https://tildalice.io/dvc-basics-track-ml-dataset-3-commands/]. After
`git checkout`, running `dvc checkout` syncs the workspace from those pointers
[source: https://doc.dvc.org/user-guide/troubleshooting].

The from-scratch implementation in
[scripts/dvc-style-versioning-pipeline.py](scripts/dvc-style-versioning-pipeline.py)
replicates this mechanism without the DVC dependency: a content-addressed cache
keyed by sha256, JSON pointer files, and a run log that records which version
each training step used.

### When it works well

- Binary data (images, audio, serialized models) that cannot be meaningfully
  diffed.
- Datasets that change in large, independent chunks — whole new partitions or
  table exports — where most of the file is different between versions.
- Teams that prioritize simple, predictable restore semantics over storage
  savings.
- Offline-first workflows where the cache lives on a shared filesystem or S3
  bucket [source: https://doc.dvc.org/user-guide/troubleshooting].

### What to watch

- Storage cost grows with the **number of versions**, not just the number of
  changed rows. A 1 GB dataset with daily 1 % changes still caches 1 GB per
  version.
- Without a remote cache, each collaborator must pull every version they need.
  "Failed to pull data from the cloud" is a common symptom of pushing Git
  changes without running `dvc push` first [source: https://doc.dvc.org/user-guide/troubleshooting].

## Diff-based versioning

### How it works

Each version stores only the delta — the operations (insert, update, delete)
needed to transform the previous version into the next one. To reconstruct a
historical version, the system applies the deltas in sequence from a base
snapshot.

Delta Lake and LakeFS are diff-based systems for tabular data: they maintain a
transaction log of changes and can serve any version by replaying commits. Git
itself is diff-based for text files — `git checkout` applies reverse deltas to
restore an old state.

### When it works well

- Text-based or structured data (CSV, JSON, Parquet) where a diff library can
  produce small, meaningful deltas.
- Datasets that change incrementally — a few rows updated or appended — where
  storing the full file each time is wasteful.
- Environments with tight storage budgets where every byte counts.

### What to watch

- Binary formats resist diffing. An image-format change produces a delta nearly
  as large as the full file, defeating the purpose.
- Reconstruction requires replaying the entire delta chain from a base snapshot.
  A long history of small changes can make restore slow.
- Diffs are not always meaningful. A reserialized Parquet file may be
  semantically identical but produce a large binary delta.
- Point-in-time consistency is harder to guarantee — a corrupted delta early in
  the chain can make later versions unrecoverable.

## Comparison

| Aspect | Snapshot-based | Diff-based |
|---|---|---|
| Storage per version | Full file (or deduplicated chunks) | Delta only |
| Restore cost | O(file size) — single fetch | O(history) — chain replay |
| Binary data | Excellent | Poor (delta ≈ full file) |
| Text / structured data | Adequate | Excellent (small deltas) |
| Integrity | Hash-verify on restore | Each delta must be validated |
| Complexity | Low — cache + pointer | High — diff engine + base snapshot |
| Best storage fit | Sparse changes, large files | Frequent small changes, text |

## When to use which

Choose snapshot-based versioning when:

- The data is binary (images, audio, serialized models).
- Changes affect large portions of the file.
- Simple, predictable restores are more valuable than storage savings.
- A shared cache (S3, NFS) makes the storage overhead manageable
  [source: https://doc.dvc.org/user-guide/troubleshooting].

Choose diff-based versioning when:

- The data is text or structured (CSV, JSON, Parquet).
- Changes are small and incremental.
- Storage is constrained and deltas are meaningfully smaller than full files.

Many real setups combine both: a snapshot layer for coarse checkpoints (weekly
full snapshots) and a diff layer for fine-grained changes (daily deltas between
checkpoints). This is the approach LakeFS recommends for large data lakes.

## Verify

- **Snapshot-based**: restore a version and compare its content hash to the
  pointer. DVC does this on `dvc checkout` — if the cached file's hash does not
  match the pointer, DVC raises an integrity error
  [source: https://doc.dvc.org/user-guide/troubleshooting].
- **Diff-based**: restore the oldest and newest versions and confirm they match
  the expected baseline and head. If any delta in the chain is corrupted, the
  reconstruction fails — diff systems therefore validate each step before
  replaying.
