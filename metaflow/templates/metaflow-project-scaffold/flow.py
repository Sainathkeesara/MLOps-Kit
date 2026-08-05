# last_verified: 2026-08-04 · metaflow 2.10.0
"""Metaflow project scaffold with @project, @schedule, and event-triggered flows.

This scaffold demonstrates three Metaflow patterns:
1. @project — project metadata and namespace isolation
2. @schedule — cron-based scheduled execution
3. Event-triggered flows — starting flows from external events

Each pattern is a self-contained flow class in this file.
"""

from metaflow import FlowSpec, Parameter, pypi, step, project, schedule, trigger


@project(name="metaflow-ml-pipeline", author="mlops-team")
class ProjectMetadataFlow(FlowSpec):
    """A flow that demonstrates the @project decorator for namespace isolation."""

    dataset = Parameter("dataset", default="iris", help="Dataset to use")

    @pypi(libraries={"scikit-learn": ">=1.0.0", "pandas": ">=1.3.0"})
    @step
    def start(self):
        print(f"Running under project: {self.project_name}")
        self.next(self.process)

    @pypi(libraries={"scikit-learn": ">=1.0.0"})
    @step
    def process(self):
        print(f"Processing dataset: {self.dataset}")
        self.next(self.end)

    @step
    def end(self):
        print("Project-scoped flow complete.")


@schedule(cron="0 8 * * *")
class ScheduledDailyFlow(FlowSpec):
    """A flow that runs daily at 08:00 via the @schedule decorator."""

    threshold = Parameter("threshold", default=0.5, help="Decision threshold")

    @pypi(libraries={"pandas": ">=1.3.0", "numpy": ">=1.21.0"})
    @step
    def start(self):
        print("Scheduled daily flow starting.")
        self.next(self.analyze)

    @pypi(libraries={"numpy": ">=1.21.0"})
    @step
    def analyze(self):
        print(f"Threshold: {self.threshold}")
        self.next(self.end)

    @step
    def end(self):
        print("Scheduled flow complete.")


@trigger(source="github", event="push", branch="main")
class EventTriggeredFlow(FlowSpec):
    """A flow triggered by external events via the @trigger decorator."""

    commit_sha = Parameter("commit_sha", help="SHA of the triggering commit")

    @pypi(libraries={"pandas": ">=1.3.0"})
    @step
    def start(self):
        print(f"Event-triggered flow starting for commit {self.commit_sha}")
        self.next(self.ingest)

    @pypi(libraries={"pandas": ">=1.3.0"})
    @step
    def ingest(self):
        print("Ingesting data from event payload.")
        self.next(self.transform)

    @pypi(libraries={"pandas": ">=1.3.0"})
    @step
    def transform(self):
        print("Transforming event data.")
        self.next(self.end)

    @step
    def end(self):
        print("Event-triggered flow complete.")


if __name__ == "__main__":
    ProjectMetadataFlow()