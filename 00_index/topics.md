# Topics

## DVC
- [primer] `dvc/notes/0000-primer-dvc.md` — DVC concepts, setup, and first steps
- [notes] `dvc/notes/2026-05-26-first-dataset-version.md` — Versioning a dataset with DVC
- [notes] `dvc/notes/2026-06-05-get-started.md` — Following the official DVC Get Started guide and documenting trip-ups
- [config] `dvc/configs/pipeline.yaml` — DVC pipeline definition with stages, dependencies, and outputs
- [script] `dvc/scripts/tried_init_dvc_and_track_dataset.sh` — Initialize a DVC project and track a dataset
- [snippet] `dvc/snippets/tried_dvc_pipeline.sh` — Shell snippet for a DVC pipeline run
- [snippet] `dvc/snippets/minimal_dvc_versioning.py` — Minimal data versioning with DVC Python API

## Feast
- [primer] `feast/notes/0000-primer-feast.md` — Feast overview and key concepts
- [notes] `feast/notes/2026-06-03-install-feast-first-feature-retrieval.md` — Installing Feast and running first feature retrieval
- [snippet] `feast/snippets/tried_first_feature_view.py` — Define and apply a first feature view

## General
- [docs] `General/docs/2026-06-06-added-dot-git-folder-to-layout.md` — Added .git/ to README Layout section
- [docs] `General/docs/2026-06-06-added-feast-folder-to-layout.md` — Added feast/ to README Layout section
- [docs] `General/docs/2026-06-06-added-readme-md-to-layout.md` — Documented README.md in README Layout section
- [docs] `General/docs/2026-06-06-document-changelog-in-readme.md` — Documented CHANGELOG.md in README Layout section
- [docs] `General/docs/2026-06-07-document-general-folder-in-readme.md` — Documented General/ in README Layout section

## Kubeflow
- [primer] `kubeflow/notes/0000-primer-kubeflow.md` — Kubeflow overview and architecture
- [notes] `kubeflow/notes/2026-05-25-install-kubeflow-and-explore-ui.md` — Kubeflow installation and UI walkthrough
- [notes] `kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md` — Setting up a local Kind cluster for Kubeflow
- [notes] `kubeflow/notes/2026-05-27-pipelines-quickstart-trip-ups.md` — Kubeflow Pipelines quickstart trip-ups
- [notes] `kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md` — Installing Kubeflow on a Kind cluster
- [notes] `kubeflow/notes/2026-06-06-explore-central-dashboard.md` — First walk through the Kubeflow Central Dashboard
- [notes] `kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md` — Installing minikube and Kubeflow CLI, verifying local setup
- [config] `kubeflow/configs/pipeline-resources.yaml` — Pipeline resource requests and limits
- [manifest] `kubeflow/manifests/minimal-hello-pipeline.yaml` — Minimal hello-world pipeline manifest
- [script] `kubeflow/scripts/tried_check_kubeflow_readiness.sh` — Verify Kubeflow component readiness
- [script] `kubeflow/scripts/tried_diagnosing_kubeflow_health.sh` — Diagnosing Kubeflow backend service health
- [snippet] `kubeflow/snippets/tried_deploy_first_pipeline.py` — Deploy and run a Kubeflow pipeline via SDK
- [snippet] `kubeflow/snippets/tried_pipeline_v2_sdk.py` — Minimal pipeline with Kubeflow Pipelines V2 SDK

## Metaflow
- [primer] `metaflow/notes/0000-primer-metaflow.md` — Metaflow primer and key concepts
- [notes] `metaflow/notes/2026-05-27-first-end-to-end-flow.md` — Running a first end-to-end Metaflow flow
- [notes] `metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md` — Metaflow quickstart trip-ups and gotchas
- [notes] `metaflow/notes/2026-05-30-install-metaflow-and-setup-dev-env.md` — Installing Metaflow and setting up dev environment
- [notes] `metaflow/notes/2026-06-05-first-flow-end-to-end.md` — Installing Metaflow and running a first flow end-to-end
- [notes] `metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md` — Exploring Metaflow UI and inspecting a completed run
- [notes] `metaflow/notes/2026-06-06-revisiting-quickstart.md` — Second pass through the Metaflow quickstart
- [config] `metaflow/configs/metaflow-project-scaffold.yaml` — Project scaffold configuration for Metaflow
- [notebook] `metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb` — End-to-end Metaflow flow with data and decisions
- [snippet] `metaflow/snippets/2026-06-06-minimal-first-flow.py` — Minimal first flow with Metaflow Python SDK
- [snippet] `metaflow/snippets/tried_first_linear_dag.py` — Minimal linear DAG with parameters
- [snippet] `metaflow/snippets/tried_parameterized_dag.py` — Parameterized DAG with branching and merging
- [snippet] `metaflow/snippets/tried_serving_model.py` — Minimal model serving with Metaflow Python API

