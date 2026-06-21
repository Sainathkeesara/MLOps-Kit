# Weights & Biases Experiment Tracking — CI/CD Project Scaffold

A template project demonstrating W&B experiment tracking integrated with GitHub Actions CI/CD for automated model training, hyperparameter sweeps, and deployment pipeline.

## Purpose

W&B provides experiment tracking and model registry capabilities. This scaffold shows how to wire W&B into a CI/CD pipeline that runs on GitHub Actions: training steps automatically log metrics and artifacts, sweeps explore hyperparameters, and registered models can be promoted through staging to production.

## When to use

- You want to track every training run in your CI/CD pipeline
- Hyperparameter optimization should happen automatically on PRs
- Your ML team uses W&B for experiment governance and model registry
- You need to compare model versions across pipeline executions

## Prerequisites

- Python 3.9+
- `wandb` Python SDK (`pip install wandb`)
- GitHub repository with Actions enabled
- W&B API key configured as GitHub secret (`WANDB_API_KEY`)
- scikit-learn for the example training workflow

## Project structure

```
wandb-cicd-project/
├── README.md
├── requirements.txt
├── train.py                  # Training script with W&B tracking
├── sweep.py                  # Hyperparameter sweep configuration
├── evaluate.py               # Evaluation script for best model selection
├── .github/workflows/
│   └── ci-cd.yml             # GitHub Actions workflow for training and deployment
└── configs/
    └── sweep-config.yaml     # W&B sweep configuration
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure W&B

Set the `WANDB_API_KEY` environment variable or add it as a GitHub secret. The CI/CD workflow uses this token to authenticate W&B runs.

### 3. Run training locally

```bash
python train.py --n-estimators 100 --max-depth 5
```

### 4. Run hyperparameter sweep

```bash
wandb sweep configs/sweep-config.yaml
wandb agent <entity>/<project>/<sweep_id>
```

### 5. CI/CD pipeline

Push to main branch to trigger the training workflow. The workflow:
- Installs dependencies
- Runs training with default parameters
- Uploads model artifact to W&B
- Logs metrics for comparison

## Verify

1. Check W&B UI → Runs tab for logged metrics and parameters
2. Check W&B UI → Artifacts tab for model artifacts
3. Review GitHub Actions run logs for pipeline execution status