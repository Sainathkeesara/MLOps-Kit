# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Concepts · 20 files

- **primer:** [Containerization](../docs/concepts/containerization/0000-primer-containerization.md)
- **primer:** [Data Versioning](../docs/concepts/data-versioning/0000-primer-data-versioning.md) — with [exercises](../docs/concepts/data-versioning/snippets/2026-07-10-data-versioning-fundamentals.py) and [snapshot script](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py)
- **primer:** [Experiment Tracking](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) — with [exercises](../docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py) and [run comparison script](../docs/concepts/experiment-tracking/scripts/tried_comparing_training_runs.py)
- **primer:** [Feature Store](../docs/concepts/feature-store/0000-primer-feature-store.md) — with [exercises](../docs/concepts/feature-store/snippets/2026-07-10-feature-store-fundamentals.py) and [online store script](../docs/concepts/feature-store/scripts/2026-07-12-writing-and-reading-features-online-store.py)
- **primer:** [Model Registry](../docs/concepts/model-registry/0000-primer-model-registry.md) — with [exercises](../docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py) and [apply script](../docs/concepts/model-registry/scripts/2026-07-10-apply-model-registry.py)
- **primer:** [Model Serving](../docs/concepts/model-serving/0000-primer-model-serving.md) — with [FastAPI inference endpoint](../docs/concepts/model-serving/scripts/2026-07-12-fastapi-inference-endpoint.py)
- **primer:** [Monitoring & Drift](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md)
- **primer:** [Pipeline Orchestration](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md) — with [exercises](../docs/concepts/pipeline-orchestration/snippets/2026-07-10-pipeline-orchestration-fundamentals.py) and [DAG workflow script](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py)

## ClearML · 4 files

- **primer:** [ClearML orchestration](../clearml/notes/0000-primer-clearml-orchestration.md)
- **notes** (2): [Web UI exploration](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md), [Pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md)
- **snippets:** [Install and first task](../clearml/snippets/tried_install_and_first_task.py)

## DVC · 8 files

