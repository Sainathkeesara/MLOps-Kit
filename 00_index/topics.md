# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Concepts · 11 files

- **primer:** [Containerization](../docs/concepts/containerization/0000-primer-containerization.md) — What containerization is and why it matters in MLOps (L1)
- **primer:** [Data Versioning](../docs/concepts/data-versioning/0000-primer-data-versioning.md) — What data versioning is and why it matters for reproducible ML (L1)
- **primer:** [Experiment Tracking](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) — What experiment tracking is and why it matters for MLOps (L1)
- **primer:** [Feature Store](../docs/concepts/feature-store/0000-primer-feature-store.md) — What a feature store is and why it matters in production ML (L1)
- **primer:** [Model Registry](../docs/concepts/model-registry/0000-primer-model-registry.md) — What a model registry is and why it matters for ML pipelines (L1)
- **primer:** [Model Serving](../docs/concepts/model-serving/0000-primer-model-serving.md) — What model serving is and why it matters for ML deployment (L1)
- **primer:** [Monitoring & Drift](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md) — What monitoring and drift detection is and why it matters for model reliability (L1)
- **primer:** [Pipeline Orchestration](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md) — What pipeline orchestration is and why it matters for ML workflows (L1)
- **scripts** (1): [Comparing training runs](../docs/concepts/experiment-tracking/scripts/tried_comparing_training_runs.py) — Compare training runs with different hyperparameters (L2)
- **snippets** (2): [Tried experiment tracking fundamentals](../docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py) (L2), [Tried model registry fundamentals](../docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py) (L2)

## ClearML · 3 files

- **primer:** [ClearML Orchestration](../clearml/notes/0000-primer-clearml-orchestration.md) — ClearML concepts, setup, and orchestration fundamentals
- **notes** (1): most recent → [ClearML Web UI exploration](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md) — First walk through the ClearML web UI
- **snippets** (1): [Install and first task](../clearml/snippets/tried_install_and_first_task.py) — Install ClearML and run my first task from a Python script (L1)

## DVC · 7 files

