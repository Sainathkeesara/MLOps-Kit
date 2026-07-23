#!/bin/bash
# 2026-07-23-kubeflow-ci-cd.sh
#
# CI/CD steps for the kubeflow-pipeline-scaffold template.
# I'm writing this as a standalone bash script because the first PR
# accidentally produced a YAML workflow file instead — the auditor
# caught the artifact-type mismatch on Pass 3.

echo "=== Step 1: Lint ==="
flake8 components/ pipelines/ tests/ --max-line-length=100

echo ""
echo "=== Step 2: Test ==="
python -m pytest tests/ -v

echo ""
echo "=== Step 3: Compile pipeline ==="
python pipeline.py

echo ""
echo "=== Step 4: Deploy to Kubeflow Pipelines ==="
python run.py \
  --host "${KFP_HOST:-http://localhost:8080}" \
  --package pipeline.yaml \
  --experiment "kubeflow-pipeline-scaffold"
