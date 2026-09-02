# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Concepts · 52 files

- **primer:** [Containerization](../docs/concepts/containerization/0000-primer-containerization.md)
  - [Multi-stage Dockerfile for MLOps](../docs/concepts/containerization/2026-07-23-multi-stage-dockerfile-for-mlops.md)
  - [Containerization + pipeline orchestration pattern](../docs/concepts/containerization/docs/containerization-pipeline-orchestration-pattern.md)
  - [Multistage ONNX Runtime serving](../docs/concepts/containerization/scripts/2026-07-13-multistage-onnxruntime-serving.py)
  - [Multi-stage ML training-serving Dockerfile](../docs/concepts/containerization/dockerfiles/2026-08-09-multi-stage-ml-training-serving.Dockerfile)
- **primer:** [Data Versioning](../docs/concepts/data-versioning/0000-primer-data-versioning.md)
  - [Snapshot vs diff versioning](../docs/concepts/data-versioning/snapshot-vs-diff-versioning.md)
  - [Track dataset snapshots](../docs/concepts/data-versioning/scripts/2026-07-10-track-dataset-snapshots.py)
  - [DVC dataset versioning](../docs/concepts/data-versioning/scripts/2026-08-07-dvc-dataset-versioning.py)
  - [Track DVC versions](../docs/concepts/data-versioning/scripts/2026-08-07-track-dvc-versions.py)
- **primer:** [Experiment Tracking](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md)
  - [Experiment tracking workflow](../docs/concepts/experiment-tracking/2026-08-04-experiment-tracking-workflow.md)
  - [Patterns and pitfalls](../docs/concepts/experiment-tracking/experiment-tracking-patterns-pitfalls.md)
  - [Comparing approaches notebook](../docs/concepts/experiment-tracking/notebooks/comparing-experiment-tracking-approaches.ipynb)
- **primer:** [Feature Store](../docs/concepts/feature-store/0000-primer-feature-store.md)
  - [Offline vs online stores](../docs/concepts/feature-store/2026-08-09-offline-vs-online-stores.md)
  - [Register and retrieve features](../docs/concepts/feature-store/scripts/2026-08-09-register-and-retrieve-features.py)
- **primer:** [Model Registry](../docs/concepts/model-registry/0000-primer-model-registry.md)
  - [Automated vs manual promotion](../docs/concepts/model-registry/automated-vs-manual-promotion.md)
  - [Model versioning workflow](../docs/concepts/model-registry/scripts/2026-08-04-model-versioning-workflow.py)
  - [Automated model promotion workflow](../docs/concepts/model-registry/scripts/automated-model-promotion-workflow.py)
- **primer:** [Model Serving](../docs/concepts/model-serving/0000-primer-model-serving.md)
  - [Minimal FastAPI inference endpoint](../docs/concepts/model-serving/snippets/2026-08-11-minimal-fastapi-inference-endpoint.py)
  - [Serving config](../docs/concepts/model-serving/configs/2026-08-11-model-serving-config.yaml)
- **primer:** [Monitoring & Drift](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md)
  - [Monitoring and drift patterns](../docs/concepts/monitoring-drift/2026-08-11-monitoring-drift-patterns.md)
  - [Data drift detection script](../docs/concepts/monitoring-drift/scripts/2026-08-11-data-drift-detection.py)
- **primer:** [Pipeline Orchestration](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md)
  - [Production orchestration patterns](../docs/concepts/pipeline-orchestration/pipeline-orchestration-patterns-for-production-mlops.md)
  - [DAG workflow script](../docs/concepts/pipeline-orchestration/scripts/2026-07-10-dag-ml-workflow.py)
  - [Build DAG pipeline](../docs/concepts/pipeline-orchestration/scripts/2026-08-07-build-dag-pipeline.py)
  - [Simple DAG pipeline](../docs/concepts/pipeline-orchestration/scripts/2026-08-07-simple-dag-pipeline.py)
  - [DAG pipeline error handling](../docs/concepts/pipeline-orchestration/scripts/dag-pipeline-error-handling.py)
  - _…and 15 more under `docs/concepts/` — browse the folder._

## Metaflow · 83 files

