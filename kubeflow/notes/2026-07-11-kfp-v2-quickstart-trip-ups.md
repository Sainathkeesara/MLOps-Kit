---
last_verified: 2026-07-11
tool_version: "2.16.1"
sources:
  - https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation
  - https://devopscube.com/kubeflow-pipelines/
  - https://www.kubeflow.org/docs/components/pipelines/v2/compile-a-pipeline
  - https://markaicode.com/howto/kubeflow-install-and-environment-variables-setup
  - https://medium.com/@sridharpillai/kubeflow-pipelines-locally-the-honest-guide-to-breaking-things-and-learning-9f0aaa04438e
  - https://devopscube.com/setup-kubeflow-pipelines-kubernetes/
---

# KFP v2 quickstart — what tripped me up

I went through the official Kubeflow Pipelines v2 quickstart to get a pipeline running.

## The steps I followed

1. Installed the kfp SDK: `pip install kfp`
2. Set up a Kind cluster with `kind create cluster`
3. Deployed KFP standalone using the manifests from the official installation guide
4. Compiled and ran a minimal pipeline

## Got stuck on

### 1. kustomize retry loop

The `kustomize build example | kubectl apply -f -` command failed the first time with CRD errors. A second run worked. The docs mention this is normal and to expect retries during first install.

### 2. kubectl port-forward needs the right namespace

I ran `kubectl port-forward svc/ml-pipeline-ui 8080:80` and got nothing. The service lives in the `kubeflow` namespace, not `default`. Adding `-n kubeflow` fixed it.

### 3. Image tag drift causes CrashLoopBackOff

Some example manifests reference `gcr.io/ml-pipeline/minio` with an old tag that no longer exists. MinIO gets stuck in `ImagePullBackOff`, which cascades into MLMD service failures and `ml-pipeline` API crashes. I patched the image to a valid tag and the pipeline came up.

### 4. Cert-manager and TLS setup

Native API mode failed until I checked cert-manager was installed and healthy. The cache-deployer requests a Kubernetes CSR for TLS, which some managed clusters deny by default. I removed cache-deployer and configured cert-manager for TLS instead, which fixed it.

### 5. Two-pod-per-step surprise

Every KFP v2 pipeline step runs in its own pod. I expected a shared filesystem or in-memory state across steps and was confused when local file writes disappeared between steps. Artifacts must be explicitly passed or stored in a shared location like MinIO or S3.

### 6. cache-deployer crashes on my cluster

The cache-deployer pod stayed in CrashLoopBackOff. On EKS and AKS the default Kubernetes CSR approval policy only lets Kubelet approve CSRs, so the cache-deployer's TLS request gets denied. I removed cache-deployer and configured cert-manager for TLS instead, which fixed it.

## What I'd try next

Set the namespace explicitly at the start next time to avoid mismatches. Also, I'd switch to just Pipelines (standalone) instead of the full distribution since I don't need the notebook server or Katib yet.
