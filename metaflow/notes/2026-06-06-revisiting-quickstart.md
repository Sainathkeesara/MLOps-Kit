# Revisiting the Metaflow quickstart — a second pass

Went back through the Metaflow tutorials — this time going past HelloFlow into branching, foreach, and the artifact system. Here's what worked and where I tripped.

## Install

Same drill — `pip install metaflow`. Already had it from last time. Upgraded with `pip install -U metaflow` to make sure I was on a recent version (2.12.x).

## Tutorial walkthrough

I followed the [Metaflow tutorials](https://docs.metaflow.org/tutorials) rather than the single-page quickstart. The tutorials are a series of notebooks that build up gradually.

### Branching and merge

The `BranchFlow` example worked first try. The pattern is:

```python
@step
def start(self):
    self.next(self.branch_a, self.branch_b)

@step
def branch_a(self):
    self.result = "a"
    self.next(self.join)

@step
def branch_b(self):
    self.result = "b"
    self.next(self.join)

@step
def join(self, inputs):
    print(inputs.branch_a.result, inputs.branch_b.result)
    self.next(self.end)
```

The `join` step receives an `inputs` object — you access each branch's data by step name. I initially tried `inputs[0]` like a list — nope, it's attribute-based.

### Foreach

The `@foreach` decorator splits work over a list. I used it to train separate models on different hyperparameter values:

```python
@step
def start(self):
    self.alphas = [0.01, 0.1, 1.0]
    self.next(self.train_foreach, foreach="alphas")
```

This fans out one `train_foreach` step per alpha value. The join step collects all results with `inputs` again. One gotcha: the foreach variable name has to be an attribute on `self` — I tried using a local variable and got a `NameError`.

### Artifacts and data passing

Metaflow pickles anything you assign to `self.X` in a step. That means passing DataFrames, models, or scalars between steps works without any serialization code. I passed a `pandas.DataFrame` between steps and it worked fine — the pickle was stored in `$METAFLOW_HOME` by default.

## Where I got stuck

### 1. `@resources` requires a real batch backend

The tutorial mentions `@resources(memory=4096, cpu=2)`. I added it to a step and ran locally — it just printed a warning and ignored it. Turns out `@resources` only takes effect when you use `--with kubernetes` or `--with batch`. Reading the docs more carefully, that makes sense — local runs can't enforce memory limits.

### 2. `@conda` base environment

I tried `@conda(libraries={"scikit-learn": "1.3.0"})` without activating conda on my system first. Metaflow errored with `CondaNotFound: conda binary not found`. You need `conda` installed separately — Metaflow doesn't bundle it. After installing miniconda, I re-ran and it created the environment automatically.

### 3. Run IDs and artifact access

Metaflow assigns every run a unique ID like `HelloFlow/1734392010`. To load artifacts from a previous run, you use `Flow.get_latest_successful_run()` or specify a run ID directly. I assumed artifact loading was automatic — it's not. You have to explicitly call `run[steps].task.data.artifact_name`. Found a few examples in the docs that cleared it up.

## What I'd try next

Setting up a remote metadata service and artifact store (S3) so runs persist beyond my laptop. Also want to try the `@pypi` decorator for on-the-fly package resolution — that seems cleaner than `@conda` for simple dependencies.
