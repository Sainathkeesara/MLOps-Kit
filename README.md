# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, configs, and templates for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, and model serving with KServe and Seldon Core. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [MLflow end-to-end experiment](mlflow/scripts/2026-07-06-end-to-end-experiment.py) — Full experiment cycle: tracking, model logging, registry registration, and stage promotion
- [Kubeflow install verification](kubeflow/snippets/2026-07-06-verify-kfp-install.py) — Verify kfp install and compile my first KFP pipeline
- [W&B dashboard exploration](wnb/notes/2026-07-05-exploring-wandb-dashboard.md) — Exploring W&B dashboard after first experiments
- [MLflow experiment with tracking](mlflow/scripts/2026-07-05-end-to-end-experiment.py) — MLflow tracking with model logging and run comparison
- [W&B first experiment (SDK)](wnb/snippets/2026-07-04-first-experiment-wb-sdk.py) — Log my first experiment with W&B Python SDK

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring notes and snippets
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, scripts, snippets, templates, dockerfiles, and notebooks
- **`kserve/`** — KServe model serving notes, configs, and snippets
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, and templates
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|
| Kubeflow | 11 | 9 | 5 | 2 | 4 | 4 | 2 | 21 | 4 |
| Metaflow | 10 | 5 | 4 | 2 | 3 | 2 | 2 | 12 | — |
| MLflow | 7 | 12 | 3 | 6 | 2 | — | 1 | — | — |
| W&B | 12 | 8 | 3 | 4 | 3 | 1 | 1 | 8 | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |
| KServe | 1 | 1 | — | 1 | — | — | — | — | — |
| Seldon | 1 | 1 | — | — | — | — | — | — | — |

Plus 11 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added MLflow end-to-end experiment scripts, Kubeflow install verification snippet, and W&B dashboard exploration notes.

---
*Last updated: 2026-07-06*
