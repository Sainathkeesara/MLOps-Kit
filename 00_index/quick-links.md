# Quick Links

## I need to...

### Set up a tool for the first time
- [ClearML Orchestration primer](../clearml/notes/0000-primer-clearml-orchestration.md)
- [ClearML install and first task](../clearml/snippets/tried_install_and_first_task.py)
- [ClearML Web UI exploration](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md)
- [ZenML primer](../zenml/notes/0000-primer-zenml.md)
- [ZenML dashboard and first stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md)
- [DVC primer](../dvc/notes/0000-primer-dvc.md)
- [DVC get started trip-ups](../dvc/notes/2026-06-05-get-started.md)
- [Feast primer](../feast/notes/0000-primer-feast.md)
- [Feast install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- [KServe primer](../kserve/notes/0000-primer-kserve.md)
- [Kubeflow primer](../kubeflow/notes/0000-primer-kubeflow.md)
- [Kubeflow install verification](../kubeflow/snippets/2026-07-06-verify-kfp-install.py) — Verify kfp install and compile my first KFP pipeline
- [Kubeflow install and explore UI](../kubeflow/notes/2026-05-25-install-kubeflow-and-explore-ui.md)
- [Kubeflow Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md)
- [Kubeflow install on Kind](../kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md)
- [Kubeflow minikube and CLI setup](../kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md)
- [KFP v2 quickstart trip-ups](../kubeflow/notes/2026-07-06-kfp-v2-quickstart-trip-ups.md) — Following the official KFP v2 quickstart and what tripped me up
- [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- [Metaflow install and first flow](../metaflow/snippets/2026-07-06-install-first-flow.py) — Install Metaflow and run my first flow locally
- [Metaflow CLI and local dev UI](../metaflow/notes/2026-07-09-explore-cli-local-dev-ui.md) — Explore Metaflow's CLI and local development UI
- [Metaflow install and dev environment setup](../metaflow/notes/2026-05-30-install-metaflow-and-setup-dev-env.md)
- [MLflow primer](../mlflow/notes/0000-primer-mlflow.md)
- [MLflow server setup](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- [MLflow tracking server with Nginx auth proxy](../mlflow/docs/production-tracking-server-nginx-auth.md)
- [Evidently AI primer](../evidently/notes/0000-primer-evidently.md)
- [Evidently Report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md)
- [W&B primer](../wnb/notes/0000-primer-wnb.md)
- [W&B first experiment (SDK)](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py) — Log my first experiment with W&B Python SDK
- [W&B quickstart trip-ups (July 2026)](../wnb/notes/2026-07-10-wandb-quickstart-trip-ups.md) — Following the official W&B quickstart and what tripped me up
- [W&B minimal hyperparameter sweep](../wnb/snippets/2026-07-10-minimal-hyperparameter-sweep.py) — Minimal hyperparameter sweep with W&B Python SDK
- [Seldon Core primer](../seldon/notes/0000-primer-seldon-core.md)

### Run an experiment
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py) — First ZenML pipeline with data loading and model training
- [Evidently first drift report](../evidently/snippets/first_drift_report.py) — Install Evidently and generate a first data drift report
- [Kubeflow Pipelines + MLflow tracking integration](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md) — Wire KFP pipeline components to an in-cluster MLflow tracking server
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py) — Build a hyperparameter sweep with W&B from scratch
- [W&B sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py) — Reusable sweep and evaluation pipeline with sklearn support, CLI subcommands, and multi-task (classification/regression) training
- [Custom MLflow model flavor](../mlflow/scripts/custom_model_flavor.py) — Build a custom pyfunc model flavor from scratch
- [KServe first InferenceService](../kserve/snippets/first_inferenceservice.py) — Install KServe and deploy my first InferenceService (L1)
- [Kubeflow backend health check](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- [Kubeflow component readiness check](../kubeflow/scripts/tried_check_kubeflow_readiness.sh)
- [Kubeflow component factory](../kubeflow/scripts/component_factory.py) — Reusable KFP component factory with resource config and caching
- [Kubeflow Central Dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md) — First walk through the Kubeflow Central Dashboard
- [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md) — KFP v2 SDK surprises during component writing and pipeline compilation
- [KFP component factory](../kubeflow/scripts/kfp_component_factory.py) — Reusable component factory with resource configuration and caching policy (L4)
- [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md) — Diagnose infrastructure failures and pod log issues in KFP pipelines
- [KFP v1 vs v2 DSL migration guide](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md) — Compare KFP v1 and v2 DSLs, document breaking changes, and migration patterns for upgrading pipelines
- [Metaflow end-to-end flow](../metaflow/notes/2026-05-27-first-end-to-end-flow.md)
- [Metaflow UI exploration](../metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md)
- [Metaflow data + decision flow](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb)
- [Metaflow full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb) — Compare a fresh run against a resumed run during iterative model development
- [Metaflow minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- [Metaflow 5-step ML pipeline](../metaflow/scripts/2026-06-12-five-step-ml-pipeline.py) — End-to-end pipeline: load → clean → feature engineering → train → evaluate
- [Metaflow end-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py) — Experiment with Metaflow tracking, model logging, and run comparison via Client API (L2)
- [Metaflow batch inference splits](../metaflow/scripts/batch_inference_splits.py) — Reusable Metaflow flow for sharded batch inference with `--splits` and `@batch`
- [Metaflow first flow with branching, retry, and foreach](../metaflow/snippets/2026-07-09-first-flow-branching-retry-foreach.py) — Build my first Metaflow flow combining branching, retry, and foreach
- [MLflow model serving](../mlflow/snippets/tried_serving_a_model.py) — Train, log, load, and serve predictions via the Python API
- [MLflow install and first experiment](../mlflow/snippets/tried_installing_mlflow_first_experiment.py) — Install MLflow and log my first experiment with the Python SDK
- [MLflow install and first run snippet](../mlflow/snippets/tried_install_and_log_first_run.py) — Install MLflow and log first run with params and metrics
- [MLflow autologging pipeline](../mlflow/snippets/2026-06-10-autologging-pipeline.py) — Training pipeline with autologging enabled
- [MLflow autolog and register](../mlflow/snippets/2026-05-26-autolog_and_register.py)
- [MLflow install and first run](../mlflow/notes/2026-05-27-install-mlflow-first-run.md)
- [MLflow UI exploration notes](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md) — First walk through the MLflow UI: runs, parameters, metrics, and compare mode
- [MLflow quickstart trip-ups (July 2026)](../mlflow/notes/2026-07-01-mlflow-quickstart-trip-ups.md) — Following the official MLflow quickstart and what tripped me up
- [MLflow autolog training snippet](../mlflow/snippets/tried_autolog_training.py) — Minimal model training with MLflow autologging (L2)
- [MLflow first run](../mlflow/snippets/log_first_run.py)
- [MLflow metrics demo](../mlflow/snippets/tried_logging_metrics.py)
- [MLflow minimal model serving](../mlflow/snippets/2026-06-10-minimal-model-serving.py) — Load a saved model and serve predictions with MLflow Python API
- [MLflow exploring runs, experiments, and model registry](../mlflow/notebooks/2026-07-09-exploring-runs-experiments-and-model-registry.ipynb) — Interactive exploration of runs, experiments, and Model Registry stages
- [MLflow autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb) — Side-by-side comparison of two tracking approaches
- [MLflow end-to-end training with autologging](../mlflow/snippets/tried_end_to_end_training.py) — Build an end-to-end training pipeline with MLflow autologging
- [MLflow autologging pipeline (wine)](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — End-to-end training pipeline with sklearn autolog, model comparison, and Model Registry registration
- [W&B training script](../wnb/scripts/train_small_model_with_wandb.py)
- [W&B metrics and params snippet](../wnb/snippets/tried_logging_metrics_and_params.py)
- [W&B first metrics and config snippet](../wnb/snippets/tried_first_metrics_and_config.py)
- [W&B minimal tracking snippet](../wnb/snippets/2026-06-06-minimal-tracking.py) — Minimal experiment tracking with W&B
- [W&B first run snippet](../wnb/snippets/tried_logging_first_run.py)
- [W&B first run with config snippet](../wnb/snippets/tried_first_wandb_run_with_config.py) — Log my first W&B run with metrics and config dict
- [W&B artifact logging snippet](../wnb/snippets/tried_artifact_logging.py) — Save and log model and dataset artifacts with wandb.Artifact
- [W&B artifact tracking in a data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md) — Link raw data, processed data, and model artifacts to a pipeline run
- [W&B metrics and artifacts snippet](../wnb/snippets/log_metrics_and_artifacts.py)
- [MLflow end-to-end experiment (Jul 6)](../mlflow/scripts/2026-07-06-end-to-end-experiment.py) — Full experiment cycle: tracking, model logging, registry registration, and stage promotion
- [MLflow experiment with tracking (Jul 5)](../mlflow/scripts/2026-07-05-end-to-end-experiment.py) — MLflow tracking with model logging and run comparison
- [MLflow end-to-end training with autologging](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py)
- [MLflow autologging pipeline](../mlflow/snippets/2026-06-10-autologging-pipeline.py)
- [MLflow autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb)
- [MLflow UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md)
- [Custom MLflow model flavor](../mlflow/scripts/custom_model_flavor.py)
- [W&B dashboard exploration](../wnb/notes/2026-07-09-explore-wandb-dashboard.md) — Exploring W&B dashboard after first experiments
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py)
- [W&B sweep and eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py)
- [W&B sweep config vs Python API](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb)
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py)
- [Evidently first drift report](../evidently/snippets/first_drift_report.py)
- [KServe first InferenceService](../kserve/snippets/first_inferenceservice.py)
- [Seldon Core install and first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py)
- [Kubeflow Pipelines + MLflow tracking integration](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md)
- [Kubeflow Central Dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md)
- [Kubeflow Central Dashboard re-exploration](../kubeflow/notes/2026-07-06-explore-central-dashboard-again.md) — Second pass: app tiles, subprojects, and what tripped me up
- [Kubeflow component factory](../kubeflow/scripts/component_factory.py)
- [KFP component factory](../kubeflow/scripts/kfp_component_factory.py)
- [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md)
- [KFP v1 vs v2 DSL migration guide](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md)
- [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md)
- [Katib vs ParallelFor for HP tuning](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb)
- [Metaflow end-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py)
- [Metaflow five-step ML pipeline](../metaflow/scripts/2026-06-12-five-step-ml-pipeline.py)
- [Metaflow batch inference splits](../metaflow/scripts/batch_inference_splits.py)
- [Metaflow full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb)
- [Metaflow CI/CD with GitHub Actions](../metaflow/notes/2026-06-12-ci-cd-with-github-actions.md)
- [DVC pipeline](../dvc/snippets/tried_dvc_pipeline.sh)
- [DVC minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py)

### Define features
- [My first feature view with Feast](../feast/snippets/tried_first_feature_view.py)
- [Feast feature store config](../feast/configs/feature_store.yaml)
- [Feature store practice: feature definitions, online/offline, point-in-time join](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) — Feature store fundamentals exercises (L2)

### Register and promote models
- [W&B Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md)
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md)
- [Apply model registry: version and promote ML models](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py) — Version and promote models with MLflow registry (L2)

### Manage compute and environments
- [Metaflow resource management](../metaflow/docs/metaflow-resource-management.md)
- [Metaflow foreach vs @batch](../metaflow/docs/foreach-vs-batch.md)
- [Metaflow + W&B integration](../metaflow/docs/metaflow-wandb-integration.md)
- [Metaflow custom runtime Docker image](../metaflow/dockerfiles/metaflow-dev.Dockerfile) — CUDA + distributed deps for Metaflow dev environment
- [W&B Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml)
- [Metaflow AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml)

### Configure a project
- [Kubeflow pipeline project scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md) — Template project with CI/CD, unit testing, and modular components
- [Kubeflow + MLflow project scaffold](../kubeflow/templates/kubeflow-mlflow-project/README.md) — Template wiring KFP with MLflow experiment tracking
- [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md) — Template wiring Metaflow with CI/CD, testing, and environment management
- [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md) — Template wiring W&B tracking with GitHub Actions CI/CD pipeline
- [MLflow project config](../mlflow/configs/mlflow-project.yaml)
- [MLflow MLproject + conda env](../mlflow/configs/MLproject)
- [KServe minimal InferenceService YAML](../kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml)
- [Kubeflow pipeline resources config](../kubeflow/configs/pipeline-resources.yaml)
- [DVC pipeline config](../dvc/configs/pipeline.yaml)
- [MLflow tracking server config (SQLite)](../mlflow/configs/mlflow_tracking.yaml)
- [MLflow tracking server config (SQLite + S3)](../mlflow/configs/2026-07-01-tracking-server-s3.yaml)
- [MLflow tracking server config (Postgres + S3)](../mlflow/configs/2026-07-06-tracking-server-postgres-s3.yaml) — Tracking server config with Postgres backend and S3 artifacts
- [ZenML stack config](../zenml/configs/zenml-stack.yaml)
- [Metaflow project scaffold config](../metaflow/configs/metaflow-project-scaffold.yaml)

### Version data
- [DVC init and first dataset track](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- [DVC first dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)
- [Data versioning practice: pointer files and snapshots](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) — Data versioning fundamentals exercises (L2)
- [Track dataset snapshots for reproducible training](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py) — Snapshot datasets and pin versions to training runs (L2)

### Learn foundational concepts
- [Experiment Tracking primer](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md)
- [Model Registry primer](../docs/concepts/model-registry/0000-primer-model-registry.md)
- [Data Versioning primer](../docs/concepts/data-versioning/0000-primer-data-versioning.md)
- [Pipeline Orchestration primer](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md)
- [Feature Store primer](../docs/concepts/feature-store/0000-primer-feature-store.md)
- [Model Serving primer](../docs/concepts/model-serving/0000-primer-model-serving.md)
- [Containerization primer](../docs/concepts/containerization/0000-primer-containerization.md)
- [Monitoring & Drift primer](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md)
- [Pipeline orchestration practice: DAG and run order exercises](../docs/concepts/pipeline-orchestration/snippets/2026-07-10-pipeline-orchestration-fundamentals.py) — Pipeline orchestration fundamentals exercises (L2)
- [Applying pipeline orchestration with a DAG-based ML workflow](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py) — Build and run a DAG-based ML pipeline (L2)

## Project
- [README](../README.md) — Project overview and repository structure
- [CHANGELOG](../CHANGELOG.md) — Record of completed tasks
