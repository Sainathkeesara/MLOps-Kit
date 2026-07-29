# MLOps-Kit
> A working engineer's mlops reference for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI.

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

- [DVC repro + metrics diff end-to-end](dvc/scripts/2026-07-28-dvc-repro-metrics-diff.sh) — Run `dvc repro` and compare metrics across commits
- [DVC stage pipeline config](dvc/configs/2026-07-28-dvc-stage-pipeline.yaml) — Minimal DVC stage pipeline with metrics-file layout
- [MLflow experiment comparison + promotion](mlflow/scripts/experiment-compare-and-promote.py) — Reusable helper for automated experiment comparison and model promotion
- [MLflow + W&B hybrid tracking](mlflow/docs/integrating-mlflow-with-weights-and-biases.md) — Run MLflow and W&B in parallel and synchronize metadata
- [Multi-stage Dockerfile for MLOps](docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md) — Build-stage training, slim runtime serving image

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
| Kubeflow | 15 | 9 | 6 | 2 | 4 | 5 | 2 | 21 | 4 | 2026-07-27 |
| Metaflow | 14 | 7 | 7 | 2 | 4 | 3 | 3 | 11 | 1 | 2026-07-28 |
| W&B | 14 | 8 | 4 | 4 | 4 | 2 | 2 | 7 | — | 2026-07-19 |
| MLflow | 7 | 13 | 5 | 9 | 4 | — | 3 | 9 | 4 | 2026-07-25 |
| ClearML | 4 | 1 | — | 1 | — | — | — | — | — | 2026-07-23 |
| Feast | 4 | 2 | 1 | 2 | — | — | — | — | — | 2026-07-27 |
| DVC | 3 | 2 | 3 | 3 | — | — | — | — | — | 2026-07-28 |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | 2026-07-14 |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | — |
| Seldon Core | 2 | 1 | — | — | — | — | — | — | — | 2026-07-12 |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | 2026-07-14 |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | 2026-07-14 |

Plus 21 files across 8 concept directories covering containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added DVC stage pipeline configs and a repro + metrics diff workflow, a Metaflow trigger hooks script, an MLflow experiment comparison and model promotion helper, and an MLflow + W&B hybrid tracking integration doc.

---
_Last updated: 2026-07-28_
