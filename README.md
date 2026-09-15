# MLOps-Kit
> A working engineer's MLOps reference for MLflow, Kubeflow, Metaflow, W&B, DVC, Feast, ClearML, BentoML, SageMaker, and more.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Top language](https://img.shields.io/github/languages/top/Sainathkeesara/MLOps-Kit)
![Languages](https://img.shields.io/github/languages/count/Sainathkeesara/MLOps-Kit)
![Repo size](https://img.shields.io/github/repo-size/Sainathkeesara/MLOps-Kit)

> **New here? Start at [the learning path](00_index/learning-path.md).** It walks you from first-contact to confident in a sensible order — read that before this table.

## Who this is for

A working MLOps engineer's shelf: first-contact notes, runnable snippets, and configs for the tools that make ML production work. Use it when you are setting up a new tool, debugging a specific issue, or trying to recall how two systems fit together. It deliberately does not try to replace each tool's official docs.

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs spanning the MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, model serving with KServe, Seldon Core, and BentoML, managed training and endpoints with SageMaker, and the Databricks ML platform. Cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project scaffolds for Kubeflow, Metaflow, MLflow, and W&B ship with tests and CI/CD wiring.

## Quick links

- [SageMaker quick primer](sag/notes/0000-primer-sag.md) — Managed training jobs, endpoints, and Studio in plain language
- [My first look at the SageMaker Studio console](sag/notes/2026-09-15-studio-console-first-impressions.md) — Notebooks, job lists, and permission trip-ups from a first visit
- [First SageMaker session](sag/snippets/2026-09-15-first-sagemaker-session.py) — Session, script-mode estimator, and one test prediction
- [Feast — writing the `data/registry.db` companion file](feast/docs/2026-09-15-write-registry-db-companion-data-file.md) — Closing the gap between the notes and the local registry path
- [BentoML quick primer](bentoml/notes/0000-primer-bentoml.md) — Service, API methods, Bento bundles, and containerize in one sitting

## Layout

- **`00_index/`** — Topics map, quick links, glossary, and learning path
- **`bentoml/`** — BentoML model serving notes, snippets, and configs
- **`clearml/`** — ClearML orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs, scripts, snippets, and notes
- **`docs/`** — Cross-cutting concept primers and scripts (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI monitoring and drift detection notes and snippets
- **`feast/`** — Feast feature store notes, snippets, scripts, configs, and docs
- **`kserve/`** — KServe model serving notes, snippets, configs, and manifests
- **`kub/`** — Kubeflow Pipelines SDK configs, scripts, docs, and manifests (KFP v2)
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mfl/`** — Metaflow crossover docs, configs, scripts, and manifests
- **`mlf/`** — MLflow first-experiment scripts, snippets, notes, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, notebooks, templates, and dockerfiles
- **`sag/`** — SageMaker first-contact notes and snippets (sessions, training jobs, Studio)
- **`seldon/`** — Seldon Core model serving notes, snippets, configs, and manifests
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, scripts, configs, and notebooks

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Docs | Snippets | Scripts | Configs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|------|----------|---------|---------|-----------|-----------|-----------|-------------|---------------|
| Metaflow | 14 | 11 | 7 | 8 | 2 | 4 | 5 | 24 | 1 | 2026-08-04 |
| Kubeflow | 15 | 4 | 10 | 8 | 3 | 7 | 2 | 23 | 3 | 2026-07-14 |
| Weights & Biases | 15 | 5 | 9 | 5 | 6 | 6 | 3 | 25 | 0 | 2026-09-04 |
| MLflow | 7 | 4 | 13 | 5 | 9 | 0 | 3 | 11 | 4 | 2026-07-30 |
| Concepts | 0 | 59 | 6 | 23 | 1 | 0 | 1 | 0 | 1 | 2026-09-08 |
| Feast | 5 | 2 | 3 | 2 | 4 | 0 | 0 | 0 | 0 | 2026-09-15 |
| DVC | 5 | 0 | 2 | 5 | 3 | 0 | 0 | 0 | 0 | 2026-09-12 |
| ClearML | 7 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2026-09-10 |
| ZenML | 3 | 0 | 2 | 2 | 3 | 0 | 1 | 0 | 0 | 2026-08-22 |
| KServe | 2 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 2026-08-22 |
| Seldon Core | 2 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2026-07-12 |
| kub (KFP SDK) | 0 | 2 | 0 | 1 | 3 | 2 | 0 | 0 | 0 | 2026-09-07 |
| Databricks | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 2026-08-27 |
| BentoML | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2026-09-13 |
| Evidently AI | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| SageMaker | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2026-09-15 |
| mfl (Metaflow crossover) | 0 | 4 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 2026-08-06 |
| mlf (MLflow first-experiments) | 1 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 2026-08-12 |

</details>

## Status

SageMaker just landed its first-contact notes — primer, Studio walkthrough, and a session snippet. Feast's local registry companion file is now on disk alongside the doc that explains it. BentoML has a fresh primer too.

---
_Last updated: 2026-09-15_
