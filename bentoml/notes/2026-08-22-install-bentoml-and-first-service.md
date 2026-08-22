---
last_verified: 2026-08-22
tool_version: "—"
sources:
  - https://theneuralbase.com/bentoml/learn/beginner/python-3-9-required/
  - https://theneuralbase.com/bentoml/learn/beginner/verify-install/
  - https://github.com/bentoml/BentoML/
  - https://theneuralbase.com/bentoml/learn/beginner/pip-install-bentoml/
---

# Install BentoML and produce my first service

> First-day notes for someone installing BentoML for the first time. Personal voice, plain language.

## What I did

Ran `pip install -U bentoml` in a fresh venv after checking `python --version` — BentoML 1.x needs Python ≥ 3.9, and 3.8 throws cryptic import errors. Confirmed `which bentoml` matched `which python` to avoid the #1 first-day gotcha: virtual-environment mismatch that causes "command not found" or silent failures.

## First service

Created a minimal service that loads a scikit-learn model and exposes `/predict`. Model loading belongs in `__init__` so the service initializes cleanly. Started with `bentoml serve service.py:svc`. Hit a 422 on the first POST because my JSON field names didn't match the API parameters. Fixed the names and got predictions back.

## What tripped me up

Docker layer caching retained stale model code across redeploys. Ran `docker system prune` before rebuilding to clear stale layers.
