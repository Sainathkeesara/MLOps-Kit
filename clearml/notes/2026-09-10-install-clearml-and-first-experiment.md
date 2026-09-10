---
last_verified: 2026-09-10
tool_version: "2.1.12"
sources:
  - https://pypi.org/project/clearml/
  - https://clear.ml/docs/latest/docs/getting_started/video_tutorials/core_component_overview/
  - https://clear.ml/docs/latest/docs/clearml_agent/
---

# Install ClearML and log my first experiment

> L1 scratch notes — I just installed ClearML and tried logging my first experiment.

## What I did

First installed the SDK and the agent as separate packages:

```bash
pip install clearml
pip install clearml-agent
```

The docs say the agent should be installed as a system package, not inside a venv — it needs to create its own venvs for tasks. Running from an existing venv breaks that.

Then ran `clearml-init` to generate `~/clearml.conf` with server credentials. Without that file the agent can't connect to anything.

## What tripped me

- `clearml-init` refuses to overwrite an existing `~/clearml.conf`. Use `clearml-init --file <path>` plus `CLEARML_CONFIG_FILE=<path>` if you need multiple environments.
- `Task.init()` MUST be called before any framework imports (TensorBoard, argparse, hydra). Their auto-logging hooks attach at import time and miss the task.
- `output_uri=True` in `Task.init()` is critical — by default it is `False`, meaning registered models are NOT uploaded to ClearML storage.
- The SDK and agent are SEPARATE packages — installing only `pip install clearml` is the most common "pipeline runs locally but agents never pick it up" mistake.
- For internal-CA servers, `REQUESTS_CA_BUNDLE` must be set BEFORE importing clearml; otherwise SDK calls fail with `CERTIFICATE_VERIFY_FAILED`.

## Logging an experiment

Once the server and agent are set up, logging is straightforward:

```python
from clearml import Task

task = Task.init(project_name="my-project", task_name="first-run")

task.connect({"learning_rate": 0.001, "epochs": 10})

task.get_logger().report_scalar("loss", "train", 0.5, iteration=0)
task.get_logger().report_scalar("loss", "train", 0.3, iteration=1)
```

## What I'll look at next

The agent bootstrap feature (`clearml-agent install-bootstrap`) lets you preinstall tools inside task containers. Want to try that with a GPU task.
