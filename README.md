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

- [Feature store online store read/write](docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py) — Writing and reading features from an online feature store (L2)
- [FastAPI inference endpoint](docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py) — Build a FastAPI inference endpoint for model serving (L2)
- [Seldon Core vs KServe for sklearn](seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md) — Comparing Seldon Core and KServe for deploying sklearn models
- [ClearML pitfalls](clearml/notes/2026-07-12-clearml-pitfalls.md) — Common ClearML gotchas and how to work around them
- [Metaflow logging and artifact tracking](metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py) — Logging and artifact tracking in Metaflow flows

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
| Kubeflow | 14 | 9 | 5 | 2 | 4 | 5 | 2 | 20 | 4 |
| Metaflow | 13 | 7 | 5 | 2 | 3 | 2 | 2 | 11 | 1 |
| W&B | 14 | 8 | 3 | 4 | 3 | 1 | 1 | 7 | — |
| MLflow | 7 | 12 | 3 | 7 | 2 | — | 2 | — | — |
| DVC | 3 | 2 | 1 | 2 | — | — | — | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| ClearML | 3 | 1 | — | — | — | — | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — |
| ZenML | 2 | 1 | — | 1 | — | — | — | — | — |
| KServe | 1 | 1 | — | 1 | — | — | — | — | — |
| Seldon | 2 | 1 | — | — | — | — | — | — | — |

Plus 19 files across 8 concept directories covering experiment tracking, model registry, data versioning, pipeline orchestration, feature stores, model serving, containerization, and monitoring & drift.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Seldon vs KServe comparison, ClearML pitfalls, and practice scripts for feature store and model serving concepts.

---
_Last updated: 2026-07-13_
