# Kubeflow pipeline debugging: infrastructure failures and pod log analysis

I was chasing a failed pipeline run and the red status in KFP UI wasn't telling me much. The error was just `Exit code 1` with no stderr. This is what I did to find the real problem.

## Purpose

When a Kubeflow pipeline run fails, the KFP UI shows a red status but often doesn't reveal why — especially when the failure is infrastructure-related (OOM, image pull errors, node pressure). This covers how to dig into pod logs, K8s events, and recover partial outputs when the pipeline doesn't finish cleanly.

## Prerequisites

- A Kubeflow deployment (tested on v1.8+ with multi-node cluster)
- `kubectl` configured with the cluster context
- A failed pipeline run to inspect

## Steps

### 1. Identify the failing component in the KFP UI

Open the KFP dashboard, find the failed run, and click on the red component node. The "Output" panel shows what the pod saw — usually just that exit code. Note the component name and the run ID from the URL (`/pipeline/#/runs/<run-id>`).

### 2. Find the pod from the run

KFP pods follow `<pipeline-name>-<component-name>-<hash>` naming. The quickest lookup uses the run ID label:

```bash
kubectl get pods -l kubeflow.org/runid=<run-id> --all-namespaces
```

Note: Older KFP versions used `pipeline/runid` instead. If the above returns nothing, try:

```bash
kubectl get pods --all-namespaces | grep <component-name>
```

Failed pods stick around longer than succeeded ones, but both get garbage-collected eventually.

### 3. Check pod logs

Once you have the pod and namespace:

```bash
kubectl logs -n <namespace> <pod-name>
```

For containers with sidecars like `ml-pipeline-ui-metadata-writer`, target the specific container:

```bash
kubectl logs -n <namespace> <pod-name> -c <container-name>
```

I saw these patterns:
- `ImagePullBackOff` / `ErrImagePull` — image doesn't exist or registry unreachable
- `OOMKilled` — memory limit hit
- `Exceeded resources` / `NodeUnschedulable` — cluster lacks capacity
- `exec user process caused: exec format error` — wrong CPU architecture in image

### 4. Check pod events when logs are empty

If the pod never started, `kubectl logs` returns nothing. Use events instead:

```bash
kubectl describe pod -n <namespace> <pod-name>
```

This revealed: `Warning  FailedScheduling  30s  default-scheduler  0/3 nodes are available: 1 Insufficient memory, 2 Insufficient cpu.` The component requested more than any node could provide.

### 5. Recover output artifacts from a failed component

Some components write partial output before crashing. I pulled them from the pod's filesystem if it was still running or just completed:

```bash
kubectl exec -n <namespace> <pod-name> -- ls /tmp/
kubectl cp -n <namespace> <pod-name>:/tmp/output.json ./output.json
```

For Argo-based workflows, the workflow YAML contains output paths that can be checked:

```bash
kubectl get wf -n <namespace> <workflow-name> -o yaml
```

### 6. Check resource constraints in the workflow

The workflow YAML embeds the resource requests. For the failing template, look at:

```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "100m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

If I see `OOMKilled`, raising `limits.memory` in the component definition or `set_resources()` call usually fixes it.

## Verify

After bumping the memory limit on my component, I re-ran the pipeline and the step passed. I also validated the container itself by running it locally with the same constraints:

```bash
docker run --memory=512m <image> python main.py
```

This doesn't catch K8s-specific issues like image pull secrets, but it confirms the container works under the limits.

## Common errors I hit

- **"pod has been deleted"** — KFP garbage-collects after a TTL. If you need longer retention, check the workflow-controller config for TTL settings.
- **"cannot find label kubeflow.org/runid"** — older clusters used different label keys. Filter by component name instead.
- **No error in logs** — the pod may have been evicted before writing stderr. Check `kubectl describe pod` events and `kubectl top nodes` for cluster pressure.

This is one approach that worked for me. The official troubleshooting guide has more patterns, and the Katib docs cover tuning setup issues if you're hitting resource problems during hyperparameter sweeps.