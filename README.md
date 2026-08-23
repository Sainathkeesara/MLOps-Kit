# MLOps-Kit
> A working MLOps engineer's quick-reference: first-contact notes, runnable snippets, and configs for MLflow, Kubeflow, Metaflow, W&B, DVC, Feast, ClearML, ZenML, KServe, Seldon Core, Databricks, and Evidently AI.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's shelf: first-contact notes, runnable snippets, and configs for the tools that make ML production work. Use it when you are setting up a new tool, debugging a specific issue, or trying to recall how two systems fit together. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs spanning the MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, and model serving with KServe and Seldon Core. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project scaffolds for Kubeflow, Metaflow, MLflow, and W&B ship with tests and CI/CD wiring.

## Quick links

- [Install BentoML and first service](bentoml/notes/2026-08-22-install-bentoml-and-first-service.md) — First-contact notes for BentoML service setup
- [Install ClearML and first experiment](clearml/notes/2026-08-22-install-clearml-and-first-experiment.md) — First experiment with ClearML tracking
- [KServe quickstart trip-ups](kserve/notes/2026-08-22-kserve-quickstart-trip-ups.md) — Gotchas from the KServe quickstart
- [BentoML service config](bentoml/configs/2026-08-22-minimal-bentoml-service.yaml) — Minimal BentoML service YAML
- [First BentoML prediction](bentoml/snippets/2026-08-22-first-bentoml-prediction.py) — Minimal prediction snippet for BentoML

## Layout

- **`README.md`** — This file
- **`CHANGELOG.md`** — Chronological record of project changes
- **`00_index/`** — Topic map, quick links, glossary, and learning path
- **`bentoml/`** — BentoML model serving notes, snippets, and configs
- **`clearml/`** — ClearML orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs and scripts
- **`docs/`** — Cross-cutting concept primers and scripts (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI monitoring and drift detection notes and snippets
- **`feast/`** — Feast feature store notes, snippets, scripts, configs, and docs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kub/`** — Kubeflow Pipelines SDK configs, scripts, and manifests (KFP v2)
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mfl/`** — Metaflow crossover docs, configs, and manifests
- **`mlf/`** — MLflow first-experiment scripts, snippets, notes, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes, snippets, configs, and manifests
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, configs, notebooks, and scripts

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Kubeflow | 18 | 10 | 7 | 3 | 4 | 7 | 2 | 23 | 4 | 2026-08-04 |
| Metaflow | 22 | 7 | 8 | 2 | 11 | 4 | 5 | 24 | 1 | 2026-08-05 |
| Weights & Biases | 15 | 9 | 5 | 6 | 5 | 3 | 3 | 26 | 0 | 2026-08-14 |
| MLflow | 7 | 13 | 5 | 9 | 4 | 0 | 3 | 11 | 4 | 2026-07-30 |
| Concepts | 16 | 6 | 21 | 3 | 1 | 0 | 0 | 0 | 1 | 2026-08-14 |
| Feast | 5 | 3 | 2 | 4 | 1 | 0 | 0 | 0 | 0 | 2026-08-15 |
| DVC | 4 | 2 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 2026-08-13 |
| ClearML | 5 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-23 |
| ZenML | 2 | 1 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 2026-07-13 |
| KServe | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-14 |
| Seldon Core | 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2026-07-12 |
| Databricks | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-14 |
| kub (KFP SDK) | 0 | 0 | 1 | 3 | 0 | 1 | 0 | 0 | 0 | 2026-08-11 |
| MLflow first-experiments | 1 | 1 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 2026-08-12 |
| Metaflow crossover | 0 | 0 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | 2026-08-13 |
| Evidently AI | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| BentoML | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | — |

</details>

## Status

Currently working through first-contact notes for BentoML, ClearML, and KServe, alongside Feast feature-store configuration and cross-tool CI/CD scaffolding.

---
_Last updated: 2026-08-23_
