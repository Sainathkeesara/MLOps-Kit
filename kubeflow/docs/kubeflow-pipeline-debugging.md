# Kubeflow pipeline debugging: infrastructure failures and pod log analysis

I was chasing a failed Kubeflow Pipelines run where the UI only showed a red node and `Exit code 1`. That is enough to know something broke, but not enough to fix it. This is the path I use when the failure looks infrastructural: bad image, no room on the node, OOM, missing files, or a pod that never started.

## Purpose

The goal is to move from the KFP run page to the actual Kubernetes pod and events behind the failed step. The KFP UI is useful for finding the run, but the useful debugging data usually lives in pod logs, pod events, the Argo workflow, and sometimes the pod filesystem while the pod is still running.

## Steps

### 1. Start from the failed KFP run

In the KFP dashboard, open the failed run and copy the run ID from the URL. In KFP v1-style URLs this is usually the value after `/runs/`. I also note the namespace used by the Kubeflow install, often `kubeflow` or a user namespace such as `kubeflow-user`.

```bash
RUN_ID=<run-id>
NAMESPACE=<namespace>
```

### 2. Find the workflow and pod labels

KFP runs are backed by Argo workflows. I first try the common run label:

```bash
kubectl get workflows.argoproj.io -n "$NAMESPACE" -l pipeline/runid="$RUN_ID" -o name
kubectl get pods -n "$NAMESPACE" -l pipeline/runid="$RUN_ID" -o wide
```

If that returns nothing, I do not assume another label key. I list workflows and inspect the labels on the workflow that matches the run:

```bash
kubectl get workflows.argoproj.io -n "$NAMESPACE"
kubectl get workflow <workflow-name> -n "$NAMESPACE" -o jsonpath='{.metadata.labels}'
```

Then I use the exact label key shown there. Some installs add their own labels, and KFP versions do not always agree.

### 3. Pick the failing pod

Once I have pods for the run, I look for `Failed`, `CrashLoopBackOff`, `OOMKilled`, `ImagePullBackOff`, or `Pending`:

```bash
kubectl get pods -n "$NAMESPACE" -l pipeline/runid="$RUN_ID" \
  -o custom-columns=NAME:.metadata.name,PHASE:.status.phase,REASON:.status.reason,NODE:.spec.nodeName
```

The pod name is usually more useful than the component display name from the UI, because Kubernetes names the pod that actually ran the container.

### 4. Read logs only after checking the container state

For a normal failed container, logs usually come from the main container:

```bash
kubectl logs -n "$NAMESPACE" <pod-name> -c main --tail=200
```

If there are sidecars, I try all containers before narrowing down:

```bash
kubectl logs -n "$NAMESPACE" <pod-name> --all-containers --tail=200
```

If the container restarted, the useful message may be in the previous instance:

```bash
kubectl logs -n "$NAMESPACE" <pod-name> -c main --previous
```

When `kubectl logs` is empty, I stop guessing and check events.

### 5. Use pod events for pods that never started

`ImagePullBackOff`, `ErrImagePull`, failed scheduling, and missing secrets often leave little or no application log. `describe` is better there:

```bash
kubectl describe pod -n "$NAMESPACE" <pod-name>
kubectl get events -n "$NAMESPACE" --sort-by=.lastTimestamp | tail -40
```

Patterns I have seen:
- `ImagePullBackOff` or `ErrImagePull`: image tag does not exist, registry is private, or the image pull secret is missing.
- `OOMKilled`: the process hit its memory limit.
- `Unschedulable`: requests are too high, node selectors are too narrow, or the cluster is under capacity.
- `exec format error`: the image was built for the wrong CPU architecture.

### 6. Check resources in the workflow

For OOM or scheduling failures, I look at the workflow YAML for the failing template:

```bash
kubectl get workflow <workflow-name> -n "$NAMESPACE" -o yaml
```

I look for `resources.requests`, `resources.limits`, `nodeSelector`, `tolerations`, and `activeDeadlineSeconds`. If the step is OOMing, I raise the memory limit in the component definition or KFP SDK resource settings, then rerun only the pipeline step if the pipeline supports retries.

### 7. Inspect partial artifacts carefully

KFP does not always publish artifacts for failed steps. The UI artifact tab may stay empty even when files exist inside the pod.

If the pod is still running, I first list the common KFP output locations:

```bash
kubectl exec -n "$NAMESPACE" <pod-name> -- find /tmp/outputs -maxdepth 3 -print 2>/dev/null
kubectl exec -n "$NAMESPACE" <pod-name> -- find /tmp/kfp_outputs -maxdepth 3 -print 2>/dev/null
```

For KFP v1-style components, outputs often live under `/tmp/outputs/<artifact-name>/data`. For KFP v2-style components, outputs are commonly under `/tmp/kfp_outputs/<artifact-name>`. If I find something useful while the pod is alive, I copy the directory out:

```bash
kubectl cp -n "$NAMESPACE" <pod-name>:/tmp/kfp_outputs ./kfp-outputs
```

If the pod has already terminated, `kubectl exec` is not a reliable artifact tool. At that point I check the artifact store configured for the pipeline, such as MinIO, S3, or GCS, and compare those paths with the workflow output definitions.

## Verify

After changing the image, resource limit, or artifact path, I rerun the pipeline and check the same run label again:

```bash
kubectl get pods -n "$NAMESPACE" -l pipeline/runid="$RUN_ID"
```

The fix is working when the failed pod no longer shows `OOMKilled`, `ImagePullBackOff`, or `Unschedulable`, the main-container log has a clean exit, and the expected artifact appears in the KFP UI or the configured artifact store.
