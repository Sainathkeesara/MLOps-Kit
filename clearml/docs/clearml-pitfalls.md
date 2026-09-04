---
last_verified: 2026-09-04
tool_version: n/a
sources:
  - https://github.com/clearml/clearml/issues/1118
  - https://clear.ml/docs/latest/docs/faq/
---

# ClearML pitfalls — queues, task dependencies, and artifact uploads

I went through the official ClearML quickstart and then tried to push real work to a remote queue. Here are the things that bit me.

## Queues: no agent subscribed = task stuck forever

The single biggest gotcha. When you enqueue a task, nothing runs unless a `clearml-agent` daemon is listening on that queue:

```bash
clearml-agent daemon --queue default
```

If no agent is up, the task sits in "Queued" forever and never errors. I lost an afternoon to this before realizing the queue was empty of workers. The task isn't broken — it's just waiting for a worker that doesn't exist.

## `clearml-init` port confusion: web (8080) ≠ API (8008)

The interactive setup prints three ports: Web App `:8080`, API `:8008`, File Store `:8081`. I pasted the web port into the API server field and got this on the first `Task.init`:

```
401/22: projects.get_all ... Unauthorized (invalid credentials)
(failed to locate provided credentials)
```

The SDK talks to the **API** server, so the API port must be right. Match the `api_server` in `clearml.conf` to `:8008`, not `:8080`.

## Task dependencies: a cloned task stays DRAFT until enqueued

After I cloned or created a task, it reported "draft mode" and the agent ignored it. A task only becomes runnable once you enqueue it. So the lifecycle is: create/clone → enqueue → agent picks up. Skipping the enqueue step is easy to do and silently does nothing.

## `Task.init` must run first to capture auto-hooks

ClearML auto-logs TensorBoard, matplotlib, and other frameworks, but only if `Task.init` runs *before* those calls. I had debug samples missing on my first run because I imported matplotlib, plotted, and only then called `Task.init`. Move `Task.init` to the very top.

## Artifact uploads: first remote run is slow by design

The agent reinstalls the original packages and fetches the original code on the first execution of a cloned task. The tutorial warns it "can take quite a long time" — that's expected, everything is cached afterward. Don't assume the agent is broken; just wait it out the first time.

## What I'd try next

I want to wire up a proper `clearml.conf` with multiple queues and a remote file-store path, then experiment with pipeline task dependencies (`PipelineController`) so steps chain automatically instead of me enqueuing each one by hand.

## Dead-link cleanup

The previous copy of this doc at `clearml/notes/2026-07-12-clearml-pitfalls.md` carried a `sources:` entry pointing at `https://github.com/clearml/clearml/blob/master/docs/tutorials/Getting_Started_3_Remote_Execution.ipynb`. That tutorial notebook was relocated on the upstream repo and the old `master/docs/tutorials/` path no longer resolves; the front-matter `sources:` list above drops it. The remaining two URLs (the issue thread and the FAQ landing page) are the only external citations this doc actually leans on.
