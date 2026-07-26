# Learning Path — MLOps

> A suggested progression from beginner to confident practitioner. Each stage builds on the previous one. If a topic is listed but has no content yet, it's marked as ⏳ (coming soon).

## Stage 1: Foundations

Start here with the core MLOps concepts that every tool builds upon. These primers are lighter reads than tool-specific docs and give you the vocabulary to understand what comes next.

- **Experiment Tracking** — Track model runs, metrics, and parameters. [Primer](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) with [exercises](../docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py).
- **Pipeline Orchestration** — Define and run ML workflows as DAGs. [Primer](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md) with [exercises](../docs/concepts/pipeline-orchestration/snippets/2026-07-10-pipeline-orchestration-fundamentals.py) and [DAG workflow script](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py).
- **Containerization** — Package ML code for reproducible deployment. [Primer](../docs/concepts/containerization/0000-primer-containerization.md) — also see the [multi-stage Dockerfile for MLOps](../docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md) and the [multistage ONNX Runtime serving container](../docs/concepts/containerization/scripts/2026-07-13-multistage-onnxruntime-serving.py).
- **Data Versioning** — Version datasets and models alongside code. [Primer](../docs/concepts/data-versioning/0000-primer-data-versioning.md) with [exercises](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) and [snapshot script](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py).
- **Model Registry** — Govern model lifecycle from staging to production. [Primer](../docs/concepts/model-registry/0000-primer-model-registry.md) with [exercises](../docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py) and [apply script](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py).
- **Feature Store** — Manage and serve ML features consistently. [Primer](../docs/concepts/feature-store/0000-primer-feature-store.md) with [exercises](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) and [online store read/write script](../docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py).
- **Model Serving** — Deploy models for inference. [Primer](../docs/concepts/model-serving/0000-primer-model-serving.md) with [FastAPI inference endpoint](../docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py).
- **Monitoring & Drift** — Detect distribution shifts and performance degradation. [Primer](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md).

## Stage 2: Core Tools

These tools are unlocked from the start and cover the fundamentals of the MLOps lifecycle.

- **MLflow** — Experiment tracking, model registry, and project packaging. Start with the [primer](../mlflow/notes/0000-primer-mlflow.md), [first run notes](../mlflow/notes/2026-05-27-install-mlflow-first-run.md), and [UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md). For logging patterns, see [autologging vs manual logging](../mlflow/docs/autologging-vs-manual-logging.md) and the [custom experiment tracking workflow](../mlflow/scripts/custom-experiment-tracking-workflow.py). For a production-ready setup, try the [Postgres + S3 tracking server config](../mlflow/configs/2026-07-14-tracking-server-postgres-s3.yaml).
- **Weights & Biases** — Experiment tracking, artifact management, and hyperparameter sweeps. Begin with the [primer](../wnb/notes/0000-primer-wnb.md), [first experiment with SDK](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py), or [dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md). For artifact versioning, see the [artifacts deep dive](../wnb/docs/wandb-artifacts-deep-dive.md) and [artifact tracking in data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md). For run analysis, explore the [parallel coordinates, correlation, and run diff notebook](../wnb/notebooks/compare-runs-parallel-coords-correlation-diff.ipynb). For artifact lineage, read the [artifacts deep dive](../wnb/docs/wandb-artifacts-deep-dive.md) and the [artifact + model registry workflow](../wnb/docs/artifact-model-registry-workflow.md).
- **Kubeflow** — Kubernetes-native pipeline orchestration and serving. Start with the [primer](../kubeflow/notes/0000-primer-kubeflow.md) and [Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md) or the newer [install KFP on Kind note](../kubeflow/notes/2026-07-14-install-kfp-on-kind.md). Follow up with [KFP v2 quickstart trip-ups](../kubeflow/notes/2026-07-11-kfp-v2-quickstart-trip-ups.md). For advanced project scaffolding, see the [pipeline scaffold template](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md).
- **Metaflow** — Human-centric ML workflow orchestration. Begin with the [primer](../metaflow/notes/0000-primer-metaflow.md), [install and hello world](../metaflow/notes/2026-07-14-install-and-hello-world.md), or [install and first flow](../metaflow/snippets/2026-07-06-install-first-flow.py). Then move to [CLI and local dev UI](../metaflow/notes/2026-07-09-explore-cli-local-dev-ui.md), the [end-to-end experiment script](../metaflow/scripts/2026-07-03-end-to-end-experiment.py), and [logging and artifact tracking script](../metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py). For parallel execution patterns, see [foreach with per-branch resources and Conda](../metaflow/scripts/foreach-resources-conda-flow.py) and [W&B real-time metric tracking across parallel steps](../metaflow/docs/wandb-metric-tracking-parallel-steps.md). For Kubernetes execution, see the [@kubernetes flow](../metaflow/scripts/2026-07-12-kubernetes-flow-metadata-tracking.py). For execution backends, explore the [@batch vs @kubernetes vs local comparison notebook](../metaflow/notebooks/2026-07-19-batch-vs-kubernetes-vs-local.ipynb). For local dev, use the [DevStack compose manifest](../metaflow/manifests/2026-07-13-metaflow-devstack-compose.yaml). To compare execution backends, read the [batch vs Kubernetes vs local notebook](../metaflow/notebooks/2026-07-19-batch-vs-kubernetes-vs-local.ipynb).
- **ZenML** — Modular MLOps pipelines with stack abstraction. Start with the [primer](../zenml/notes/0000-primer-zenml.md) and [stack config](../zenml/configs/zenml-stack.yaml). For MLflow integration, see the [MLflow+S3 stack config](../zenml/configs/2026-07-12-zenml-stack-mlflow-s3.yaml) and the [multi-step pipeline script](../zenml/scripts/2026-07-13-multi-step-zenml-mlflow-pipeline.py). For advanced patterns, explore the [parent-child pipelines and artifact lineage notebook](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb).

