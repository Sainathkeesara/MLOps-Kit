---
last_verified: 2026-07-06
tool_version: "2.16.1"
sources:
  - https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/
  - https://markaicode.com/howto/kubeflow-install-and-environment-variables-setup/
  - https://www.kubeflow.org/docs/started/installing-kubeflow/
---

# kub-025 — Following the KFP v2 quickstart and what tripped me up

I went through the official Kubeflow Pipelines v2 quickstart to get a pipeline running.

## The steps I followed

1. Installed the kfp SDK: `pip install kfp`
2. Set up a Kind cluster with `kind create cluster`
3. Deployed KFP standalone using the manifests from `https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/`
4. Compiled and ran a minimal pipeline

## Where I got stuck

**kustomize retry loop.** The `kustomize build example | kubectl apply -f -` command failed the first time with CRD errors. A second run worked — the kubeflow docs mention this is normal and to expect 10-15 minutes.

**kubectl port-forward needs the right namespace.** I ran `kubectl port-forward svc/ml-pipeline-ui 8080:80` and got nothing. The service lives in the `kubeflow` namespace, not `default`. Adding `-n kubeflow` fixed it.

**GCR images causing ImagePullBackOff.** Some example manifests still reference `gcr.io/kubeflow/pipelines/…` images. The repos moved to `ghcr.io/kubeflow/*`. Had to replace the registry prefix.

**Cert-manager version matters.** Native API mode failed until I checked the cert-manager version — needs v1.18.2+ for the admission webhook certificates.

## What I'd try next

Set `KUBEFLOW_NAMESPACE=kubeflow` at the start next time to avoid namespace mismatches. Also, I'd switch to just Pipelines (standalone) instead of the full distribution since I don't need the notebook server or Katib yet.
