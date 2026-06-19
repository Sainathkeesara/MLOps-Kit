# Wiring Kubeflow Pipelines to an in-cluster MLflow tracking server

## Purpose

Kubeflow Pipeline components run as containers inside the same Kubernetes cluster. When an MLflow tracking server is also running in that cluster, pipeline steps can log parameters, metrics, and artifacts directly to it without routing traffic through the public internet. This doc covers the wiring — environment variables, service DNS, and credential mounting — needed to make the connection work reliably.

## Prerequisites

- Kubeflow 1.7+ with KFP v1 or v2 installed on Kubernetes.
- MLflow tracking server deployed in the same cluster (e.g., in namespace `mlflow-system`). The server is exposed via a Kubernetes Service.
- Pipeline components that use the MLflow Python SDK (`mlflow`) to log runs.

## Steps

### 1. Confirm the MLflow Service DNS

Inside the cluster, a Service named `mlflow` in namespace `mlflow-system` resolves as:

```
http://mlflow.mlflow-system.svc.cluster.local:5000
```

Verify reachability from a temporary pod:

```bash
kubectl run --rm -it test-mlflow --image=python:3.10-slim --restart=Never \
  -- python -c "import urllib.request; print(urllib.request.urlopen('http://mlflow.mlflow-system.svc.cluster.local:5000/health').read())"
```

The response should include `{ "status": "OK" }` or similar. If this step fails, the MLflow Service may not be running or the port is wrong — check `kubectl get svc -n mlflow-system`.

### 2. Set the tracking URI in each component

Every pipeline component that calls `mlflow.log_param()`, `mlflow.log_metric()`, or `mlflow.start_run()` must see `MLFLOW_TRACKING_URI` pointing to the in-cluster MLflow server.

**KFP v2 (decorator-based `@component`):**

```python
from kfp import dsl
from kfp.dsl import component

@component(
    base_image="python:3.10-slim",
    packages_to_install=["mlflow"],
)
def train_and_log(
    learning_rate: float,
    mlflow_tracking_uri: str,
) -> None:
    import mlflow

    mlflow.set_tracking_uri(mlflow_tracking_uri)
    mlflow.set_experiment("kubeflow-pipeline")

    with mlflow.start_run():
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_metric("accuracy", 0.95)

@dsl.pipeline(name="train-pipeline")
def train_pipeline(learning_rate: float = 0.01):
    train_and_log(
        learning_rate=learning_rate,
        mlflow_tracking_uri="http://mlflow.mlflow-system.svc.cluster.local:5000",
    )
```

Passing the URI as a parameter keeps the component testable — you can supply a local URI when running outside the cluster.

**KFP v1 (container op):**

```python
from kfp import dsl
from kfp.dsl import ContainerOp

def train_op(learning_rate: float) -> ContainerOp:
    return dsl.ContainerOp(
        name="train",
        image="python:3.10-slim",
        command=["python", "-c", """
import mlflow
mlflow.set_tracking_uri("http://mlflow.mlflow-system.svc.cluster.local:5000")
mlflow.set_experiment("kubeflow-pipeline")
with mlflow.start_run():
    mlflow.log_param("lr", $0)
    mlflow.log_metric("acc", 0.95)
""".format(learning_rate)],
    ).set_display_name("Train")
```

A cleaner approach for v1 is to set the environment variable directly on the container op:

```python
train = train_op(learning_rate=0.01)
train.container.add_env_variable(
    k8s_client.V1EnvVar(
        name="MLFLOW_TRACKING_URI",
        value="http://mlflow.mlflow-system.svc.cluster.local:5000",
    )
)
```

### 3. Handle authentication if the MLflow server requires it

If the MLflow server uses HTTP Basic Auth or a token:

**Basic Auth — pass credentials in the URI:**

```python
mlflow.set_tracking_uri("http://user:password@mlflow.mlflow-system.svc.cluster.local:5000")
```

**Token-based auth — set environment variables:**

```python
import os
os.environ["MLFLOW_TRACKING_URI"] = "http://mlflow.mlflow-system.svc.cluster.local:5000"
os.environ["MLFLOW_TRACKING_TOKEN"] = os.environ.get("MLFLOW_TOKEN", "")
```

Store the token as a Kubernetes Secret and mount it as an environment variable in the pipeline component:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mlflow-auth
  namespace: kubeflow-user
type: Opaque
stringData:
  MLFLOW_TOKEN: "your-token-here"
```

Then reference the secret in the KFP v2 component:

```python
@component(
    base_image="python:3.10-slim",
    packages_to_install=["mlflow"],
)
def train_with_auth(learning_rate: float):
    import os
    import mlflow

    mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
    mlflow.set_experiment("kubeflow-pipeline")
    with mlflow.start_run():
        mlflow.log_param("learning_rate", learning_rate)
```

And mount the secret when constructing the pipeline:

```python
from kubernetes import client as k8s_client

train = train_with_auth(learning_rate=0.01)
train.set_env_variable(
    name="MLFLOW_TRACKING_URI",
    value="http://mlflow.mlflow-system.svc.cluster.local:5000",
)
train.set_env_variable(
    name="MLFLOW_TRACKING_TOKEN",
    value_from=k8s_client.V1EnvVarSource(
        secret_key_ref=k8s_client.V1SecretKeySelector(
            name="mlflow-auth", key="MLFLOW_TOKEN",
        )
    ),
)
```

### 4. Confirm artifact logging

MLflow logs artifacts to its configured artifact store (local filesystem, S3, GCS, or MinIO). When the tracking server runs in-cluster and uses a local `./mlruns` directory, artifacts are stored on the server pod's disk. This works for demos but is lost on pod restart.

For persistent artifact storage, configure the MLflow server with an external store (S3/GCS/MinIO) and ensure the KFP component pods have the necessary credentials to write to the store when using MLflow's artifact logging via the server proxy. In most setups, if the tracking URI points to the in-cluster server, artifact logging goes through the server and does not require direct store access from the component pod.

## Verify

1. Run the pipeline from the KFP dashboard or SDK.
2. Open the MLflow UI (e.g., `http://mlflow.mlflow-system.svc.cluster.local:5000` or its ingress URL).
3. Confirm a new experiment named `kubeflow-pipeline` exists and contains a run with the logged parameters and metrics.
4. Check that the run's source field in MLflow UI points to the KFP run ID or pipeline name.

## Common errors

| Error | Likely cause | Fix |
|-------|-------------|-----|
| `ConnectionRefusedError` / `[Errno 111]` | MLflow server not running or wrong port | `kubectl get pods -n mlflow-system` and verify the Service port |
| `HTTP 401` / `HTTP 403` | Auth required but not configured | Add credentials to the URI or set `MLFLOW_TRACKING_TOKEN` or `MLFLOW_TRACKING_USERNAME` + `MLFLOW_TRACKING_PASSWORD` |
| `mlflow.exceptions.MlflowException: Experiment not found` | Experiment does not exist | Call `mlflow.set_experiment()` before `start_run()`; it creates the experiment if missing |
| Artifacts missing in MLflow UI | Artifact store not configured or inaccessible | Check the MLflow server's `--default-artifact-root` and verify the component pod can reach it if bypassing the server proxy |

## References

- [MLflow tracking server deployment on Kubernetes](https://mlflow.org/docs/latest/tracking.html)
- [Kubeflow Pipelines v2 component specification](https://www.kubeflow.org/docs/components/pipelines/v2/)
- [Kubernetes Service DNS naming](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
