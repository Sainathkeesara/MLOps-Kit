# MLOps-Kit
> A working engineer's MLOps reference for MLflow, Kubeflow, Metaflow, W&B, DVC, Feast, ClearML, BentoML, and more.

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

- [Model serving patterns in production MLOps projects](docs/concepts/model-serving/model-serving-patterns-in-production-mlops-projects.md) — Production patterns for connecting model serving to experiment tracking, feature stores, containerization, and monitoring
- [Combining model serving with containerization](docs/concepts/model-serving/scripts/combining-model-serving-with-containerization.py) — Integration script that stages a model bundle, generates a FastAPI app, and produces a Dockerfile
- [Documenting kub folder (Sep 7)](kub/docs/2026-09-07-documenting-kub-folder.md) — SDK-first vs platform-first perspective on the kub/ folder
- [Documenting kub folder (Sep 5)](kub/docs/2026-09-05-documenting-kub-folder.md) — First-day notes on what's in kub/ and why it's separate from kubeflow/
- [Dynamic parallelism and conditional branching](kubeflow/scripts/2026-09-04-dynamic-parallelism-conditional.py) — KFP v2 pipeline with dynamic fan-out and conditional step execution

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
- **`kub/`** — Kubeflow Pipelines SDK configs, scripts, docs, and manifests (KFP v2)
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
| Metaflow | 14 | 7 | 8 | 2 | 11 | 4 | 5 | 24 | 1 | — |
| Kubeflow | 15 | 10 | 8 | 3 | 4 | 7 | 2 | 22 | 3 | — |
| Weights & Biases | 15 | 9 | 5 | 6 | 5 | 5 | 3 | 24 | 0 | — |
| MLflow | 7 | 13 | 5 | 9 | 4 | 0 | 3 | 11 | 4 | — |
| Concepts | 0 | 6 | 23 | 1 | 21 | 0 | 1 | 0 | 1 | 2026-09-08 |
| Feast | 5 | 3 | 2 | 4 | 1 | 0 | 0 | 0 | 0 | 2026-08-15 |
| DVC | 4 | 2 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | — |
| ClearML | 6 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2026-09-04 |
| ZenML | 3 | 2 | 2 | 3 | 0 | 0 | 1 | 0 | 0 | — |
| KServe | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | — |
| Seldon Core | 2 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 2026-07-12 |
| MLflow first-experiments | 1 | 1 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | — |
| Metaflow crossover | 0 | 0 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | — |
| BentoML | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-08-22 |
| kub (KFP SDK) | 0 | 0 | 1 | 3 | 2 | 2 | 0 | 0 | 0 | 2026-09-07 |
| Databricks | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-08-27 |
| Evidently AI | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |

</details>

## Status

Active across BentoML, ClearML, Databricks ML, DVC, KServe, Metaflow, W&B, and ZenML — filling first-contact notes, snippets, and project scaffolds.

---
_Last updated: 2026-09-09_
