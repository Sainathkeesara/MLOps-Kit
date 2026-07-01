# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, configs, and templates for Kubeflow, Metaflow, MLflow, W&B, DVC, Feast, ZenML, ClearML, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Python](https://img.shields.io/badge/Python-71-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-87-000000?logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-23-CB171E?logo=yaml&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-5-F37626?logo=jupyter&logoColor=white)
![Files](https://img.shields.io/badge/files-197-blue)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, and drift monitoring with Evidently. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|
| Kubeflow | 11 | 7 | 5 | 2 | 4 | 4 | 2 | 21 | 4 |
| Metaflow | 10 | 5 | 3 | 2 | 3 | 2 | 2 | 12 | — |
| MLflow | 6 | 10 | 1 | 5 | 2 | — | 1 | — | — |
| W&B | 9 | 6 | 3 | 4 | 3 | 1 | 1 | 8 | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Evidently AI | 1 | 1 | — | — | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |

Plus 11 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

## Quick links

- [MLflow UI exploration](mlflow/notes/2026-06-30-exploring-mlflow-ui.md) — First walk through the MLflow UI: runs, parameters, metrics, and compare mode
- [MLflow install + first experiment](mlflow/snippets/tried_installing_mlflow_first_experiment.py) — Install MLflow and log my first experiment with the Python SDK
- [Kubeflow pipeline scaffold](kubeflow/templates/kubeflow-pipeline-scaffold/README.md) — Template project with KFP pipeline, unit tests, CI/CD, and modular components (L5)
- [Kubeflow + MLflow project scaffold](kubeflow/templates/kubeflow-mlflow-project/README.md) — Template wiring KFP pipelines with MLflow experiment tracking
- [Metaflow CI/CD with GitHub Actions](metaflow/notes/2026-06-12-ci-cd-with-github-actions.md) — Wiring Metaflow flows into a GitHub Actions CI/CD pipeline

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring notes and snippets
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, and templates
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added MLflow UI notes and install-first-experiment snippet; Kubeflow pipeline scaffold template with CI/CD and unit testing (L5).

---
_Last updated: 2026-07-01_
