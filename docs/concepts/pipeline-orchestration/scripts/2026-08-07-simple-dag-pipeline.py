# last_verified: 2026-08-07 · python

from typing import Dict, List, Set


class Task:
    def __init__(self, name: str, action):
        self.name = name
        self.action = action
        self.dependencies: List[str] = []

    def run(self):
        print(f"  -> {self.name}")
        self.action()


class DAGPipeline:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def add_task(self, name: str, action):
        self.tasks[name] = Task(name, action)

    def add_dependency(self, task_name: str, depends_on: str):
        self.tasks[task_name].dependencies.append(depends_on)

    def execute(self):
        executed: Set[str] = set()

        def _run(name):
            if name in executed:
                return
            for dep in self.tasks[name].dependencies:
                _run(dep)
            self.tasks[name].run()
            executed.add(name)

        for name in self.tasks:
            _run(name)


if __name__ == '__main__':
    pipeline = DAGPipeline()

    pipeline.add_task("load_data", lambda: print("Loading dataset..."))
    pipeline.add_task("preprocess", lambda: print("Cleaning and transforming..."))
    pipeline.add_task("train", lambda: print("Training model..."))
    pipeline.add_task("evaluate", lambda: print("Computing metrics..."))

    pipeline.add_dependency("preprocess", "load_data")
    pipeline.add_dependency("train", "preprocess")
    pipeline.add_dependency("evaluate", "train")

    print("Running DAG pipeline:")
    pipeline.execute()
    print("Pipeline complete.")
