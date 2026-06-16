# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, and Weights & Biases notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-82-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for six core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, and feature stores with Feast.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks |
|------|-------|----------|---------|---------|-----------|------|-----------|
| MLflow | 5 | 5 | 1 | 3 | — | 2 | 1 |
| Kubeflow | 10 | 5 | 2 | 1 | 2 | 1 | — |
| Metaflow | 9 | 4 | — | 1 | — | — | 1 |
| DVC | 3 | 2 | 1 | 1 | — | — | — |
| W&B | 8 | 6 | 1 | 3 | — | 1 | — |
| Feast | 2 | 1 | — | 2 | — | — | — |
| General | — | — | — | — | — | 13 | — |

## Quick links

- [`kubeflow/snippets/tried_my_first_component.py`](kubeflow/snippets/tried_my_first_component.py) — My first Kubeflow Pipelines component — just adds two numbers
- [`mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py`](mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — End-to-end training pipeline with sklearn autolog, model comparison, and Model Registry registration
- [`metaflow/scripts/2026-06-12-five-step-ml-pipeline.py`](metaflow/scripts/2026-06-12-five-step-ml-pipeline.py) — End-to-end pipeline: load, clean, feature engineering, train, evaluate
- [`metaflow/notes/2026-06-12-ci-cd-with-github-actions.md`](metaflow/notes/2026-06-12-ci-cd-with-github-actions.md) — Wiring Metaflow flows into a GitHub Actions CI/CD pipeline
- [`mlflow/docs/production-tracking-server-nginx-auth.md`](mlflow/docs/production-tracking-server-nginx-auth.md) — Deploy a production MLflow Tracking Server behind an Nginx reverse proxy with HTTP basic auth

## Layout

- **`.git/`** — Git version history, branches, and object store
- **`00_index/`** — Topic index, quick links, and glossary
- **`CHANGELOG.md`** — Chronological record of project changes
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`dvc/configs/`** — DVC pipeline YAML configuration
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`General/`** — Cross-tool documentation and project-level guides
- **`kubeflow/`** — Kubeflow notes, docs, configs, manifests, scripts, and snippets
- **`metaflow/`** — Metaflow notes, configs, notebooks, and snippets
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, and configs

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Kubeflow KFP components, MLflow end-to-end autologging pipeline, Metaflow CI/CD with GitHub Actions, and production MLflow tracking server setup.

---
_Last updated: 2026-06-15_
