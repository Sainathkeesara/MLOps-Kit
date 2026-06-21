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
- [config] `feast/configs/feature_store.yaml` — Feature store configuration with SQLite online store
- [config] `feast/configs/README.md` — Feast configs directory overview
- [snippet] `feast/snippets/tried_first_feature_view.py` — Define and apply a first feature view

## General
- [docs] `General/docs/2026-06-06-added-dot-git-folder-to-layout.md` — Added .git/ to README Layout section
- [docs] `General/docs/2026-06-06-added-feast-folder-to-layout.md` — Added feast/ to README Layout section
- [docs] `General/docs/2026-06-06-added-readme-md-to-layout.md` — Documented README.md in README Layout section
- [docs] `General/docs/2026-06-06-document-changelog-in-readme.md` — Documented CHANGELOG.md in README Layout section
- [docs] `General/docs/2026-06-07-document-general-folder-in-readme.md` — Documented General/ in README Layout section
- [docs] `General/docs/2026-06-08-document-feast-folder-in-readme.md` — Documented feast/ in README Layout and Coverage sections
- [docs] `General/docs/2026-06-09-document-feast-configs-in-readme.md` — Documented feast/configs/ in README Layout section
- [docs] `General/docs/2026-06-13-changelog-in-readme-layout.md` — Added CHANGELOG.md to README Layout section
- [docs] `General/docs/2026-06-13-document-00-index-folder-in-readme.md` — Documented 00_index/ in README Layout section
- [docs] `General/docs/2026-06-14-document-dvc-configs-in-readme.md` — Documented dvc/configs/ in README Layout and Coverage sections
- [docs] `General/docs/2026-06-14-empty-root-item-pass.md` — Second pass on empty root-item task text
- [docs] `General/docs/2026-06-14-readme-md-layout-pass.md` — Confirmed README.md entry and aligned README counts
- [docs] `General/docs/2026-06-14-root-layout-audit.md` — Checked actual root entries and made .git/ / dvc/configs/ visible in README

## Kubeflow
- [primer] `kubeflow/notes/0000-primer-kubeflow.md` — Kubeflow overview and architecture
- [notes] `kubeflow/notes/2026-05-25-install-kubeflow-and-explore-ui.md` — Kubeflow installation and UI walkthrough
- [notes] `kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md` — Setting up a local Kind cluster for Kubeflow
- [notes] `kubeflow/notes/2026-05-27-pipelines-quickstart-trip-ups.md` — Kubeflow Pipelines quickstart trip-ups
- [notes] `kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md` — Installing Kubeflow on a Kind cluster
- [notes] `kubeflow/notes/2026-06-06-explore-central-dashboard.md` — First walk through the Kubeflow Central Dashboard
- [notes] `kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md` — Installing minikube and Kubeflow CLI, verifying local setup
- [notes] `kubeflow/notes/2026-06-08-kubeflow-pipelines-quickstart-trip-ups.md` — Kubeflow Pipelines quickstart second pass trip-ups
- [notes] `kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md` — KFP v2 SDK surprises during component writing and pipeline compilation
- [notes] `kubeflow/notes/2026-06-09-kubeflow-pipelines-quickstart-trip-ups.md` — Kubeflow Pipelines quickstart third pass trip-ups
- [config] `kubeflow/configs/pipeline-resources.yaml` — Pipeline resource requests and limits
- [docs] `kubeflow/docs/kubeflow-pipeline-debugging.md` — Diagnose infrastructure failures and pod log issues in KFP pipelines
- [manifest] `kubeflow/manifests/minimal-hello-pipeline.yaml` — Minimal hello-world pipeline manifest
- [manifest] `kubeflow/manifests/2026-06-08-pipeline-job-set.yaml` — Multi-component pipeline (prep, train, evaluate) as a Kubernetes Job set
- [notebook] `kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb` — Compare Katib managed tuning vs custom ParallelFor grid search for KFP hyperparameter optimization
- [script] `kubeflow/scripts/tried_check_kubeflow_readiness.sh` — Verify Kubeflow component readiness
- [script] `kubeflow/scripts/tried_diagnosing_kubeflow_health.sh` — Diagnosing Kubeflow backend service health
- [snippet] `kubeflow/snippets/tried_deploy_first_pipeline.py` — Deploy and run a Kubeflow pipeline via SDK
- [snippet] `kubeflow/snippets/tried_pipeline_v2_sdk.py` — Minimal pipeline with Kubeflow Pipelines V2 SDK
- [snippet] `kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py` — Minimal KFP v2 pipeline with data prep, train, and evaluate steps
- [snippet] `kubeflow/snippets/2026-06-14-tried_kfp_v2_minimal.py` — Minimal KFP v2 pipeline with add + multiply arithmetic steps
- [snippet] `kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py` — Pipeline with conditional deploy/retrain branching and per-component resource constraints
- [snippet] `kubeflow/snippets/tried_my_first_component.py` — My first Kubeflow Pipelines component — just adds two numbers
- [snippet] `kubeflow/snippets/2026-06-14-tried_kfp_v2_minimal.py` — Minimal KFP v2 pipeline with add + multiply arithmetic steps
- [snippet] `kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py` — Pipeline with conditional deploy/retrain branching and per-component resource constraints
- [dockerfile] `kubeflow/dockerfiles/requirements.txt` — Python dependencies for custom KFP component Docker image
- [dockerfile] `kubeflow/dockerfiles/sklearn-train-component.Dockerfile` — Build a custom container component with RandomForest training
- [dockerfile] `kubeflow/dockerfiles/train.py` — Training script used in the custom KFP Dockerfile component
- [notebook] `kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb` — Compare Katib managed tuning vs custom ParallelFor grid search for KFP hyperparameter optimization
- [template] `kubeflow/templates/kubeflow-mlflow-project/README.md` — Template project wiring KFP pipelines with MLflow experiment tracking
- [template] `kubeflow/templates/kubeflow-mlflow-project/components/__init__.py` — Template component package init
- [template] `kubeflow/templates/kubeflow-mlflow-project/components/evaluate.py` — Template evaluation component
- [template] `kubeflow/templates/kubeflow-mlflow-project/components/train.py` — Template training component
- [template] `kubeflow/templates/kubeflow-mlflow-project/configs/mlflow-config.yaml` — Template MLflow configuration for KFP project
- [template] `kubeflow/templates/kubeflow-mlflow-project/pipeline.py` — Template KFP pipeline definition
- [template] `kubeflow/templates/kubeflow-mlflow-project/requirements.txt` — Template project Python dependencies
- [template] `kubeflow/templates/kubeflow-mlflow-project/run.py` — Template pipeline runner script

