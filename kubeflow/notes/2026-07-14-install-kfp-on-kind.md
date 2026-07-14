---
last_verified: 2026-07-14
tool_version: "2.17.0"
sources:
  - https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/
  - https://markaicode.com/howto/kubeflow-setup-and-configuration-guide
---

# kub-033 — Installing Kubeflow Pipelines standalone on Kind

I wanted to try KFP without spinning up a full Kubeflow deployment. The standalone install worked, but there were a few surprises.

## Steps I followed

1. Created a Kind cluster: `kind create cluster --name kfp`
2. Downloaded the KFP manifests: `export PIPELINE_VERSION=2.4.0` then `kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"`
3. Applied the environment-scoped resources with `kubectl wait` for CRDs
4. Port-forwarded the UI: `kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80`

## What tripped me up

- **Namespace matters.** The default install puts everything in `kubeflow`, not `default`. I kept hitting `kubectl get pods` with no results until I added `-n kubeflow`.
- **Apply twice.** The first `kubectl apply` fails on CRD ordering — the docs say to just run it again and the second pass works.
- **Docker resource limits.** On a 8 GB laptop, some pods (especially MinIO and MySQL) got OOMKilled. I raised Docker's memory limit and restarted the cluster.

## The UI

Once the port-forward was up, `http://localhost:8080` showed the KFP dashboard with experiments, runs, and pipelines sections. I created a "hello world" pipeline from the "Samples" tab and it ran in about 90 seconds.
