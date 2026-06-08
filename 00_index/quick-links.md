# Quick Links

## I need to...

### Set up a tool for the first time
- [Metaflow install and dev environment setup](../metaflow/notes/2026-05-30-install-metaflow-and-setup-dev-env.md)
- [MLflow primer](../mlflow/notes/0000-primer-mlflow.md)
- [MLflow server setup](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- [MLflow quickstart trip-ups](../mlflow/notes/2026-05-27-mlflow-quickstart-trip-ups.md)
- [MLflow Tracking quickstart trip-ups](../mlflow/notes/2026-05-28-mlflow-tracking-quickstart-trip-ups.md)
- [Kubeflow primer](../kubeflow/notes/0000-primer-kubeflow.md)
- [Kubeflow install guide](../kubeflow/notes/2026-05-25-install-kubeflow-and-explore-ui.md)
- [Kubeflow Kind cluster setup](../kubeflow/notes/2026-05-27-kind-cluster-for-kubeflow.md)
- [Kubeflow Pipelines quickstart trip-ups](../kubeflow/notes/2026-27-pipelines-quickstart-trip-ups.md)
- [Kubeflow install on Kind](../kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md)
- [Kubeflow minikube and CLI setup](../kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md)
- [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- [Metaflow quickstart trip-ups](../metaflow/notes/2026-05-27-metaflow-quickstart-trip-ups.md)
- [Metaflow first end-to-end flow](../metaflow/notes/2026-06-05-first-flow-end-to-end.md)
- [Metaflow second pass through quickstart](../metaflow/notes/2026-06-06-revisiting-quickstart.md)
- [DVC primer](../dvc/notes/0000-primer-dvc.md)
- [DVC get started trip-ups](../dvc/notes/2026-06-05-get-started.md)
- [W&B primer](../wnb/notes/0000-primer-wnb.md)
- [W&B first run](../wnb/notes/2026-05-25-install-wandb-and-first-run.md)
- [W&B quickstart trip-ups](../wnb/docs/wandb-quickstart-trip-ups.md)
- [W&B first experiment tracking](../wnb/notes/2026-05-27-install-wandb-first-experiment.md)
- [W&B experiment tracking session](../wnb/notes/2026-05-31-first-wandb-experiment-tracking.md)
- [W&B first tracking session](../wnb/notes/2026-06-01-my-first-wandb-session.md)
- [Feast primer](../feast/notes/0000-primer-feast.md)
- [Feast install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- [W&B first team experiment](../wnb/notes/2026-06-05-configure-wandb-first-team-experiment.md)
- [W&B model training + dashboard review](../wnb/notes/2026-06-06-train-model-and-review-dashboard.md)

### Run an experiment
- [Custom MLflow model flavor](../mlflow/scripts/custom_model_flavor.py) — Build a custom pyfunc model flavor from scratch
- [Kubeflow backend health check](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- [Kubeflow component readiness check](../kubeflow/scripts/tried_check_kubeflow_readiness.sh)
- [Metaflow end-to-end flow](../metaflow/notes/2026-05-27-first-end-to-end-flow.md)
- [Metaflow UI exploration](../metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md)
- [Metaflow data + decision flow](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb)
- [MLflow autolog and register](../mlflow/snippets/2026-05-26-autolog_and_register.py)
- [MLflow install and first run](../mlflow/notes/2026-05-27-install-mlflow-first-run.md)
- [MLflow first run](../mlflow/snippets/log_first_run.py)
- [MLflow metrics demo](../mlflow/snippets/tried_logging_metrics.py)
- [MLflow autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb) — Side-by-side comparison of two tracking approaches
- [W&B training script](../wnb/scripts/train_small_model_with_wandb.py)
- [W&B metrics and params snippet](../wnb/snippets/tried_logging_metrics_and_params.py)
- [W&B first metrics and config snippet](../wnb/snippets/tried_first_metrics_and_config.py)
- [DVC pipeline](../dvc/snippets/tried_dvc_pipeline.sh)
- [DVC minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py)
- [W&B first run snippet](../wnb/snippets/tried_logging_first_run.py)
- [W&B metrics and artifacts snippet](../wnb/snippets/log_metrics_and_artifacts.py)

### Compare model versions
- [Comparing registered model versions](../mlflow/docs/comparing-model-versions.md) — Register, compare, and promote MLflow models in the Model Registry

### Define features
- [My first feature view with Feast](../feast/snippets/tried_first_feature_view.py)

### Configure a project
- [MLflow project config](../mlflow/configs/mlflow-project.yaml)
- [MLflow MLproject + conda env](../mlflow/configs/MLproject)
- [MLflow conda environment](../mlflow/configs/conda.yaml)
- [Metaflow project scaffold](../metaflow/configs/metaflow-project-scaffold.yaml)
- [Metaflow linear DAG with parameters](../metaflow/snippets/tried_first_linear_dag.py)
- [Metaflow parameterized DAG with branching and merging](../metaflow/snippets/tried_parameterized_dag.py)
- [Metaflow minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- [Metaflow model serving flow](../metaflow/snippets/tried_serving_model.py)
- [Metaflow @step decorator DAG ordering](../metaflow/notes/2026-06-08-step-decorator-dag-ordering.md) — How Metaflow builds and enforces the DAG through `self.next()` calls
- [Kubeflow pipeline manifest](../kubeflow/manifests/minimal-hello-pipeline.yaml)
- [Kubeflow V2 pipeline snippet](../kubeflow/snippets/tried_pipeline_v2_sdk.py)
- [Kubeflow deploy pipeline snippet](../kubeflow/snippets/tried_deploy_first_pipeline.py) — Deploy and run a Kubeflow pipeline via SDK
- [Kubeflow pipeline resources config](../kubeflow/configs/pipeline-resources.yaml)
- [W&B sweep config (my first)](../wnb/configs/2026-06-08-first-sweep-config.yaml) — My first W&B hyperparameter sweep config with Bayesian optimization
- [W&B sweep config (reference)](../wnb/configs/sweep_config.yaml)
- [W&B project settings config](../wnb/configs/project-settings.yaml)
- [DVC pipeline config](../dvc/configs/pipeline.yaml)

### Version data
- [DVC init and first dataset track](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- [DVC first dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)

## Project
- [README](../README.md) — Project overview and repository structure
- [CHANGELOG](../CHANGELOG.md) — Record of completed tasks
- [.git/ folder layout doc](../General/docs/2026-06-06-added-dot-git-folder-to-layout.md) — Documented .git/ in README Layout section
- [README.md in layout doc](../General/docs/2026-06-06-added-readme-md-to-layout.md) — Documented README.md in README Layout section
- [feast/ folder layout doc](../General/docs/2026-06-06-added-feast-folder-to-layout.md) — Documented feast/ in README Layout section
- [General/ folder layout doc](../General/docs/2026-06-07-document-general-folder-in-readme.md) — Documented General/ in README Layout section
- [CHANGELOG.md in layout doc](../General/docs/2026-06-06-document-changelog-in-readme.md) — Documented CHANGELOG.md in README Layout section
- [Kubeflow central dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md) — First wander through the Kubeflow Central Dashboard
- [W&B quickstart trip-ups](../wnb/notes/2026-06-06-first-wandb-quickstart-trip-ups.md) — Following the official W&B quickstart and what tripped me up
- [W&B minimal tracking snippet](../wnb/snippets/2026-06-06-minimal-tracking.py) — Minimal experiment tracking with W&B: log params, metrics, and a histogram
