# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, Weights & Biases, and ZenML notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-148-blue)
![Python](https://img.shields.io/badge/Python-46-3776AB?logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-68-000000?logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-19-CB171E?logo=yaml&logoColor=white)

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

- [`metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb`](metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb) — Compare a fresh run against a resumed run during iterative model development (L2)
- [`wnb/notes/2026-06-17-first-dashboard-exploration.md`](wnb/notes/2026-06-17-first-dashboard-exploration.md) — First walk through the W&B web UI: runs, projects, and experiment comparison (L2)
- [`wnb/configs/2026-06-17-declarative-sweep-config.yaml`](wnb/configs/2026-06-17-declarative-sweep-config.yaml) — YAML-based hyperparameter sweep for team collaboration (L3)
- [`wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb`](wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb) — Side-by-side comparison of declarative YAML vs programmatic Python API for defining hyperparameter sweeps (L3)
- [`clearml/notes/0000-primer-clearml-orchestration.md`](clearml/notes/0000-primer-clearml-orchestration.md) — ClearML concepts, setup, and orchestration fundamentals (L1)

## Layout

- **`00_index/`** — Topic index, quick links, and glossary
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets (L1)
 - **`dvc/`** — DVC notes, snippets, scripts, and configs
 - **`evidently/`** — Evidently AI drift monitoring and data quality notes and snippets (L1)
 - **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs (L1)

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Metaflow full-run vs resume notebook, W&B dashboard exploration notes, declarative sweep config, and ClearML Orchestration primer.

---
_Last updated: 2026-06-22_