## Stage 3: Building Skills

Tools that expand your toolkit with specialised capabilities, or deeper tooling within the core families you already know.

- **ClearML Orchestration** — Managed MLOps platform with built-in experiment tracking. Requires Pipeline Orchestration foundation. [Primer](../clearml/notes/0000-primer-clearml-orchestration.md), [web UI walkthrough](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md), [common pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md), and [agent first tasks](../clearml/notes/2026-07-23-clearml-agent-first-tasks.md).
- **DVC** — Data versioning for ML pipelines. Unlocked after MLflow L1 complete; requires Experiment Tracking + Data Versioning. [Primer](../dvc/notes/0000-primer-dvc.md) and [end-to-end CLI walkthrough](../dvc/scripts/2026-07-22-dvc-end-to-end.sh).
- **Feast** — Centralized feature management. Unlocked after MLflow L2 complete; requires Data Versioning + Model Registry. [Primer](../feast/notes/0000-primer-feast.md), [Parquet offline store setup](../feast/notes/2026-07-23-install-feast-parquet-offline-store.md), [data source registration](../feast/snippets/2026-07-23-register-data-source-and-inspect-schema.py), and [entity/FeatureView historical retrieval](../feast/scripts/2026-07-22-entity-and-featureview-historical-retrieval.py).

## Stage 4: Advanced Tools

Tools that depend on multiple foundational concepts and integrate several tool families.

- **Evidently AI** — Monitoring and drift detection. Unlocked after Kubeflow L4 complete; requires Monitoring & Drift + Pipeline Orchestration. [Primer](../evidently/notes/0000-primer-evidently.md) and [Report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md).
- **KServe** — Model serving on Kubernetes. Parent: Kubeflow must reach L4. Requires Containerization + Pipeline Orchestration. [Primer](../kserve/notes/0000-primer-kserve.md), [first InferenceService](../kserve/snippets/first_inferenceservice.py), and [custom predictor with explainer](../kserve/snippets/2026-07-14-custom-predictor-explainer.py).
- **Seldon Core** — Advanced model deployment on Kubernetes. Parent: Kubeflow must reach L4. Requires Containerization + Model Serving. [Primer](../seldon/notes/0000-primer-seldon-core.md), [first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py), and [vs KServe comparison](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md).

## Stage 5: Mastery

Platform-specific deployment, advanced HPO, and cross-tool integration patterns.

- ⏳ **SageMaker** — AWS-native managed MLOps. Requires Model Serving + Pipeline Orchestration. Prerequisite: Metaflow L5.
- ⏳ **Vertex AI** — GCP-native managed MLOps. Requires Model Serving + Containerization. Prerequisite: Kubeflow L5.
- **Databricks ML** — Unified analytics and ML platform with Unity Catalog integration. Requires Model Registry + Experiment Tracking. Prerequisite: MLflow L5. [Unity Catalog setup](../databricks/configs/2026-07-14-unity-catalog-setup.yaml) and [model promotion script](../databricks/scripts/2026-07-14-model-promotion-unity-catalog.py).
- ⏳ **BentoML** — Model serving and packaging. Requires DVC L1 and MLflow L3.

## Progression Map

```
Stage 1: Foundations
├── Experiment Tracking ──► MLflow ──► ZenML
│                         └──► W&B
├── Data Versioning ──────► DVC ──────► Feast
├── Model Registry ───────► DVC
│                         └──► Feast
├── Containerization ────► Kubeflow ──► KServe
│                           │           └──► Seldon Core
│                           └──► ZenML
├── Pipeline Orchestration ──► Kubeflow
│                              ├──► ClearML Orchestration
│                              └──► ZenML
├── Monitoring & Drift ───► Evidently AI ──► SageMaker / Vertex AI
└── Model Serving ────────► KServe / Seldon Core ──► SageMaker / Vertex AI

Metaflow ──────────────────► SageMaker
```

_Progress by working through primer notes first, then experiment snippets, and finally the integration docs that tie tools together._
