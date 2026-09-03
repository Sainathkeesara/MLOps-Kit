# MLOps-Kit
> A working MLOps engineer's reference for MLflow, Kubeflow, Metaflow, W&B, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, BentoML, Databricks, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's shelf: first-contact notes, runnable snippets, and configs for the tools that make ML production work. Use it when you are setting up a new tool, debugging a specific issue, or trying to recall how two systems fit together. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs spanning the MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, model serving with KServe, Seldon Core, and BentoML, and the Databricks ML platform. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project scaffolds for Kubeflow, Metaflow, MLflow, and W&B ship with tests and CI/CD wiring.

## Quick links

- [Databricks ML primer](databricks/notes/0000-primer-databricks.md) — Unity Catalog, workspace setup, and first experiments
- [First Databricks run](databricks/snippets/2026-08-27-first-databricks-run.py) — First-contact script for running a Databricks workload
- [KServe flowers sample](kserve/manifests/2026-08-27-flowers-sample.yaml) — Sample KServe InferenceService manifest for the flowers model
- [W&B PyTorch scaffold CI/CD](wnb/manifests/2026-08-26-wandb-pytorch-scaffold-ci-cd.yaml) — CI/CD workflow manifest for the W&B PyTorch scaffold
- [Snapshot vs diff versioning](docs/concepts/data-versioning/comparing-snapshot-vs-diff-versioning.md) — Comparing versioning strategies for ML datasets

## Layout

- **`README.md`** — This file
- **`CHANGELOG.md`** — Chronological record of project changes
- **`00_index/`** — Topic map, quick links, glossary, and learning path
- **`bentoml/`** — BentoML model serving notes, snippets, and configs
- **`clearml/`** — ClearML orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs, scripts, snippets, and notes
- **`docs/`** — Cross-cutting concept primers and scripts (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI monitoring and drift detection notes and snippets
- **`feast/`** — Feast feature store notes, snippets, scripts, configs, and docs
- **`kserve/`** — KServe model serving notes, snippets, configs, and manifests
- **`kub/`** — Kubeflow Pipelines SDK configs, scripts, and manifests (KFP v2)
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mfl/`** — Metaflow crossover docs, configs, scripts, and manifests
- **`mlf/`** — MLflow first-experiment scripts, snippets, notes, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, notebooks, templates, and dockerfiles
- **`seldon/`** — Seldon Core model serving notes, snippets, configs, and manifests
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, scripts, configs, and notebooks

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Metaflow | 14 | 15 | 8 | 2 | 11 | 4 | 5 | 23 | 1 | 2026-08-04 |
| Kubeflow | 18 | 10 | 8 | 3 | 4 | 7 | 2 | 22 | 3 | 2026-07-14 |
| Weights & Biases | 15 | 9 | 5 | 6 | 5 | 5 | 3 | 24 | 0 | 2026-08-11 |
| MLflow | 7 | 13 | 5 | 9 | 4 | 0 | 3 | 10 | 4 | 2026-07-30 |
| Concepts | 16 | 6 | 20 | 1 | 1 | 0 | 1 | 0 | 1 | 2026-09-02 |
| Feast | 5 | 3 | 2 | 4 | 1 | 0 | 0 | 0 | 0 | 2026-08-15 |
| DVC | 4 | 2 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 2026-08-13 |
| ClearML | 6 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-08-22 |
| ZenML | 3 | 2 | 2 | 3 | 0 | 0 | 1 | 0 | 0 | 2026-08-22 |
| KServe | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2026-08-22 |
| Seldon Core | 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2026-07-12 |
| MLflow first-experiments | 1 | 1 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 2026-08-12 |
| Metaflow crossover | 0 | 0 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | 2026-08-06 |
| BentoML | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-08-22 |
| kub (KFP SDK) | 0 | 0 | 1 | 3 | 0 | 2 | 0 | 0 | 0 | — |
| Databricks | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-08-27 |
| Evidently AI | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |

</details>

## Status

Currently working through first-contact notes for Databricks ML, BentoML, ClearML, and KServe, alongside ZenML pipeline configuration and cross-tool CI/CD scaffolding.

---
_Last updated: 2026-09-03_
