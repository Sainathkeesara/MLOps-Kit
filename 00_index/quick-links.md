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
- [ClearML primer](../clearml/notes/0000-primer-clearml-orchestration.md) — Orchestration setup and first task
- [ZenML primer](../zenml/notes/0000-primer-zenml.md) — Stack setup and first pipeline
- [Install KFP on Kind](../kubeflow/notes/2026-07-14-install-kfp-on-kind.md) — Kubeflow Pipelines on a local Kind cluster
- [ClearML agent first tasks](../clearml/notes/2026-07-23-clearml-agent-first-tasks.md) — Queue, clone, and run a task remotely via clearml-agent CLI
- [ClearML common pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md) — Gotchas and workarounds for ClearML
- [Seldon Core vs KServe for sklearn](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md) — Comparing two model-serving frameworks
- [KServe custom predictor with explainer](../kserve/snippets/2026-07-14-custom-predictor-explainer.py) — Custom model predictor and explainer for KServe
- [ClearML remote GPU execution config](../clearml/configs/2026-07-14-remote-gpu-execution.yaml) — Remote GPU execution configuration for ClearML
- [Feast Parquet offline store setup](../feast/notes/2026-07-23-install-feast-parquet-offline-store.md) — Configure a Parquet-backed offline store for feature retrieval

### Set up Databricks
- [Databricks Unity Catalog setup](../databricks/configs/2026-07-14-unity-catalog-setup.yaml) — Unity Catalog configuration for Databricks ML
- [Databricks model promotion to Unity Catalog](../databricks/scripts/2026-07-14-model-promotion-unity-catalog.py) — Promote MLflow models to Unity Catalog

### Run an experiment
- [MLflow tracking quickstart](../mlflow/snippets/2026-07-14-mlflow-tracking-quickstart.py) — First experiment with MLflow tracking
- [MLflow end-to-end training with autologging](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — sklearn autolog, model comparison, and registry registration
- [MLflow + W&B hybrid tracking](../mlflow/docs/integrating-mlflow-with-weights-and-biases.md) — Run MLflow and W&B in parallel and synchronize metadata
- [MLflow custom experiment tracking workflow](../mlflow/scripts/custom-experiment-tracking-workflow.py) — Custom workflow with MlflowClient for search, compare, and register
- [MLflow experiment comparison + promotion](../mlflow/scripts/experiment-compare-and-promote.py) — Reusable helper for automated experiment comparison and model promotion
- [MLflow experiment comparison via Search API](../mlflow/notebooks/mlflow-experiment-comparison-search-api.ipynb) — Programmatic experiment comparison with MLflow Search API
- [Install MLflow and log first experiment](../mlf/snippets/2026-08-01-install-mlflow-first-experiment.py) — Install MLflow and log your first experiment with the Python SDK
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py) — Build a sweep from scratch with the Python SDK
- [W&B sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py) — Multi-task sweep and evaluation with CLI subcommands
- [W&B custom sweep with early termination](../wnb/scripts/custom-sweep-early-termination.py) — Custom search space and early-stopping strategy
- [W&B report generator](../wnb/scripts/wandb-report-generator.py) — Generate correlation and parallel-coords reports from W&B sweep runs
- [W&B artifacts deep dive](../wnb/docs/wandb-artifacts-deep-dive.md) — Versioning, lineage, and reuse of artifacts across runs
- [W&B run comparison: parallel coords and correlation diff](../wnb/notebooks/compare-runs-parallel-coords-correlation-diff.ipynb) — Compare runs with parallel coordinates and correlation plots
- [Comparing W&B Artifacts vs MLflow Model Registry](../wnb/notebooks/comparing-wb-artifacts-vs-mlflow-model-registry.ipynb) — Compare artifact lineage and model registry entries across W&B and MLflow
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py) — Data loading, training, and artifact logging
- [ZenML parent-child pipelines and artifact lineage](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb) — Multi-pipeline DAGs and artifact tracking with ZenML
- [Evidently first drift report](../evidently/snippets/first_drift_report.py) — Generate and view a data drift report
- [Metaflow Kubernetes flow with metadata tracking](../metaflow/scripts/2026-07-12-kubernetes-flow-metadata-tracking.py) — Run Metaflow on Kubernetes with cloud metadata
- [Feast data source registration and schema inspection](../feast/snippets/2026-07-23-register-data-source-and-inspect-schema.py) — Register a data source and inspect its schema with the Feast Python SDK
- [W&B PyTorch sweep config](../wnb/templates/wandb-pytorch-scaffold/configs/sweep-config.yaml) — Declarative sweep configuration for W&B hyperparameter optimization
- [W&B PyTorch training script](../wnb/templates/wandb-pytorch-scaffold/train.py) — Training script with W&B metric and artifact logging

