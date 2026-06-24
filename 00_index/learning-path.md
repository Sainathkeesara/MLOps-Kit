# Learning Path — MLOps

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

Start here with the core MLOps concepts that every tool builds upon. These primers are lighter reads than tool-specific docs and give you the vocabulary to understand what comes next.

- **Experiment Tracking** — Record what you did during a training run so you can reproduce and compare results later. Primer available in [docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md).
- **Data Versioning** — Snapshots of datasets you can checkout and branch, like git for data. Primer available in [docs/concepts/data-versioning/0000-primer-data-versioning.md](../docs/concepts/data-versioning/0000-primer-data-versioning.md).
- **Model Registry** — A central store to version, tag, and promote trained models from staging to production. Primer available in [docs/concepts/model-registry/0000-primer-model-registry.md](../docs/concepts/model-registry/0000-primer-model-registry.md).

## Stage 2: Core Tools

These tools are unlocked from the start and cover the fundamentals of the MLOps lifecycle. Learn one from each family (tracking, orchestration, versioning) before moving deeper.

- **MLflow** — Experiment tracking, model registry, and project packaging. Start with the [primer](../mlflow/notes/0000-primer-mlflow.md) and [first run notes](../mlflow/notes/2026-05-27-install-mlflow-first-run.md).
- **Weights & Biases** — Experiment tracking, artifact management, and hyperparameter sweeps. Begin with the [primer](../wnb/notes/0000-primer-wnb.md) or [dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md).
- **Kubeflow** — Kubernetes-native pipeline orchestration and serving. Start with the [primer](../kubeflow/notes/0000-primer-kubeflow.md) and local [Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md).
- **Metaflow** — Human-centric ML workflow orchestration. Begin with the [primer](../metaflow/notes/0000-primer-metaflow.md) and [end-to-end flow notes](../metaflow/notes/2026-06-05-first-flow-end-to-end.md).
- **DVC** — Data versioning for ML pipelines. Start with the [primer](../dvc/notes/0000-primer-dvc.md) and [first dataset version](../dvc/notes/2026-05-26-first-dataset-version.md).

## Stage 3: Building Skills

Tools that expand your toolkit with specialised capabilities, or deeper tooling within the core families you already know.

- **ZenML** — Modular MLOps pipelines with stack abstraction. Requires Pipeline Orchestration + Experiment Tracking foundations. Start with the [primer](../zenml/notes/0000-primer-zenml.md) and [dashboard setup](../zenml/notes/2026-06-19-first-dashboard-and-stack.md).
- **ClearML Orchestration** — Managed MLOps platform with built-in experiment tracking. Requires Pipeline Orchestration foundation. Primer available in [clearml/notes/0000-primer-clearml-orchestration.md](../clearml/notes/0000-primer-clearml-orchestration.md).
- **Feast** — Centralized feature management. Requires Data Versioning + Model Registry foundations. Start with the [primer](../feast/notes/0000-primer-feast.md) and [first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md).
- **Evidently AI** — Drift monitoring and data quality. Requires Monitoring & Drift foundation. Primer available in [evidently/notes/0000-primer-evidently.md](../evidently/notes/0000-primer-evidently.md).

## Stage 4: Advanced Tools

Tools that depend on multiple foundational concepts and integrate several tool families.

- ⏳ **KServe** — Model serving on Kubernetes. Requires Containerization + Pipeline Orchestration. Parent: Kubeflow must reach L4.
- ⏳ **Seldon Core** — Advanced model deployment on Kubernetes. Requires Containerization + Model Serving. Parent: Kubeflow must reach L4.
- ⏳ **BentoML** — Model packaging and serving. Requires Model Registry + Containerization + Data Versioning.
- ⏳ **Databricks ML** — MLflow-integrated platform tooling. Requires Model Registry + Experiment Tracking. Parent: MLflow must reach L5.

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
