# Quick Links

## I need to...

### Set up a tool for the first time
- [Install BentoML and first service](../bentoml/notes/2026-08-22-install-bentoml-and-first-service.md) — First-contact notes for BentoML service setup
- [Install ClearML and first experiment](../clearml/notes/2026-08-22-install-clearml-and-first-experiment.md) — First experiment with ClearML tracking
- [KServe quickstart trip-ups](../kserve/notes/2026-08-22-kserve-quickstart-trip-ups.md) — Gotchas from the KServe quickstart
- [Install ZenML and explore CLI](../zenml/notes/2026-08-22-install-zenml-and-explore-cli.md) — First ZenML CLI exploration
- [MLflow primer](../mlflow/notes/0000-primer-mlflow.md) — Install, run the UI, and log my first experiment
- [W&B primer](../wnb/notes/0000-primer-wnb.md) — SDK setup, first run, and dashboard tour
- [Install W&B and log my first run](../wnb/notes/2026-08-11-install-wandb-and-log-my-first-run.md) — First experiment, first metric, and a tour of the dashboard
- [Kubeflow primer](../kubeflow/notes/0000-primer-kubeflow.md) — Cluster setup, install, and first pipeline
- [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md) — Local install, first flow, and CLI/UI
- [DVC primer](../dvc/notes/0000-primer-dvc.md) — Data versioning setup and first snapshot
- [Install DVC and log first dataset version](../dvc/notes/2026-08-13-install-dvc-and-log-first-dataset-version.md) — First DVC dataset version and tracking walkthrough
- [Feast primer](../feast/notes/0000-primer-feast.md) — Feature store setup and first retrieval
- [KServe primer](../kserve/notes/0000-primer-kserve.md) — Model serving setup and first InferenceService
- [Seldon Core primer](../seldon/notes/0000-primer-seldon-core.md) — Model serving setup and first deploy
- [ClearML primer](../clearml/notes/0000-primer-clearml-orchestration.md) — Orchestration setup and first task
- [ClearML agent first tasks](../clearml/notes/2026-07-23-clearml-agent-first-tasks.md) — Queue, clone, and run a task remotely via clearml-agent CLI
- [ClearML remote GPUs notebook](../clearml/notes/Getting_Started_3_Remote_Execution.ipynb) — First-contact notes for running ClearML tasks on remote GPUs
- [ZenML primer](../zenml/notes/0000-primer-zenml.md) — Stack setup and first pipeline
- [Install KFP on Kind](../kubeflow/notes/2026-07-14-install-kfp-on-kind.md) — Kubeflow Pipelines on a local Kind cluster
- [ClearML common pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md) — Gotchas and workarounds for ClearML
- [Seldon Core vs KServe for sklearn](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md) — Comparing two model-serving frameworks
- [KServe custom predictor with explainer](../kserve/snippets/2026-07-14-custom-predictor-explainer.py) — Custom model predictor and explainer for KServe
- [ClearML remote GPU execution config](../clearml/configs/2026-07-14-remote-gpu-execution.yaml) — Remote GPU execution configuration for ClearML
- [Feast Parquet offline store setup](../feast/notes/2026-07-23-install-feast-parquet-offline-store.md) — Configure a Parquet-backed offline store for feature retrieval
- [Follow Feast quickstart](../feast/notes/2026-08-02-follow-feast-quickstart.md) — Follow the Feast quickstart with feature retrieval and online store setup
- [Online vs offline feature serving](../feast/docs/comparing-online-vs-offline-serving.md) — When to use `get_historical_features()` vs `get_online_features()`
- [Offline vs online stores](../docs/concepts/feature-store/2026-08-09-offline-vs-online-stores.md) — Offline vs online stores and point-in-time joins in Feast

### Set up Databricks
- [Databricks Unity Catalog setup](../databricks/configs/2026-07-14-unity-catalog-setup.yaml) — Unity Catalog configuration for Databricks ML
- [Databricks model promotion to Unity Catalog](../databricks/scripts/2026-07-14-model-promotion-unity-catalog.py) — Promote MLflow models to Unity Catalog

