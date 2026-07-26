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

- [Kubeflow CI/CD script](kubeflow/scripts/2026-07-23-kubeflow-ci-cd.sh) — Lint, test, compile, and deploy a pipeline scaffold template
- [ClearML agent first tasks](clearml/notes/2026-07-23-clearml-agent-first-tasks.md) — Queue, clone, and run a task remotely via clearml-agent CLI
- [Multi-stage Dockerfile for MLOps](docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md) — Build-stage training, slim runtime serving image
- [Feast data source registration](feast/snippets/2026-07-23-register-data-source-and-inspect-schema.py) — Register a data source and inspect its schema with the Feast Python SDK
- [Feast Parquet offline store setup](feast/notes/2026-07-22-install-feast-parquet-offline-store.md) — Configure a Parquet-backed offline store for feature retrieval

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
| Kubeflow | 14 | 8 | 5 | 1 | 3 | 4 | 1 | 18 | 3 | 2026-07-14 |
| Metaflow | 13 | 7 | 6 | 1 | 4 | 2 | 3 | 10 | 1 | 2026-07-19 |
| W&B | 14 | 8 | 4 | 4 | 4 | 2 | 2 | 6 | — | 2026-07-19 |
| MLflow | 7 | 13 | 4 | 8 | 3 | — | 3 | — | — | 2026-07-17 |
| ClearML | 4 | 1 | — | 1 | — | — | — | — | — | 2026-07-23 |
| Feast | 4 | 2 | 1 | 1 | — | — | — | — | — | 2026-07-23 |
| DVC | 3 | 2 | 2 | 2 | — | — | — | — | — | — |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | — |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | — |
| Seldon Core | 2 | 1 | — | — | — | — | — | — | — | 2026-07-12 |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | — |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | — |

Plus 21 files across 8 concept directories covering containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration.

</details>

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added ClearML agent CLI notes, a multi-stage Dockerfile for MLOps, Feast data source registration snippet, Feast Parquet offline store setup notes, and a DVC end-to-end CLI walkthrough.

---
_Last updated: 2026-07-24_
