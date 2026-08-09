# MLOps-Kit
> A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for Kubeflow, Metaflow, MLflow, W&B, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, Databricks, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's shelf: first-contact notes, runnable snippets, and configs for the tools that make ML production work. Use it when you are setting up a new tool, debugging a specific issue, or trying to recall how two systems fit together. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, model serving with KServe and Seldon Core, and Databricks ML with Unity Catalog. Nine cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [Offline vs online stores](docs/concepts/feature-store/2026-08-09-offline-vs-online-stores.md) — Offline vs online stores and point-in-time joins in Feast
- [Register and retrieve features](docs/concepts/feature-store/scripts/2026-08-09-register-and-retrieve-features.py) — Register features in a local Feast store and retrieve them
- [Multistage Dockerfile for ML](docs/concepts/containerization/scripts/2026-08-09-multistage-dockerfile-for-ml.sh) — Multi-stage Dockerfile for ML training and serving
- [SeldonDeployment manifest](seldon/manifests/seldondeployment.yaml) — Minimal sklearn SeldonDeployment manifest
- [W&B PyTorch CI/CD scaffold README](wnb/templates/wandb-pytorch-ci-scaffold/README.md) — W&B sweep + PyTorch training with CI/CD scaffold

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
- **`seldon/`** — Seldon Core model serving notes, snippets, and manifests
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, configs, notebooks, and scripts

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Kubeflow | 15 | 10 | 9 | 3 | 4 | 7 | 2 | 20 | 4 | 2026-08-04 |
| Weights & Biases | 14 | 8 | 5 | 7 | 5 | 2 | 3 | 20 | — | 2026-08-08 |
| Metaflow | 14 | 7 | 8 | 4 | 4 | 4 | 5 | 14 | 1 | 2026-08-04 |
| MLflow | 7 | 13 | 5 | 10 | 4 | — | 3 | 8 | 4 | 2026-07-30 |
| Concepts | — | 5 | 15 | — | — | — | — | — | — | 2026-08-09 |
| Feast | 5 | 3 | 1 | 3 | — | — | — | — | — | 2026-08-02 |
| DVC | 3 | 2 | 3 | 3 | — | — | — | — | — | 2026-07-28 |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | 2026-07-13 |
| ClearML | 4 | 1 | — | 1 | — | — | — | — | — | 2026-07-23 |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | 2026-07-14 |
| Seldon Core | 2 | 1 | — | — | — | 1 | — | — | — | 2026-07-12 |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | — |
| MLflow first-experiments | — | 1 | 1 | — | — | 1 | — | — | — | — |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | 2026-07-14 |
| kub (KFP SDK) | — | — | 1 | — | — | 1 | — | — | — | 2026-08-07 |
| MLflow extras | — | — | — | — | 1 | — | — | — | — | 2026-08-06 |

</details>

## Status

Recently added offline vs online stores and feature retrieval scripts for Feast, multistage Dockerfile for ML training and serving, Seldon Core deployment manifest, and W&B PyTorch CI/CD scaffold.

---
_Last updated: 2026-08-09_
