# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, and configs for MLflow, Kubeflow, Metaflow, DVC, W&B, Feast, ZenML, ClearML, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for nine core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, feature stores with Feast, experiment tracking with ClearML, and data drift monitoring with Evidently AI.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks | Dockerfiles | Templates |
|------|-------|----------|---------|---------|-----------|------|-----------|-------------|-----------|
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| Evidently | 1 | 1 | — | — | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Kubeflow | 10 | 6 | 2 | 1 | 4 | 2 | 1 | 3 | 8 |
| Metaflow | 9 | 5 | 3 | 1 | 2 | 3 | 2 | — | — |
| MLflow | 5 | 9 | 1 | 5 | — | 2 | 1 | — | — |
| W&B | 9 | 6 | 3 | 4 | 1 | 3 | 1 | — | 8 |
| ZenML | 2 | 1 | — | — | — | — | — | — | — |

## Quick links

- [`metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb`](metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb) — Compare a fresh run against a resumed run during iterative model development
- [`wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb`](wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb) — Side-by-side comparison of declarative YAML vs programmatic Python API for hyperparameter sweeps
- [`kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb`](kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb) — Compare Katib managed tuning vs custom ParallelFor grid search for KFP HPO
- [`clearml/notes/2026-06-22-clearml-web-ui-exploration.md`](clearml/notes/2026-06-22-clearml-web-ui-exploration.md) — First walk through the ClearML web UI: projects, experiments, and dashboards
- [`zenml/notes/2026-06-19-first-dashboard-and-stack.md`](zenml/notes/2026-06-19-first-dashboard-and-stack.md) — Exploring the ZenML dashboard and configuring an S3 artifact store stack

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML experiment tracking notes, snippets, and configs
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI data drift monitoring notes and snippets
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, dockerfiles, and templates
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, and templates
- **`zenml/`** — ZenML notes and snippets

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added ClearML orchestration and web UI exploration, Evidently AI drift monitoring, W&B dashboard exploration and sweep configuration, Metaflow full-run vs resume notebook, and ZenML dashboard exploration.

---
_Last updated: 2026-06-23_