- **primer:** [DVC concepts and setup](../dvc/notes/0000-primer-dvc.md)
- **notes** (3): most recent → [Get started trip-ups](../dvc/notes/2026-06-05-get-started.md), [First dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)
- **snippets** (2): [Minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py), [DVC pipeline shell](../dvc/snippets/tried_dvc_pipeline.sh)
- **scripts** (1): [Init DVC and track dataset](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- **configs** (2): [dvc.yaml](../dvc/configs/dvc.yaml), [Pipeline YAML](../dvc/configs/pipeline.yaml)

## Evidently AI · 3 files

- **primer:** [Evidently AI and data drift](../evidently/notes/0000-primer-evidently.md)
- **notes:** [Report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md)
- **snippets:** [First drift report](../evidently/snippets/first_drift_report.py)

## Feast · 5 files

- **primer:** [Feast overview](../feast/notes/0000-primer-feast.md)
- **notes** (2): [Install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- **configs** (2): [feature_store.yaml](../feast/configs/feature_store.yaml), [Config README](../feast/configs/README.md)
- **snippets** (1): [First feature view](../feast/snippets/tried_first_feature_view.py)

## KServe · 3 files

- **primer:** [KServe overview](../kserve/notes/0000-primer-kserve.md)
- **configs** (1): [Minimal sklearn InferenceService](../kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml)
- **snippets** (1): [First InferenceService](../kserve/snippets/first_inferenceservice.py)

## Kubeflow · 65 files

- **primer:** [Kubeflow overview](../kubeflow/notes/0000-primer-kubeflow.md)
- **notes** (14): most recent → [KFP v2 quickstart trip-ups (Jul 11)](../kubeflow/notes/2026-07-11-kfp-v2-quickstart-trip-ups.md), [KFP v2 quickstart trip-ups (Jul 6)](../kubeflow/notes/2026-07-06-kfp-v2-quickstart-trip-ups.md), [Central dashboard re-exploration](../kubeflow/notes/2026-07-06-explore-central-dashboard-again.md)
- **snippets** (9): [Verify KFP install](../kubeflow/snippets/2026-07-06-verify-kfp-install.py), [Conditional branching pipeline](../kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py), [Minimal KFP v2](../kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py)
- **scripts** (5): [Kubeflow health diagnosis](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh), [Component readiness check](../kubeflow/scripts/tried_check_kubeflow_readiness.sh), [KFP component factory](../kubeflow/scripts/kfp_component_factory.py), [Component factory](../kubeflow/scripts/component_factory.py)
- **configs** (2): [Pipeline resources](../kubeflow/configs/pipeline-resources.yaml)
- **docs** (4): [KFP v1 vs v2 DSL](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md), [Kubeflow + MLflow tracking](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md), [Pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md)
- **manifests** (5): [Minimal hello pipeline](../kubeflow/manifests/minimal-hello-pipeline.yaml), [Katib HPO random search](../kubeflow/manifests/katib-hpo-random-search-pytorch.yaml), [Pipeline job set](../kubeflow/manifests/2026-06-08-pipeline-job-set.yaml)
- **notebooks** (2): [Katib vs ParallelFor HPO](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb)
- **dockerfiles** (4): [Sklearn component Dockerfile](../kubeflow/dockerfiles/sklearn-train-component.Dockerfile)
- **templates** (20): [Kubeflow pipeline scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md), [Kubeflow + MLflow project](../kubeflow/templates/kubeflow-mlflow-project/README.md)
- _…and 18 more under `kubeflow/templates/` — browse the folder._

## Metaflow · 48 files

- **primer:** [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- **notes** (13): most recent → [Metaflow quickstart trip-ups (Jul 11)](../metaflow/notes/2026-07-11-metaflow-quickstart-trip-ups.md), [CLI and local dev UI (Jul 9)](../metaflow/notes/2026-07-09-explore-cli-local-dev-ui.md), [CLI and local dev UI (Jul 6)](../metaflow/notes/2026-07-06-explore-cli-local-dev-ui.md)
- **snippets** (7): [First flow with branching, retry, and foreach](../metaflow/snippets/2026-07-09-first-flow-branching-retry-foreach.py), [Install and first flow](../metaflow/snippets/2026-07-06-install-first-flow.py), [Minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- **scripts** (6): [Kubernetes flow metadata tracking](../metaflow/scripts/2026-07-12-kubernetes-flow-metadata-tracking.py), [Logging artifact flow](../metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py), [End-to-end experiment (Jul 3)](../metaflow/scripts/2026-07-03-end-to-end-experiment.py)
- **configs** (2): [Project scaffold config](../metaflow/configs/metaflow-project-scaffold.yaml), [Config README](../metaflow/configs/README.md)
- **docs** (3): [W&B integration](../metaflow/docs/metaflow-wandb-integration.md), [Resource management](../metaflow/docs/metaflow-resource-management.md), [Foreach vs @batch](../metaflow/docs/foreach-vs-batch.md)
- **manifests** (3): [DevStack compose](../metaflow/manifests/2026-07-13-metaflow-devstack-compose.yaml), [AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml), [Manifest README](../metaflow/manifests/README.md)
- **notebooks** (2): [Full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb), [End-to-end flow with data](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb)
- **dockerfiles** (1): [Metaflow development container](../metaflow/dockerfiles/metaflow-dev.Dockerfile)
- **templates** (11): [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md)
- _…and 10 more under `metaflow/templates/` — browse the folder._

## MLflow · 33 files

- **primer:** [MLflow concepts and setup](../mlflow/notes/0000-primer-mlflow.md)
- **notes** (7): [UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md), [Quickstart trip-ups (Jul 2026)](../mlflow/notes/2026-07-01-mlflow-quickstart-trip-ups.md), [First MLflow server](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- **snippets** (12): [Minimal autologging](../mlflow/snippets/2026-07-02-minimal-autologging.py), [End-to-end autologging pipeline](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py), [Model serving](../mlflow/snippets/2026-06-10-minimal-model-serving.py)
- **scripts** (3): [End-to-end experiment (Jul 6)](../mlflow/scripts/2026-07-06-end-to-end-experiment.py), [End-to-end experiment (Jul 5)](../mlflow/scripts/2026-07-05-end-to-end-experiment.py), [Custom model flavor](../mlflow/scripts/custom_model_flavor.py)
- **configs** (7): [Tracking server Postgres+S3](../mlflow/configs/2026-07-06-tracking-server-postgres-s3.yaml), [Tracking server S3](../mlflow/configs/2026-07-01-tracking-server-s3.yaml), [MLproject](../mlflow/configs/MLproject)
- **docs** (2): [Comparing model versions](../mlflow/docs/comparing-model-versions.md), [Production tracking server with Nginx auth](../mlflow/docs/production-tracking-server-nginx-auth.md)
- **notebooks** (2): [Exploring runs, experiments, and model registry](../mlflow/notebooks/2026-07-09-exploring-runs-experiments-and-model-registry.ipynb), [Autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb)

## Seldon Core · 3 files

- **primer:** [Seldon Core overview](../seldon/notes/0000-primer-seldon-core.md)
- **notes:** [Seldon vs KServe comparison](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md)
- **snippets** (1): [Install and first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py)

## Weights & Biases · 42 files

- **primer:** [W&B primer](../wnb/notes/0000-primer-wnb.md)
- **notes** (14): most recent → [W&B quickstart trip-ups (Jul 11)](../wnb/notes/2026-07-11-first-wandb-quickstart-trip-ups.md), [Dashboard exploration (Jul 9)](../wnb/notes/2026-07-09-explore-wandb-dashboard.md), [Dashboard exploration (Jul 5)](../wnb/notes/2026-07-05-exploring-wandb-dashboard.md)
- **snippets** (8): [First experiment SDK](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py), [Minimal tracking](../wnb/snippets/2026-06-06-minimal-tracking.py), [Artifact logging](../wnb/snippets/tried_artifact_logging.py)
- **scripts** (3): [Sweep and eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py), [Hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py)
- **configs** (4): [Declarative sweep config](../wnb/configs/2026-06-17-declarative-sweep-config.yaml), [First sweep config](../wnb/configs/2026-06-08-first-sweep-config.yaml)
- **docs** (3): [Artifact + Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md), [Artifact tracking in data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md)
- **manifests** (2): [CI/CD workflow](../wnb/manifests/2026-07-13-wandb-ci-cd-workflow.yaml), [Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml)
- **notebooks** (1): [Sweep config vs Python API](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb)
- **templates** (7): [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md)

## ZenML · 7 files

- **primer:** [ZenML overview](../zenml/notes/0000-primer-zenml.md)
- **notes** (2): [Dashboard and first stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md)
- **snippets** (1): [First training pipeline](../zenml/snippets/tried_first_training_pipeline.py)
- **scripts** (1): [Multi-step ZenML + MLflow pipeline](../zenml/scripts/2026-07-13-multi-step-zenml-mlflow-pipeline.py)
- **configs** (2): [Stack with MLflow+S3](../zenml/configs/2026-07-12-zenml-stack-mlflow-s3.yaml), [ZenML stack config](../zenml/configs/zenml-stack.yaml)
- **notebooks** (1): [Parent-child pipelines & lineage](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb)