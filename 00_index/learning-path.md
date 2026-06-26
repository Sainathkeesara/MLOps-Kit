# Learning Path — MLOps

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

Start here with the core MLOps concepts that every tool builds upon. These primers are lighter reads than tool-specific docs and give you the vocabulary to understand what comes next.

- **Experiment Tracking** — Track model runs, metrics, and parameters. [Primer](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) with [exercises](../docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py).
- **Pipeline Orchestration** — Define and run ML workflows as DAGs. [Primer](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md).
- **Containerization** — Package ML code for reproducible deployment. [Primer](../docs/concepts/containerization/0000-primer-containerization.md).
- **Data Versioning** — Version datasets and models alongside code. [Primer](../docs/concepts/data-versioning/0000-primer-data-versioning.md).
- **Model Registry** — Govern model lifecycle from staging to production. [Primer](../docs/concepts/model-registry/0000-primer-model-registry.md) with [exercises](../docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py).
- **Feature Store** — Manage and serve ML features consistently. [Primer](../docs/concepts/feature-store/0000-primer-feature-store.md).
- **Model Serving** — Deploy models for inference. [Primer](../docs/concepts/model-serving/0000-primer-model-serving.md).
- **Monitoring & Drift** — Detect distribution shifts and performance degradation. [Primer](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md).

## Stage 2: Core Tools

These tools are unlocked from the start and cover the fundamentals of the MLOps lifecycle.

- **MLflow** (L1) — Experiment tracking, model registry, and project packaging. Start with the [primer](../mlflow/notes/0000-primer-mlflow.md) and [first run notes](../mlflow/notes/2026-05-27-install-mlflow-first-run.md).
- **Weights & Biases** (L4) — Experiment tracking, artifact management, and hyperparameter sweeps. Begin with the [primer](../wnb/notes/0000-primer-wnb.md) or [dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md).
- **Kubeflow** (L4) — Kubernetes-native pipeline orchestration and serving. Start with the [primer](../kubeflow/notes/0000-primer-kubeflow.md) and [Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md).
- **Metaflow** (L4) — Human-centric ML workflow orchestration on AWS. Begin with the [primer](../metaflow/notes/0000-primer-metaflow.md) and [end-to-end flow notes](../metaflow/notes/2026-06-05-first-flow-end-to-end.md).
- **ZenML** (L1) — Modular MLOps pipelines with stack abstraction. Start with the [primer](../zenml/notes/0000-primer-zenml.md) and [stack config](../zenml/configs/zenml-stack.yaml).

## Stage 3: Building Skills

Tools that expand your toolkit with specialised capabilities, or deeper tooling within the core families you already know.

- **ClearML Orchestration** — Managed MLOps platform with built-in experiment tracking. Requires Pipeline Orchestration foundation. [Primer](../clearml/notes/0000-primer-clearml-orchestration.md) and [web UI walkthrough](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md).

## Stage 4: Advanced Tools

Tools that depend on multiple foundational concepts and integrate several tool families.

- **DVC** — Data versioning for ML pipelines. Unlocked after MLflow L1 complete; requires Experiment Tracking + Data Versioning. [Primer](../dvc/notes/0000-primer-dvc.md).
- **Feast** — Centralized feature management. Unlocked after MLflow L2 complete; requires Data Versioning + Model Registry. [Primer](../feast/notes/0000-primer-feast.md).
- **Evidently AI** — Monitoring and drift detection. Unlocked after Kubeflow L4 complete; requires Monitoring & Drift + Pipeline Orchestration. [Primer](../evidently/notes/0000-primer-evidently.md).
- **KServe** — Model serving on Kubernetes. Parent: Kubeflow must reach L4. Requires Containerization + Pipeline Orchestration. ⏳
- **Seldon Core** — Advanced model deployment on Kubernetes. Parent: Kubeflow must reach L4. Requires Containerization + Model Serving. ⏳
- **BentoML** — Model serving and packaging. Requires DVC L1 and MLflow L3. ⏳

## Stage 5: Mastery

Platform-specific deployment, advanced HPO, and cross-tool integration patterns.

- ⏳ **SageMaker** — AWS-native managed MLOps. Requires Model Serving + Pipeline Orchestration. Prerequisite: Metaflow L5.
- ⏳ **Vertex AI** — GCP-native managed MLOps. Requires Model Serving + Containerization. Prerequisite: Kubeflow L5.
- ⏳ **Databricks ML** — Unified analytics and ML platform. Requires Model Registry + Experiment Tracking. Prerequisite: MLflow L5.

## Progression Map

```
Stage 1: Foundations
├── Experiment Tracking ──► MLflow ──► ZenML
│                         └──► W&B
├── Data Versioning ──────► DVC ──────► BentoML
│                         └──► Feast
├── Model Registry ───────► DVC
│                         └──► Feast
└── Containerization ─────► Kubeflow ──► KServe
                            │            └──► Seldon Core
                            └──► ZenML

Stage 1: Pipeline Orchestration ──► Kubeflow
│                                   │
│                                   └──► ClearML Orchestration
│                                   └──► ZenML
└── Metaflow ──────────────────────────────────└──► SageMaker

Stage 1: Monitoring & Drift ──► Evidently AI ────► SageMaker / Vertex AI
Stage 1: Model Serving ───────► KServe / Seldon Core / BentoML ──► SageMaker / Vertex AI
```

_Progress by working through primer notes first, then experiment snippets, and finally the integration docs that tie tools together._
