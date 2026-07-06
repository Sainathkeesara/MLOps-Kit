# Topics

> A map of what's here. For a beginner-to-advanced reading order, see [learning-path.md](learning-path.md).

## Concepts · 11 files

- **primer:** [Containerization](../docs/concepts/containerization/0000-primer-containerization.md)
- **primer:** [Data Versioning](../docs/concepts/data-versioning/0000-primer-data-versioning.md)
- **primer:** [Experiment Tracking](../docs/concepts/experiment-tracking/0000-primer-experiment-tracking.md) — with [exercises](../docs/concepts/experiment-tracking/snippets/tried_experiment_tracking_fundamentals.py) and [run comparison script](../docs/concepts/experiment-tracking/scripts/tried_comparing_training_runs.py)
- **primer:** [Feature Store](../docs/concepts/feature-store/0000-primer-feature-store.md)
- **primer:** [Model Registry](../docs/concepts/model-registry/0000-primer-model-registry.md) — with [exercises](../docs/concepts/model-registry/snippets/tried_model_registry_fundamentals.py)
- **primer:** [Model Serving](../docs/concepts/model-serving/0000-primer-model-serving.md)
- **primer:** [Monitoring & Drift](../docs/concepts/monitoring-drift/0000-primer-monitoring-drift.md)
- **primer:** [Pipeline Orchestration](../docs/concepts/pipeline-orchestration/0000-primer-pipeline-orchestration.md)

## ClearML · 3 files

- **primer:** [ClearML orchestration](../clearml/notes/0000-primer-clearml-orchestration.md)
- **notes** (2): [Web UI exploration](../clearml/notes/2026-06-22-clearml-web-ui-exploration.md)
- **scripts** (1): [Install and first task](../clearml/snippets/tried_install_and_first_task.py)

## DVC · 7 files

- **primer:** [DVC concepts and setup](../dvc/notes/0000-primer-dvc.md)
- **notes** (3): [First dataset version](../dvc/notes/2026-05-26-first-dataset-version.md), [Get started trip-ups](../dvc/notes/2026-06-05-get-started.md)
- **snippets** (2): [DVC pipeline shell](../dvc/snippets/tried_dvc_pipeline.sh), [Minimal data versioning](../dvc/snippets/minimal_dvc_versioning.py)
- **scripts** (1): [Init DVC and track dataset](../dvc/scripts/tried_init_dvc_and_track_dataset.sh)
- **configs** (1): [Pipeline YAML](../dvc/configs/pipeline.yaml)

## Evidently AI · 3 files

- **primer:** [Evidently AI and data drift](../evidently/notes/0000-primer-evidently.md)
- **notes:** [Report vs TestSuite APIs](../evidently/notes/2026-07-03-comparing-report-and-testsuite-apis.md)
- **snippets:** [First drift report](../evidently/snippets/first_drift_report.py)

## Feast · 5 files

- **primer:** [Feast overview](../feast/notes/0000-primer-feast.md)
- **notes** (2): [Install and first feature retrieval](../feast/notes/2026-06-03-install-feast-first-feature-retrieval.md)
- **configs** (2): [Feature store YAML](../feast/configs/feature_store.yaml)
- **snippets** (1): [First feature view](../feast/snippets/tried_first_feature_view.py)

## KServe · 3 files

- **primer:** [KServe overview](../kserve/notes/0000-primer-kserve.md)
- **configs** (1): [Minimal sklearn InferenceService](../kserve/configs/2026-07-04-minimal-sklearn-inferenceservice.yaml)
- **snippets** (1): [First InferenceService](../kserve/snippets/first_inferenceservice.py)

## Kubeflow · 62 files

