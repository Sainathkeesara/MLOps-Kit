# kub-004 — Installing Kubeflow on Kind — what tripped me up

I had a Kind cluster running already (from the last attempt). Now I needed to actually install Kubeflow on it.

**Kubeflow Pipelines install**

I used the official manifests approach:

```
export PIPELINE_VERSION=2.1.0
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for=condition=established crd/applications.app.k8s.io --timeout=60s
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```

First `apply` creates the CRDs. Second one deploys the actual pipeline components into the `kubeflow` namespace.

**what tripped me up**

- The `kubectl wait` for CRDs timed out the first time. I ran it again and it worked — probably just needed a few more seconds for the API server to register them.
- Lots of pods stayed in `Pending` because the cluster didn't have enough resources. I had to bump Docker Desktop to 4 CPUs and 8 GB RAM, then delete and recreate the Kind cluster.
- The `platform-agnostic-pns` env is important — PNS stands for "Pipelines Notary Service"? Not sure. The default env uses Minio which needs PVs. PNS mode avoids that for local dev. I used it because I don't have a storage provisioner on Kind.
- After install, `kubectl get pods -n kubeflow` showed some `Init:0/1` pods. Giving it a few minutes fixed most of them.

**what's running now**

```
kubectl get pods -n kubeflow
```

I see `ml-pipeline`, `ml-pipeline-ui`, `metadata-writer`, `minio`, `mysql`, and `cache-server`. Most are Running. A couple took 2-3 minutes to become Ready.

**next step**

Try running a pipeline component on this cluster to make sure the whole thing actually works end-to-end.
