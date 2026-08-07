# MLOps-Kit
> A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, W&B, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, Databricks, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, W&B, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, Databricks, and Evidently AI. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, model serving with KServe and Seldon Core, and Databricks ML with Unity Catalog. Nine cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [KFP v2 branching and parallel pipeline](kub/scripts/2026-08-07-kfp-v2-branching-parallel-pipeline.py) — KFP v2 pipeline with conditional branching and parallel execution
- [Track DVC dataset versions](docs/concepts/data-versioning/scripts/2026-08-07-track-dvc-versions.py) — Track and version datasets with DVC for reproducible training
- [Build DAG pipeline](docs/concepts/pipeline-orchestration/scripts/2026-08-07-build-dag-pipeline.py) — Build and run a DAG-based ML pipeline with step dependencies
- [DVC dataset versioning](docs/concepts/data-versioning/scripts/2026-08-07-dvc-dataset-versioning.py) — Version datasets and pin them to training runs with DVC
- [Simple DAG pipeline](docs/concepts/pipeline-orchestration/scripts/2026-08-07-simple-dag-pipeline.py) — Minimal DAG-based ML workflow with training, evaluation, and registration steps

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs and scripts
- **`docs/`** — Cross-cutting concept primers (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI monitoring and drift detection notes and snippets
- **`feast/`** — Feast feature store notes, snippets, scripts, and configs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kub/`** — Kubeflow SDK snippets and scripts (KFP v2)
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mfl/`** — MLflow first-experiment snippets, scripts, manifests, and docs
- **`mlf/`** — MLflow first-experiment snippets, scripts, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes and snippets
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, configs, notebooks, and scripts

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Kubeflow | 15 | 10 | 9 | 3 | 4 | 7 | 2 | 20 | 4 | 2026-07-14 |
| Metaflow | 14 | 7 | 8 | 4 | 4 | 4 | 5 | 14 | 1 | 2026-08-04 |
| W&B | 14 | 8 | 5 | 6 | 5 | 2 | 3 | 14 | — | 2026-07-31 |
| MLflow | 7 | 13 | 5 | 10 | 4 | — | 3 | 8 | 4 | 2026-07-30 |
| ClearML | 4 | 1 | — | 1 | — | — | — | — | — | 2026-07-23 |
| Feast | 5 | 3 | 1 | 3 | — | — | — | — | — | 2026-08-02 |
| DVC | 3 | 2 | 3 | 3 | — | — | — | — | — | 2026-07-28 |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | 2026-07-14 |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | 2026-07-03 |
| Seldon Core | 2 | 1 | — | — | — | — | — | — | — | 2026-07-12 |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | 2026-07-14 |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | 2026-07-14 |
| MLflow extras | — | 1 | 1 | — | — | 1 | — | — | — | 2026-08-06 |
| kub (KFP SDK) | — | 1 | 1 | — | — | — | — | — | — | 2026-08-04 |
| Concepts | — | 5 | 12 | — | 27 | — | — | — | — | 2026-08-04 |

Plus 27 files across 9 concept directories covering containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration.

</details>

## Status

Recently added KFP v2 branching and parallel pipeline script, DVC dataset versioning and tracking scripts, and simple DAG pipeline examples.

---
_Last updated: 2026-08-08_