## Metaflow
- [primer] `metaflow/notes/0000-primer-metaflow.md` — Metaflow primer and key concepts
- [notes] `metaflow/notes/2026-05-27-first-end-to-end-flow.md` — Running a first end-to-end Metaflow flow
- [notes] `metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md` — Metaflow quickstart trip-ups and gotchas
- [notes] `metaflow/notes/2026-05-30-install-metaflow-and-setup-dev-env.md` — Installing Metaflow and setting up dev environment
- [notes] `metaflow/notes/2026-06-05-first-flow-end-to-end.md` — Installing Metaflow and running a first flow end-to-end
- [notes] `metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md` — Exploring Metaflow UI and inspecting a completed run
- [notes] `metaflow/notes/2026-06-06-revisiting-quickstart.md` — Second pass through the Metaflow quickstart
- [notes] `metaflow/notes/2026-06-08-step-decorator-dag-ordering.md` — How Metaflow builds and enforces the DAG through `self.next()` calls
- [notes] `metaflow/notes/2026-06-12-ci-cd-with-github-actions.md` — Wiring Metaflow flows into a GitHub Actions CI/CD pipeline
- [config] `metaflow/configs/metaflow-project-scaffold.yaml` — Project scaffold configuration for Metaflow
- [docs] `metaflow/docs/metaflow-resource-management.md` — Pin dependencies with @conda, request CPU/memory/GPU with @resources, and set step timeouts
- [notebook] `metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb` — End-to-end Metaflow flow with data and decisions
- [notebook] `metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb` — Compare a fresh run against a resumed run during iterative model development
- [script] `metaflow/scripts/2026-06-12-five-step-ml-pipeline.py` — End-to-end pipeline: load, clean, feature engineering, train, evaluate
- [snippet] `metaflow/snippets/2026-06-06-minimal-first-flow.py` — Minimal first flow with Metaflow Python SDK
- [snippet] `metaflow/snippets/tried_first_linear_dag.py` — Minimal linear DAG with parameters
- [snippet] `metaflow/snippets/tried_parameterized_dag.py` — Parameterized DAG with branching and merging
- [snippet] `metaflow/snippets/tried_parameterizing_a_flow.py` — Pass runtime config via @parameters decorator
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
- [config] `mlflow/configs/mlflow_tracking.yaml` — Local backend store configuration for MLflow Tracking server
- [docs] `mlflow/docs/comparing-model-versions.md` — Comparing registered model versions with Model Registry
- [docs] `mlflow/docs/production-tracking-server-nginx-auth.md` — Deploy a production MLflow Tracking Server behind an Nginx reverse proxy with HTTP basic auth
- [notebook] `mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb` — Side-by-side comparison of autologging and manual tracking
- [script] `mlflow/scripts/custom_model_flavor.py` — Building a custom MLflow model flavor
- [snippet] `mlflow/snippets/2026-05-26-autolog_and_register.py` — Autologging and model registry example
- [snippet] `mlflow/snippets/2026-06-10-autologging-pipeline.py` — Training pipeline with autologging enabled
- [snippet] `mlflow/snippets/2026-06-10-minimal-model-serving.py` — Load a saved model and serve predictions with MLflow Python API
- [snippet] `mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py` — End-to-end training pipeline with sklearn autolog, model comparison, and Model Registry registration
- [snippet] `mlflow/snippets/log_first_run.py` — Logging a first MLflow run
- [snippet] `mlflow/snippets/tried_end_to_end_training.py` — Build an end-to-end training pipeline with MLflow autologging
- [snippet] `mlflow/snippets/tried_install_and_log_first_run.py` — Install MLflow and log first run with params and metrics
- [snippet] `mlflow/snippets/tried_logging_metrics.py` — Logging first metrics and parameters with MLflow Tracking
- [snippet] `mlflow/snippets/tried_serving_a_model.py` — Train, log, load, and serve predictions via the Python API

