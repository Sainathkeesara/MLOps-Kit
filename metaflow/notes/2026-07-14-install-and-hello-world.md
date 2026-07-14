---
last_verified: 2026-07-14
tool_version: n/a
---

# Metaflow — install, hello world, and CLI

Installed Metaflow with `pip install metaflow` — no issues. It pulled in the core package and some dependencies.

Wrote the hello world flow from the docs. A simple `HelloFlow` with a `@step('start')` that says "HelloFlow is starting" and a `@step('end')` that says "HelloFlow is complete". The decorators define the DAG order. Ran it with `python helloflow.py run`:

```
Metaflow 2.x.y executing HelloFlow for user:me
    [me/HelloFlow/1] Task is starting.
    [me/HelloFlow/1] HelloFlow is starting.
    [me/HelloFlow/1] Task finished successfully.
    [me/HelloFlow/1] Task is starting.
    [me/HelloFlow/1] HelloFlow is complete.
    [me/HelloFlow/1] Task finished successfully.
```

The CLI is straightforward. `python helloflow.py run` executes the flow. `python helloflow.py status` shows the latest run. `python helloflow.py show` prints the DAG structure. `metaflow --help` lists subcommands — not many, which is nice.

I poked around `~/.metaflowconfig/` — no config file was created automatically, which surprised me. Might need one when I add cloud compute.

Next I want to try passing data between steps with artifacts and running a parameterized flow.
