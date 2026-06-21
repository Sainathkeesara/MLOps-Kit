# foreach vs @batch in Metaflow: comparing fan-out and resource scaling approaches

> How to choose between in-process parallelism with foreach and infrastructure-level fan-out with @batch.

## Purpose

Metaflow offers two distinct mechanisms for parallel execution. The `foreach` keyword fans out over a data set within a single step's process pool, while the `@batch` decorator submits each step (including each foreach split) as an independent AWS Batch job. Choosing between them — or combining them — depends on data volume, compute requirements, and cost profile.

## When to use

| Mechanism | Use when |
|---|---|
| `foreach` | Fanning out over a small-to-medium list (up to a few thousand items) where each split takes seconds to minutes and fits in a single process. All splits share the same compute environment — no extra infrastructure cost. |
| `@batch` | A step needs more memory or CPU than the local machine provides, or you want each parallel task to run on dedicated hardware without resource contention. |
| `foreach` + `@batch` | You need both: fan out over many items, and each item needs significant compute. Applied to a foreach step, each split becomes an independent Batch job. |

## Steps

### 1. foreach without @batch — in-process fan-out

foreach splits run inside the Metaflow client process on a single machine. The number of parallel workers is controlled by `--max-workers`.

```python
from metaflow import FlowSpec, step

class ForeachOnlyFlow(FlowSpec):

    @step
    def start(self):
        self.items = list(range(50))
        self.next(self.process, foreach="items")

    @step
    def process(self):
        self.result = self.input ** 2
        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = [inp.result for inp in inputs]
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ForeachOnlyFlow()
```

```bash
python foreach_only.py run --max-workers=4
```

The default `--max-workers` is 16. Pushing this too high on a single machine can saturate CPU or memory — foreach does not isolate resources between splits.

### 2. foreach + @batch — each split as a separate Batch job

When `@batch` decorates a step inside a foreach, each split is submitted as its own AWS Batch job. Instead of competing for local resources, each split gets a dedicated container with the requested CPU and memory.

```python
from metaflow import FlowSpec, step, batch

class ForeachBatchFlow(FlowSpec):

    @step
    def start(self):
        self.items = list(range(10))
        self.next(self.train, foreach="items")

    @batch(cpu=4, memory=8192)
    @step
    def train(self):
        self.result = self._train_model(self.input)
        self.next(self.join)

    @step
    def join(self, inputs):
        self.results = [inp.result for inp in inputs]
        self.next(self.end)

    @step
    def end(self):
        pass

    def _train_model(self, item):
        return {"item": item, "score": round(item * 0.95, 2)}

if __name__ == "__main__":
    ForeachBatchFlow()
```

```bash
python foreach_batch.py run --with batch
```

One thing the docs do not spell out: `@batch` must be on the step inside the foreach, not on the foreach step itself or on a flow-level decorator. Each split then becomes a separate Batch job.

### 3. @batch without foreach — single-step job

Without foreach, `@batch` runs the entire step as a single Batch job. Useful when a step needs more resources than the local machine provides but does not need fan-out.

```python
from metaflow import FlowSpec, step, batch

class BatchOnlyFlow(FlowSpec):

    @batch(cpu=8, memory=16384, image="python:3.10")
    @step
    def train(self):
        self.model = self._train()
        self.next(self.end)

    @step
    def end(self):
        pass

    def _train(self):
        return {"accuracy": 0.94}

if __name__ == "__main__":
    BatchOnlyFlow()
```

```bash
python batch_only.py run --with batch
```

## Verify

1. **foreach only**: Run `ForeachOnlyFlow` with `--max-workers=1` and then with `--max-workers=8`. The wall time should decrease with more workers. Metaflow's log shows how many splits ran in parallel.
2. **foreach + @batch**: Run `ForeachBatchFlow` and check the AWS Batch console. Each split appears as a separate job in the queue. The Metaflow run log prints `Submitting ...` for each split.
3. **Resource requests**: After a `@batch` run, inspect the Batch job details in the AWS console — vCPUs and memory should match what was requested in the decorator.

A limit I haven't been able to confirm from the docs: whether there is a hard ceiling on concurrent splits with `@batch`. The AWS Batch queue itself caps at 256 jobs in SUBMITTED state by default, but Metaflow may pace submissions below that. For workloads over a few hundred splits I would test with a smaller batch first.