## MLflow
- [primer] `mlflow/notes/0000-primer-mlflow.md` — MLflow concepts and setup
- [notes] `mlflow/notes/2026-05-24-first-mlflow-server.md` — Running MLflow server for the first time
- [notes] `mlflow/notes/2026-05-27-install-mlflow-first-run.md` — Installing MLflow and running a first tracking experiment
- [notes] `mlflow/notes/2026-05-27-mlflow-quickstart-trip-ups.md` — MLflow quickstart trip-ups
- [notes] `mlflow/notes/2026-05-28-mlflow-tracking-quickstart-trip-ups.md` — MLflow Tracking quickstart trip-ups
- [config] `mlflow/configs/MLproject` — MLflow Project definition with entry points
- [config] `mlflow/configs/conda.yaml` — Conda environment for MLflow Project
- [config] `mlflow/configs/mlflow-project.yaml` — Alternative MLflow Project configuration
- [docs] `mlflow/docs/comparing-model-versions.md` — Comparing registered model versions with Model Registry
- [notebook] `mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb` — Side-by-side comparison of autologging and manual tracking
- [script] `mlflow/scripts/custom_model_flavor.py` — Building a custom MLflow model flavor
- [snippet] `mlflow/snippets/2026-05-26-autolog_and_register.py` — Autologging and model registry example
- [snippet] `mlflow/snippets/log_first_run.py` — Logging a first MLflow run
- [snippet] `mlflow/snippets/tried_logging_metrics.py` — Logging first metrics and parameters with MLflow Tracking

## Weights & Biases
- [primer] `wnb/notes/0000-primer-wnb.md` — W&B primer and setup
- [notes] `wnb/notes/2026-05-25-install-wandb-and-first-run.md` — Installing wandb and first experiment
- [notes] `wnb/notes/2026-05-27-install-wandb-first-experiment.md` — Installing W&B and running a first experiment tracking
- [notes] `wnb/notes/2026-05-31-first-wandb-experiment-tracking.md` — First W&B experiment tracking session
- [notes] `wnb/notes/2026-06-01-my-first-wandb-session.md` — My first W&B tracking session
- [notes] `wnb/notes/2026-06-05-configure-wandb-first-team-experiment.md` — Configuring W&B settings and running a first team experiment
- [notes] `wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md` — Following the official W&B quickstart and documenting trip-ups
- [notes] `wnb/notes/2026-06-06-train-model-and-review-dashboard.md` — Training a model with W&B and reviewing the dashboard
- [config] `wnb/configs/2026-06-08-first-sweep-config.yaml` — First hyperparameter sweep config with Bayesian optimization
- [config] `wnb/configs/project-settings.yaml` — W&B project settings and tracking environment
- [config] `wnb/configs/sweep_config.yaml` — W&B hyperparameter sweep configuration
- [docs] `wnb/docs/wandb-quickstart-trip-ups.md` — W&B quickstart trip-ups
- [script] `wnb/scripts/train_small_model_with_wandb.py` — Training script instrumented with W&B
- [snippet] `wnb/snippets/2026-06-06-minimal-tracking.py` — Minimal experiment tracking with W&B Python API
- [snippet] `wnb/snippets/log_metrics_and_artifacts.py` — Logging metrics and artifacts with W&B SDK
- [snippet] `wnb/snippets/tried_first_metrics_and_config.py` — First metrics and config logging experiment
- [snippet] `wnb/snippets/tried_logging_first_run.py` — First run logging with W&B
- [snippet] `wnb/snippets/tried_logging_metrics_and_params.py` — Logging first metrics and parameters with W&B
