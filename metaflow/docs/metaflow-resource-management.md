# Metaflow resource management: @conda, @resources, and timeout configuration

> How to pin dependencies per step, request compute resources, and enforce time limits in Metaflow flows.

## Purpose

Metaflow provides three decorators that control the execution environment of individual steps. `@conda` manages isolated Python environments, `@resources` declares CPU/memory/GPU requirements, and timeout configuration caps how long a step can run. These tools are essential when moving a flow from a local laptop to a remote batch or Kubernetes backend, where resource guarantees and environment consistency matter.

## When to use

| Decorator / mechanism | Use when |
|---|---|
| `@conda` | A step needs specific library versions that differ from the system Python, or you want reproducible environments across machines. |
| `@resources` | A step needs a known amount of CPU, memory, or GPU — especially on remote backends (AWS Batch, Kubernetes). |
| `@timeout` | A step might stall or run longer than expected, and you want the flow to fail fast rather than hang indefinitely. |

All three are optional. A flow without them runs in the system Python environment with no resource or time constraints — fine for local prototyping, risky for production.

## Steps

### 1. Install conda (if using `@conda`)

Metaflow does not bundle conda. The `@conda` decorator requires conda to be available on the system.

```bash
# Install miniconda (Linux/macOS)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda3
eval "$(~/miniconda3/bin/conda shell.bash hook)"
conda init
```

Verify conda is on `PATH` before running any flow that uses `@conda`:

```bash
which conda
```

If conda is not found, Metaflow raises `CondaNotFound: conda binary not found` at the first step decorated with `@conda`.

### 2. Apply `@conda` to steps

`@conda` creates an isolated conda environment for each decorated step. Libraries are installed when the step runs for the first time.

```python
from metaflow import FlowSpec, step, conda

class CondaFlow(FlowSpec):

    @conda(libraries={"scikit-learn": "1.3.0", "pandas": "2.0.3"})
    @step
    def train(self):
        import pandas as pd
        from sklearn.ensemble import RandomForestClassifier
        # scikit-learn and pandas are available in this step's environment
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    CondaFlow()
```

To run with conda isolation active, pass `--with conda` on the command line:

```bash
python conda_flow.py run --with conda
```

Key behaviors:
- Each `@conda`-decorated step gets its own environment. Libraries specified in one step are **not** available in another unless also decorated.
- The `@conda` decorator also works with `@pypi` (a newer pip-based alternative). The docs suggest that `@pypi` resolves packages faster because it uses pip's resolver instead of conda's.
- The base image or system still needs the libraries if conda installation fails — a fallback path is not automatic.

### 3. Declare resources with `@resources`

`@resources` announces how much CPU, memory, or how many GPUs a step needs. On a local run this is advisory only (Metaflow prints a warning and continues). On a remote backend (AWS Batch, Kubernetes) the scheduler uses these values to pick or provision the right instance.

```python
from metaflow import FlowSpec, step, resources

class ResourceFlow(FlowSpec):

    @resources(memory=4096, cpu=2, gpu=1)
    @step
    def train(self):
        # This step requests 4 GB RAM, 2 vCPUs, 1 GPU
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ResourceFlow()
```

Run locally (resources warning is expected):

```bash
python resource_flow.py run
# Output includes: "@resources decorator is only used on remote backends, not locally"
```

Run on Kubernetes:

```bash
python resource_flow.py run --with kubernetes
```

On AWS Batch:

```bash
python resource_flow.py run --with batch
```

One thing that is easy to miss: `@resources` does **not** reserve resources on the local scheduler. It's a declaration for the remote scheduler. The same flow runs with or without it locally — the values are silently ignored.

### 4. Set step timeouts

Metaflow does not have a dedicated `@timeout` decorator. Instead, timeout is configured per step using the `@step` decorator's `timeout` parameter.

```python
from metaflow import FlowSpec, step

class TimedFlow(FlowSpec):

    @step
    def start(self):
        self.next(self.train)

    @step(timeout=60)
    def train(self):
        import time
        # This step will be killed if it runs longer than 60 seconds
        time.sleep(10)
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    TimedFlow()
```

The `timeout` value is in seconds. When a step exceeds the timeout, Metaflow raises a `StepTimeoutError` and the run is marked as failed. Timeout works on both local and remote backends.

A common pattern is to set generous timeouts on data-loading steps (where network latency is unpredictable) and tighter timeouts on compute steps.

### 5. Combine all three

These decorators compose on the same step:

```python
from metaflow import FlowSpec, step, conda, resources

class ProductionFlow(FlowSpec):

    @conda(libraries={"scikit-learn": "1.3.0", "pandas": "2.0.3", "numpy": "1.24.3"})
    @resources(memory=8192, cpu=4)
    @step(timeout=300)
    def train(self):
        import pandas as pd
        from sklearn.ensemble import GradientBoostingClassifier
        import numpy as np

        # Simulated training
        X = np.random.rand(1000, 20)
        y = np.random.randint(0, 2, 1000)
        model = GradientBoostingClassifier().fit(X, y)
        self.model = model
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ProductionFlow()
```

The decorator order does not matter — Metaflow merges them internally.

## Verify

1. **`@conda`**: Run a flow with `--with conda` and check the logs for `Installing conda environment ...` followed by `Conda environment installed`. If conda is missing, the error is immediate.
2. **`@resources`**: Run locally with `--with kubernetes` (or batch) and inspect the `@resources` line in the run's metadata. The Step page in the UI shows the requested resources.
3. **Timeout**: Add a step with `timeout=1` and a `time.sleep(10)` inside it. The run should fail within a few seconds with `StepTimeoutError`.

## Common errors

- **`CondaNotFound`** — Conda is not installed or not on `PATH`. Install miniconda and ensure `conda` is reachable.
- **`@resources` values ignored locally** — This is expected. The values are only consumed by remote backends. The warning in the log is informational.
- **Timeout not honored** — The timeout is checked between Python bytecode instructions. A long-running C extension (e.g., a native library call) may not be interrupted until it returns control to Python. For most ML training loops this is not an issue.
- **`@conda` environment rebuilds every run** — By default, conda environments are cached per step signature. If the library list changes, the environment is rebuilt, which can take a minute. This is normal.

## References

- [Metaflow @conda decorator docs](https://docs.metaflow.org/scaling/envlock)
- [Metaflow @resources decorator docs](https://docs.metaflow.org/scaling/resources)
- [Metaflow @timeout docs](https://docs.metaflow.org/scaling/timeout)
- [Metaflow @pypi decorator (alternative to @conda)](https://docs.metaflow.org/scaling/envlock/pypi)
