---
last_verified: 2026-07-30
tool_version: n/a
---

# W&B + PyTorch Project Scaffold

A template project for Weights & Biases experiment tracking with PyTorch training, hyperparameter sweeps, artifact logging, and CI/CD integration.

## Purpose

This scaffold provides a minimal working structure for a PyTorch project that uses W&B for experiment tracking. It includes a training script with metric and artifact logging, a sweep configuration for hyperparameter optimization, and a GitHub Actions workflow for automated CI/CD runs.

## When to use

Starting a new PyTorch project that needs W&B experiment tracking. The scaffold assumes you are already familiar with basic PyTorch training loops and W&B concepts.

## Prerequisites

- Python 3.9 or later
- A W&B account and API key
- A GitHub repository with Actions enabled
- PyTorch and the dependencies listed in `requirements.txt`

## Project structure

```
wandb-pytorch-scaffold/
├── README.md
├── requirements.txt
├── train.py                  # PyTorch training script with W&B tracking
├── sweep.py                  # Sweep runner script
├── configs/
│   └── sweep-config.yaml    # W&B sweep configuration
├── components/              # Reusable training components
│   └── __init__.py
└── .github/workflows/
    └── ci-cd.yml           # GitHub Actions CI/CD workflow
```

## Steps

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure W&B authentication

Set the `WANDB_API_KEY` environment variable or add it as a GitHub secret. The CI/CD workflow references this secret for automated runs.

### 3. Run training locally

```bash
python train.py --epochs 10 --batch-size 32 --lr 0.001
```

### 4. Run a hyperparameter sweep

```bash
wandb sweep configs/sweep-config.yaml
wandb agent
```

### 5. CI/CD pipeline

Push to the repository to trigger the GitHub Actions workflow, which runs linting, training, and sweep steps automatically.

## Verify

After running training, check the W&B dashboard to confirm that metrics, hyperparameters, and artifacts appear in the expected project and run.

## Common errors

- Missing `WANDB_API_KEY` causes `wandb.init()` to fail silently or prompt for login; export the key before running any script.
- Sweep early termination can occur if the sweep config specifies too few iterations; verify `min_iter` in the sweep config matches the expected training duration.