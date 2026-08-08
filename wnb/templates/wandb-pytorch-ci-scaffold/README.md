---
last_verified: 2026-08-08
tool_version: n/a
---

# W&B + PyTorch CI Scaffold

## Purpose
A project scaffold for PyTorch training with Weights & Biases experiment tracking, hyperparameter sweeps, model artifact logging, and GitHub Actions CI/CD. Provides a minimal working structure that can be cloned and adapted for new experiments.

## Project structure

```
wandb-pytorch-ci-scaffold/
├── README.md
├── requirements.txt
├── train.py                  # PyTorch training script with W&B tracking and artifact logging
├── sweep.py                  # Sweep runner script
├── configs/
│   └── sweep-config.yaml    # W&B bayesian sweep configuration
├── components/
│   └── __init__.py
└── .github/workflows/
    └── ci-cd.yml           # GitHub Actions lint → test → sweep → deploy pipeline
```

## Prerequisites

- Python 3.9 or later
- A W&B account and API key
- A GitHub repository with Actions enabled
- PyTorch and the dependencies listed in `requirements.txt`

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure W&B authentication

Set the `WANDB_API_KEY` environment variable locally and as a GitHub secret. The CI/CD workflow uses this secret for automated runs.

### 3. Run training locally

```bash
python train.py --epochs 10 --batch-size 32 --lr 0.001
```

### 4. Run a hyperparameter sweep

```bash
wandb sweep configs/sweep-config.yaml
wandb agent <sweep-id>
```

### 5. CI/CD pipeline

Push to the repository to trigger the GitHub Actions workflow, which runs linting, tests, a training smoke test, and a sweep step.

## Verify

After running training locally, confirm in the W&B dashboard that metrics, hyperparameters, and model artifacts appear in the expected project and run. After pushing, confirm the GitHub Actions workflow completes all jobs.

## Common errors

- Missing `WANDB_API_KEY` causes `wandb.init()` to fail or prompt for login; export the key before running any script.
- Sweep early termination can occur if `min_iter` in the sweep config is lower than the training script's logging frequency; align these values.
- PyTorch version mismatches between local and CI environments can cause CUDA-related import errors; pin versions in `requirements.txt`.
