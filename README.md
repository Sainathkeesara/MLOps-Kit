# MLOps-Kit

> A working engineer's MLOps reference — notes, snippets, configs, and templates for Kubeflow, Metaflow, MLflow, W&B, DVC, Feast, ZenML, KServe, Seldon Core, ClearML, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Language count](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)

> **New here?** Start at [the learning path](00_index/learning-path.md). It walks you from first-contact to confident in a sensible order.

## Who this is for

A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for experiment tracking, pipeline orchestration, data versioning, feature stores, model serving, drift monitoring, and project templating. Use it as a shelf you grab from, not a tutorial site. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, model serving with KServe and Seldon Core, and drift monitoring with Evidently. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [W&B first experiment with Python SDK](wnb/snippets/2026-07-04-first-experiment-wb-sdk.py) — Log my first experiment with W&B Python SDK (L1)
- [Metaflow end-to-end experiment](metaflow/scripts/2026-07-03-end-to-end-experiment.py) — Experiment with Metaflow tracking, model logging, and run comparison via Client API (L2)
- [KServe minimal InferenceService config](kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml) — Minimal InferenceService for a sklearn model (L1)
- [Seldon Core primer](seldon/notes/0000-primer-seldon-core.md) — What is Seldon Core? (L1)
- [Seldon Core install and first deploy](seldon/snippets/2026-07-04-install-and-first-deploy.py) — Install Seldon Core and deploy my first model via Python (L1)

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

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|
| Kubeflow | 11 | 8 | 5 | 2 | 4 | 4 | 2 | 21 | 4 |
| Metaflow | 10 | 5 | 4 | 2 | 3 | 2 | 2 | 12 | — |
| MLflow | 7 | 12 | 1 | 6 | 2 | — | 1 | — | — |
| W&B | 11 | 8 | 3 | 4 | 3 | 1 | 1 | 8 | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — |
| ClearML | 2 | 1 | — | — | — | — | — | — | — |
| KServe | 1 | 1 | — | 1 | — | — | — | — | — |
| Seldon | 1 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |

Plus 11 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Seldon Core primer and first deploy, KServe minimal InferenceService, Metaflow end-to-end experiment, and W&B first experiment with Python SDK.

---
_Last updated: 2026-07-04_