### Orchestrate a pipeline
- [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md) — Component writing and compilation pitfalls
- [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md) — Diagnose pod failures and Artifact store issues
- [Kubeflow Pipelines + MLflow tracking integration](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md) — Wire KFP to an in-cluster MLflow server
- [Metaflow + W&B real-time metric tracking across parallel steps](../metaflow/docs/wandb-metric-tracking-parallel-steps.md) — Stream per-branch W&B metrics during Metaflow foreach execution
- [Metaflow end-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py) — Tracking, model logging, and run comparison via Client API
- [Metaflow resource management](../metaflow/docs/metaflow-resource-management.md) — CPU, memory, and GPU scheduling
- [Metaflow logging artifact flow](../metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py) — Log artifacts and metadata in Metaflow flows
- [Metaflow trigger hooks](../metaflow/scripts/2026-07-28-metaflow-trigger-hooks.py) — Wire @trigger, @trigger_on_finish, and @exit_hook across flows
- [Metaflow @batch vs @kubernetes vs local](../metaflow/notebooks/2026-07-19-batch-vs-kubernetes-vs-local.ipynb) — Compare execution backends for the same flow
- [ZenML parent-child pipelines & lineage](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb) — Hierarchical pipelines and artifact lineage
- [Pipeline orchestration practice exercises](../docs/concepts/pipeline-orchestration/snippets/2026-07-10-pipeline-orchestration-fundamentals.py) — DAG, dependencies, and run order
- [Applying DAG-based ML workflow](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py) — Build and run a DAG-based ML pipeline
- [Kubeflow CI/CD pipeline](../kubeflow/scripts/2026-07-23-kubeflow-ci-cd.sh) — Lint, test, compile, and deploy a pipeline scaffold template

### Version and register models
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md) — MLflow Model Registry version comparison
- [W&B Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md) — Version, register, and promote artifacts
- [Apply model registry: version and promote ML models](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py) — End-to-end registry promotion script (L2)
- [MLflow experiment comparison + promotion script](../mlflow/scripts/experiment-compare-and-promote.py) — Reusable helper for automated experiment comparison and model promotion

### Version data
- [Data versioning fundamentals exercises](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) — Pointer files, snapshots, and restore logic
- [Track dataset snapshots for reproducible training](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py) — Snapshot datasets and pin to training runs
- [DVC end-to-end CLI walkthrough](../dvc/scripts/2026-07-22-dvc-end-to-end.sh) — Init repo, track dataset, set remote, push, and verify cache
- [DVC repro + metrics diff end-to-end](../dvc/scripts/2026-07-28-dvc-repro-metrics-diff.sh) — Run `dvc repro` and compare metrics across commits
- [Minimal DVC versioning](../dvc/snippets/minimal_dvc_versioning.py) — Read a DVC-tracked CSV back into pandas
- [DVC pipeline shell](../dvc/snippets/tried_dvc_pipeline.sh) — Reproduce a tracked pipeline with `dvc repro`
- [Feature store fundamentals exercises](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) — Feature definitions, online/offline, point-in-time joins
- [Writing and reading features from online store](../docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py) — Populate and query an online feature store
- [FastAPI inference endpoint](../docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py) — Serve a model with FastAPI for real-time inference
- [DVC stage pipeline config](../dvc/configs/2026-07-28-dvc-stage-pipeline.yaml) — Minimal DVC stage pipeline with metrics-file layout

### Manage compute and environments
- [Metaflow foreach vs @batch](../metaflow/docs/foreach-vs-batch.md) — Parallelism patterns and execution backends
- [Metaflow AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml) — Batch compute for Metaflow flows
- [Metaflow DevStack compose manifest](../metaflow/manifests/2026-07-13-metaflow-devstack-compose.yaml) — Local Metaflow dev environment with Minikube, Tilt, and Postgres
- [Metaflow custom runtime Docker image](../metaflow/dockerfiles/metaflow-dev.Dockerfile) — CUDA + distributed deps for dev
- [W&B Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml) — Local compute for W&B sweeps
- [Multi-stage ONNX Runtime serving](../docs/concepts/containerization/scripts/2026-07-13-multistage-onnxruntime-serving.py) — Slim serving image from a fat training stage
- [Multi-stage Dockerfile for MLOps](../docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md) — Build-stage training, slim runtime serving image

### Configure a project
- [Kubeflow pipeline project scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md) — CI/CD, unit testing, modular components
- [Kubeflow + MLflow project scaffold](../kubeflow/templates/kubeflow-mlflow-project/README.md) — KFP wired with MLflow tracking
- [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md) — Metaflow with CI/CD, testing, and env management
- [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md) — W&B tracking with GitHub Actions
- [W&B + PyTorch scaffold](../wnb/templates/wandb-pytorch-scaffold/README.md) — PyTorch training with W&B sweep, artifact logging, and CI/CD
- [MLflow project config](../mlflow/configs/mlflow-project.yaml) — Project packaging and entry points
- [MLflow sklearn model serving project](../mlflow/configs/sklearn-model-serving-project.yaml) — Packaged serving project with Conda env and entry points
- [DVC pipeline config](../dvc/configs/pipeline.yaml) — Data and model pipeline stages
- [DVC stage pipeline config](../dvc/configs/2026-07-28-dvc-stage-pipeline.yaml) — Minimal DVC stage pipeline with metrics-file layout
- [MLflow tracking server Postgres+S3](../mlflow/configs/2026-07-14-tracking-server-postgres-s3.yaml) — Production-ready MLflow tracking server with PostgreSQL and S3
- [ZenML stack with MLflow+S3](../zenml/configs/2026-07-12-zenml-stack-mlflow-s3.yaml) — ZenML stack config with MLflow tracking and S3 artifact store

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