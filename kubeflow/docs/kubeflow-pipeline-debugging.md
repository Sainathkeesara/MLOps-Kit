# Kubeflow pipeline debugging: infrastructure failures and pod log analysis

## Purpose

When a Kubeflow pipeline run fails, the KFP UI shows a red status but often doesn't reveal why — especially when the failure is infrastructure-related (OOM, image pull errors, node pressure) rather than a Python exception. This doc covers how to diagnose those failures using pod logs, K8s events, and KFP's own artifact inspection.

## Prerequisites

- A Kubeflow deployment (tested on v1.8+ with multi-node cluster)
- `kubectl` configured with the cluster context
- A failed pipeline run to inspect

## Steps

### 1. Identify the failing component in the KFP UI

Open the KFP dashboard, find the failed run, and click on the red component node. The "Output" panel shows the error message as the pod sees it — sometimes just `Exit code 1` with no stderr. Note the component name and the run ID from the URL (`/pipeline/#/runs/<run-id>`).

### 2. Resolve the pod name from the run

KFP pods follow the pattern `<pipeline-name>-<component-name>-<hash>`. The quickest way to find the pod is to filter by the run ID label:

```bash
kubectl get pods -l pipeline/runid=<run-id> --all-namespaces
```

If the pod has already been garbage-collected (KFP deletes succeeded pods after a configurable TTL), check `kubectl get pods --all-namespaces | grep <component-name>` — failed pods typically aren't cleaned up immediately, but this isn't guaranteed.

### 3. Inspect pod logs

Once you have the pod name and namespace:

```bash
kubectl logs -n <namespace> <pod-name>
```

For a pod that ran multiple containers (sidecar patterns like ml-pipeline-ui-metadata-writer):

```bash
kubectl logs -n <namespace> <pod-name> -c <container-name>
```

Common log patterns:

| Log line | Likely cause |
|---|---|
| `ImagePullBackOff` / `ErrImagePull` | The component image doesn't exist or the registry is unreachable |
| `OOMKilled` | Container exceeded its memory limit |
| `Exceeded resources` / `NodeUnschedulable` | Cluster doesn't have enough CPU/memory to schedule the pod |
| `exec user process caused: exec format error` | Image built for the wrong architecture |
| `Back-off restarting failed container` | The entrypoint script exited immediately — usually a missing dependency |

### 4. Check pod events for scheduling failures

If the pod never started, `kubectl logs` returns nothing. Use events instead:

```bash
kubectl describe pod -n <namespace> <pod-name>
```

The `Events:` section at the bottom reveals scheduling issues. For example:

```
Warning  FailedScheduling  30s  default-scheduler  0/3 nodes are available: 1 Insufficient memory, 2 Insufficient cpu.
```

This means the component requested more resources than any node can provide — either increase the cluster size or lower the component's resource requests.

### 5. Inspect KFP artifacts (failed component output)

Some components write partial output before failing. Download the artifact from the KFP UI or via the SDK:

```python
import kfp
from kfp import dsl

client = kfp.Client()
run = client.get_run(run_id="<run-id>")

# List all output artifacts for the failed component
for metric in run.pipeline_runtime.workflow_manifest.get("status", {}).get("nodes", {}).values():
    if metric.get("displayName") == "<component-name>":
        print(metric.get("outputs", {}))
```

This is one way to do it; the SDK also exposes `client.get_run_detail()` which returns a richer object with typed artifacts when the component code used `dsl.Output()`.

### 6. Check the workflow YAML for resource constraints

When a pipeline compiles, resource requests are embedded in the Argo workflow YAML. Pull the workflow directly:

```bash
kubectl get wf -n <namespace> <workflow-name> -o yaml
```

Look for the failing template's `resources` block:

```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "100m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

If the pod is OOMKilled, raising `limits.memory` in the component definition or the pipeline's `set_resources()` call usually resolves it.

## Verify

After applying a fix (increase memory limit, fix image tag, add resource quota), re-run the pipeline from the KFP UI and confirm the previously failing step passes. A quicker check — if the fix was resource-related — is to run the component container locally with the same limits:

```bash
docker run --memory=512m --cpus=0.5 <image> python main.py
```

This won't catch K8s-specific issues (image pull secrets, node taints) but it validates the container itself under constrained resources.

## Common errors

- **"pod has been deleted"** — KFP garbage-collects pods after a TTL. If you need to debug after cleanup, enable artifact streaming in the KFP config so logs are persisted to MinIO or S3 before the pod is removed.
- **"cannot find label pipeline/runid"** — Older KFP versions used different label keys. Try `pipeline/run-id` (with hyphen) or filter by component name directly.
- **The KFP UI shows no error message** — This often means the pod was evicted before it could write stderr. Check `kubectl describe pod` events and the cluster node conditions via `kubectl top nodes`.

## References

- [KFP troubleshooting guide](https://www.kubeflow.org/docs/components/pipelines/troubleshooting/)
- [Kubeflow resource configuration](https://www.kubeflow.org/docs/components/pipelines/sdk/resource-management/)
