# Quick Links

## I need to...

### Set up a tool for the first time
- [MLflow primer](../mlflow/notes/0000-primer-mlflow.md) — Install, run the UI, and log my first experiment
- [W&B primer](../wnb/notes/0000-primer-wnb.md) — SDK setup, first run, and dashboard tour
- [Kubeflow primer](../kubeflow/notes/0000-primer-kubeflow.md) — Cluster setup, install, and first pipeline
- [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md) — Local install, first flow, and CLI/UI
- [DVC primer](../dvc/notes/0000-primer-dvc.md) — Data versioning setup and first snapshot
- [Feast primer](../feast/notes/0000-primer-feast.md) — Feature store setup and first retrieval
- [KServe primer](../kserve/notes/0000-primer-kserve.md) — Model serving setup and first InferenceService
- [Seldon Core primer](../seldon/notes/0000-primer-seldon-core.md) — Model serving setup and first deploy
- [ClearML primer](../clearml/notes/0000-primer-clearml-orchestration.md) — ClearML orchestration setup and first task
- [ClearML common pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md) — Gotchas and workarounds for ClearML
- [Seldon Core vs KServe for sklearn](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md) — Comparing two model-serving frameworks

### Run an experiment
- [MLflow end-to-end training with autologging](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — sklearn autolog, model comparison, and registry registration
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py) — Build a sweep from scratch with the Python SDK
- [W&B sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py) — Multi-task sweep and evaluation with CLI subcommands
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py) — Data loading, training, and artifact logging
- [Evidently first drift report](../evidently/snippets/first_drift_report.py) — Generate and view a data drift report

### Orchestrate a pipeline
- [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md) — Component writing and compilation pitfalls
- [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md) — Diagnose pod failures and Artifact store issues
- [Kubeflow Pipelines + MLflow tracking integration](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md) — Wire KFP to an in-cluster MLflow server
- [Metaflow end-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py) — Tracking, model logging, and run comparison via Client API
- [Metaflow logging and artifact tracking](../metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py) — Logging and artifact tracking in Metaflow flows
- [Metaflow resource management](../metaflow/docs/metaflow-resource-management.md) — CPU, memory, and GPU scheduling

### Version and register models
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md) — MLflow Model Registry version comparison
- [W&B Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md) — Version, register, and promote artifacts
- [Apply model registry: version and promote ML models](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py) — End-to-end registry promotion script (L2)

### Version data
- [Data versioning fundamentals exercises](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) — Pointer files, snapshots, and restore logic (L2)
- [Track dataset snapshots for reproducible training](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py) — Snapshot datasets and pin to training runs (L2)
- [Pipeline orchestration practice exercises](../docs/concepts/pipeline-orchestration/snippets/2026-07-10-pipeline-orchestration-fundamentals.py) — DAG, dependencies, and run order (L2)
- [Applying DAG-based ML workflow](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py) — Build and run a DAG-based ML pipeline (L2)
- [Feature store fundamentals exercises](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) — Feature definitions, online/offline, point-in-time joins (L2)
- [Feature store online store read/write](../docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py) — Write and read features from an online store (L2)
- [FastAPI inference endpoint for model serving](../docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py) — Build a FastAPI inference API (L2)

### Manage compute and environments
- [Metaflow foreach vs @batch](../metaflow/docs/foreach-vs-batch.md) — Parallelism patterns and execution backends
- [Metaflow AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml) — Batch compute for Metaflow flows
- [Metaflow custom runtime Docker image](../metaflow/dockerfiles/metaflow-dev.Dockerfile) — CUDA + distributed deps for dev
- [W&B Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml) — Local compute for W&B sweeps

### Configure a project
- [Kubeflow pipeline project scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md) — CI/CD, unit testing, modular components
- [Kubeflow + MLflow project scaffold](../kubeflow/templates/kubeflow-mlflow-project/README.md) — KFP wired with MLflow tracking
- [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md) — Metaflow with CI/CD, testing, and env management
- [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md) — W&B tracking with GitHub Actions
- [MLflow project config](../mlflow/configs/mlflow-project.yaml) — Project packaging and entry points
- [DVC pipeline config](../dvc/configs/pipeline.yaml) — Data and model pipeline stages

### Learn foundational concepts
- [Experiment Tracking primer](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md)
- [Model Registry primer](../docs/concepts/model-registry/0000-primer-model-registry.md)
- [Data Versioning primer](../docs/concepts/data-versioning/0000-primer-data-versioning.md)
- [Pipeline Orchestration primer](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md)
- [Feature Store primer](../docs/concepts/feature-store/0000-primer-feature-store.md)
- [Model Serving primer](../docs/concepts/model-serving/0000-primer-model-serving.md)
- [Containerization primer](../docs/concepts/containerization/0000-primer-containerization.md)
- [Monitoring & Drift primer](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md)

## Project
- [README](../README.md) — Project overview and repository structure
- [CHANGELOG](../CHANGELOG.md) — Record of completed tasks
