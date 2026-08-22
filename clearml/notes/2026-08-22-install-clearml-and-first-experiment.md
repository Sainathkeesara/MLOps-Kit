---
last_verified: 2026-08-22
tool_version: "3.0.3"
sources:
  - https://pypi.org/project/clearml-agent/
  - https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/
  - https://clear.ml/docs/latest/docs/clearml_agent/
---

# Install ClearML and log my first experiment

> L1 scratch notes — I just installed ClearML and tried logging something.

## What I did

Installed the agent first:

```bash
pip install clearml-agent
```

The docs say install it as a system package, not inside a venv. The agent needs to create its own venvs for tasks, so running from an existing venv breaks that.

Then ran `clearml-agent init` which writes `~/clearml.conf` with server credentials. Without that file the agent can't connect to anything.

## What tripped me

- The agent doesn't bring its own Python — your system needs the version you want already installed.
- GPU allocation grabs everything by default via `NVIDIA_VISIBLE_DEVICES`. Use `--cpu-only` or `--gpus 0` if you don't want that.
- Cache lives at `~/.clearml` — if things go weird, nuking `~/.clearml/cache/*` is the first thing to try.

## Logging an experiment

Once the agent is set up, logging is straightforward with the Python SDK:

```python
from clearml import Task

task = Task.init(project_name="my-project", task_name="first-run")

# log some params
task.connect({"learning_rate": 0.001, "epochs": 10})

# log a metric
task.get_logger().report_scalar("loss", "train", 0.5, iteration=0)
task.get_logger().report_scalar("loss", "train", 0.3, iteration=1)
```

## What I'll look at next

The agent bootstrap feature (`clearml-agent install-bootstrap`) lets you preinstall tools inside task containers. Want to try that with a GPU task.
