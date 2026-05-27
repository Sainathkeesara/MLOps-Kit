# Metaflow quickstart — what tripped me up

Followed the [Metaflow quickstart](https://docs.metaflow.org/getting-started/install) to get a flow running. Here's what happened.

## Install

`pip install metaflow` — that's it. Python 3.8+ required. I'm on 3.10, worked fine.

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

## Where I got stuck

### 1. `@step` decorator order matters
I wrote a flow where `end` didn't have `self.next(...)` — it's the terminal step so it shouldn't need one, right? Wrong. Metaflow expects every step to call `self.next()` except the last one (which must NOT call it). The error message was vague: `MetaflowStepException: Step end needs to call self.next()`. Took me a minute to realize the issue was my `start` step calling `self.next(self.end)` correctly, but then I was overthinking the terminal step. Actually the real bug was I forgot `self.next()` in a non-terminal step. Error wasn't super clear.

### 2. Running with `--no-pylint` helped
The quickstart says Metaflow runs pylint automatically before execution. On my first run pylint flagged some style things and the flow didn't start until I fixed them. Passing `--no-pylint` skips that check — handy for quick iteration.

### 3. Click params syntax
The `run` subcommand uses Click under the hood. If you pass `--param` with a hyphen instead of an underscore for a flow parameter, Click silently ignores it. Spent a few minutes wondering why my `--my-param` wasn't showing up — switched to `--my_param` and it worked.

## What I'd try next

Branching and merging flows, then parameterizing runs from the CLI. Also want to see how Metaflow handles larger data — the quickstart examples use tiny strings.
