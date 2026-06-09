# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, and Weights & Biases notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-57-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for six core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, and feature stores with Feast.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks |
|------|-------|----------|---------|---------|-----------|------|-----------|
| MLflow | 5 | 3 | 1 | 3 | — | 1 | 1 |
| Kubeflow | 6 | 1 | 2 | 1 | 1 | — | — |
| Metaflow | 5 | 2 | — | 1 | — | — | 1 |
| DVC | 2 | 1 | 1 | — | — | — | — |
| W&B | 5 | 5 | 1 | 2 | — | 1 | — |
| Feast | 2 | 1 | — | 1 | — | — | — |
| Root | — | — | — | — | — | 2 | — |

## Quick links

- [`feast/notes/0000-primer-feast.md`](feast/notes/0000-primer-feast.md) — Feast primer: what it is and how it fits in the stack
- [`feast/snippets/tried_first_feature_view.py`](feast/snippets/tried_first_feature_view.py) — First feature view with Feast SDK
- [`feast/notes/2026-06-03-install-feast-first-feature-retrieval.md`](feast/notes/2026-06-03-install-feast-first-feature-retrieval.md) — Installing Feast and running first feature retrieval
- [`metaflow/snippets/tried_first_linear_dag.py`](metaflow/snippets/tried_first_linear_dag.py) — Minimal linear DAG with parameters in Metaflow
- [`wnb/snippets/tried_logging_first_run.py`](wnb/snippets/tried_logging_first_run.py) — First run logging with W&B SDK

## Layout

- **`.git/`** — Git version history, branches, and object store
- **`00_index/`** — Index, quick-links, glossary
- **`00_index/topics.md`** — Topic-based index of all tool-specific artifacts and files
- **`dvc/`** — DVC notes, snippets, and scripts
- **`feast/`** — Feast feature store notes, snippets, and configs
 - **`feast/configs/`** — Feast feature store YAML configurations
 - **`General/`** — Cross-tool documentation and project-level guides
- **`CHANGELOG.md`** — Chronological record of project changes and feature additions
- **`kubeflow/`** — Kubeflow notes, configs, manifests, scripts, and snippets
- **`metaflow/`** — Metaflow notes, configs, notebooks, and snippets
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`mlflow/docs/`** — MLflow reference documentation, comparisons, and how-to guides
- **`mlflow/notebooks/`** — MLflow Jupyter notebooks for guided experiments and walkthroughs
- **`mlflow/scripts/`** — MLflow custom model flavors, automation, and utility scripts
- **`README.md`** — Project overview, coverage table, and quick links
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, and configs

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Feast primer and install notes, Metaflow linear DAG, and W&B first-run snippet.

---
_Last updated: 2026-06-06_