- **primer:** [Kubeflow overview](../kubeflow/notes/0000-primer-kubeflow.md)
- **notes** (11): most recent → [KFP v2 SDK gotchas](../kubeflow/notes/2026-06-09-kfp-v2-sdk-gotchas.md), [Central dashboard exploration](../kubeflow/notes/2026-06-06-explore-central-dashboard.md), [Install on Kind](../kubeflow/notes/2026-05-30-install-kubeflow-on-kind.md)
- **snippets** (9): [KFP install verification](../kubeflow/snippets/2026-07-06-verify-kfp-install.py), [Conditional branching pipeline](../kubeflow/snippets/2026-06-15-conditional-branching-pipeline.py), [Minimal KFP v2](../kubeflow/snippets/2026-06-09-minimal-kfp-v2-end-to-end.py)
- **scripts** (5): [Component factory](../kubeflow/scripts/component_factory.py), [KFP component factory](../kubeflow/scripts/kfp_component_factory.py), [Kubeflow health diagnosis](../kubeflow/scripts/tried_diagnosing_kubeflow_health.sh)
- **configs** (2): [Pipeline resources](../kubeflow/configs/pipeline-resources.yaml)
- **docs** (4): [KFP v1 vs v2 DSL](../kubeflow/docs/choosing-between-kfp-v1-and-v2-dsl.md), [Kubeflow + MLflow tracking](../kubeflow/docs/kubeflow-mlflow-tracking-integration.md), [Pipeline debugging](../kubeflow/docs/kubeflow-pipeline-debugging.md)
- **manifests** (4): [Katib HPO random search](../kubeflow/manifests/katib-hpo-random-search-pytorch.yaml), [Pipeline job set](../kubeflow/manifests/2026-06-08-pipeline-job-set.yaml)
- **notebooks** (2): [Katib vs ParallelFor HPO](../kubeflow/notebooks/kfp-hp-tuning-katib-vs-parallelfor.ipynb)
- **dockerfiles** (4): [Sklearn component Dockerfile](../kubeflow/dockerfiles/sklearn-train-component.Dockerfile)
- **templates** (21): [Kubeflow pipeline scaffold](../kubeflow/templates/kubeflow-pipeline-scaffold/README.md), [Kubeflow + MLflow project](../kubeflow/templates/kubeflow-mlflow-project/README.md)
- _…and 21 more under `kubeflow/templates/` — browse the folder._

## Metaflow · 40 files

- **primer:** [Metaflow primer](../metaflow/notes/0000-primer-metaflow.md)
- **notes** (10): [CI/CD with GitHub Actions](../metaflow/notes/2026-06-12-ci-cd-with-github-actions.md), [Step decorator DAG ordering](../metaflow/notes/2026-06-08-step-decorator-dag-ordering.md), [UI and inspect run](../metaflow/notes/2026-06-06-explore-ui-and-inspect-run.md)
- **snippets** (5): [Minimal first flow](../metaflow/snippets/2026-06-06-minimal-first-flow.py), [Parameterized DAG](../metaflow/snippets/tried_parameterized_dag.py), [Model serving](../metaflow/snippets/tried_serving_model.py)
- **scripts** (4): [End-to-end experiment](../metaflow/scripts/2026-07-03-end-to-end-experiment.py), [Five-step ML pipeline](../metaflow/scripts/2026-06-12-five-step-ml-pipeline.py), [Batch inference splits](../metaflow/scripts/batch_inference_splits.py)
- **configs** (2): [Project scaffold config](../metaflow/configs/metaflow-project-scaffold.yaml)
- **docs** (3): [Resource management](../metaflow/docs/metaflow-resource-management.md), [Foreach vs @batch](../metaflow/docs/foreach-vs-batch.md), [Metaflow + W&B integration](../metaflow/docs/metaflow-wandb-integration.md)
- **manifests** (2): [AWS Batch infrastructure](../metaflow/manifests/aws-batch-infrastructure.yaml)
- **notebooks** (2): [Full run vs resume](../metaflow/notebooks/2026-06-17-full-run-vs-resume.ipynb), [End-to-end flow with data](../metaflow/notebooks/2026-05-28-first-end-to-end-flow-with-data.ipynb)
- **templates** (12): [Metaflow project scaffold](../metaflow/templates/metaflow-project-scaffold/README.md)
- _…and 8 more under `metaflow/templates/` — browse the folder._

## MLflow · 31 files

