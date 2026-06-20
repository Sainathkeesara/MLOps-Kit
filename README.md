# MLOps-Kit

> A working engineer's MLOps reference — MLflow, Kubeflow, DVC, Metaflow, Feast, Weights & Biases, and ZenML notes, snippets, and configs.

![Last commit](https://img.shields.io/github/last-commit/Sainathkeesara/MLOps-Kit)
![Files](https://img.shields.io/badge/files-138-blue)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?logo=gnu-bash&logoColor=white)

## What's in here

Hands-on notes, runnable snippets, and ready-to-use configs for seven core MLOps tools. Each tool has its own directory with a primer, setup notes, and working examples — from experiment tracking with MLflow and W&B, to data versioning with DVC, pipeline orchestration with Kubeflow, workflow management with Metaflow, feature stores with Feast, and pipeline frameworks with ZenML.

## Coverage

| Tool | Notes | Snippets | Scripts | Configs | Manifests | Docs | Notebooks | Dockerfiles | Templates |
|------|-------|----------|---------|---------|-----------|------|-----------|-------------|-----------|
| MLflow | 5 | 9 | 1 | 4 | — | 2 | 1 | — | — |
| Kubeflow | 10 | 6 | 2 | 1 | 3 | 2 | 1 | 3 | 8 |
| Metaflow | 9 | 5 | 1 | 1 | — | 2 | 2 | — | — |
| DVC | 3 | 2 | 1 | 1 | — | — | — | — | — |
| W&B | 9 | 6 | 3 | 4 | 1 | 3 | 1 | — | — |
| Feast | 2 | 1 | — | 2 | — | — | — | — | — |
| ZenML | 2 | 1 | — | — | — | — | — | — | — |
| General | — | — | — | — | — | 13 | — | — | — |

## Quick links

- [`wnb/docs/artifact-model-registry-workflow.md`](wnb/docs/artifact-model-registry-workflow.md) — Integrate W&B Artifacts with the Model Registry for versioned model governance and promotion through staging aliases
- [`wnb/scripts/sweep_and_eval_pipeline.py`](wnb/scripts/sweep_and_eval_pipeline.py) — Reusable sweep and evaluation pipeline with sklearn support and CLI subcommands
- [`metaflow/docs/foreach-vs-batch.md`](metaflow/docs/foreach-vs-batch.md) — Compare in-process fan-out with infrastructure-level parallelism via AWS Batch
- [`zenml/notes/2026-06-19-first-dashboard-and-stack.md`](zenml/notes/2026-06-19-first-dashboard-and-stack.md) — Exploring the ZenML dashboard and configuring an S3 artifact store stack
- [`zenml/snippets/tried_first_training_pipeline.py`](zenml/snippets/tried_first_training_pipeline.py) — First ZenML pipeline with data loading and model training

## Layout

- **`00_index/`** — Topic index, quick links, and glossary
- **`CHANGELOG.md`** — Chronological record of project changes
- **`dvc/`** — DVC notes, snippets, scripts, and configs
- **`feast/`** — Feast feature store notes, snippets, and configs
- **`General/`** — Cross-tool documentation and project-level guides
- **`kubeflow/`** — Kubeflow notes, docs, configs, manifests, scripts, snippets, notebooks, Dockerfiles, and templates
- **`metaflow/`** — Metaflow notes, configs, notebooks, scripts, and snippets
- **`mlflow/`** — MLflow notes, configs, docs, scripts, snippets, and notebooks
- **`wnb/`** — Weights & Biases notes, docs, scripts, snippets, configs, and manifests
- **`zenml/`** — ZenML notes and snippets

## Status

Working through first-contact notes and runnable experiments for each tool. Recently added Kubeflow KFP + MLflow tracking integration, Kubeflow Katib HPO with PyTorch, W&B Model Registry workflow, reusable sweep and eval pipeline, Metaflow foreach vs @batch comparison, and ZenML pipeline snippets.

---
_Last updated: 2026-06-21_
