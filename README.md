# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, and Weights & Biases notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-78-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for six core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, and feature stores with Feast.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks |
|------|-------|----------|---------|---------|-----------|------|-----------|
| MLflow | 5 | 4 | 1 | 3 | — | 2 | 1 |
| Kubeflow | 10 | 3 | 2 | 1 | 2 | — | — |
| Metaflow | 9 | 4 | — | 1 | — | — | 1 |
| DVC | 3 | 2 | 1 | 1 | — | — | — |
| W&B | 8 | 5 | 1 | 3 | — | 1 | — |
| Feast | 2 | 1 | — | 2 | — | — | — |
| General | — | — | — | — | — | 5 | — |

## Quick links

- [`metaflow/notes/2026-06-06-revisiting-quickstart.md`](metaflow/notes/2026-06-06-revisiting-quickstart.md) — Second pass through the Metaflow quickstart
- [`kubeflow/notes/2026-06-06-explore-central-dashboard.md`](kubeflow/notes/2026-06-06-explore-central-dashboard.md) — First walk through the Kubeflow Central Dashboard
- [`wnb/configs/2026-06-08-first-sweep-config.yaml`](wnb/configs/2026-06-08-first-sweep-config.yaml) — First hyperparameter sweep config with W&B Bayesian optimization
- [`wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md`](wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md) — Following the official W&B quickstart and what tripped me up
- [`feast/notes/0000-primer-feast.md`](feast/notes/0000-primer-feast.md) — Feast primer: what it is and how it fits in the stack

## Layout

- **`00_index/`** — Topic index, quick links, and glossary
- **`CHANGELOG.md`** — Chronological record of project changes and feature additions
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`General/`** — Cross-tool documentation and project-level guides
- **`kubeflow/`** — Kubeflow notes, configs, manifests, scripts, and snippets
- **`metaflow/`** — Metaflow notes, configs, notebooks, and snippets
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, and configs

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added W&B sweep config, Kubeflow Central Dashboard notes, and Metaflow quickstart revisit.

---
_Last updated: 2026-06-10_
