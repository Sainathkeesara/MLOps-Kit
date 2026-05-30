# Metaflow — install and dev environment setup

Installed Metaflow with `pip install metaflow`. The install was clean — no system deps needed.

Ran `python -c "import metaflow; print(metaflow.__version__)"` to verify. Got `2.14.6`.

Next I created a project directory and wrote a tiny flow to check everything works:

```python
from metaflow import FlowSpec, step

class CheckInstall(FlowSpec):

    @step
    def start(self):
        print("metaflow is installed")
        self.next(self.end)

    @step
    def end(self):
        print("done")

if __name__ == "__main__":
    CheckInstall().run()
```

Saved it as `check_install.py` and ran it with `python check_install.py`. The flow ran without errors and printed the step transitions.

Noticed that Metaflow stores run metadata in `~/.metaflow/` by default — good to know for cleanup.

Stuff that tripped me up:
- The first run asked me about tracking metadata remotely — I said no for now (local mode is fine for getting started).
- The step method names (`start`, `end`) are special — you don't have to name them that but they're the convention for the first and last steps.

Next steps: set up a real flow with data loading and parameters.
