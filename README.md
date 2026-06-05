# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, and Weights & Biases notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-37-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for five core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B to data versioning with DVC, pipeline orchestration with Kubeflow, and workflow management with Metaflow.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs |
|------|-------|----------|---------|---------|-----------|------|
| MLflow | 5 | 3 | 1 | 3 | — | 1 |
| Kubeflow | 5 | 1 | 2 | 1 | 1 | — |
| Metaflow | 4 | 2 | — | 1 | — | — |
| DVC | 2 | 1 | 1 | — | — | — |
| W&B | 5 | 4 | 1 | 2 | — | 1 |
| Root | — | — | — | — | — | 2 |

## Quick links

- [`metaflow/snippets/tried_first_linear_dag.py`](metaflow/snippets/tried_first_linear_dag.py) — Minimal linear DAG with parameters in Metaflow
- [`metaflow/snippets/tried_parameterized_dag.py`](metaflow/snippets/tried_parameterized_dag.py) — Parameterized DAG with branching and merging in Metaflow
- [`wnb/snippets/tried_logging_first_run.py`](wnb/snippets/tried_logging_first_run.py) — First metrics and params logging with W&B SDK
- [`wnb/snippets/tried_first_metrics_and_config.py`](wnb/snippets/tried_first_metrics_and_config.py) — First metrics and config logging experiment with W&B
- [`kubeflow/scripts/tried_diagnosing_kubeflow_health.sh`](kubeflow/scripts/tried_diagnosing_kubeflow_health.sh) — Diagnosing Kubeflow backend health
- [`metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md`](metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md) — Metaflow quickstart trip-ups and gotchas
- [`kubeflow/notes/2026-05-27-pipelines-quickstart-trip-ups.md`](kubeflow/notes/2026-05-27-pipelines-quickstart-trip-ups.md) — Kubeflow Pipelines quickstart trip-ups

## Layout

- **`CHANGELOG.md`** — Record of completed tasks and additions
- **`00_index/`** — Index, quick-links, glossary
- **`dvc/`** — DVC notes, snippets, and scripts
- **`kubeflow/`** — Kubeflow notes, configs, manifests, scripts, and snippets
- **`metaflow/`** — Metaflow notes, configs, notebooks, and snippets
- **`mlflow/`** — MLflow notes, configs, and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, and configs

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Metaflow linear DAG with parameters, W&B first-run snippet, and updated README layout.

---
_Last updated: 2026-06-03_