- **primer:** [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- **notes** (14): most recent → [Install and hello world](../metaflow/notes/2026-07-14-install-and-hello-world.md), [Metaflow quickstart trip-ups](../metaflow/notes/2026-07-11-metaflow-quickstart-trip-ups.md), [CLI and local dev UI](../metaflow/notes/2026-07-09-explore-cli-local-dev-ui.md)
- **snippets** (15): [First flow with branching, retry, and foreach](../metaflow/snippets/2026-07-09-first-flow-branching-retry-foreach.py), [Install and first flow](../metaflow/snippets/2026-07-06-install-first-flow.py), [Minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py)
- **scripts** (8): [Kubernetes flow metadata tracking](../metaflow/scripts/2026-07-12-kubernetes-flow-metadata-tracking.py), [Logging artifact flow](../metaflow/scripts/2026-07-12-metaflow-logging-artifact-flow.py), [Trigger hooks](../metaflow/scripts/2026-07-28-metaflow-trigger-hooks.py)
- **docs** (11): [W&B integration](../metaflow/docs/metaflow-wandb-integration.md), [Resource management](../metaflow/docs/metaflow-resource-management.md), [Foreach vs @batch](../metaflow/docs/foreach-vs-batch.md), [W&B real-time metric tracking](../metaflow/docs/wandb-metric-tracking-parallel-steps.md)
- **manifests** (4): [DevStack compose](../metaflow/manifests/2026-07-13-metaflow-devstack-compose.yaml), [AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml), [Production Argo deployment](../metaflow/manifests/production-metaflow-argo-deployment.yaml)
- **notebooks** (5): [Full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb), [End-to-end flow with data](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb), [Batch vs Kubernetes vs local](../metaflow/notebooks/2026-07-19-batch-vs-kubernetes-vs-local-alt.ipynb)
- **dockerfiles** (1): [Metaflow development container](../metaflow/dockerfiles/metaflow-dev.Dockerfile)
- **templates** (13): [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md)
  - _…and 22 more under `metaflow/templates/` — browse the folder._

## Kubeflow · 75 files

- **primer:** [Kubeflow overview](../kubeflow/notes/0000-primer-kubeflow.md)
- **notes** (18): most recent → [Install KFP on Kind](../kubeflow/notes/2026-07-14-install-kfp-on-kind.md), [KFP v2 quickstart trip-ups](../kubeflow/notes/2026-07-11-kfp-v2-quickstart-trip-ups.md), [KFP v2 quickstart trip-ups](../kubeflow/notes/2026-07-06-kfp-v2-quickstart-trip-ups.md)
- **snippets** (10): [Verify KFP install](../kubeflow/snippets/2026-07-06-verify-kfp-install.py), [Install KFP SDK](../kubeflow/snippets/2026-08-04-install-kfp-sdk.py), [Conditional branching pipeline](../kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py), [Minimal KFP v2](../kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py)
- **scripts** (8): [Kubeflow CI/CD pipeline](../kubeflow/scripts/2026-07-23-kubeflow-ci-cd.sh), [KFP v2 pipeline conditionals](../kubeflow/scripts/2026-08-04-tried-kfp-v2-pipeline-conditionals.py), [Kubeflow health diagnosis](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- **configs** (3): [Pipeline resources](../kubeflow/configs/pipeline-resources.yaml), [Config README](../kubeflow/configs/README.md)
- **docs** (4): [KFP v1 vs v2 DSL](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md), [Kubeflow + MLflow tracking](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md), [Pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md)
- **manifests** (7): [Pipeline CI/CD workflow](../kubeflow/manifests/2026-07-27-kubeflow-pipeline-scaffold-ci-cd.yaml), [CI/CD workflow for scaffold](../kubeflow/manifests/2026-08-02-kubeflow-pipeline-scaffold-ci-cd.yml), [Minimal hello pipeline](../kubeflow/manifests/minimal-hello-pipeline.yaml), [Katib HPO random search](../kubeflow/manifests/katib-hpo-random-search-pytorch.yaml)
- **notebooks** (2): [Katib vs ParallelFor HPO](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb)
- **dockerfiles** (3): [Sklearn component Dockerfile](../kubeflow/dockerfiles/sklearn-train-component.Dockerfile)
- **templates** (22): [Kubeflow pipeline scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md), [Kubeflow + MLflow project](../kubeflow/templates/kubeflow-mlflow-project/README.md)
  - _…and 20 more under `kubeflow/templates/` — browse the folder._

## Weights & Biases · 72 files

- **primer:** [W&B primer](../wnb/notes/0000-primer-wnb.md)
- **notes** (15): most recent → [Install W&B and log my first run](../wnb/notes/2026-08-11-install-wandb-and-log-my-first-run.md), [W&B quickstart trip-ups](../wnb/notes/2026-07-11-first-wandb-quickstart-trip-ups.md), [Dashboard exploration](../wnb/notes/2026-07-09-explore-wandb-dashboard.md)
- **snippets** (9): [Log my first metric](../wnb/snippets/2026-08-11-log-my-first-metric.py), [First experiment SDK](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py), [Minimal tracking](../wnb/snippets/2026-06-06-minimal-tracking.py)
- **scripts** (5): [Custom sweep with early termination](../wnb/scripts/custom-sweep-early-termination.py), [Sweep and eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py), [Hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py)
- **configs** (6): [Declarative sweep config](../wnb/configs/2026-06-17-declarative-sweep-config.yaml), [First sweep config](../wnb/configs/2026-06-08-first-sweep-config.yaml), [Sweep config](../wnb/configs/sweep_config.yaml)
- **docs** (5): [Artifact + Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md), [Artifact tracking in data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md), [W&B quickstart trip-ups](../wnb/docs/wandb-quickstart-trip-ups.md)
- **manifests** (5): [CI/CD workflow manifest](../wnb/manifests/2026-07-13-wandb-ci-cd-workflow.yaml), [Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml), [W&B PyTorch scaffold CI/CD](../wnb/manifests/2026-08-26-wandb-pytorch-scaffold-ci-cd.yaml)
- **notebooks** (3): [Sweep config vs Python API](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb), [Run comparison with parallel coords](../wnb/notebooks/compare-runs-parallel-coords-correlation-diff.ipynb), [Comparing W&B Artifacts vs MLflow Model Registry](../wnb/notebooks/comparing-wb-artifacts-vs-mlflow-model-registry.ipynb)
- **templates** (24): [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md), [W&B + PyTorch scaffold](../wnb/templates/wandb-pytorch-scaffold/README.md), [W&B + PyTorch CI/CD scaffold](../wnb/templates/wandb-pytorch-ci-scaffold/README.md)
  - _…and 21 more under `wnb/templates/` — browse the folder._

## MLflow · 52 files

- **primer:** [MLflow concepts and setup](../mlflow/notes/0000-primer-mlflow.md)
- **notes** (7): [UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md), [Quickstart trip-ups (Jul 2026)](../mlflow/notes/2026-07-01-mlflow-quickstart-trip-ups.md), [First MLflow server](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- **snippets** (13): [MLflow tracking quickstart](../mlflow/snippets/2026-07-14-mlflow-tracking-quickstart.py), [Minimal autologging](../mlflow/snippets/2026-07-02-minimal-autologging.py), [End-to-end autologging pipeline](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py)
- **scripts** (5): [Experiment comparison + promotion](../mlflow/scripts/experiment-compare-and-promote.py), [End-to-end experiment](../mlflow/scripts/2026-07-06-end-to-end-experiment.py), [End-to-end experiment](../mlflow/scripts/2026-07-05-end-to-end-experiment.py)
- **configs** (9): [Sklearn model serving project](../mlflow/configs/sklearn-model-serving-project.yaml), [Tracking server Postgres+S3](../mlflow/configs/2026-07-14-tracking-server-postgres-s3.yaml), [Tracking server Postgres+S3](../mlflow/configs/2026-07-06-tracking-server-postgres-s3.yaml)
- **docs** (4): [Comparing model versions](../mlflow/docs/comparing-model-versions.md), [Production tracking server with Nginx auth](../mlflow/docs/production-tracking-server-nginx-auth.md), [MLflow + W&B hybrid tracking](../mlflow/docs/integrating-mlflow-with-weights-and-biases.md)
- **notebooks** (3): [Experiment comparison via Search API](../mlflow/notebooks/mlflow-experiment-comparison-search-api.ipynb), [Exploring runs, experiments, and model registry](../mlflow/notebooks/2026-07-09-exploring-runs-experiments-and-model-registry.ipynb), [Autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb)
- **dockerfiles** (4): [Tracking server Postgres+MinIO](../mlflow/dockerfiles/tracking-server-postgres-minio/README.md)
- **templates** (7): [MLflow model registry scaffold](../mlflow/templates/mlflow-model-registry-scaffold/README.md)
  - _…and 6 more under `mlflow/templates/` — browse the folder._

## Feast · 15 files

- **primer:** [Feast overview](../feast/notes/0000-primer-feast.md)
- **notes** (5): most recent → [Follow Feast quickstart](../feast/notes/2026-08-02-follow-feast-quickstart.md), [Parquet offline store (Jul 23)](../feast/notes/2026-07-23-install-feast-parquet-offline-store.md), [Parquet offline store (Jul 22)](../feast/notes/2026-07-22-install-feast-parquet-offline-store.md), [Install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- **docs:** [Online vs offline feature serving](../feast/docs/comparing-online-vs-offline-serving.md) — when to use `get_historical_features()` vs `get_online_features()`
- **snippets** (3): [Minimal feature retrieval](../feast/snippets/2026-08-02-minimal-feature-retrieval.py), [Register data source and inspect schema](../feast/snippets/2026-07-23-register-data-source-and-inspect-schema.py), [First feature view](../feast/snippets/tried_first_feature_view.py)
- **scripts** (2): [Entity/FeatureView historical retrieval](../feast/scripts/2026-07-22-entity-and-featureview-historical-retrieval.py), [Feature retrieval pipeline](../feast/scripts/feature-retrieval-pipeline.py)
- **configs** (4): [Feature store Redis Parquet config](../feast/configs/2026-08-02-feast-feature-store-redis-parquet.yaml), [Training/serving config](../feast/configs/feature-store-training-serving.yaml), [feature_store.yaml](../feast/configs/feature_store.yaml), [Config README](../feast/configs/README.md)

## DVC · 14 files

- **primer:** [DVC concepts and setup](../dvc/notes/0000-primer-dvc.md)
- **notes** (4): most recent → [Install DVC and log first dataset version](../dvc/notes/2026-08-13-install-dvc-and-log-first-dataset-version.md), [Get started trip-ups](../dvc/notes/2026-06-05-get-started.md), [First dataset version](../dvc/notes/2026-05-26-first-dataset-version.md)
- **snippets** (2): [Minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py), [DVC pipeline shell](../dvc/snippets/tried_dvc_pipeline.sh)
- **scripts** (5): [End-to-end DVC CLI walkthrough](../dvc/scripts/2026-07-22-dvc-end-to-end.sh), [Repro + metrics diff end-to-end](../dvc/scripts/2026-07-28-dvc-repro-metrics-diff.sh), [Init DVC and track dataset](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- **configs** (3): [dvc.yaml](../dvc/configs/dvc.yaml), [Pipeline YAML](../dvc/configs/pipeline.yaml), [Stage pipeline config](../dvc/configs/2026-07-28-dvc-stage-pipeline.yaml)

## ZenML · 11 files

- **primer:** [ZenML overview](../zenml/notes/0000-primer-zenml.md)
- **notes** (3): most recent → [Install ZenML and explore CLI](../zenml/notes/2026-08-22-install-zenml-and-explore-cli.md), [First dashboard and stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md)
- **snippets** (2): [First training pipeline](../zenml/snippets/tried_first_training_pipeline.py), [Log first pipeline run](../zenml/snippets/2026-08-23-log-first-pipeline-run.py)
- **scripts:** [Multi-step ZenML+MLflow pipeline](../zenml/scripts/2026-07-13-multi-step-zenml-mlflow-pipeline.py)
- **configs** (3): [Stack with MLflow+S3](../zenml/configs/2026-07-12-zenml-stack-mlflow-s3.yaml), [ZenML stack config](../zenml/configs/zenml-stack.yaml), [Minimal pipeline config](../zenml/configs/2026-08-23-minimal-pipeline-config.yaml)
- **notebooks:** [Parent-child pipelines and artifact lineage](../zenml/notebooks/2026-07-14-parent-child-pipelines-artifact-lineage.ipynb)

## ClearML · 8 files

- **primer:** [ClearML orchestration](../clearml/notes/0000-primer-clearml-orchestration.md)
- **notes** (6): most recent → [Install ClearML and first experiment](../clearml/notes/2026-08-22-install-clearml-and-first-experiment.md), [Agent first tasks](../clearml/notes/2026-07-23-clearml-agent-first-tasks.md), [Pitfalls](../clearml/notes/2026-07-12-clearml-pitfalls.md)
- **snippets:** [Install and first task](../clearml/snippets/tried_install_and_first_task.py)
- **configs:** [Remote GPU execution](../clearml/configs/2026-07-14-remote-gpu-execution.yaml)

## Metaflow crossover · 7 files

- **docs:** [Metaflow Argo vs Kubeflow Pipelines](../mfl/docs/metaflow-argo-vs-kubeflow-pipelines.md) — Comparing orchestration backends for Metaflow deployments
  - _…and 3 more under `mfl/docs/` — browse the folder._
- **scripts:** [First flow data transform](../mfl/scripts/2026-08-12-first-flow-data-transform.py)
- **manifests:** [Metaflow scaffold CI/CD manifest](../mfl/manifests/2026-08-13-metaflow-project-scaffold-ci-cd.yaml)
- **configs:** [Metaflow scaffold CI/CD workflow](../mfl/configs/2026-08-12-metaflow-project-scaffold-ci-cd.yaml)

## MLflow first-experiments · 6 files

- **notes:** [Install MLflow and log first experiment](../mlf/notes/2026-08-12-install-mlflow-first-experiment.md) — First experiment with the MLflow Python SDK
- **snippets:** [Install MLflow and log first experiment](../mlf/snippets/2026-08-01-install-mlflow-first-experiment.py) — Install MLflow and log your first experiment with the Python SDK
- **scripts:** [Run first MLflow experiment](../mlf/scripts/2026-08-02-run-first-mlflow-experiment.py) — Install MLflow and log your first experiment with the Python SDK
- **manifests** (3): [MLflow UI Kubernetes manifest](../mlf/manifests/mlflow-ui-kubernetes.yaml), [MLflow Model Registry CI/CD manifest](../mlf/manifests/2026-08-09-mlflow-model-registry-ci-cd.yaml), [MLflow model registry scaffold CI/CD](../mlf/manifests/mlflow-model-registry-scaffold-ci-cd.yaml)

## KServe · 6 files

- **primer:** [KServe overview](../kserve/notes/0000-primer-kserve.md)
- **notes:** [KServe quickstart trip-ups](../kserve/notes/2026-08-22-kserve-quickstart-trip-ups.md) — Gotchas from the KServe quickstart
- **snippets** (2): [Custom predictor with explainer](../kserve/snippets/2026-07-14-custom-predictor-explainer.py), [First InferenceService](../kserve/snippets/first_inferenceservice.py)
- **configs:** [Minimal sklearn InferenceService](../kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml)
- **manifests:** [Flowers sample](../kserve/manifests/2026-08-27-flowers-sample.yaml) — Sample InferenceService for the flowers model

## kub (KFP SDK) · 6 files

- **configs** (3): [Minimal Kubeflow pipeline](../kub/configs/2026-08-11-minimal-kubeflow-pipeline.yaml), [Kind config](../kub/configs/kind-config.yaml), [Pipeline YAML](../kub/configs/pipeline.yaml)
- **scripts:** [KFP v2 branching and parallel pipeline](../kub/scripts/2026-08-07-kfp-v2-branching-parallel-pipeline.py)
- **manifests** (2): [KFP pipeline deployment manifest](../kub/manifests/2026-08-06-kfp-pipeline-deployment-manifest.yaml), [Pipeline scaffold CI/CD](../kub/manifests/kubeflow-pipeline-scaffold-ci-cd.yaml)

## Seldon Core · 5 files

- **primer:** [Seldon Core overview](../seldon/notes/0000-primer-seldon-core.md)
- **notes:** [Seldon vs KServe comparison](../seldon/notes/2026-07-12-seldon-vs-kserve-sklearn.md)
- **snippets:** [Install and first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py)
- **manifests:** [SeldonDeployment manifest](../seldon/manifests/seldondeployment.yaml)
- **configs:** [SeldonDeployment config](../seldon/configs/seldondeployment.yaml)

## Databricks · 4 files

- **notes:** [Databricks primer](../databricks/notes/0000-primer-databricks.md) — Unity Catalog, workspace setup, and first experiments
- **snippets:** [First Databricks run](../databricks/snippets/2026-08-27-first-databricks-run.py) — First-contact script for running a Databricks workload
- **scripts:** [Model promotion to Unity Catalog](../databricks/scripts/2026-07-14-model-promotion-unity-catalog.py)
- **configs:** [Unity Catalog setup](../databricks/configs/2026-07-14-unity-catalog-setup.yaml)

## BentoML · 3 files

- **primer:** [Install BentoML and first service](../bentoml/notes/2026-08-22-install-bentoml-and-first-service.md) — First-contact notes for BentoML service setup
- **snippets:** [First BentoML prediction](../bentoml/snippets/2026-08-22-first-bentoml-prediction.py) — Minimal prediction snippet for BentoML
- **configs:** [Minimal BentoML service](../bentoml/configs/2026-08-22-minimal-bentoml-service.yaml) — Minimal BentoML service YAML

## Evidently AI · 3 files

- **primer:** [Evidently AI and data drift](../evidently/notes/0000-primer-evidently.md)
- **notes:** [Report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md)
- **snippets:** [First drift report](../evidently/snippets/first_drift_report.py)