### Run an experiment
- [Install MLflow and log first experiment](../mlf/scripts/2026-08-02-run-first-mlflow-experiment.py) — Install MLflow and log your first experiment with the Python SDK
- [Install MLflow and log first experiment (notes)](../mlf/notes/2026-08-12-install-mlflow-first-experiment.md) — Installing MLflow and logging my first experiment
- [MLflow tracking quickstart](../mlflow/snippets/2026-07-14-mlflow-tracking-quickstart.py) — First experiment with MLflow tracking
- [MLflow end-to-end training with autologging](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — sklearn autolog, model comparison, and registry registration
- [MLflow + W&B hybrid tracking](../mlflow/docs/integrating-mlflow-with-weights-and-biases.md) — Run MLflow and W&B in parallel and synchronize metadata
- [MLflow custom experiment tracking workflow](../mlflow/scripts/custom-experiment-tracking-workflow.py) — Custom workflow with MlflowClient for search, compare, and register
- [MLflow experiment comparison + promotion](../mlflow/scripts/experiment-compare-and-promote.py) — Reusable helper for automated experiment comparison and model promotion
- [MLflow experiment comparison via Search API](../mlflow/notebooks/mlflow-experiment-comparison-search-api.ipynb) — Programmatic experiment comparison with MLflow Search API
- [Log my first W&B metric](../wnb/snippets/2026-08-11-log-my-first-metric.py) — First metric logged with the W&B Python SDK
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py) — Build a sweep from scratch with the Python SDK
- [W&B sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py) — Multi-task sweep and evaluation with CLI subcommands
- [W&B custom sweep with early termination](../wnb/scripts/custom-sweep-early-termination.py) — Custom search space and early-stopping strategy
- [W&B report generator](../wnb/scripts/wandb-report-generator.py) — Generate correlation and parallel-coords reports from W&B sweep runs
- [W&B artifacts deep dive](../wnb/docs/wandb-artifacts-deep-dive.md) — Versioning, lineage, and reuse of artifacts across runs
- [W&B run comparison: parallel coords and correlation diff](../wnb/notebooks/compare-runs-parallel-coords-correlation-diff.ipynb) — Compare runs with parallel coordinates and correlation plots
- [Comparing W&B Artifacts vs MLflow Model Registry](../wnb/notebooks/comparing-wb-artifacts-vs-mlflow-model-registry.ipynb) — Compare artifact lineage and model registry entries across W&B and MLflow
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py) — Data loading, training, and artifact logging
- [ZenML parent-child pipelines and artifact lineage](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb) — Multi-pipeline DAGs and artifact tracking with ZenML
- [Log first pipeline run with ZenML](../zenml/snippets/2026-08-23-log-first-pipeline-run.py) — Minimal ZenML pipeline run with MLflow tracking
- [Evidently first drift report](../evidently/snippets/first_drift_report.py) — Generate and view a data drift report
- [Metaflow Kubernetes flow with metadata tracking](../metaflow/scripts/2026-07-12-kubernetes-flow-metadata-tracking.py) — Run Metaflow on Kubernetes with cloud metadata
- [Feast data source registration and schema inspection](../feast/snippets/2026-07-23-register-data-source-and-inspect-schema.py) — Register a data source and inspect its schema with the Feast Python SDK
- [Feast minimal feature retrieval](../feast/snippets/2026-08-02-minimal-feature-retrieval.py) — Minimal Feast feature retrieval from the online store
- [Register and retrieve features](../docs/concepts/feature-store/scripts/2026-08-09-register-and-retrieve-features.py) — Register features in a local Feast store and retrieve them
- [W&B PyTorch sweep config](../wnb/templates/wandb-pytorch-scaffold/configs/sweep-config.yaml) — Declarative sweep configuration for W&B hyperparameter optimization
- [W&B PyTorch training script](../wnb/templates/wandb-pytorch-scaffold/train.py) — Training script with W&B metric and artifact logging
- [Metaflow event trigger component](../metaflow/templates/metaflow-project-scaffold/components/event_trigger.py) — Event trigger component for Metaflow project scaffold
- [Metaflow schedule config](../metaflow/templates/metaflow-project-scaffold/configs/schedule-config.yaml) — Declarative schedule configuration for Metaflow flows
- [MLflow Kubernetes manifest with Service and Ingress](../mlf/manifests/mlflow-ui-kubernetes.yaml) — Kubernetes manifest for MLflow tracking server with Service and Ingress
- [Metaflow event trigger tests](../metaflow/templates/metaflow-project-scaffold/tests/test_event_trigger.py) — Unit tests for Metaflow event trigger component
- [Experiment tracking workflow](../docs/concepts/experiment-tracking/2026-08-04-experiment-tracking-workflow.md) — End-to-end experiment tracking workflow with MLflow and W&B
- [Experiment tracking patterns and pitfalls](../docs/concepts/experiment-tracking/experiment-tracking-patterns-pitfalls.md) — Common mistakes and anti-patterns in experiment tracking
- [Comparing experiment tracking approaches](../docs/concepts/experiment-tracking/notebooks/comparing-experiment-tracking-approaches.ipynb) — Notebook comparing MLflow and W&B approaches

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
- [Build DAG pipeline](../docs/concepts/pipeline-orchestration/scripts/2026-08-07-build-dag-pipeline.py) — Build and run a DAG-based ML pipeline with step dependencies
- [Simple DAG pipeline](../docs/concepts/pipeline-orchestration/scripts/2026-08-07-simple-dag-pipeline.py) — Minimal DAG-based ML workflow with training, evaluation, and registration
- [DAG pipeline error handling](../docs/concepts/pipeline-orchestration/scripts/dag-pipeline-error-handling.py) — Error handling and retry patterns for DAG-based ML pipelines
- [First flow data transform](../mfl/scripts/2026-08-12-first-flow-data-transform.py) — My first Metaflow flow end-to-end with a simple data transform
- [Kubeflow CI/CD pipeline](../kubeflow/scripts/2026-07-23-kubeflow-ci-cd.sh) — Lint, test, compile, and deploy a pipeline scaffold template
- [Kubeflow pipeline scaffold CI/CD workflow](../kubeflow/manifests/2026-08-02-kubeflow-pipeline-scaffold-ci-cd.yml) — CI/CD workflow for kubeflow-pipeline-scaffold with lint, test, compile, and deploy steps
- [KFP pipeline scaffold CI/CD workflow (kub)](../kub/manifests/kubeflow-pipeline-scaffold-ci-cd.yaml) — CI/CD workflow manifest for KFP pipeline scaffold
- [KFP v2 pipeline conditionals](../kubeflow/scripts/2026-08-04-tried-kfp-v2-pipeline-conditionals.py) — KFP v2 pipeline with conditional branching and parallel execution
- [Install KFP SDK](../kubeflow/snippets/2026-08-04-install-kfp-sdk.py) — Install the KFP SDK and verify the installation
- [KFP v2 branching and parallel pipeline](../kub/scripts/2026-08-07-kfp-v2-branching-parallel-pipeline.py) — KFP v2 pipeline with conditional branching and parallel execution
- [Metaflow scaffold CI/CD workflow](../mfl/configs/2026-08-12-metaflow-project-scaffold-ci-cd.yaml) — CI/CD with lint, test, flow-run, and deploy jobs for the Metaflow template
- [Containerization + pipeline orchestration pattern](../docs/concepts/containerization/docs/containerization-pipeline-orchestration-pattern.md) — Combining containerization with pipeline orchestration for ML workloads
- [Combining containerization with model serving](../docs/concepts/containerization/scripts/combining-containerization-with-model-serving.py) — End-to-end script tying containerization to model serving
- [Pipeline orchestration patterns for production](../docs/concepts/pipeline-orchestration/pipeline-orchestration-patterns-for-production-mlops.md) — Production-grade orchestration patterns for MLOps

### Version and register models
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md) — MLflow Model Registry version comparison
- [W&B Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md) — Version, register, and promote artifacts
- [Apply model registry: version and promote ML models](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py) — End-to-end registry promotion script (L2)
- [MLflow experiment comparison + promotion script](../mlflow/scripts/experiment-compare-and-promote.py) — Reusable helper for automated experiment comparison and model promotion
- [Model versioning workflow](../docs/concepts/model-registry/scripts/2026-08-04-model-versioning-workflow.py) — Model versioning workflow with MLflow Model Registry
- [Automated vs manual model promotion](../docs/concepts/model-registry/automated-vs-manual-promotion.md) — Comparing automated and manual promotion strategies
- [Automated model promotion workflow](../docs/concepts/model-registry/scripts/automated-model-promotion-workflow.py) — Automated promotion script with metric thresholds
- [MLflow Model Registry CI/CD manifest](../mlf/manifests/2026-08-09-mlflow-model-registry-ci-cd.yaml) — CI/CD workflow for MLflow Model Registry promotions
- [MLflow model registry scaffold CI/CD](../mlf/manifests/mlflow-model-registry-scaffold-ci-cd.yaml) — CI/CD workflow for mlflow-model-registry-scaffold with lint, test, train, register, and deploy jobs

### Version data
- [Data versioning fundamentals exercises](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) — Pointer files, snapshots, and restore logic
- [Track dataset snapshots for reproducible training](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py) — Snapshot datasets and pin to training runs
- [DVC end-to-end CLI walkthrough](../dvc/scripts/2026-07-22-dvc-end-to-end.sh) — Init repo, track dataset, set remote, push, and verify cache
- [DVC repro + metrics diff end-to-end](../dvc/scripts/2026-07-28-dvc-repro-metrics-diff.sh) — Run `dvc repro` and compare metrics across commits
- [Minimal DVC versioning](../dvc/snippets/minimal_dvc_versioning.py) — Read a DVC-tracked CSV back into pandas
- [DVC pipeline shell](../dvc/snippets/tried_dvc_pipeline.sh) — Reproduce a tracked pipeline with `dvc repro`
- [DVC-style versioning pipeline](../docs/concepts/data-versioning/scripts/dvc-style-versioning-pipeline.py) — Content-addressed cache, pointer files, and repo stage definitions
- [Feature store fundamentals exercises](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) — Feature definitions, online/offline, point-in-time joins
- [Writing and reading features from online store](../docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py) — Populate and query an online feature store
- [FastAPI inference endpoint](../docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py) — Serve a model with FastAPI for real-time inference
- [Minimal FastAPI inference endpoint](../docs/concepts/model-serving/snippets/2026-08-11-minimal-fastapi-inference-endpoint.py) — Minimal FastAPI endpoint with /health and /predict routes for model serving
- [DVC stage pipeline config](../dvc/configs/2026-07-28-dvc-stage-pipeline.yaml) — Minimal DVC stage pipeline with metrics-file layout
- [Track DVC dataset versions](../docs/concepts/data-versioning/scripts/2026-08-07-track-dvc-versions.py) — Track and version datasets with DVC for reproducible training
- [DVC dataset versioning](../docs/concepts/data-versioning/scripts/2026-08-07-dvc-dataset-versioning.py) — Version datasets and pin them to training runs with DVC
- [Track dataset versions with DVC and reproduce a training run](../docs/concepts/data-versioning/scripts/2026-08-08-track-dataset-versions-with-dvc-and-reproduce-a-training-run.py) — End-to-end demo tracking a dataset, mutating it, and restoring the original version
- [Snapshot vs diff versioning](../docs/concepts/data-versioning/snapshot-vs-diff-versioning.md) — Comparing versioning strategies for ML datasets

