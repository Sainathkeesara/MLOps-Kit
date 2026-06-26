# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, and configs for MLflow, Kubeflow, Metaflow, DVC, W&B, Feast, ZenML, ClearML, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/sainathkeesara-mlops/MLOps-Kit)
![Python](https://img.shields.io/badge/Python-58-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-84-000000?logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-22-CB171E?logo=yaml&logoColor=white)
![Files](https://img.shields.io/badge/files-179-blue)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for nine MLOps tools — from experiment tracking with MLflow and W&B to data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML, pipeline frameworks with ZenML, and drift monitoring with Evidently. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|-----------|------|-----------|-----------|-------------|
| MLflow | 5 | 9 | 1 | 5 | — | 2 | 1 | — | — |
| Kubeflow | 11 | 7 | 3 | 2 | 4 | 3 | 2 | 8 | 4 |
| Metaflow | 10 | 5 | 3 | 2 | 2 | 3 | 2 | 12 | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| W&B | 9 | 6 | 3 | 4 | 1 | 3 | 1 | 8 | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Evidently AI | 1 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |

## Quick links

- [`docs/concepts/experiment-tracking/scripts/tried_comparing_training_runs.py`](docs/concepts/experiment-tracking/scripts/tried_comparing_training_runs.py) — Compare training runs with different hyperparameters side by side (L2)
- [`docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py`](docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py) — Practice logging params, metrics, and artifacts with experiment tracking (L2)
- [`docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py`](docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py) — Practice registering, versioning, and aliasing models (L2)
- [`docs/concepts/containerization/0000-primer-containerization.md`](docs/concepts/containerization/0000-primer-containerization.md) — Containerization primer for MLOps
- [`docs/concepts/feature-store/0000-primer-feature-store.md`](docs/concepts/feature-store/0000-primer-feature-store.md) — Feature store primer for production ML

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets (L1)
- **`docs/`** — Cross-cutting concept primers: containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring and data quality notes and snippets (L1)
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, and templates
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs (L1)

## Status

Recently added L2 exercises for experiment tracking and model registry; foundational primers for containerization, feature stores, model serving, monitoring & drift, and pipeline orchestration. Working through first-contact notes and runnable experiments for each tool.

---
_Last updated: 2026-06-26_
