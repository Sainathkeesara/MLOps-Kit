# DVC — quick primer

> First-day notes for someone who's never used DVC. Personal voice, plain language.

## What is it?

DVC (Data Version Control) is an open-source tool that brings Git-like version control to machine learning datasets and pipelines. If you already use Git for code, DVC extends that same workflow to large files — CSVs, images, model weights — without actually storing the bytes in your Git repo. Think of it as "Git for data," but it also does pipeline tracking (like a lightweight Makefile for ML).

## What does it do?

It lets you track datasets and models in a Git-friendly way, reproduce ML pipelines by recording which data and commands produced each output, and share large artifacts via cloud storage (S3, GCS, etc.) without bloating your repo.

## Why does it exist?

Before DVC, teams either stuffed large CSVs into Git (breaks cloning and diffs), used ad-hoc scripts to download data from S3 (nobody could reproduce the exact dataset), or paid for enterprise MLOps platforms. DVC gives a free, open-source, Git-integrated workflow that anyone with `pip install dvc` and a cloud bucket can use. Data scientists and ML engineers use it day-to-day to keep experiments reproducible.

## Key terminology

- **DVC-tracked file** — A file that DVC manages via a `.dvc` file instead of committing the raw bytes to Git. Example: `dvc add data/train.csv` creates `data/train.csv.dvc` and adds `data/train.csv` to `.gitignore`.
- **.dvc file** — A small YAML file that stores the hash and storage location of a DVC-tracked file. Example: `data/train.csv.dvc` contains `md5: a1b2c3...` and `outs:`.
- **Remote storage** — Where DVC actually stores the file contents: S3, GCS, Azure Blob, a local directory, or SSH. Example: `dvc remote add myremote s3://my-bucket/dvc-store`.
- **Pipeline stage** — A command wrapped by DVC with declared dependencies and outputs. Example: `dvc stage add -n clean -d data/raw.csv -o data/clean.csv -- python clean.py`.
- **dvc.yaml** — The file that defines pipeline stages (dependencies, commands, outputs). What makes `dvc repro` work.
- **dvc.lock** — Auto-generated file recording the hashes of all inputs and outputs from a pipeline run. Commit this to Git to lock reproducibility.
- **`dvc repro`** — The command that re-runs only pipeline stages whose dependencies have changed. Like `make` but for data pipelines.
- **Cache** — The local directory (`.dvc/cache`) where DVC keeps the actual file contents.
- **`dvc push` / `dvc pull`** — Upload/download DVC-tracked files to/from remote storage. Like `git push`/`git pull` but for data.

## A tiny example

```bash
pip install dvc
git init && dvc init
dvc add data/train.csv          # track a dataset
git add data/train.csv.dvc .gitignore
git commit -m "track train.csv"
dvc remote add myremote s3://my-bucket/dvc
dvc push                         # upload to S3
```

This initializes DVC, tracks a CSV, and pushes it to S3 — all without bloating the Git repo.

## What I'll cover next

After this primer, I want to actually install DVC and version a real dataset, then wire up a full pipeline that goes from raw data to a trained model. I also need to understand how `dvc repro` behaves when I change parameters vs data.
