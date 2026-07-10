# last_verified: 2026-07-10 · python

"""con-018 — Pipeline orchestration fundamentals exercises (L2)

Three small exercises that make the core ideas of pipeline
orchestration concrete: a DAG, its task dependencies, and a
topological run order. I wrote them without any orchestration
tool so the shape of a pipeline is obvious before I touch
Airflow / Metaflow / Kubeflow.
"""

from collections import defaultdict, deque


# --- Exercise 1: define a pipeline as a DAG of tasks ---


def exercise_1_define_dag() -> dict:
    """Exercise 1: build a tiny 4-task training pipeline DAG.

    Edges read as "child depends on parent", i.e. (child, parent).
    ingest -> validate -> train -> evaluate
    """
    dag = {
        "ingest": [],
        "validate": ["ingest"],
        "train": ["validate"],
        "evaluate": ["train"],
    }
    print("DAG tasks and their upstream deps:")
    for task, deps in dag.items():
        print(f"  {task} <- {deps or '[] (root)'}")
    assert dag["ingest"] == [], "ingest should be a root with no deps"
    assert dag["train"] == ["validate"], "train must wait on validate"
    return dag


# --- Exercise 2: list dependencies for a given task ---


def exercise_2_list_deps(dag: dict, task: str) -> list:
    """Exercise 2: what must finish before `task` can run?"""
    deps = dag.get(task, [])
    print(f"Task '{task}' waits on: {deps}")
    return deps


# --- Exercise 3: topological run order (no cycles allowed) ---


def topo_order(dag: dict) -> list:
    """Return tasks in dependency order using Kahn's algorithm."""
    indegree = {t: 0 for t in dag}
    children = defaultdict(list)
    for task, parents in dag.items():
        indegree[task] = len(parents)
        for p in parents:
            children[p].append(task)

    queue = deque(sorted(t for t in dag if indegree[t] == 0))
    order: list = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for child in children[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)

    if len(order) != len(dag):
        raise ValueError("cycle detected — pipeline is not a DAG")
    return order


def exercise_3_run_order(dag: dict) -> list:
    """Exercise 3: print a valid execution order for the whole pipeline."""
    order = topo_order(dag)
    print("Valid run order:", " -> ".join(order))
    assert order.index("validate") < order.index("train")
    return order


if __name__ == "__main__":
    g = exercise_1_define_dag()
    exercise_2_list_deps(g, "train")
    exercise_3_run_order(g)
    print("All orchestration exercises passed.")
