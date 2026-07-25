# MLflow + Model Registry — Project Scaffold

A template project showing how to wire training, model registration, and serving into a repeatable pipeline using the MLflow Model Registry. The scaffold covers the full lifecycle: log a training run, register the resulting model, promote it through stages, and serve it from the registry.

## Purpose

MLflow Tracking records parameters, metrics, and artifacts per run. The Model Registry adds version management and stage transitions (Staging → Production → Archived) on top of those runs. This scaffold connects the two: training logs a run and auto-registers a model, registration handles stage transitions separately, and serving loads models directly from the registry URI.

## When to use

- You need to version models and control which version is in production.
- You want training, registration, and serving as separate, testable steps.
- You are setting up a CI/CD pipeline that trains a model, registers it, and optionally deploys it.

## Prerequisites

- Python 3.9+
- `mlflow` (`pip install mlflow`)
- A running MLflow Tracking Server (local or remote)
- `scikit-learn` (for the example training script)

## Project structure

```
mlflow-model-registry-scaffold/
├── README.md
├── requirements.txt
├── train.py              # Train a model, log to MLflow, register version
├── register.py           # CLI for version registration, promotion, listing
├── serve.py              # Serve a registered model via MLflow's built-in server
├── configs/
│   └── tracking-config.yaml   # MLflow tracking URI and model name defaults
├── tests/
│   ├── test_train.py          # Unit tests for training
│   └── test_register.py       # Unit tests for registration
└── .github/workflows/
    └── ci-cd.yml              # CI/CD: test, train, register
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure MLflow tracking

Edit `configs/tracking-config.yaml`:

```yaml
mlflow_tracking_uri: "http://localhost:5000"
experiment_name: "model-registry-demo"
registered_model_name: "IrisClassifier"
default_stage: "Staging"
```

The tracking URI can also be set via the `MLFLOW_TRACKING_URI` environment variable, which overrides the config.

### 3. Train and register

```bash
python train.py

# Register a specific run (or use the auto-registration from train.py)
python register.py register --run-id <run_id>
```

The `train.py` script logs parameters and metrics, then registers the model under the name configured in the tracking config. By default it creates a `Staging` version.

### 4. Promote a version

```bash
python register.py promote --version 1
python register.py list
```

### 5. Serve the model

```bash
python serve.py --model-uri models:/IrisClassifier/Staging --port 5001
```

This starts an MLflow model server on port 5001. Send a prediction request:

```bash
curl -X POST http://localhost:5001/invocations \
  -H "Content-Type: application/json" \
  -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}'
```

## Verify

1. Run `python -m pytest tests/ -v` — all tests pass.
2. Run `python train.py` — a new run appears in the MLflow UI under the experiment `model-registry-demo`.
3. Check the Model Registry in the MLflow UI — the model `IrisClassifier` has at least one version in `Staging`.
4. Run `python serve.py --model-uri models:/IrisClassifier/Staging` and curl the endpoint — a prediction is returned.

## Common errors

- **`MLFLOW_TRACKING_URI` not set** — the tracking server URI must be accessible. If the server is local, start it with `mlflow server --host 0.0.0.0 --port 5000`.
- **Model not found in registry** — the first `train.py` run registers the model. If `register.py` is used with a run that did not call `mlflow.sklearn.log_model(registered_model_name=...)`, the artifact path may differ. Use `runs:/<run_id>/model` as the model URI.
- **Server returns 404 on /invocations** — verify the model URI format. The correct form is `models:/<model_name>/<stage>` or `models:/<model_name>/<version>`.
