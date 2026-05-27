# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, and Weights & Biases notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-24-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for five core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B to data versioning with DVC, pipeline orchestration with Kubeflow, and workflow management with Metaflow.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs |
|------|-------|----------|---------|---------|-----------|------|
| MLflow | 4 | 3 | — | 1 | — | — |
| Kubeflow | 3 | — | — | — | 1 | — |
| Metaflow | 2 | — | — | 1 | — | — |
| DVC | 2 | 1 | — | — | — | — |
| W&B | 2 | 2 | 1 | 1 | — | 1 |
| Root | — | — | — | — | — | 1 |

## Quick links

- [`dvc/notes/0000-primer-dvc.md`](dvc/notes/0000-primer-dvc.md) — DVC primer and setup notes
- [`dvc/notes/2026-05-26-first-dataset-version.md`](dvc/notes/2026-05-26-first-dataset-version.md) — First dataset versioning walkthrough
- [`dvc/snippets/tried_dvc_pipeline.sh`](dvc/snippets/tried_dvc_pipeline.sh) — DVC pipeline experiment
- [`mlflow/configs/mlflow-project.yaml`](mlflow/configs/mlflow-project.yaml) — MLflow Project configuration
- [`mlflow/snippets/2026-05-26-autolog_and_register.py`](mlflow/snippets/2026-05-26-autolog_and_register.py) — Autologging and model registry example

## Layout

- **`CHANGELOG.md`** — Record of completed tasks and additions
- **`00_index/`** — Index, quick-links, glossary
- **`mlflow/configs/`** — MLflow Project configurations and YAML definitions
- **`mlflow/notes/`** — MLflow learning notes and primers
- **`mlflow/snippets/`** — MLflow runnable code examples
- **`kubeflow/`** — Kubeflow notes, manifests
- **`metaflow/`** — Metaflow notes, configs
- **`dvc/`** — DVC notes, snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs

## Status

Working through first-contact notes and runnable experiments for each tool. Currently filling out DVC and MLflow workflows alongside Kubeflow and Metaflow foundations.

---
_Last updated: 2026-05-27_
