---
last_verified: 2026-07-23
tool_version: n/a
---

# ClearML — First tasks with clearml-agent CLI

I installed `clearml-agent` and wanted to run a task on a remote machine without opening the web UI.

## Queuing a task

I had an existing experiment in the UI. From the CLI I cloned it and queued it:

```
clearml-agent queue --docker python:3.11-slim --queue default my_experiment_id
```

This pulled the task from the queue, spun up a Docker container on the agent machine, and ran it. The logs streamed back to the ClearML server.

## Cloning and running remotely

I cloned a finished run to try different hyperparams:

```bash
clearml-task --project my_project --name retry-run --docker python:3.11-slim \
  --script train.py --queue gpu-queue
```

The agent picked it up, installed deps from the task's pip requirements, and executed `train.py`. Output artifacts appeared in the UI automatically.

## Gotchas

- The `--docker` flag is required unless the agent machine matches your dev environment exactly.
- If the task has uncommitted code, the agent uploads a git diff patch — confusing at first because I expected it to clone the repo.
- Queuing a task without specifying a queue name silently drops it into the `default` queue; I spent ten minutes wondering why nothing ran.

## Next

I want to try chaining tasks so a training task automatically queues an evaluation task when it finishes.
