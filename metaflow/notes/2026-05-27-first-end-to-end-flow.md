# meta-003 — Run my first end-to-end Metaflow flow

I wrote a real flow today — not just HelloFlow but something that actually loads data, trains a model, and evaluates it.

**what I built**

A three-step flow called `TinyTrainFlow`:

1. **load_data** — generated 100 synthetic points with `sklearn.datasets.make_classification`
2. **train_model** — fit a `RandomForestClassifier` with 50 trees
3. **evaluate** — printed accuracy on the same data (no train/test split yet — keeping it simple)

```python
from metaflow import FlowSpec, step
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

class TinyTrainFlow(FlowSpec):

    @step
    def load_data(self):
        self.X, self.y = make_classification(n_samples=100, random_state=42)
        self.next(self.train_model)

    @step
    def train_model(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.model.fit(self.X, self.y)
        self.next(self.evaluate)

    @step
    def evaluate(self):
        acc = self.model.score(self.X, self.y)
        print(f"Training accuracy: {acc:.3f}")
        self.next(self.end)

    @step
    def end(self):
        print("Done")

if __name__ == "__main__":
    TinyTrainFlow().run()
```

**what I noticed**

- Passing data between steps works via `self.X = ...` — Metaflow pickles it automatically. Felt weird at first but it just works.
- The run output is verbose — I can see each step start/finish with timestamps.
- Failed the first time because I forgot `self.next(self.end)` in `evaluate`. Metaflow gave a clear error about orphan steps.
- `python flow.py run` is the command. No config needed for local runs.

**next**

Try adding a `@conda` environment and running with `--with conda`. Also want to actually split train/test.
