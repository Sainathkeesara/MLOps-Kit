# Kubeflow Pipeline Project — Scaffold

A production-ready template project for Kubeflow Pipelines with CI/CD integration and comprehensive unit testing. This scaffold demonstrates how to structure a Kubeflow ML pipeline project for collaborative development, with automated testing in GitHub Actions and local development support.

## Purpose

Kubeflow Pipelines orchestrates containerized ML workflows on Kubernetes. This scaffold provides the foundational structure for:
- Multi-step pipeline definitions using KFP v2 SDK
- Extracted component logic for unit testing without cluster access
- CI/CD workflow that validates code changes and compiles pipelines
- Resource configuration and caching patterns via the component factory pattern

## When to use

- Building a new Kubeflow Pipelines project with test-driven development
- Teams requiring automated validation before pipeline deployment
- Projects transitioning from experimental to production pipelines
- Scenarios where pipeline reproducibility and testability are requirements

## Prerequisites

- Python 3.9+
- `kfp` SDK v2 (`pip install kfp>=2.0.0`)
- A Kubeflow cluster or local deployment (Kind / minikube / kubectl)
- GitHub repository with Actions enabled (for CI/CD)
- kubectl configured for cluster access

## Project structure

```
kubeflow-pipeline-scaffold/
├── README.md
├── requirements.txt
├── pipeline.py                           # KFP v2 pipeline definition
├── run.py                                # CLI entrypoint: compile and submit pipeline
├── components/
│   ├── __init__.py
│   ├── train.py                          # KFP training component with MLflow logging
│   └── evaluate.py                       # KFP evaluation component with metrics logging
├── scripts/
│   ├── train_logic.py                    # Extracted training logic for unit testing
│   └── evaluate_logic.py                 # Extracted evaluation logic for unit testing
├── tests/
│   ├── __init__.py
│   ├── conftest.py                       # Pytest configuration
│   └── test_components.py                # Unit tests for extracted component logic
└── .github/workflows/
    └── ci-cd.yml                         # GitHub Actions workflow: lint, test, compile
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Review the pipeline

`pipeline.py` defines a 2-step pipeline:
1. **train** — Trains a model using scikit-learn, logs to MLflow
2. **evaluate** — Evaluates the model and logs metrics to MLflow

Core logic is extracted to `scripts/` for unit testing independent of KFP runtime.

### 3. Run tests locally

```bash
pip install pytest
pytest tests/ -v
```

### 4. Compile the pipeline

```bash
python pipeline.py
```

This generates `pipeline.yaml` in the project root.

### 5. Submit to Kubeflow

```bash
python run.py --host https://your-kubeflow-host --experiment your-experiment
```

## Verify

1. Run `pytest tests/ -v` — all tests pass
2. Run `python pipeline.py` — pipeline compiles without errors
3. Submit via `python run.py` — pipeline appears in Kubeflow UI
4. Check GitHub Actions after push — CI workflow completes successfully

## Rollback

If a pipeline version causes issues:
1. Revert to previous commit in git
2. The CI workflow will re-run on the reverted code
3. Previously compiled `pipeline.yaml` remains unaffected until new compilation

## Common errors

- **Component image pull failures** — ensure container registry access in cluster. For private registries, create Kubernetes secrets.
- **Test import errors** — verify `components/` is in PYTHONPATH. Tests import functions directly without KFP runtime.
- **Pipeline compilation errors** — check KFP SDK version compatibility. v2 syntax differs from v1.

## References

- [Kubeflow Pipelines documentation](https://www.kubeflow.org/docs/components/pipelines/)
- [KFP v2 SDK reference](https://kubeflow-pipelines.readthedocs.io/en/stable/)