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

- [Databricks Unity Catalog setup](databricks/configs/2026-07-14-unity-catalog-setup.yaml) — Unity Catalog configuration for Databricks ML
- [Databricks model promotion to Unity Catalog](databricks/scripts/2026-07-14-model-promotion-unity-catalog.py) — Promote MLflow models to Unity Catalog
- [ClearML remote GPU execution config](clearml/configs/2026-07-14-remote-gpu-execution.yaml) — Remote GPU execution configuration for ClearML
- [Metaflow install and hello world](metaflow/notes/2026-07-14-install-and-hello-world.md) — First Metaflow install and hello world walkthrough
- [MLflow tracking server config with PostgreSQL backend and S3 artifact store](mlflow/configs/2026-07-14-tracking-server-postgres-s3.yaml) — Production-ready MLflow tracking server stack

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs and scripts
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, configs, notebooks, and scripts

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Kubeflow | 15 | 9 | 5 | 2 | 4 | 5 | 2 | 20 | 4 | 2026-07-14 |
| Metaflow | 14 | 7 | 6 | 2 | 3 | 3 | 2 | 11 | 1 | 2026-07-14 |
| W&B | 14 | 8 | 3 | 4 | 3 | 2 | 1 | 7 | — | 2026-07-11 |
| MLflow | 7 | 13 | 3 | 8 | 2 | — | 2 | — | — | 2026-07-04 |
| DVC | 3 | 2 | 1 | 2 | — | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — | — |
| ClearML | 3 | 1 | — | 1 | — | — | — | — | — | 2026-07-12 |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | — |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | — |
| Seldon | 2 | 1 | — | — | — | — | — | — | — | 2026-07-12 |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | — |

Plus 20 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Databricks Unity Catalog config and model promotion script, ClearML remote GPU execution config, Metaflow install and hello world, and MLflow tracking server config with PostgreSQL and S3.

---
_Last updated: 2026-07-16_