---
last_verified: 2026-07-11
tool_version: "2.19.35"
sources:
  - https://docs.metaflow.org/getting-started/install
  - https://docs.metaflow.org/api/step-decorators/step
  - https://docs.metaflow.org/metaflow/basics
  - https://docs.metaflow.org/metaflow/configuring-flows/basic-configuration
  - https://docs.metaflow.org/metaflow/debugging
---

# Metaflow quickstart — what tripped me up

Followed the official Metaflow quickstart to get a flow running. Here's what happened.

## Install

`pip install metaflow` — that's it. I'm on Python 3.10, worked fine.

## First flow

Pasted the "HelloFlow" example into `hello.py`:

```python
from metaflow import FlowSpec, step

class HelloFlow(FlowSpec):
    @step
    def start(self):
        self.message = "hello metaflow"
        self.next(self.end)

    @step
    def end(self):
        print(self.message)

if __name__ == "__main__":
    HelloFlow()
```

Ran `python hello.py run` and it printed "hello metaflow". First win.

## Got stuck on

### 1. `@step` decorator order is strict

I wrote a flow where `end` didn't have `self.next(...)` — it's the terminal step so it shouldn't need one, right? Wrong. Metaflow expects every step to call `self.next()` except the last one (which must NOT call it). The error was vague. Took me a minute to realize the issue was my `start` step calling `self.next(self.end)` correctly, but then I was overthinking the terminal step. Actually the real bug was I forgot `self.next()` in a non-terminal step. Error wasn't super clear.

Also, `@step` must be the innermost decorator. I tried stacking `@timeout` below `@step` and got a runtime error. The docs say decorators like `@batch`, `@retry`, `@timeout` must appear above `@step`.

### 2. `self.next()` is mandatory for flow graph construction

I wrote linear step methods and forgot to call `self.next(self.end)` in my `start` step. The flow ran but produced an empty graph. Metaflow can't infer execution order — you have to wire it explicitly.

### 3. `Config` vs `Parameter` confusion

I used `Parameter` for everything — S3 paths, timeout thresholds. That means I have to pass them every time I run the flow. `Config` is read-only and evaluated at deploy time, which is what I wanted for environment-specific defaults. Beginners use `Parameter` for everything and end up unable to change configs without redeploying.

### 4. Namespace isolation

By default Metaflow uses the OS username as the namespace. On my shared laptop, I ran a flow and my teammate couldn't see it in the UI. We're in different namespaces. Fix with `--namespace` or `METAFLOW_DEFAULT_NAMESPACE`.

### 5. `resume` reuses original parameters

When I resumed a failed run with `metaflow resume --origin-run-id <id>`, I changed a parameter expecting a fresh value. The change was silently ignored — resume always uses the original run's parameters.

## What I'd try next

Branching and merging flows, then parameterizing runs from the CLI. Also want to see how Metaflow handles larger data — the quickstart examples use tiny strings. I'd also experiment with `@kubernetes` decorator instead of `@batch` since the AWS-only decorator naming asymmetry keeps tripping me up.
