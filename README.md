# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, and configs for MLflow, Kubeflow, Metaflow, DVC, W&B, Feast, ZenML, ClearML, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Python](https://img.shields.io/badge/Python-55-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-72-000000?logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-20-CB171E?logo=yaml&logoColor=white)
![Files](https://img.shields.io/badge/files-166-blue)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for eight core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, feature stores with Feast, orchestration with ClearML, pipeline frameworks with ZenML, and drift monitoring with Evidently AI. ZenML configs are now tracked separately.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks |
|------|-------|----------|---------|---------|-----------|------|-----------|
| MLflow | 5 | 9 | 1 | 5 | — | 2 | 1 |
| Kubeflow | 11 | 6 | 3 | 2 | 4 | 2 | 1 |
| Metaflow | 10 | 5 | 3 | 2 | 2 | 3 | 2 |
| DVC | 3 | 2 | 1 | 1 | — | — | — |
| W&B | 9 | 6 | 3 | 4 | 1 | 3 | 1 |
| Feast | 2 | 1 | — | 2 | — | — | — |
| Evidently AI | 1 | 1 | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — |
| ClearML | 1 | 1 | — | — | — | — | — |

## Quick links

- [`clearml/notes/0000-primer-clearml-orchestration.md`](clearml/notes/0000-primer-clearml-orchestration.md) — ClearML concepts, setup, and orchestration fundamentals (L1)
- [`docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md`](docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) — Primer on experiment tracking concepts and tooling (L1)
- [`docs/concepts/data-versioning/0000-primer-data-versioning.md`](docs/concepts/data-versioning/0000-primer-data-versioning.md) — Primer on data versioning concepts and DVC fundamentals (L1)

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets (L1)
 - **`dvc/`** — DVC notes, snippets, scripts, and configs
 - **`evidently/`** — Evidently AI drift monitoring and data quality notes and snippets (L1)
 - **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, and templates
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs (L1)

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added foundational concept primers for experiment tracking, data versioning, and model registry; ZenML stack config with S3 artifact store; ClearML Orchestration primer and first task snippet.

---
_Last updated: 2026-06-24_
