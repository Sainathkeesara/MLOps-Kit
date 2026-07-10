# last_verified: 2026-07-10 · python

"""con-019 — Applying pipeline orchestration with DAG-based ML workflows (L2)

A small orchestrator that runs an ML pipeline as a DAG of steps.
I kept it dependency-free so the orchestration mechanics are
visible: each step declares upstream steps, I order them
topologically, then run them in sequence. This is the same
shape Airflow / Metaflow / Kubeflow Pipelines use, minus the
scheduler and UI.
"""

import time
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass
class Step:
    name: str
    upstream: list = field(default_factory=list)
    run: callable = None


def plan_run(steps: list) -> list:
    """Topologically sort steps so every upstream runs first."""
    by_name = {s.name: s for s in steps}
    indegree = {s.name: len(s.upstream) for s in steps}
    children = defaultdict(list)
    for s in steps:
        for up in s.upstream:
            children[up].append(s.name)

    queue = deque(sorted(n for n, d in indegree.items() if d == 0))
    order: list = []
    while queue:
        node = queue.popleft()
        order.append(by_name[node])
        for child in children[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    if len(order) != len(steps):
        raise ValueError("cycle detected in pipeline DAG")
    return order


# --- A toy ML workflow: ingest -> validate -> train -> evaluate ---


def ingest():
    print("ingest: loaded 1000 rows")
    return {"rows": 1000}


def validate(ctx):
    assert ctx["rows"] > 0, "no data to validate"
    print("validate: schema + null checks passed")


def train(ctx):
    print("train: fit a toy model")
    ctx["accuracy"] = 0.91


def evaluate(ctx):
    print(f"evaluate: accuracy={ctx['accuracy']:.2f}")


def build_pipeline():
    ctx: dict = {}
    steps = [
        Step("ingest", run=lambda: ctx.update(ingest())),
        Step("validate", upstream=["ingest"], run=lambda: validate(ctx)),
        Step("train", upstream=["validate"], run=lambda: train(ctx)),
        Step("evaluate", upstream=["train"], run=lambda: evaluate(ctx)),
    ]
    return steps, ctx


if __name__ == "__main__":
    steps, ctx = build_pipeline()
    for step in plan_run(steps):
        t0 = time.time()
        step.run()
        print(f"  -> {step.name} done in {time.time() - t0:.3f}s")
    print("Pipeline finished. Final ctx:", ctx)
