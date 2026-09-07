---
last_verified: 2026-09-07
tool_version: n/a
sources: []
---

# Documenting the kub folder

> First-day notes on what's actually in `kub/` and why it's separate from `kubeflow/`.

I opened the README Layout table and saw `kub/` listed as "Kubeflow Pipelines SDK configs, scripts, and manifests (KFP v2)". That's accurate but useless if I don't know what those configs actually do.

Looking inside `kub/`, I see three subfolders: `configs/`, `manifests/`, and `scripts/`. The configs hold YAML for a Kind cluster and a minimal pipeline. The manifests are Kubernetes resources for deploying the pipeline and a CI/CD workflow. The script is a Python file that builds a branching and parallel pipeline using the KFP v2 SDK.

The split between `kub/` and `kubeflow/` is about perspective. `kub/` is SDK-first — these are the files I write before I have a cluster running. `kubeflow/` is platform-first — it assumes Kubeflow is already deployed and covers the UI, CRDs, integration patterns, and heavier templates.

This note maps the folder contents so I can find the right file without digging around.

## What I'll cover next

I'll read through the configs and script to see how the KFP v2 compiler turns them into a deployable pipeline, then run the whole thing locally.
