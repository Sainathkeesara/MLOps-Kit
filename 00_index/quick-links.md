# Quick Links

## I need to...

### Set up a tool for the first time
- [ZenML primer](../zenml/notes/0000-primer-zenml.md)
- [ZenML dashboard and first stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md) — Exploring the ZenML dashboard and configuring an S3 artifact store stack (L1)
- [DVC primer](../dvc/notes/0000-primer-dvc.md)
- [DVC get started trip-ups](../dvc/notes/2026-06-05-get-started.md)
- [Feast primer](../feast/notes/0000-primer-feast.md)
- [Feast install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- [Kubeflow primer](../kubeflow/notes/0000-primer-kubeflow.md)
- [Kubeflow install guide](../kubeflow/notes/2026-05-25-install-kubeflow-and-explore-ui.md)
- [Kubeflow Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md)
- [Kubeflow Pipelines quickstart trip-ups](../kubeflow/notes/2026-05-27-pipelines-quickstart-trip-ups.md)
- [Kubeflow Pipelines quickstart second pass trip-ups](../kubeflow/notes/2026-06-08-kubeflow-pipelines-quickstart-trip-ups.md)
- [Kubeflow Pipelines quickstart third pass trip-ups](../kubeflow/notes/2026-06-09-kubeflow-pipelines-quickstart-trip-ups.md)
- [Kubeflow install on Kind](../kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md)
- [Kubeflow minikube and CLI setup](../kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md)
- [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- [Metaflow install and dev environment setup](../metaflow/notes/2026-05-30-install-metaflow-and-setup-dev-env.md)
- [Metaflow quickstart trip-ups](../metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md)
- [Metaflow first end-to-end flow](../metaflow/notes/2026-06-05-first-flow-end-to-end.md)
- [Metaflow second pass through quickstart](../metaflow/notes/2026-06-06-revisiting-quickstart.md)
- [MLflow primer](../mlflow/notes/0000-primer-mlflow.md)
- [MLflow server setup](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- [MLflow tracking server with Nginx auth proxy](../mlflow/docs/production-tracking-server-nginx-auth.md) — Deploy a production MLflow Tracking Server behind an Nginx reverse proxy with HTTP basic auth
- [MLflow quickstart trip-ups](../mlflow/notes/2026-05-27-mlflow-quickstart-trip-ups.md)
- [MLflow Tracking quickstart trip-ups](../mlflow/notes/2026-05-28-mlflow-tracking-quickstart-trip-ups.md)
- [W&B primer](../wnb/notes/0000-primer-wnb.md)
- [W&B first run](../wnb/notes/2026-05-25-install-wandb-and-first-run.md)
- [W&B first experiment tracking](../wnb/notes/2026-05-27-install-wandb-first-experiment.md)
- [W&B experiment tracking session](../wnb/notes/2026-05-31-first-wandb-experiment-tracking.md)
- [W&B first tracking session](../wnb/notes/2026-06-01-my-first-wandb-session.md)
- [W&B first team experiment](../wnb/notes/2026-06-05-configure-wandb-first-team-experiment.md)
- [W&B quickstart trip-ups](../wnb/docs/wandb-quickstart-trip-ups.md) — W&B quickstart trip-ups
- [W&B quickstart trip-ups (notes)](../wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md)
- [W&B dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md) — First walk through the W&B web UI: runs, projects, and experiment comparison
- [W&B model training + dashboard review](../wnb/notes/2026-06-06-train-model-and-review-dashboard.md)
- [W&B sweep config vs Python API notebook](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb) — Side-by-side comparison of declarative YAML vs programmatic Python API for defining hyperparameter sweeps (L3)

### Run an experiment
- [ZenML first training pipeline](../zenml/snippets/tried_first_training_pipeline.py) — First ZenML pipeline with data loading and model training (L1)
- [Kubeflow Pipelines + MLflow tracking integration](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md) — Wire KFP pipeline components to an in-cluster MLflow tracking server (L4)
- [W&B hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py) — Build a hyperparameter sweep with W&B from scratch (L3)
- [W&B sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py) — Reusable sweep and evaluation pipeline with sklearn support, CLI subcommands, and multi-task (classification/regression) training (L4)
- [Custom MLflow model flavor](../mlflow/scripts/custom_model_flavor.py) — Build a custom pyfunc model flavor from scratch
- [Kubeflow backend health check](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- [Kubeflow component readiness check](../kubeflow/scripts/tried_check_kubeflow_readiness.sh)
- [Kubeflow Central Dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md) — First walk through the Kubeflow Central Dashboard
- [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md) — KFP v2 SDK surprises during component writing and pipeline compilation
- [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md) — Diagnose infrastructure failures and pod log issues in KFP pipelines
- [Metaflow end-to-end flow](../metaflow/notes/2026-05-27-first-end-to-end-flow.md)
- [Metaflow UI exploration](../metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md)
- [Metaflow data + decision flow](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb)
- [Metaflow full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb) — Compare a fresh run against a resumed run during iterative model development
- [Metaflow minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- [Metaflow 5-step ML pipeline](../metaflow/scripts/2026-06-12-five-step-ml-pipeline.py) — End-to-end pipeline: load → clean → feature engineering → train → evaluate
- [MLflow model serving](../mlflow/snippets/tried_serving_a_model.py) — Train, log, load, and serve predictions via the Python API
- [MLflow install and first run snippet](../mlflow/snippets/tried_install_and_log_first_run.py) — Install MLflow and log first run with params and metrics (L1)
- [MLflow autologging pipeline](../mlflow/snippets/2026-06-10-autologging-pipeline.py) — Training pipeline with autologging enabled
- [MLflow autolog and register](../mlflow/snippets/2026-05-26-autolog_and_register.py)
- [MLflow install and first run](../mlflow/notes/2026-05-27-install-mlflow-first-run.md)
- [MLflow first run](../mlflow/snippets/log_first_run.py)
- [MLflow metrics demo](../mlflow/snippets/tried_logging_metrics.py)
- [MLflow minimal model serving](../mlflow/snippets/2026-06-10-minimal-model-serving.py) — Load a saved model and serve predictions with MLflow Python API
- [MLflow autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb) — Side-by-side comparison of two tracking approaches
- [MLflow end-to-end training with autologging](../mlflow/snippets/tried_end_to_end_training.py) — Build an end-to-end training pipeline with MLflow autologging
- [MLflow autologging pipeline (wine)](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py) — End-to-end training pipeline with sklearn autolog, model comparison, and Model Registry registration
- [W&B training script](../wnb/scripts/train_small_model_with_wandb.py)
- [W&B metrics and params snippet](../wnb/snippets/tried_logging_metrics_and_params.py)
- [W&B first metrics and config snippet](../wnb/snippets/tried_first_metrics_and_config.py)
- [W&B minimal tracking snippet](../wnb/snippets/2026-06-06-minimal-tracking.py) — Minimal experiment tracking with W&B
- [W&B first run snippet](../wnb/snippets/tried_logging_first_run.py)
- [W&B artifact logging snippet](../wnb/snippets/tried_artifact_logging.py) — Save and log model and dataset artifacts with wandb.Artifact
- [W&B artifact tracking in a data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md) — Link raw data, processed data, and model artifacts to a pipeline run
- [W&B metrics and artifacts snippet](../wnb/snippets/log_metrics_and_artifacts.py)
- [DVC pipeline](../dvc/snippets/tried_dvc_pipeline.sh)
- [DVC minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py)

### Define features
 - [My first feature view with Feast](../feast/snippets/tried_first_feature_view.py)
 - [Feast feature store config](../feast/configs/feature_store.yaml) — Feature store configuration with SQLite online store

### Register and promote models
- [W&B Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md) — Integrate W&B Artifacts with the Model Registry for versioned model governance and promotion through staging aliases (L4)

### Manage compute and environments
- [Metaflow resource management](../metaflow/docs/metaflow-resource-management.md) — Pin dependencies with @conda, request CPU/memory/GPU with @resources, and set step timeouts (L3)
- [Metaflow foreach vs @batch](../metaflow/docs/foreach-vs-batch.md) — Compare in-process fan-out with infrastructure-level parallelism via AWS Batch (L3)

### Configure a project
- [W&B + CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md) — Template project wiring W&B experiment tracking with GitHub Actions CI/CD pipeline (L4)
- [Kubeflow + MLflow project scaffold](../kubeflow/templates/kubeflow-mlflow-project/README.md) — Template project wiring KFP pipelines with MLflow experiment tracking (L4)
- [MLflow project config](../mlflow/configs/mlflow-project.yaml)
- [MLflow MLproject + conda env](../mlflow/configs/MLproject)
- [MLflow conda environment](../mlflow/configs/conda.yaml)
- [Metaflow project scaffold](../metaflow/configs/metaflow-project-scaffold.yaml)
- [Metaflow linear DAG with parameters](../metaflow/snippets/tried_first_linear_dag.py)
- [Metaflow parameterized DAG with branching and merging](../metaflow/snippets/tried_parameterized_dag.py)
- [Metaflow parameterized flow](../metaflow/snippets/tried_parameterizing_a_flow.py) — Pass runtime config via @parameters decorator
- [Metaflow minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- [Metaflow model serving flow](../metaflow/snippets/tried_serving_model.py)
- [Metaflow @step decorator DAG ordering](../metaflow/notes/2026-06-08-step-decorator-dag-ordering.md) — How Metaflow builds and enforces the DAG through `self.next()` calls
- [Metaflow CI/CD with GitHub Actions](../metaflow/notes/2026-06-12-ci-cd-with-github-actions.md) — Wiring Metaflow flows into a GitHub Actions CI/CD pipeline
- [Katib HPO random search + PyTorch](../kubeflow/manifests/katib-hpo-random-search-pytorch.yaml) — Hyperparameter tuning experiment with random search algorithm and PyTorch training (L4)
- [Kubeflow pipeline manifest](../kubeflow/manifests/minimal-hello-pipeline.yaml)
- [Kubeflow pipeline with K8s Job set](../kubeflow/manifests/2026-06-08-pipeline-job-set.yaml) — multi-component pipeline (prep → train → evaluate) as a Kubernetes Job set
- [Kubeflow V2 pipeline snippet](../kubeflow/snippets/tried_pipeline_v2_sdk.py)
- [Kubeflow deploy pipeline snippet](../kubeflow/snippets/tried_deploy_first_pipeline.py) — Deploy and run a Kubeflow pipeline via SDK
- [KFP v2 end-to-end snippet](../kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py) — Minimal KFP v2 pipeline with data prep, train, and evaluate steps
- [KFP v2 conditional branching pipeline](../kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py) — Pipeline with conditional deploy/retrain branching and per-component resource constraints (L3)
- [Katib vs ParallelFor for HP tuning](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb) — Compare Katib managed tuning vs custom ParallelFor grid search for KFP hyperparameter optimization (L3)
- [KFP v2 minimal pipeline](../kubeflow/snippets/2026-06-14-tried_kfp_v2_minimal.py) — Minimal KFP v2 pipeline with add + multiply arithmetic steps (L2)
- [KFP minimal component](../kubeflow/snippets/tried_my_first_component.py) — My first Kubeflow Pipelines component — just adds two numbers
- [KFP custom sklearn component Dockerfile](../kubeflow/dockerfiles/sklearn-train-component.Dockerfile) — Build a custom container component with RandomForest training, argument parsing, and cloudpickle serialization (L4)
- [Kubeflow pipeline resources config](../kubeflow/configs/pipeline-resources.yaml)
- [W&B sweep config (first)](../wnb/configs/2026-06-08-first-sweep-config.yaml) — First hyperparameter sweep config with Bayesian optimization
- [W&B sweep config (reference)](../wnb/configs/sweep_config.yaml)
- [W&B declarative sweep config](../wnb/configs/2026-06-17-declarative-sweep-config.yaml) — YAML-based hyperparameter sweep for team collaboration (L3)
- [W&B project settings config](../wnb/configs/project-settings.yaml)
- [W&B Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml) — Deploy a W&B Launch agent locally with Docker Compose (L4)
- [DVC pipeline config](../dvc/configs/pipeline.yaml)
- [MLflow tracking server config](../mlflow/configs/mlflow_tracking.yaml) — Local backend store configuration for MLflow Tracking server

### Compare model versions
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md) — Register, compare, and promote MLflow models in the Model Registry

### Version data
- [DVC init and first dataset track](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- [DVC first dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)

## Project
- [README](../README.md) — Project overview and repository structure
- [CHANGELOG](../CHANGELOG.md) — Record of completed tasks
- [Root layout audit](../General/docs/2026-06-14-root-layout-audit.md) — Checked actual root entries and made `.git/` / `dvc/configs/` visible in README
- [Empty root item pass](../General/docs/2026-06-14-empty-root-item-pass.md) — Second pass on empty root-item task text
- [README.md layout pass](../General/docs/2026-06-14-readme-md-layout-pass.md) — Confirmed README.md entry and aligned README counts
- [dvc/configs/ Layout + Coverage doc](../General/docs/2026-06-14-document-dvc-configs-in-readme.md) — Documented dvc/configs/ in README Layout and Coverage sections
- [00_index/ folder layout doc](../General/docs/2026-06-13-document-00-index-folder-in-readme.md) — Documented 00_index/ in README Layout section
- [.git/ folder layout doc](../General/docs/2026-06-06-added-dot-git-folder-to-layout.md) — Documented .git/ in README Layout section
- [README.md in layout doc](../General/docs/2026-06-06-added-readme-md-to-layout.md) — Documented README.md in README Layout section
- [feast/ folder layout doc](../General/docs/2026-06-06-added-feast-folder-to-layout.md) — Documented feast/ in README Layout section
- [feast/ folder Layout + Coverage doc](../General/docs/2026-06-08-document-feast-folder-in-readme.md) — Documented feast/ in README Layout and Coverage sections
- [feast/configs/ Layout doc](../General/docs/2026-06-09-document-feast-configs-in-readme.md) — Documented feast/configs/ in README Layout section
- [General/ folder layout doc](../General/docs/2026-06-07-document-general-folder-in-readme.md) — Documented General/ in README Layout section
- [CHANGELOG.md in layout doc](../General/docs/2026-06-06-document-changelog-in-readme.md) — Documented CHANGELOG.md in README Layout section
- [CHANGELOG.md in layout (second pass)](../General/docs/2026-06-13-changelog-in-readme-layout.md) — Actually added CHANGELOG.md to README Layout section
