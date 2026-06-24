# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, Metaflow, Weights & Biases, DVC, Feast, ClearML, Evidently, and ZenML: notes, snippets, configs, and templates.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-176-blue)
![Python](https://img.shields.io/badge/Python-55-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-84-000000?logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-22-CB171E?logo=yaml&logoColor=white)

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

- [`docs/concepts/containerization/0000-primer-containerization.md`](docs/concepts/containerization/0000-primer-containerization.md) — What containerization is and why it matters in MLOps (L1)
- [`docs/concepts/feature-store/0000-primer-feature-store.md`](docs/concepts/feature-store/0000-primer-feature-store.md) — What a feature store is and why it matters in production ML (L1)
- [`docs/concepts/model-serving/0000-primer-model-serving.md`](docs/concepts/model-serving/0000-primer-model-serving.md) — What model serving is and why it matters for ML deployment (L1)
- [`docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md`](docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md) — What monitoring and drift detection is and why it matters for model reliability (L1)
- [`docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md`](docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md) — What pipeline orchestration is and why it matters for ML workflows (L1)

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets (L1)
- **`docs/`** — Cross-cutting concept primers: containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring and data quality notes and snippets (L1)
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, templates, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs (L1)

## Status

Working through first-contact notes and concept primers. Recently added eight cross-cutting MLOps concept primers covering containerization, feature stores, model serving, monitoring & drift, and pipeline orchestration, plus a ZenML stack config.

---
_Last updated: 2026-06-25_
