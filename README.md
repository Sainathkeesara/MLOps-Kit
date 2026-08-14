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

Hands-on notes, runnable snippets, and ready-to-use configs covering the full MLOps lifecycle — experiment tracking with MLflow and W&B, data versioning with DVC, pipeline orchestration with Kubeflow and Metaflow, feature stores with Feast, orchestration with ClearML and ZenML, drift monitoring with Evidently AI, model serving with KServe and Seldon Core, and Databricks ML with Unity Catalog. Eight cross-cutting concept primers cover containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, and pipeline orchestration. Project templates for Kubeflow, Metaflow, MLflow, and W&B provide CI/CD-ready scaffolding for production pipelines.

## Quick links

- [Metaflow scaffold CI/CD workflow](mfl/configs/2026-08-12-metaflow-project-scaffold-ci-cd.yaml) — CI/CD with lint, test, flow-run, and deploy jobs for the Metaflow template
- [Monitoring and drift detection patterns](docs/concepts/monitoring-drift/2026-08-11-monitoring-drift-patterns.md) — Baseline snapshots, scheduled checks, threshold alerting, and retraining triggers
- [Data drift detection script](docs/concepts/monitoring-drift/scripts/2026-08-11-data-drift-detection.py) — Detect drift with z-score comparison against a reference baseline
- [Model serving config](docs/concepts/model-serving/configs/2026-08-11-model-serving-config.yaml) — Minimal serving config with batching, health checks, and logging
- [Install W&B and log your first run](wnb/notes/2026-08-11-install-wandb-and-log-my-first-run.md) — First experiment, first metric, and a tour of the dashboard

## Layout

- **`00_index/`** — Topic index, quick links, glossary, and learning path
- **`CHANGELOG.md`** — Chronological record of project changes
- **`clearml/`** — ClearML Orchestration notes, snippets, and configs
- **`databricks/`** — Databricks ML configs and scripts
- **`docs/`** — Cross-cutting concept primers and scripts (containerization, data versioning, experiment tracking, feature stores, model registry, model serving, monitoring & drift, pipeline orchestration)
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`evidently/`** — Evidently AI monitoring and drift detection notes and snippets
- **`feast/`** — Feast feature store notes, snippets, scripts, and configs
- **`kserve/`** — KServe model serving notes, snippets, and configs
- **`kub/`** — Kubeflow SDK snippets, configs, and manifests (KFP v2)
- **`kubeflow/`** — Kubeflow notes, configs, manifests, docs, notebooks, scripts, snippets, templates, and dockerfiles
- **`metaflow/`** — Metaflow notes, configs, docs, notebooks, scripts, snippets, manifests, templates, and dockerfiles
- **`mfl/`** — Metaflow crossover docs and configs
- **`mlf/`** — MLflow first-experiment scripts, snippets, and manifests
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`seldon/`** — Seldon Core model serving notes, snippets, and manifests
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, manifests, notebooks, and templates
- **`zenml/`** — ZenML notes, snippets, configs, notebooks, and scripts

## Coverage

<details><summary>Coverage table</summary>

| Tool | Notes | Snippets | Scripts | Configs | Docs | Manifests | Notebooks | Templates | Dockerfiles | Last verified |
|------|-------|----------|---------|---------|------|-----------|-----------|-----------|-------------|---------------|
| Kubeflow | 15 | 10 | 7 | 2 | 4 | 7 | 2 | 20 | 4 | 2026-08-04 |
| Weights & Biases | 15 | 9 | 5 | 4 | 5 | 2 | 3 | 21 | — | 2026-08-11 |
| Metaflow | 14 | 7 | 8 | 2 | 4 | 4 | 5 | 14 | 1 | 2026-08-05 |
| MLflow | 7 | 13 | 5 | 9 | 4 | — | 3 | 8 | 4 | 2026-07-30 |
| Concepts | 14 | 6 | 18 | 1 | — | — | — | — | 1 | 2026-08-11 |
| Feast | 5 | 3 | 1 | 3 | — | — | — | — | — | 2026-08-02 |
| DVC | 3 | 2 | 3 | 3 | — | — | — | — | — | 2026-07-28 |
| ZenML | 2 | 1 | 1 | 2 | — | — | 1 | — | — | 2026-07-14 |
| ClearML | 4 | 1 | — | 1 | — | — | — | — | — | 2026-07-23 |
| KServe | 1 | 2 | — | 1 | — | — | — | — | — | 2026-07-14 |
| Seldon Core | 2 | 1 | — | — | — | 1 | — | — | — | 2026-07-12 |
| Databricks | — | — | 1 | 1 | — | — | — | — | — | 2026-07-14 |
| kub (KFP SDK) | — | — | 1 | 1 | — | 1 | — | — | — | 2026-08-11 |
| MLflow first-experiments | 1 | 1 | 1 | — | — | 3 | — | — | — | 2026-08-12 |
| Metaflow crossover | — | — | 1 | 1 | 1 | — | — | — | — | 2026-08-12 |
| Evidently AI | 2 | 1 | — | — | — | — | — | — | — | — |

</details>

## Status

Currently working through monitoring and drift detection patterns, data versioning workflows, and CI/CD scaffold workflows for the project templates — with first-contact notes for W&B and Metaflow keeping pace.

---
_Last updated: 2026-08-12_
