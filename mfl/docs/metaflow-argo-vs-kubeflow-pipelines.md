---
last_verified: 2026-08-06
tool_version: n/a
sources:
  - https://kodekloud.com/blog/using-kubernetes-for-mlops
---

# Metaflow + Argo vs Kubeflow Pipelines: orchestration integration patterns

> How to run Metaflow flows under external orchestration engines — Argo Workflows and
> Kubeflow Pipelines — and how to choose between them when Metaflow's native orchestration
> service does not fit the platform.

## Purpose

Metaflow ships with its own orchestration service for production runs. The
`@batch` decorator submits steps to AWS Batch, `@kubernetes` launches
Kubernetes pods, and `@schedule` / `@trigger` provide event-driven entry points.
However, many organizations have already standardized on an external orchestration
platform that manages both ML and non-ML workloads. Two common targets are Argo
Workflows — a general-purpose Kubernetes workflow engine — and Kubeflow Pipelines,
an ML-specific pipeline platform that also runs on Argo at its core.

This document describes how to containerize a Metaflow flow and embed it in each
platform, then compares the trade-offs so a team can pick the integration that
matches their existing stack and maturity level.

## When to use

| Factor | Choose Argo Workflows | Choose Kubeflow Pipelines |
|---|---|---|
| Workload scope | Mixed ML + non-ML steps; arbitrary containers | ML-centric pipelines with shared tracking |
| Existing platform | Argo Workflows already installed and managed | KFP adopted as the MLOps foundation |
| Step granularity | Fine-grained; each Metaflow step is a separate container task | Coarse; the whole flow or a logical unit is one component |
| Scheduling | Cron and event triggers via Workflow templates | `RecurringRun` API with experiment versioning |
| Artifact storage | Rely on Metaflow datastore or mount S3/GCS | KFP artifact store plus Metaflow datastore |
| Team maturity | Platform team comfortable with raw Kubernetes CRDs | Data science team using the KFP SDK |
| Migration effort | Containerize flows; no DSL rewrite | Wrap Metaflow CLI calls in KFP components |

## Prerequisites

- A Metaflow flow that runs locally (`python my_flow.py run`)
- A Dockerfile that packages the flow and its dependencies into a container image
- A container registry accessible from the target Kubernetes cluster
- A cluster with either Argo Workflows or Kubeflow Pipelines installed
- For KFP: the KFP SDK is available in the local Python environment (`pip install kfp`)

## Steps

### 1. Package the Metaflow flow as a container

Both integration paths start from the same step. Build a Docker image that
contains the Metaflow flow file, its dependencies, and an entrypoint that
invokes the Metaflow CLI.

```dockerfile
FROM python:3.10-slim

RUN pip install metaflow

COPY orchestration_flow.py /app/
WORKDIR /app

ENTRYPOINT ["python", "orchestration_flow.py", "run"]
```

Push the image to a registry the cluster can pull:

```bash
docker build -t my-registry.example.com/metaflow-flow:latest .
docker push my-registry.example.com/metaflow-flow:latest
```

The flow itself stays unchanged. A flow with `foreach` fan-out and
`@batch` resource hints looks like:

```python
from metaflow import FlowSpec, step, batch


class OrchestrationFlow(FlowSpec):

    @step
    def start(self):
        self.items = [1, 2, 3, 4, 5]
        self.next(self.transform, foreach="items")

    @batch(cpu=2, memory=4096)
    @step
    def transform(self):
        self.result = self.input ** 2
        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = sorted(inp.result for inp in inputs)
        self.next(self.end)

    @step
    def end(self):
        print(f"results: {self.results}")


if __name__ == "__main__":
    OrchestrationFlow()
```

### 2. Integrate with Argo Workflows

In Argo, each Metaflow step becomes a container template in a DAG. The
`start` step runs first; the `transform` step fan-out uses Argo's
`withItems` to mirror Metaflow's `foreach`; the `join` step depends on
all `transform` tasks completing.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: metaflow-orchestration-
spec:
  entrypoint: metaflow-dag
  templates:
    - name: metaflow-dag
      dag:
        tasks:
          - name: start
            template: metaflow-step

          - name: transform
            template: metaflow-step
            withItems:
              - 1
              - 2
              - 3
              - 4
              - 5
            dependencies: [start]

          - name: join
            template: metaflow-step
            dependencies: [transform]

    - name: metaflow-step
      container:
        image: my-registry.example.com/metaflow-flow:latest
```

Important details:
- Each container invocation starts a fresh Metaflow run. To correlate
  steps across containers, pass a shared run ID via an environment variable
  or a parameter and configure Metaflow's datastore to a shared backend
  (S3/GCS) so artifacts persist across container boundaries.
- `@batch` and `@resources` decorators are honored only when Metaflow's
  own backend executes the step. Under Argo these decorators are inert;
  resource requests must be declared directly on the container spec
  (`resources.requests` / `resources.limits`).
- For production scheduling, add a `cron` or `workflowtemplate` resource
  alongside the `Workflow` to trigger runs on a schedule or in response to
  events.

### 3. Integrate with Kubeflow Pipelines

In KFP, the Metaflow flow runs as a component inside a pipeline. The simplest
pattern treats the entire flow as one component; for finer control the flow
can be split into per-step components, but that requires breaking the
`FlowSpec` across separate entry points.

```python
from kfp import dsl, Client


