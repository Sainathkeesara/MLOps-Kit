"""mfl-030 — Metaflow flow with @step, custom logging, and artifact persistence.

L2 — I wanted to see how Metaflow handles plain Python logging and what
happens to data I stash on `self`. Spoiler: anything I assign to `self`
becomes a persisted artifact I can pull back with the Client API later.
So this flow trains a tiny model and keeps the model + metrics as artifacts.
"""

import logging

from metaflow import FlowSpec, step, Parameter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mfl-030")


class LoggingArtifactFlow(FlowSpec):
    """Practice flow: custom logger + artifact persistence across steps."""

    epochs = Parameter("epochs", default=3, type=int, help="Training epochs")
    seed = Parameter("seed", default=42, type=int, help="Random seed")

    @step
    def start(self):
        """Set up the dataset. I log with the standard library `logging`
        module instead of `print` so the console output has levels."""
        logger.info("start: preparing toy dataset")
        self.num_samples = 200
        self.feature_dim = 4
        # A tiny deterministic "dataset" — just shapes, this is a toy example
        self.X = [[float((i + j) % 5) for j in range(self.feature_dim)]
                  for i in range(self.num_samples)]
        self.y = [i % 2 for i in range(self.num_samples)]
        logger.info("start: built %d samples of dim %d", self.num_samples, self.feature_dim)
        self.next(self.train)

    @step
    def train(self):
        """Train a throwaway classifier and persist it as an artifact.

        Assigning to `self.model` / `self.metrics` is all Metaflow needs to
        snapshot them — no explicit save/log call required.
        """
        logger.info("train: training for %d epochs", self.epochs)
        from sklearn.linear_model import LogisticRegression

        clf = LogisticRegression(random_state=self.seed, max_iter=200)
        clf.fit(self.X, self.y)
        # simple accuracy on the same data — toy metric, just to have something
        acc = clf.score(self.X, self.y)
        self.model = clf
        self.metrics = {"accuracy": acc, "epochs": self.epochs, "seed": self.seed}
        logger.info("train: accuracy=%.4f", acc)
        self.next(self.end)

    @step
    def end(self):
        """Final step — just confirm the artifacts are attached to the run."""
        logger.info("end: run finished, artifacts ready")
        logger.info("end: accuracy=%.4f", self.metrics["accuracy"])
        # Reminder to myself for pulling these back later via the Client API:
        #   from metaflow import Flow
        #   run = Flow('LoggingArtifactFlow').latest_run
        #   run.data.model, run.data.metrics


if __name__ == "__main__":
    LoggingArtifactFlow()
