---
last_verified: 2026-07-05
tool_version: n/a
sources:
  - https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/
---

# Explore the Kubeflow Central Dashboard

> First-day notes after opening the Central Dashboard for the first time.

Tried the Kubeflow Central Dashboard today after getting it running locally. I wanted to see what each section does before building my first pipeline.

## What's on the landing page

The landing page shows a cluster topology view and overall CPU/memory usage. The top navigation has five main sections:

- **Pipelines** — opens the KFP UI in a separate browser tab
- **Notebook Servers** — launch Jupyter notebooks directly on the cluster
- **Katib** — hyperparameter tuning interface
- **Volumes** — list of persistent volume claims
- **Catalog** — sample workflows I can import

## What confused me

The "Kubeflow Pipelines SDK" checkbox in Notebook Servers felt unnecessary, so I unchecked it and picked a CPU-only image instead. The Pipelines tab also loads as a completely separate single-page app, which makes the Dashboard feel like it jumps contexts.

## Command I needed

To reach the UI from my laptop I run:
```bash
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```
The `-n kubeflow` flag is required because the service lives in the `kubeflow` namespace, not `default`.

## What I'll try next

Compile a hello-world pipeline from the SDK and watch a run execute inside the Pipelines UI.