@dsl.component
def run_metaflow_flow():
    import subprocess
    subprocess.run(
        ["python", "orchestration_flow.py", "run",
         "--datastore-root", "/shared/artifacts"],
        check=True,
    )


@dsl.pipeline(
    name="metaflow-orchestration-pipeline",
    description="Runs a Metaflow flow inside a KFP pipeline",
)
def metaflow_pipeline():
    run_metaflow_flow()


if __name__ == "__main__":
    client = Client()
    client.create_run_from_pipeline_func(metaflow_pipeline, arguments={})
```

For periodic execution, create a `RecurringRun`:

```python
from kfp import Client

client = Client()
experiment = client.create_experiment("metaflow-experiments")
client.create_recurring_run(
    experiment_id=experiment.id,
    job_name="metaflow-daily-run",
    schedule="0 0 * * *",
    pipeline_func=metaflow_pipeline,
)
```

Key considerations:
- The container image must be listed in the component spec; KFP does not
  automatically resolve `pip install metaflow` at pipeline-definition time.
- KFP's artifact store and experiment metadata are separate from Metaflow's
  own tracking. If the team relies on Metaflow's UI for inspection, ensure
  the flow writes to a shared datastore so runs are queryable after the
  pipeline completes.
- For step-level parallelism that mirrors Metaflow's `foreach`, use KFP's
  `dsl.ParallelFor` — but the fan-out items must be materialized as a KFP
  parameter list, not as Metaflow's `self.input`.

### 4. Use Metaflow native orchestration (alternative)

If the deployment target is AWS, Metaflow's native `@batch` decorator and
Metaflow Services provide the simplest path. No external orchestrator is
needed; the flow definition stays unchanged and Metaflow handles job
submission, retries, and artifact storage. The pattern below shows a flow
ready for remote execution:

```python
from metaflow import FlowSpec, step, batch


class NativeFlow(FlowSpec):

    @batch(cpu=4, memory=8192, image="my-registry.example.com/metaflow-flow:latest")
    @step
    def train(self):
        self.model = self._train()
        self.next(self.end)

    @step
    def end(self):
        pass

    def _train(self):
        # training logic here
        return {"accuracy": 0.94}


if __name__ == "__main__":
    NativeFlow()
```

```bash
python native_flow.py run --with batch
```

## Verify

1. **Argo integration**: Apply the Workflow manifest with
   `kubectl apply -f metaflow_argo_workflow.yaml`. In the Argo UI, each
   step should transition from `Pending` to `Running` to `Succeeded`.
   Check container logs for the Metaflow run ID printed at startup.
2. **KFP integration**: Run the pipeline script, then open the KFP UI.
   The run should progress through all steps. Confirm the Metaflow flow
   completed by checking for the `results:` print in the pod logs.
3. **Recurring schedule**: After creating the `RecurringRun`, verify in
   the KFP UI that the next scheduled run appears. Trigger an immediate
   run from the UI to confirm the schedule configuration is valid.
4. **Native**: Run `python native_flow.py run --with batch`. In the AWS
   console, each `@batch` step should spawn a separate Batch job with
   matching vCPU and memory requests.

## Common errors

- **Container image not found**: The Metaflow flow image is not accessible
  from the orchestrator's pod. Ensure the image is pushed to a registry
  the cluster can reach, and that `imagePullSecrets` are configured if
  the registry is private.
- **Metadata backend conflict**: Metaflow's local metadata does not
  propagate across container steps in the DAG. Configure a shared datastore
  (S3/GCS) via `--datastore-root` or the `METAFLOW_*_URI` environment
  variables so artifacts and run history are queryable after the run.
- **Resource mismatch**: The `@batch` / `@resources` decorators are
  inert under Argo. Resource requests declared in Metaflow are not
  forwarded to the container; they must be set on the workflow template
  or KFP component spec directly.
- **Step ordering drift**: If the external DAG does not mirror the
  flow's `self.next()` logic, steps run out of order or in parallel
  unexpectedly. Keep the DAG definition in sync with the flow's step
  graph; changes to the flow must be reflected in the workflow manifest
  or pipeline code.
- **foreach vs withItems**: Metaflow's `foreach` fan-out maps to Argo's
  `withItems` or KFP's `ParallelFor`. If the item list is generated
  dynamically inside a step, it must be persisted to the shared datastore
  and materialized as a parameter list before the orchestrator can
  expand it.

## References

- Containerization's role in portable MLOps pipeline execution —
  how orchestration tools like Metaflow, Kubeflow, and Airflow get
  portable execution units that run on any cluster node:
  [Using Kubernetes for MLOps](https://kodekloud.com/blog/using-kubernetes-for-mlops)
