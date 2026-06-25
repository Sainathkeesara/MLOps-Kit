# Data Versioning — quick primer

> First-day notes on Data Versioning. What it is, why it matters, and the key ideas to know.

## What is it?

Data versioning is the practice of taking snapshots of your datasets so you can re-create any past state. It's like git for data: you commit a dataset, tag a version, and later you can check out that exact version and run a training pipeline against it. Tools like DVC (Data Version Control) and LakeFS do this — they store pointers to data in a lightweight metadata file while the actual data lives in S3, GCS, or a local store.

I think of it as the bridge between code versioning and data: code is versioned in git, but the data it trains on is usually not. If someone changes the raw CSV on disk, your next training run silently uses different data. Data versioning makes that explicit — you're running against `data_v3`, not `data.csv`.

## Why does it matter for MLOps?

Reproducibility is the core promise of MLOps: you should be able to re-run a training pipeline from six months ago and get the same results. That's impossible if the data keeps changing without versioning.

Data versioning matters because:

- It pins which dataset a model was trained on, so audits and debug work are grounded in facts.
- It enables data pipelines: processing code reads version N of raw data and produces version N+1 of processed data.
- It makes rollbacks possible: if you discover a data quality bug in the current dataset, you can roll training back to the last clean version.
- It lets multiple team members work on data without stepping on each other — each has their own branch.

Without it, you're hoping nobody overwrote that Parquet file in the shared bucket. With it, every dataset snapshot is immutable and named.

## Key terminology

- **Data version** — A snapshot of a dataset at a point in time, identified by a hash or tag. Example: `raw_data_v3` with MD5 `a1b2c3...`.
- **Pointer file** — A small text file git tracks instead of the full dataset. It contains the hash pointing to the actual data in S3. Example: `data.csv.dvc`.
- **PUSH** — Upload the current dataset snapshot to remote storage (S3, GCS). Example: `dvc push` sends cached data to the remote.
- **PULL** — Download a specific dataset snapshot matching the pointer file. Example: `dvc pull` restores `data.csv` from the hash in `data.csv.dvc`.
- **Pipeline** — A directed acyclic graph (DAG) of data processing stages, where each stage outputs a versioned artifact. Example: `raw → clean → features → train_data`.
- **Cache** — A local directory where DVC stores all previously downloaded data snapshots so it doesn't re-download them.
- **Branch** — Like git branches, but for data — allows experimenting with data transformations without affecting the main dataset.

## A concrete example

```bash
# Pseudo-code for data versioning with DVC
dvc init                              # track data in this repo
dvc add data/raw_sales.csv            # hash the file, create pointer
git add data/raw_sales.csv.dvc .dvc   # commit pointer to git
git commit -m "add raw_sales v1"
dvc push                              # upload actual data to S3

# Later, on another machine:
git pull                              # get pointer file
dvc pull                              # download actual data matching hash
```

This shows the workflow: the heavy data never goes into git — only the pointer does. `dvc pull` restores the exact bytes from the hash.

## How this connects to what's next

Data versioning pairs naturally with pipeline orchestration (each pipeline step reads a versioned input and writes a versioned output) and with experiment tracking (every run ID records which data version was used). It's also a prerequisite for feature stores — they version feature definitions and the data they compute from.
