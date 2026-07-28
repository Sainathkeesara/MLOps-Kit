#!/bin/bash
# last_verified: 2026-07-28 · DVC n/a
# first dvc repro + metrics diff end-to-end
# I'm setting up a tiny pipeline with a metrics file,
# then running repro and comparing metrics across commits

pip install dvc
mkdir -p dvc-repro-demo && cd dvc-repro-demo
git init
dvc init
git add .
git commit -m "init dvc"

printf "features: 3\naccuracy: 0.82\n" > metrics.json
cat > dvc.yaml <<'EOF'
stages:
  train:
    cmd: python train.py
    metrics:
      - metrics.json
EOF

cat > train.py <<'EOF'
import json
with open("metrics.json", "w") as f:
    json.dump({"features": 4, "accuracy": 0.87}, f)
EOF

git add .
git commit -m "add pipeline and metrics"

dvc repro
dvc metrics diff
