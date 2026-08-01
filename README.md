# MLOps-Kit
> A working engineer's MLOps reference for Kubeflow, Metaflow, MLflow, Weights & Biases, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, and Evidently AI.

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

- [Comparing W&B Artifacts vs MLflow Model Registry](wnb/notebooks/comparing-wb-artifacts-vs-mlflow-model-registry.ipynb) — Compare artifact lineage and model registry entries across W&B and MLflow
- [W&B report generator](wnb/scripts/wandb-report-generator.py) — Generate correlation and parallel-coords reports from W&B sweep runs
- [MLflow + W&B hybrid tracking](wnb/docs/integrating-wandb-mlflow-hybrid-tracking.md) — Run MLflow and W&B in parallel and synchronize metadata
- [W&B PyTorch scaffold CI/CD workflow](wnb/templates/wandb-pytorch-scaffold/.github/workflows/ci-cd.yml) — GitHub Actions CI/CD for the W&B + PyTorch project template
- [W&B PyTorch scaffold gitignore](wnb/templates/wandb-pytorch-scaffold/.gitignore) — Gitignore for the W&B + PyTorch project template

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
| Kubeflow | 15 | 9 | 8 | 3 | 4 | 6 | 2 | 20 | 4 | 2026-07-27 |
| Metaflow | 14 | 7 | 8 | 3 | 4 | 3 | 3 | 11 | 1 | 2026-07-28 |
| W&B | 14 | 8 | 5 | 6 | 5 | 2 | 3 | 15 | — | 2026-07-31 |
| MLflow | 7 | 13 | 5 | 10 | 4 | — | 3 | 8 | 4 | 2026-07-30 |
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

Recently added a W&B notebook comparing artifacts vs MLflow model registry, a W&B report generator script, an MLflow + W&B hybrid tracking integration doc, and a W&B PyTorch scaffold template with CI/CD workflow and gitignore.

---
_Last updated: 2026-08-01_