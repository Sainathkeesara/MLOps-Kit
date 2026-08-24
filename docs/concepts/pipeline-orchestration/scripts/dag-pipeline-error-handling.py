# last_verified: 2026-08-24 · python

"""
con-111 — Build a DAG-based pipeline with error handling and retry logic (L3)

This script demonstrates a minimal DAG orchestrator that supports:
  1. Topological execution order
  2. Parallel branches where upstreams are independent
  3. Per-step retry with exponential backoff
  4. Explicit error propagation so failed steps stop downstream work

It is intentionally dependency-free so the mechanics are visible without
hiding them behind a framework like Airflow or Prefect.
"""

from __future__ import annotations

import math
import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Step:
    """A single node in the pipeline DAG."""

    name: str
    upstream: List[str] = field(default_factory=list)
    run: Callable[[], Any] = None  # type: ignore[assignment]
    max_retries: int = 2
    retry_delay: float = 1.0
    _result: Optional[Any] = field(default=None, repr=False)
    _error: Optional[BaseException] = field(default=None, repr=False)
    _attempts: int = field(default=0, repr=False)


class Pipeline:
    """Minimal DAG orchestrator with retry and error handling."""

    def __init__(self) -> None:
        self._steps: Dict[str, Step] = {}
        self._lock = threading.Lock()

    def add(self, step: Step) -> None:
        self._steps[step.name] = step

    def _topo_order(self) -> List[Step]:
        indegree = {s.name: len(s.upstream) for s in self._steps.values()}
        children: Dict[str, List[str]] = defaultdict(list)
        for s in self._steps.values():
            for up in s.upstream:
                children[up].append(s.name)

        queue = deque(sorted(n for n, d in indegree.items() if d == 0))
        order: List[Step] = []
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
        for attempt in range(1, step.max_retries + 1):
            step._attempts = attempt
            try:
                step._result = step.run()
                return
            except Exception as exc:
                step._error = exc
                if attempt == step.max_retries:
                    raise
                time.sleep(step.retry_delay * (2 ** (attempt - 1)))

    def execute(self) -> Dict[str, Any]:
        order = self._topo_order()
        ready: Dict[str, threading.Event] = {
            s.name: threading.Event() for s in order
        }
        threads: Dict[str, threading.Thread] = {}

        def worker(step: Step) -> None:
            for upstream in step.upstream:
                ready[upstream].wait()
                if self._steps[upstream]._error is not None:
                    step._error = RuntimeError(
                        f"upstream failed: {upstream}"
                    )
                    return
            try:
                self._run_step(step)
            except Exception as exc:
                step._error = exc
            finally:
                ready[step.name].set()

        for step in order:
            threads[step.name] = threading.Thread(
                target=worker, args=(step,)
            )
            threads[step.name].start()

        for step in order:
            threads[step.name].join()

        failed = [s.name for s in order if s._error is not None]
        if failed:
            raise RuntimeError(f"pipeline failed at: {', '.join(failed)}")

        return {s.name: s._result for s in order}


def prep_data() -> str:
    return "data.csv"


def train_model() -> dict:
    return {"accuracy": 0.91}


def evaluate_model() -> dict:
    return {"loss": 0.12}


def main() -> None:
    pipeline = Pipeline()
    pipeline.add(Step(name="prep", run=prep_data))
    pipeline.add(
        Step(name="train", upstream=["prep"], run=train_model)
    )
    pipeline.add(
        Step(name="evaluate", upstream=["train"], run=evaluate_model)
    )
    results = pipeline.execute()
    print(results)


if __name__ == "__main__":
    main()