### Monitor models and drift
- [Monitoring and drift detection patterns](../docs/concepts/monitoring-drift/2026-08-11-monitoring-drift-patterns.md) — Baseline snapshots, scheduled checks, threshold alerting, and retraining triggers
- [Data drift detection script](../docs/concepts/monitoring-drift/scripts/2026-08-11-data-drift-detection.py) — Z-score comparison of features against a reference baseline
- [Evidently report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md) — Choosing between Evidently's two check styles

### Manage compute and environments
- [Metaflow foreach vs @batch](../metaflow/docs/foreach-vs-batch.md) — Parallelism patterns and execution backends
- [Metaflow AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml) — Batch compute for Metaflow flows
- [Metaflow DevStack compose manifest](../metaflow/manifests/2026-07-13-metaflow-devstack-compose.yaml) — Local Metaflow dev environment with Minikube, Tilt, and Postgres
- [Metaflow custom runtime Docker image](../metaflow/dockerfiles/metaflow-dev.Dockerfile) — CUDA + distributed deps for dev
- [W&B Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml) — Local compute for W&B sweeps
- [Multi-stage ONNX Runtime serving](../docs/concepts/containerization/scripts/2026-07-13-multistage-onnxruntime-serving.py) — Slim serving image from a fat training stage
- [Multi-stage Dockerfile for MLOps](../docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md) — Build-stage training, slim runtime serving image
- [Multistage Dockerfile for ML](../docs/concepts/containerization/scripts/2026-08-09-multistage-dockerfile-for-ml.sh) — Multi-stage Dockerfile for ML training and serving
- [Containerization serving entrypoint](../docs/concepts/containerization/serve.py) — Minimal serving entrypoint for multi-stage Docker workflows
- [Containerization training entrypoint](../docs/concepts/containerization/train.py) — Minimal training entrypoint for multi-stage Docker workflows
- [Containerization dependency list](../docs/concepts/containerization/requirements.txt) — Training and serving dependency lists for multi-stage builds
- [Containerization serving notes](../docs/concepts/containerization/serve.txt) — Quick reference for serving container setup
- [Containerization base config](../docs/concepts/containerization/config.yaml) — Base image and dependency config for ML container builds
- [Production Metaflow Argo deployment](../metaflow/manifests/production-metaflow-argo-deployment.yaml) — Argo Workflows deployment manifest for production Metaflow
- [Batch vs Kubernetes vs local](../metaflow/notebooks/2026-07-19-batch-vs-kubernetes-vs-local-alt.ipynb) — Compare execution backends for the same Metaflow flow

