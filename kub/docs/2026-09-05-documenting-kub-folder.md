---
last_verified: 2026-09-05
tool_version: n/a
sources: []
---

# Documenting the kub folder

> First-day notes on what's actually in `kub/` and why it's separate from `kubeflow/`.

I was looking at the README Layout section and saw that `kub/` gets one line: "Kubeflow Pipelines SDK configs, scripts, and manifests (KFP v2)". That's technically correct but it doesn't tell me what's inside.

The `kub/` folder holds the raw KFP SDK artifacts — three configs, two manifests, and one script. The configs are YAML files for pipelines and a Kind cluster setup. The manifests are Kubernetes resources for deploying a KFP pipeline and a CI/CD workflow. The script is a Python example that builds a branching and parallel pipeline with the v2 SDK.

It's distinct from `kubeflow/` because `kub/` is SDK-first: it's the code you write before you have a full cluster. `kubeflow/` is platform-first: it assumes Kubeflow is running and covers UI exploration, CRDs, multi-tool integration, and heavier templates.

This doc just maps what's in `kub/` so I don't have to guess when I need a quick config reference.

## What I'll cover next

I should look at the actual configs and script in `kub/` to understand how they relate to the KFP v2 compiler, then try running the pipeline end-to-end.