- **primer:** [MLflow concepts and setup](../mlflow/notes/0000-primer-mlflow.md)
- **notes** (7): [UI exploration](../mlflow/notes/2026-06-30-exploring-mlflow-ui.md), [Quickstart trip-ups (Jul 2026)](../mlflow/notes/2026-07-01-mlflow-quickstart-trip-ups.md), [First MLflow server](../mlflow/notes/2026-05-24-first-mlflow-server.md)
- **snippets** (12): [End-to-end autologging pipeline](../mlflow/snippets/2026-06-12-end-to-end-autologging-pipeline.py), [Minimal autologging](../mlflow/snippets/2026-07-02-minimal-autologging.py), [Model serving](../mlflow/snippets/2026-06-10-minimal-model-serving.py)
- **scripts** (3): [End-to-end experiment (Jul 6)](../mlflow/scripts/2026-07-06-end-to-end-experiment.py), [End-to-end experiment (Jul 5)](../mlflow/scripts/2026-07-05-end-to-end-experiment.py), [Custom model flavor](../mlflow/scripts/custom_model_flavor.py)
- **configs** (6): [Tracking server S3](../mlflow/configs/2026-07-01-tracking-server-s3.yaml), [MLproject](../mlflow/configs/MLproject), [Conda env](../mlflow/configs/conda.yaml)
- **docs** (2): [Comparing model versions](../mlflow/docs/comparing-model-versions.md), [Production tracking server with Nginx auth](../mlflow/docs/production-tracking-server-nginx-auth.md)
- **notebooks** (1): [Autologging vs manual tracking](../mlflow/notebooks/2026-06-01-autologging-vs-manual-tracking.ipynb)

## Seldon Core · 2 files

- **primer:** [Seldon Core overview](../seldon/notes/0000-primer-seldon-core.md)
- **snippets** (1): [Install and first deploy](../seldon/snippets/2026-07-04-install-and-first-deploy.py)

## Weights & Biases · 40 files

- **primer:** [W&B primer](../wnb/notes/0000-primer-wnb.md)
- **notes** (12): [W&B dashboard exploration (Jul 5)](../wnb/notes/2026-07-05-exploring-wandb-dashboard.md), [What's on the dashboard](../wnb/notes/2026-07-02-whats-on-the-wandb-dashboard.md), [Dashboard exploration (Jul 1)](../wnb/notes/2026-07-01-exploring-wandb-dashboard.md)
- **snippets** (8): [First experiment SDK](../wnb/snippets/2026-07-04-first-experiment-wb-sdk.py), [Minimal tracking](../wnb/snippets/2026-06-06-minimal-tracking.py), [Artifact logging](../wnb/snippets/tried_artifact_logging.py)
- **scripts** (3): [Sweep and eval pipeline](../wnb/scripts/sweep_and_eval_pipeline.py), [Hyperparameter sweep](../wnb/scripts/hyperparameter_sweep.py)
- **configs** (4): [Declarative sweep config](../wnb/configs/2026-06-17-declarative-sweep-config.yaml), [First sweep config](../wnb/configs/2026-06-08-first-sweep-config.yaml)
- **docs** (3): [Artifact + Model Registry workflow](../wnb/docs/artifact-model-registry-workflow.md), [Artifact tracking in data pipeline](../wnb/docs/artifact-tracking-in-data-pipeline.md)
- **manifests** (1): [Launch agent Docker Compose](../wnb/manifests/wandb-launch-agent-docker-compose.yaml)
- **notebooks** (1): [Sweep config vs Python API](../wnb/notebooks/2026-06-16-sweep-config-vs-python-api.ipynb)
- **templates** (8): [W&B CI/CD project scaffold](../wnb/templates/wandb-cicd-project/README.md)
- _…and 5 more under `wnb/templates/` — browse the folder._

## ZenML · 4 files

- **primer:** [ZenML overview](../zenml/notes/0000-primer-zenml.md)
- **notes** (2): [Dashboard and first stack](../zenml/notes/2026-06-19-first-dashboard-and-stack.md)
- **snippets** (1): [First training pipeline](../zenml/snippets/tried_first_training_pipeline.py)
- **configs** (1): [ZenML stack config](../zenml/configs/zenml-stack.yaml)
