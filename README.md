# MLOps-Kit
> A working engineer's MLOps reference — notes, snippets, configs, and templates for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, and model serving with KServe and Seldon Core. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [KFP v2 quickstart trip-ups — July 2026](kubeflow/notes/2026-07-11-kfp-v2-quickstart-trip-ups.md) — Following the official KFP v2 quickstart and what tripped me up
- [Metaflow quickstart trip-ups — July 2026](metaflow/notes/2026-07-11-metaflow-quickstart-trip-ups.md) — Following the official Metaflow quickstart and what tripped me up
- [W&B quickstart trip-ups — July 2026](wnb/notes/2026-07-11-first-wandb-quickstart-trip-ups.md) — Following the official W&B quickstart and what tripped me up
- [Feature store fundamentals exercises](docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) — Feature store fundamentals exercises (L2)
- [DAG-based ML workflow script](docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py) — Build and run a DAG-based ML pipeline (L2)

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes and snippets
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI drift monitoring notes and snippets
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, and configs

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|
| Kubeflow | 14 | 9 | 7 | 3 | 4 | 5 | 2 | 21 | 4 |
| Metaflow | 13 | 7 | 4 | 3 | 3 | 2 | 2 | 11 | 1 |
| W&B | 14 | 8 | 3 | 5 | 3 | 1 | 1 | 7 | — |
| MLflow | 7 | 12 | 3 | 7 | 2 | — | 2 | — | — |
| DVC | 3 | 2 | 1 | 2 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |
| KServe | 1 | 1 | — | 1 | — | — | — | — | — |
| Seldon | 1 | 1 | — | — | — | — | — | — | — |

Plus 14 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added KFP v2 and Metaflow quickstart trip-ups (July 2026), feature store and pipeline orchestration practice exercises, and W&B dashboard exploration notes.

---
_Last updated: 2026-07-11_