## Weights & Biases
- [primer] `wnb/notes/0000-primer-wnb.md` — W&B primer and setup
- [notes] `wnb/notes/2026-05-25-install-wandb-and-first-run.md` — Installing wandb and first experiment
- [notes] `wnb/notes/2026-05-27-install-wandb-first-experiment.md` — Installing W&B and running a first experiment tracking
- [notes] `wnb/notes/2026-05-31-first-wandb-experiment-tracking.md` — First W&B experiment tracking session
- [notes] `wnb/notes/2026-06-01-my-first-wandb-session.md` — My first W&B tracking session
- [notes] `wnb/notes/2026-06-05-configure-wandb-first-team-experiment.md` — Configuring W&B settings and running a first team experiment
- [notes] `wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md` — Following the official W&B quickstart and documenting trip-ups
- [notes] `wnb/notes/2026-06-06-train-model-and-review-dashboard.md` — Training a model with W&B and reviewing the dashboard
- [notes] `wnb/notes/2026-06-17-first-dashboard-exploration.md` — First walk through the W&B web UI: runs, projects, and experiment comparison
- [config] `wnb/configs/2026-06-08-first-sweep-config.yaml` — First hyperparameter sweep config with Bayesian optimization
- [config] `wnb/configs/2026-06-17-declarative-sweep-config.yaml` — YAML-based hyperparameter sweep for team collaboration
- [config] `wnb/configs/project-settings.yaml` — W&B project settings and tracking environment
- [config] `wnb/configs/sweep_config.yaml` — W&B hyperparameter sweep configuration
- [docs] `wnb/docs/artifact-tracking-in-data-pipeline.md` — Link raw data, processed data, and model artifacts to a pipeline run
- [docs] `wnb/docs/wandb-quickstart-trip-ups.md` — W&B quickstart trip-ups
- [notebook] `wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb` — Side-by-side comparison of declarative YAML vs programmatic Python API for defining hyperparameter sweeps
- [script] `wnb/scripts/hyperparameter_sweep.py` — Build a hyperparameter sweep with W&B from scratch
- [script] `wnb/scripts/train_small_model_with_wandb.py` — Training script instrumented with W&B
- [snippet] `wnb/snippets/2026-06-06-minimal-tracking.py` — Minimal experiment tracking with W&B Python API
- [snippet] `wnb/snippets/log_metrics_and_artifacts.py` — Logging metrics and artifacts with W&B SDK
- [snippet] `wnb/snippets/tried_artifact_logging.py` — Save and log model and dataset artifacts with wandb.Artifact
- [snippet] `wnb/snippets/tried_first_metrics_and_config.py` — First metrics and config logging experiment
- [snippet] `wnb/snippets/tried_logging_first_run.py` — First run logging with W&B
- [snippet] `wnb/snippets/tried_logging_metrics_and_params.py` — Logging first metrics and parameters with W&B

## ZenML
- [primer] `zenml/notes/0000-primer-zenml.md` — ZenML overview and key concepts
- [notes] `zenml/notes/2026-06-19-first-dashboard-and-stack.md` — Exploring the ZenML dashboard and configuring an S3 artifact store stack
- [snippet] `zenml/snippets/tried_first_training_pipeline.py` — First ZenML pipeline with data loading and model training