- **primer:** [DVC](../dvc/notes/0000-primer-dvc.md) — DVC concepts, setup, and first steps
- **notes** (2): most recent → [Get started trip-ups](../dvc/notes/2026-06-05-get-started.md), [First dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)
- **scripts** (1): [Init DVC and track dataset](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- **snippets** (2): [Tried DVC pipeline](../dvc/snippets/tried_dvc_pipeline.sh), [Minimal DVC versioning](../dvc/snippets/minimal_dvc_versioning.py)
- **configs** (1): [Pipeline config](../dvc/configs/pipeline.yaml)

## Evidently AI · 3 files

- **primer:** [Evidently AI](../evidently/notes/0000-primer-evidently.md) — Evidently AI concepts and data drift monitoring (L1)
- **notes** (1): most recent → [Comparing Report and TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md) (L1)
- **snippets** (1): [First drift report](../evidently/snippets/first_drift_report.py) — Install Evidently and generate a first data drift report

## Feast · 5 files

- **primer:** [Feast](../feast/notes/0000-primer-feast.md) — Feast overview and key concepts
- **notes** (1): [Install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- **snippets** (1): [First feature view](../feast/snippets/tried_first_feature_view.py)
- **configs** (2): [Feature store config](../feast/configs/feature_store.yaml), [Configs README](../feast/configs/README.md)

## KServe · 3 files

- **primer:** [KServe](../kserve/notes/0000-primer-kserve.md) — KServe overview and key concepts (L1)
- **snippets** (1): [First InferenceService](../kserve/snippets/first_inferenceservice.py) — Install KServe and deploy my first InferenceService (L1)
- **configs** (1): [Minimal sklearn InferenceService](../kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml) (L1)

## Kubeflow · 61 files

- **primer:** [Kubeflow](../kubeflow/notes/0000-primer-kubeflow.md) — Kubeflow overview and architecture
- **notes** (10): most recent → [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md), [Central Dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md), [Minikube and CLI setup](../kubeflow/notes/2026-06-06-install-minikube-and-kubeflow-cli.md)
- **snippets** (7): most useful → [KFP v2 end-to-end](../kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py), [Conditional branching pipeline](../kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py), [Deploy first pipeline](../kubeflow/snippets/tried_deploy_first_pipeline.py)
- **scripts** (4): [Component factory](../kubeflow/scripts/component_factory.py) (L4), [KFP component factory](../kubeflow/scripts/kfp_component_factory.py) (L4), [Diagnose health](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- **docs** (3): [Kubeflow pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md), [KFP v1 vs v2 DSL](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md) (L4), [Kubeflow + MLflow tracking](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md) (L4)
- **manifests** (3): [Katib HPO random search + PyTorch](../kubeflow/manifests/katib-hpo-random-search-pytorch.yaml), [Pipeline Job set](../kubeflow/manifests/2026-06-08-pipeline-job-set.yaml), [Minimal hello pipeline](../kubeflow/manifests/minimal-hello-pipeline.yaml)
- **notebooks** (1): [Katib vs ParallelFor for HP tuning](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb)
- **dockerfiles** (3): [Custom sklearn component Dockerfile](../kubeflow/dockerfiles/sklearn-train-component.Dockerfile), [Requirements](../kubeflow/dockerfiles/requirements.txt), [Train script](../kubeflow/dockerfiles/train.py)
- **templates** (21): [Pipeline scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md) with CI/CD, testing, and modular components (L5); [Kubeflow + MLflow project](../kubeflow/templates/kubeflow-mlflow-project/README.md) (L4)
- _…and 6 more under `kubeflow/` — browse the folder._

## Metaflow · 40 files

- **primer:** [Metaflow](../metaflow/notes/0000-primer-metaflow.md) — Metaflow primer and key concepts
- **notes** (9): most recent → [CI/CD with GitHub Actions](../metaflow/notes/2026-06-12-ci-cd-with-github-actions.md), [Step decorator DAG ordering](../metaflow/notes/2026-06-08-step-decorator-dag-ordering.md), [UI and run inspection](../metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md)
- **snippets** (5): [Minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py), [First linear DAG](../metaflow/snippets/tried_first_linear_dag.py), [Parameterized DAG](../metaflow/snippets/tried_parameterized_dag.py)
- **scripts** (3): [End-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py) (L2), [Five-step ML pipeline](../metaflow/scripts/2026-06-12-five-step-ml-pipeline.py), [Batch inference splits](../metaflow/scripts/batch_inference_splits.py)
- **docs** (3): [Resource management](../metaflow/docs/metaflow-resource-management.md), [Foreach vs @batch](../metaflow/docs/foreach-vs-batch.md), [Metaflow + W&B integration](../metaflow/docs/metaflow-wandb-integration.md)
- **notebooks** (2): [End-to-end flow with data](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb), [Full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb)
- **manifests** (1): [AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml)
- **configs** (1): [Project scaffold config](../metaflow/configs/metaflow-project-scaffold.yaml)
- **templates** (11): [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md) with CI/CD, testing, and environment management (L4)
- _…and 2 more under `metaflow/` — browse the folder._

## MLflow · 29 files

- **primer:** [MLflow](../mlflow/notes/0000-primer-mlflow.md) — MLflow concepts and setup
- **notes** (6): most recent → [MLflow quickstart trip-ups (July)](../mlflow/notes/2026-07-01-mlflow-quickstart-trip-ups.md), [UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md), [First MLflow server](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- **snippets** (12): [Autologging pipeline](../mlflow/snippets/2026-06-10-autologging-pipeline.py), [End-to-end autologging](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py), [Minimal model serving](../mlflow/snippets/2026-06-10-minimal-model-serving.py), [Minimal autologging](../mlflow/snippets/2026-07-02-minimal-autologging.py)
- **scripts** (1): [Custom model flavor](../mlflow/scripts/custom_model_flavor.py)
- **configs** (5): [Tracking server config (S3)](../mlflow/configs/2026-07-01-tracking-server-s3.yaml), [MLproject](../mlflow/configs/MLproject), [Conda env](../mlflow/configs/conda.yaml), [Tracking config](../mlflow/configs/mlflow_tracking.yaml), [Project config](../mlflow/configs/mlflow-project.yaml)
- **docs** (2): [Comparing model versions](../mlflow/docs/comparing-model-versions.md), [Production tracking server with Nginx auth](../mlflow/docs/production-tracking-server-nginx-auth.md)
- **notebooks** (1): [Autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb)

## Seldon Core · 2 files

- **primer:** [Seldon Core](../seldon/notes/0000-primer-seldon-core.md) — What is Seldon Core? (L1)
- **snippets** (1): [Install and first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py) — Install Seldon Core and deploy my first model via Python (L1)

## Weights & Biases · 39 files

- **primer:** [W&B](../wnb/notes/0000-primer-wnb.md) — W&B primer and setup
- **notes** (10): most recent → [W&B dashboard — what's there](../wnb/notes/2026-07-02-whats-on-the-wandb-dashboard.md), [Exploring W&B dashboard](../wnb/notes/2026-07-01-exploring-wandb-dashboard.md), [First dashboard exploration](../wnb/notes/2026-06-17-first-dashboard-exploration.md)
- **snippets** (8): [First experiment with SDK](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py) (L1), [Minimal tracking](../wnb/snippets/2026-06-06-minimal-tracking.py), [Metrics and artifacts](../wnb/snippets/log_metrics_and_artifacts.py)
- **scripts** (3): [Hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py), [Sweep + eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py), [Training with W&B](../wnb/scripts/train_small_model_with_wandb.py)
- **docs** (3): [Artifact + model registry workflow](../wnb/docs/artifact-model-registry-workflow.md), [Artifact tracking in data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md), [Quickstart trip-ups](../wnb/docs/wandb-quickstart-trip-ups.md)
- **configs** (4): [Sweep configs](../wnb/configs/sweep_config.yaml), [Project settings](../wnb/configs/project-settings.yaml)
- **manifests** (1): [Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml)
- **notebooks** (1): [Sweep config vs Python API](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb)
- **templates** (8): [W&B CI/CD project](../wnb/templates/wandb-cicd-project/README.md) with experiment tracking and CI/CD (L4)

## ZenML · 4 files

- **primer:** [ZenML](../zenml/notes/0000-primer-zenml.md) — ZenML overview and key concepts
- **notes** (1): [First dashboard and stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md)
- **snippets** (1): [First training pipeline](../zenml/snippets/tried_first_training_pipeline.py)
- **configs** (1): [ZenML stack config](../zenml/configs/zenml-stack.yaml)
