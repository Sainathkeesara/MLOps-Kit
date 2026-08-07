# last_verified: 2026-08-07 · python

"""
con-088 — Practice: build a simple DAG-based pipeline with Python (L2)

I wrote this to understand the mechanics behind tools like Airflow,
Metaflow, and Kubeflow Pipelines without pulling in a heavyweight
scheduler.  The Pipeline class handles three things that real
orchestrators also do:

  1. Topological ordering  — steps run only after their upstreams finish.
  2. Parallel execution    — independent branches run concurrently.
  3. Conditional branching — a failed validation step skips training.

Everything is dependency-free: threading gives us parallelism, and
the step graph is just a list of dicts.
"""

from __future__ import annotations

import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass
class Step:
    name: str
    upstream: list[str] = field(default_factory=list)
    run: callable = None  # type: ignore[assignment]
    optional: bool = False


class Pipeline:
    """A minimal DAG orchestrator with parallel and branching support."""

    def __init__(self) -> None:
        self._steps: dict[str, Step] = {}
        self._results: dict[str, object] = {}

    def add(self, step: Step) -> None:
        self._steps[step.name] = step

    def _topo_order(self) -> list[Step]:
        """Kahn's algorithm — returns steps in execution order."""
        indegree = {s.name: len(s.upstream) for s in self._steps.values()}
        children: dict[str, list[str]] = defaultdict(list)
        for s in self._steps.values():
            for up in s.upstream:
                children[up].append(s.name)

        queue = deque(sorted(n for n, d in indegree.items() if d == 0))
        order: list[Step] = []
        while queue:
            node = queue.popleft()
            order.append(self._steps[node])
            for child in children[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        if len(order) != len(self._steps):
            raise ValueError("cycle detected in pipeline DAG")
        return order

    def _run_step(self, step: Step) -> None:
        """Execute a single step, storing its result."""
        ctx = self._results
        t0 = time.time()
        try:
            result = step.run(ctx)
            ctx[step.name] = result
            print(f"  {step.name}: done in {time.time() - t0:.3f}s")
        except Exception as exc:
            msg = f"{step.name}: FAILED ({exc})"
            print(f"  {msg}")
            ctx[step.name] = exc

    def run(self) -> dict[str, object]:
        """Execute the pipeline, running independent steps in parallel."""
        order = self._topo_order()
        # group steps by how many unresolved upstreams they still have
        ready: list[Step] = []
        remaining: set[str] = set(s.name for s in order)
        done: set[str] = set()
        upstream_done: dict[str, set[str]] = defaultdict(set)

        while remaining or ready:
            # find steps whose upstreams are all satisfied
            for name in sorted(remaining):
                step = self._steps[name]
                if upstream_done[name] >= set(step.upstream):
                    ready.append(step)

            if not ready:
                break  # nothing runnable (cycle would have been caught earlier)

            remaining -= {s.name for s in ready}
            threads = []
            for step in ready:
                upstream_done.pop(step.name, None)
                t = threading.Thread(target=self._run_step, args=(step,))
                threads.append(t)
                t.start()
            for t in threads:
                t.join()
            done.update(s.name for s in ready)
            ready = []

        return self._results


# ── A toy ML workflow with branching ──────────────────────────────────────
# ingest -> validate -> (train -> evaluate)   or   (skip -> notify)
# validate and ingest are sequential; train/evaluate are parallel-able
# with notify in a separate branch.


def build_pipeline() -> Pipeline:
    pl = Pipeline()

    def ingest(ctx):
        rows = [{"id": 1, "x": 0.5}, {"id": 2, "x": 0.8}]
        print(f"ingest: loaded {len(rows)} rows")
        ctx["rows"] = rows
        return rows

    def validate(ctx):
        rows = ctx.get("rows", [])
        if not rows:
            raise ValueError("no data ingested")
        missing = [r for r in rows if "x" not in r]
        if missing:
            raise ValueError(f"schema error on rows: {missing}")
        print("validate: schema + null checks passed")
        return "ok"

    def train(ctx):
        # only runs if validate succeeded
        if isinstance(ctx.get("validate"), Exception):
            raise RuntimeError("skipped — upstream validate failed")
        rows = ctx["rows"]
        xs = [r["x"] for r in rows]
        avg = sum(xs) / len(xs)
        ctx["model"] = {"avg": avg}
        print(f"train: fitted model with avg={avg:.3f}")
        return avg

    def evaluate(ctx):
        if isinstance(ctx.get("train"), Exception):
            raise RuntimeError("skipped — upstream train failed")
        score = ctx["train"] * 100
        ctx["score"] = score
        print(f"evaluate: score={score:.1f}")
        return score

    def notify(ctx):
        # optional cleanup branch — runs in parallel with train/evaluate
        print("notify: data-quality report sent")

    pl.add(Step("ingest", run=ingest))
    pl.add(Step("validate", upstream=["ingest"], run=validate))
    pl.add(Step("train", upstream=["validate"], run=train))
    pl.add(Step("evaluate", upstream=["train"], run=evaluate))
    pl.add(Step("notify", upstream=["ingest"], run=notify, optional=True))
    return pl


if __name__ == "__main__":
    print("── Pipeline run ──")
    results = build_pipeline().run()
    print("\nFinal context:", {k: v for k, v in results.items() if not isinstance(v, Exception)})