### Configure a project
- [Kubeflow pipeline project scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md) — CI/CD, unit testing, modular components
- [Kubeflow + MLflow project scaffold](../kubeflow/templates/kubeflow-mlflow-project/README.md) — KFP wired with MLflow tracking
- [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md) — Metaflow with CI/CD, testing, and env management
- [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md) — W&B tracking with GitHub Actions
- [W&B + PyTorch scaffold](../wnb/templates/wandb-pytorch-scaffold/README.md) — PyTorch training with W&B sweep, artifact logging, and CI/CD
- [W&B + PyTorch CI/CD scaffold](../wnb/templates/wandb-pytorch-ci-scaffold/README.md) — PyTorch training with W&B sweep and CI/CD
- [MLflow project config](../mlflow/configs/mlflow-project.yaml) — Project packaging and entry points
- [MLflow sklearn model serving project](../mlflow/configs/sklearn-model-serving-project.yaml) — Packaged serving project with Conda env and entry points
- [DVC pipeline config](../dvc/configs/pipeline.yaml) — Data and model pipeline stages
- [MLflow tracking server Postgres+S3](../mlflow/configs/2026-07-14-tracking-server-postgres-s3.yaml) — Production-ready MLflow tracking server with PostgreSQL and S3
- [MLflow tracking server Postgres+MinIO](../mlflow/dockerfiles/tracking-server-postgres-minio/README.md) — Self-hosted MLflow server via Docker Compose
- [ZenML stack with MLflow+S3](../zenml/configs/2026-07-12-zenml-stack-mlflow-s3.yaml) — ZenML stack config with MLflow tracking and S3 artifact store
- [Feast feature store Redis Parquet config](../feast/configs/2026-08-02-feast-feature-store-redis-parquet.yaml) — Feast config with Redis online store and Parquet offline store
- [KFP pipeline deployment manifest](../kub/manifests/2026-08-06-kfp-pipeline-deployment-manifest.yaml) — KFP pipeline deployment manifest for production
- [SeldonDeployment manifest](../seldon/manifests/seldondeployment.yaml) — Minimal sklearn SeldonDeployment manifest
- [Minimal pipeline config for ZenML](../zenml/configs/2026-08-23-minimal-pipeline-config.yaml) — ZenML pipeline configuration with MLflow integration

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
