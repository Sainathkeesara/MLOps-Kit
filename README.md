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

- [Containerization + pipeline orchestration pattern](docs/concepts/containerization/docs/containerization-pipeline-orchestration-pattern.md) — Combining containerization with pipeline orchestration for ML workloads
- [Combining containerization with model serving](docs/concepts/containerization/scripts/combining-containerization-with-model-serving.py) — End-to-end script tying containerization to model serving
- [W&B PyTorch scaffold CI/CD workflow](wnb/manifests/wandb-pytorch-scaffold-ci-cd.yaml) — CI/CD workflow for the W&B PyTorch scaffold
- [W&B PyTorch CI/CD workflow template](wnb/templates/wandb-pytorch-scaffold/.github/workflows/ci-cd.yml) — GitHub Actions workflow for W&B PyTorch CI/CD
- [Install DVC and log first dataset version](dvc/notes/2026-08-13-install-dvc-and-log-first-dataset-version.md) — First DVC dataset version and tracking walkthrough

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
| Kubeflow | 15 | 10 | 7 | 2 | 4 | 7 | 2 | 20 | 1 | 2026-07-14 |
| Weights & Biases | 15 | 9 | 5 | 4 | 5 | 3 | 3 | 22 | 0 | 2026-08-11 |
| Metaflow | 14 | 7 | 8 | 2 | 4 | 4 | 5 | 14 | 1 | 2026-08-04 |
| MLflow | 7 | 13 | 5 | 9 | 4 | 0 | 3 | 8 | 1 | 2026-07-30 |
| Concepts | 14 | 6 | 19 | 1 | 1 | 0 | 0 | 0 | 2 | 2026-08-14 |
| Feast | 5 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 2026-08-02 |
| DVC | 4 | 2 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 2026-08-13 |
| ZenML | 2 | 1 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 2026-07-14 |
| ClearML | 4 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-23 |
| KServe | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-14 |
| Seldon Core | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2026-07-12 |
| Databricks | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2026-07-14 |
| kub (KFP SDK) | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 2026-08-11 |
| MLflow first-experiments | 1 | 1 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 2026-08-12 |
| Metaflow crossover | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 2026-08-06 |
| Evidently AI | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |

</details>

## Status

Currently adding containerization + pipeline orchestration patterns, W&B CI/CD scaffolds, and DVC first-contact notes.

---
_Last updated: 2026-08-14_
