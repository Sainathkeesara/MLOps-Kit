# Kubeflow Pipelines + MLflow Tracking — Project Scaffold

A template project showing how to wire MLflow experiment tracking into Kubeflow Pipelines components. Each pipeline step logs parameters and metrics to a shared MLflow Tracking server, and the pipeline compiles and runs via the KFP v2 Python SDK.

## Purpose

Kubeflow Pipelines orchestrates containerised ML workflows on Kubernetes. MLflow Tracking records parameters, metrics, and artifacts per run. This scaffold bridges the two: KFP components call `mlflow.*` APIs inside their containers, pointing at a common tracking server so every step of a pipeline appears under one experiment run.

## When to use

- You have a KFP cluster (or access to one) and want to track training runs.
- You need to compare results across pipeline executions, not just within a single component.
- You already use MLflow for experiment tracking and want to keep using it inside KFP.

## Prerequisites

- Python 3.9+
- `kfp` SDK v2 (`pip install kfp==2.*`)
- `mlflow` (`pip install mlflow`)
- A Kubeflow cluster or a local deployment (Kind / minikube)
- An MLflow Tracking Server URL — the template expects the `MLFLOW_TRACKING_URI` environment variable

## Project structure

```
kubeflow-mlflow-project/
├── README.md
├── requirements.txt
├── pipeline.py                  # KFP pipeline definition — wires components together
├── run.py                       # Compile and submit the pipeline
├── components/
│   ├── train.py                 # Training component — logs params & metrics to MLflow
│   └── evaluate.py              # Evaluation component — logs eval metrics to MLflow
└── configs/
    └── mlflow-config.yaml       # MLflow tracking URI and experiment name
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure MLflow tracking

Edit `configs/mlflow-config.yaml`:

```yaml
mlflow_tracking_uri: "http://mlflow-server.example.com:5000"
experiment_name: "kubeflow-pipeline-demo"
```

The tracking URI can also be set via the `MLFLOW_TRACKING_URI` env var at runtime, which overrides the config file.

### 3. Review the components

- `components/train.py` — loads a small scikit-learn dataset, trains a model, logs `alpha` and `l1_ratio` as parameters and `rmse` / `mae` as metrics.
- `components/evaluate.py` — loads the trained model and a hold-out set, logs eval metrics.

Both components accept `mlflow_tracking_uri` and `experiment_name` as inputs so the pipeline can pass them through.

### 4. Compile and run

```bash
python pipeline.py              # compiles to pipeline.yaml
python run.py                   # submits to KFP and starts a run
```

Alternatively, upload `pipeline.yaml` through the Kubeflow Central Dashboard.

## Verify

1. Open the Kubeflow Central Dashboard → **Pipelines** → your run.
2. Open the MLflow UI and find the experiment named in the config — each pipeline step appears as a separate run under the same experiment.
3. Compare parameter/metric values between pipeline executions in the MLflow compare view.

## Common errors

- **`MLFLOW_TRACKING_URI` not set** — the component container needs the env var or the pipeline input. Set it in the component decorator or pass it through pipeline parameters.
- **Tracking server unreachable** — the KFP cluster must be able to resolve the tracking server host. If running locally, use `host.docker.internal` or a service DNS name.
- **Run shows in MLflow but under different experiment names** — verify every component receives the same `experiment_name` string. A typo creates a separate experiment.
