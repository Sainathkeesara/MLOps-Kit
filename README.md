# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, Weights & Biases, and ZenML notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-138-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for seven core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, feature stores with Feast, and pipeline frameworks with ZenML.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks |
|------|-------|----------|---------|---------|-----------|------|-----------|
| MLflow | 5 | 9 | 1 | 4 | — | 2 | 1 |
| Kubeflow | 10 | 6 | 2 | 1 | 2 | 1 | 1 |
| Metaflow | 9 | 5 | 1 | 1 | 1 | 1 | 2 |
| DVC | 3 | 2 | 1 | 1 | — | — | — |
| W&B | 9 | 6 | 3 | 4 | — | 2 | 1 |
| Feast | 2 | 1 | — | 2 | — | — | — |
| ZenML | 1 | 1 | — | — | — | — | — |
| General | — | — | — | — | — | 13 | — |

## Quick links

- [`metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb`](metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb) — Compare a fresh run against a resumed run during iterative model development
- [`wnb/notes/2026-06-17-first-dashboard-exploration.md`](wnb/notes/2026-06-17-first-dashboard-exploration.md) — First walk through the W&B web UI: runs, projects, and experiment comparison
- [`wnb/configs/2026-06-17-declarative-sweep-config.yaml`](wnb/configs/2026-06-17-declarative-sweep-config.yaml) — YAML-based hyperparameter sweep for team collaboration
- [`wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb`](wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb) — Side-by-side comparison of declarative YAML vs programmatic Python API for defining hyperparameter sweeps
- [`metaflow/docs/metaflow-resource-management.md`](metaflow/docs/metaflow-resource-management.md) — Pin dependencies with @conda, request CPU/memory/GPU with @resources, and set step timeouts

## Layout

- **`00_index/`** — Topic index, quick links, and glossary
- **`CHANGELOG.md`** — Chronological record of project changes
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`General/`** — Cross-tool documentation and project-level guides
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, and snippets
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, and manifests
- **`zenml/`** — ZenML notes and snippets

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Metaflow full-run vs resume notebook, W&B dashboard exploration notes, declarative sweep config, and hyperparameter optimization notebook.

---
_Last updated: 2026-06-21_
