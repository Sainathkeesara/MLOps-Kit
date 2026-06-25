# Learning Path — MLOps

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

Start here with the core MLOps concepts that every tool builds upon. These primers are lighter reads than tool-specific docs and give you the vocabulary to understand what comes next.

- **Experiment Tracking** — Track model runs, metrics, and parameters. Primer available in [MLflow](../mlflow/notes/0000-primer-mlflow.md) and [Weights & Biases](../wnb/notes/0000-primer-wnb.md).
- **Pipeline Orchestration** — Define and run ML workflows as DAGs. Primer available in [Kubeflow](../kubeflow/notes/0000-primer-kubeflow.md) and [Metaflow](../metaflow/notes/0000-primer-metaflow.md).
- **Containerization** — Package ML code and models for reproducible deployment. Covered in Kubeflow's [dockerfiles](../kubeflow/dockerfiles/).

## Stage 2: Core Tools

These tools are unlocked from the start and cover the fundamentals of the MLOps lifecycle. Learn one from each family (tracking, orchestration, versioning) before moving deeper.

- **MLflow** (L1) — Experiment tracking, model registry, and project packaging. Start with the [primer](../mlflow/notes/0000-primer-mlflow.md) and [first run notes](../mlflow/notes/2026-05-27-install-mlflow-first-run.md).
- **Weights & Biases** (L4) — Experiment tracking, artifact management, and hyperparameter sweeps. Begin with the [primer](../wnb/notes/0000-primer-wnb.md) or [dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md).
- **Kubeflow** (L4) — Kubernetes-native pipeline orchestration and serving. Start with the [primer](../kubeflow/notes/0000-primer-kubeflow.md) and local [Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md).
- **Metaflow** (L4) — Human-centric ML workflow orchestration on AWS. Begin with the [primer](../metaflow/notes/0000-primer-metaflow.md) and [end-to-end flow notes](../metaflow/notes/2026-06-05-first-flow-end-to-end.md).
- **ZenML** (L1) — Modular MLOps pipelines with stack abstraction. Start with the [primer](../zenml/notes/0000-primer-zenml.md) and [dashboard setup](../zenml/notes/2026-06-19-first-dashboard-and-stack.md).

## Stage 3: Building Skills

Tools that expand your toolkit with specialised capabilities, or deeper tooling within the core families you already know.

- **ClearML Orchestration** (L1) — Managed MLOps platform with built-in experiment tracking. Requires Pipeline Orchestration foundation. Primer available in [clearml/notes/0000-primer-clearml-orchestration.md](../clearml/notes/0000-primer-clearml-orchestration.md).

## Stage 4: Advanced Tools

Tools that depend on multiple foundational concepts and integrate several tool families.

- **DVC** — Data versioning for ML pipelines. Currently locked; requires Experiment Tracking + Data Versioning at L2.
- **Feast** — Centralized feature management. Currently locked; requires Data Versioning + Model Registry at L2.
- **KServe** (L1) — Model serving on Kubernetes. Parent: Kubeflow must reach L4. Covered in [kubeflow/templates/kubeflow-mlflow-project/README.md](../kubeflow/templates/kubeflow-mlflow-project/README.md).
- **Seldon Core** (L1) — Advanced model deployment on Kubernetes. Parent: Kubeflow must reach L4.

## Stage 5: Mastery

Platform-specific deployment, advanced HPO, and cross-tool integration patterns.

- ⏳ **SageMaker** — AWS-native managed MLOps. Requires Model Serving + Pipeline Orchestration. Prerequisite: Metaflow L5.
- ⏳ **Vertex AI** — GCP-native managed MLOps. Requires Model Serving + Containerization. Prerequisite: Kubeflow L5.

## Progression Map

```
Stage 1: Foundations
├── Experiment Tracking ──► MLflow ──► ZenML ──► Databricks ML
│                         └──► W&B
├── Data Versioning ──────► DVC ──────► BentoML
│                         └──► Feast
└── Model Registry ───────► DVC
                          └──► Feast

Stage 1: Pipeline Orchestration ──► Kubeflow ──► KServe
│                                   │            └──► Seldon Core
│                                   └──► ZenML
│                                   └──► ClearML Orchestration
└── Metaflow ───────────────────────────────────└──► SageMaker

Stage 1: Containerization ──► Kubeflow/KMetaflow ──► KServe/Seldon Core/BentoML
Stage 1: Monitoring & Drift ──► Evidently AI ───────────────────────────────► SageMaker/Vertex AI
```

_Progress by working through primer notes first, then experiment snippets, and finally the integration docs that tie tools together._
