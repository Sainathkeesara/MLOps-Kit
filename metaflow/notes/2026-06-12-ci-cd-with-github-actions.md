# mfl-010 — How I wired Metaflow into a CI/CD workflow with GitHub Actions

I wanted to run my Metaflow flows automatically whenever I push code to GitHub — CI/CD for ML pipelines, basically. Here's what I set up and where I tripped.

## What I wanted

A GitHub Actions workflow that:
- Installs dependencies
- Runs a Metaflow flow (`python flow.py run`)
- Passes or fails the commit based on whether the flow succeeds

## Step 1 — basic workflow file

Started with a `.github/workflows/metaflow-ci.yml`:

```yaml
name: metaflow-ci
on: [push]
jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install metaflow scikit-learn pandas
      - run: python iris_flow.py run
```

Pushed it. It ran, installed everything, then died on `Flow is using @conda decorator but conda is not installed`.

## Step 2 — adding conda

Several of my Metaflow steps use `@conda` to pin library versions. GitHub Actions runners don't have conda by default. I added miniconda setup:

```yaml
- uses: conda-incubator/setup-miniconda@v3
  with:
    python-version: "3.11"
    auto-update-conda: true
```

This installs conda and makes it available. Re-ran. It worked but took 4+ minutes — conda env resolution is slow even on a fresh runner.

## Step 3 — metadata service

Metaflow defaults to a local metadata service. In CI, each run starts fresh so the local metadata works fine — no need for a remote metadata service. But I realized my flow also calls `Flow.get_latest_successful_run()` to compare against a previous run. That fails on the first CI run because there's no previous run.

Fixed by wrapping it:

```python
try:
    prev = IrisFlow.get_latest_successful_run()
except Exception:
    prev = None
```

## Step 4 — artifact store

By default Metaflow stores artifacts in `$METAFLOW_HOME` (usually `~/.metaflow`). In GitHub Actions, the runner gets a fresh filesystem each time so artifacts from previous CI runs don't persist. That's fine for now — I'm just validating the flow runs without errors. If I wanted cross-run artifact persistence I'd need S3.

## Got stuck on

### 1. Conda cache between runs

Every CI run downloads and resolves the same conda packages. I added a cache step:

```yaml
- name: Cache conda
  uses: actions/cache@v4
  with:
    path: ~/.conda/envs
    key: conda-${{ runner.os }}-${{ hashFiles('**/conda.yaml') }}
```

This cut the conda setup from 4 minutes to ~30 seconds on cache hit.

### 2. Matrix strategy — multiple param sets

I wanted to run the same flow with different parameters across runners. Added a matrix:

```yaml
strategy:
  matrix:
    n_estimators: [50, 100, 200]
    max_depth: [3, 5]
```

Each matrix job runs the full flow with those params. But Metaflow runs inside a job couldn't share artifacts between matrix jobs — each job is its own runner. I logged results to a CSV and uploaded them as an Actions artifact:

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: results-${{ matrix.n_estimators }}-${{ matrix.max_depth }}
    path: results.csv
```

### 3. Flow imports failing

My flow imports `metaflow` and some data-processing modules. I had a weird failure where GitHub Actions couldn't find a local module (`from preprocessing import clean_data`). Turned out I forgot `__init__.py` in the preprocessing folder. Adding it fixed the import.

## What I'd try next

Set up a remote metadata service and an S3 artifact store so CI runs are visible in the Metaflow UI and artifacts survive across runs. Also want to experiment with the `@pypi` decorator instead of `@conda` — it uses pip under the hood and might be faster in CI.
