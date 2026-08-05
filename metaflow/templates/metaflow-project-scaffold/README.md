---
last_verified: 2026-08-04
tool_version: 2.10.0
sources: []
---

# Metaflow ML Pipeline — Project Scaffold

A template project that wires a multi-step ML pipeline into Metaflow with CI/CD, unit testing, and environment management. Each step is a self-contained `@step` method, data flows between steps through `self` attributes, and the full pipeline compiles down to a DAG that Metaflow schedules and tracks.

## Purpose

Metaflow gives you a DAG-based Python framework for ML pipelines where each step can request its own compute resources, dependencies, and parallelism. This scaffold shows a typical setup: a flow that loads data, preprocesses it, trains a model, and evaluates it — with tests that verify the pipeline logic without running the full flow, and a GitHub Actions workflow that runs the flow on every push.

## When to use

- You are starting a new Metaflow project and want a repeatable directory layout
- You need CI/CD that actually runs the flow (not just lints the code)
- Your team uses `@pypi` or `@conda` decorators and wants to pin dependencies per step
- You want unit-test coverage on step logic without invoking the Metaflow runtime

## Prerequisites

- Python 3.9+
- `metaflow` (`pip install metaflow`)
- scikit-learn and pandas for the example pipeline
- A GitHub repository with Actions enabled (for CI/CD)
- Optional: conda if you use `@conda` decorators (miniconda setup included in CI)

## Project structure

```
metaflow-project-scaffold/
├── README.md
├── requirements.txt
├── flow.py                       # Metaflow FlowSpec — pipeline DAG + @project/@schedule/@trigger flows
├── run.py                        # CLI entrypoint: run any flow variant
├── components/
│   ├── data.py                   # Data loading and preprocessing helpers
│   ├── train.py                  # Model training logic (extracted from step for testability)
│   ├── evaluate.py               # Evaluation metrics and reporting
│   └── event_trigger.py          # Event-trigger payload validation and normalization
├── configs/
│   ├── metaflow-config.yaml      # Metaflow environment configuration
│   └── schedule-config.yaml      # Schedule and trigger configuration
├── tests/
│   ├── test_flow.py              # Pytest tests for component functions
│   └── test_event_trigger.py     # Pytest tests for event-trigger helpers
└── .github/workflows/
    └── ci-cd.yml                 # GitHub Actions — install, test, and run the flow
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Review the flow

`flow.py` defines a 4-step pipeline and three advanced patterns:

1. **start** — Load the Iris dataset and split into train/test
2. **preprocess** — Standard-scale features (fit on train, transform both)
3. **train** — Train a RandomForest classifier, log parameters and accuracy
4. **evaluate** — Predict on the test set and print a classification report

Each step uses `@pypi` to pin the libraries it needs. Data moves between steps as `self` attributes — Metaflow serialises them to the artifact store automatically.

### Advanced patterns

#### @project — Project metadata and namespace isolation

`ProjectMetadataFlow` demonstrates the `@project` decorator, which scopes the flow to a named project namespace. This isolates runs, artifacts, and metadata from other flows in the same Metaflow environment.

#### @schedule — Cron-based scheduled execution

`ScheduledDailyFlow` uses the `@schedule` decorator with a cron expression (`0 8 * * *`) to run automatically at 08:00 UTC every day. The schedule is configured in `configs/schedule-config.yaml`.

#### Event-triggered flows

`EventTriggeredFlow` demonstrates the `@trigger` decorator, which starts a flow in response to external events (e.g., a GitHub push to the `main` branch). The `components/event_trigger.py` helper validates and normalizes incoming event payloads.

### 3. Run locally

```bash
python flow.py run
```

Override parameters:

```bash
python flow.py run --n_estimators 200 --test_size 0.3
```

### 4. Run with the helper script

```bash
python run.py project
python run.py scheduled --threshold 0.7
python run.py event --commit-sha abc123
```

### 5. Run tests

```bash
pip install pytest
pytest tests/ -v
```

### 6. Configure Metaflow

Edit `configs/metaflow-config.yaml` to set data-store and metadata-service URLs for your environment. The flow reads this config at runtime if the file exists next to the flow.

Edit `configs/schedule-config.yaml` to adjust cron schedules and trigger settings.

## Verify

1. Run `python flow.py run` — the flow should complete with a classification report printed at the end
2. Check the Metaflow UI (`metaflow ui`) or `~/.metaflow` for artifact storage
3. Run `pytest tests/ -v` — all tests pass
4. Push to GitHub — the Actions workflow runs the flow and reports success

## Common errors

- **`@pypi` packages not found** — the `@pypi` decorator requires an internet connection at step start. If running offline, switch to `@conda(libraries=...)` or install globally and remove `@pypi`.
- **`MetaflowNotFound` when running tests** — test helper functions that don't call `self.next()` should be extracted to `components/` and imported; keep only `@step` methods in `flow.py`.
- **GitHub Actions conda resolution is slow** — the CI workflow includes a conda cache step. On first run it takes ~4 minutes; subsequent runs hit the cache and complete faster.
