# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, configs, and templates for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, and model serving with KServe and Seldon Core. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [Track dataset snapshots for reproducible training](docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py) — Snapshot datasets and pin versions to training runs (L2)
- [Apply model registry: version and promote ML models](docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py) — Version and promote models with MLflow registry (L2)
- [Data versioning fundamentals exercises](docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) — Data versioning fundamentals exercises (L2)
- [Metaflow CLI and local dev UI](metaflow/notes/2026-07-09-explore-cli-local-dev-ui.md) — Explore Metaflow's CLI and local development UI
- [W&B dashboard exploration](wnb/notes/2026-07-09-explore-wandb-dashboard.md) — Exploring W&B dashboard after first experiments

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring notes and snippets
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|
| Kubeflow | 13 | 9 | 5 | 2 | 4 | 4 | 2 | 20 | 4 |
| Metaflow | 12 | 7 | 4 | 2 | 3 | 2 | 2 | 11 | 1 |
| MLflow | 7 | 12 | 3 | 7 | 2 | — | 2 | — | — |
| W&B | 13 | 8 | 3 | 4 | 3 | 1 | 1 | 7 | — |
| DVC | 3 | 2 | 1 | 2 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |
| KServe | 1 | 1 | — | 1 | — | — | — | — | — |
| Seldon | 1 | 1 | — | — | — | — | — | — | — |

Plus 14 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added data versioning and model registry practice scripts, MLflow notebook on runs and registry, and Metaflow branching/retry/foreach snippet.

---
_Last updated: 2026-07-10_
