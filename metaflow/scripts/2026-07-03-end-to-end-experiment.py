"""mfl-028 — End-to-end experiment with Metaflow tracking, model logging, and run comparison.

L2 — I built this flow to practice running multiple experiments with
different hyperparameters, logging models as artifacts, and comparing
runs using the Metaflow Client API. Metaflow handles tracking and
artifact management natively — no separate server needed.
"""

from metaflow import FlowSpec, step, Parameter, current
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


class EndToEndExperiment(FlowSpec):
    """Run an experiment end-to-end: train a model and log results as artifacts."""

    n_estimators = Parameter("n_estimators", default=50, help="Number of trees")
    max_depth = Parameter("max_depth", default=4, help="Max tree depth")
    seed = Parameter("seed", default=42, help="Random seed")

    @step
    def start(self):
        """Load data and split — I keep this as a separate step so I can inspect
        the raw data later via the UI or Client API."""
        iris = load_iris()
        self.df = pd.DataFrame(iris.data, columns=[f"feat_{i}" for i in range(iris.data.shape[1])])
        self.labels = iris.target
        self.target_names = list(iris.target_names)
        print(f"Loaded {len(self.df)} rows, {self.df.shape[1]} features")
        self.next(self.train)

    @step
    def train(self):
        """Split, train, and capture all artifacts in one step.

        Artifacts (X_train, model, metrics, etc.) are automatically persisted
        by Metaflow — no explicit log_metric() or log_model() needed.
        """
        X_train, X_test, y_train, y_test = train_test_split(
            self.df, self.labels, test_size=0.3, random_state=self.seed
        )
        self.X_train_shape = X_train.shape
        self.X_test_shape = X_test.shape

        clf = RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            random_state=self.seed,
        )
        clf.fit(X_train, y_train)

        train_preds = clf.predict(X_train)
        test_preds = clf.predict(X_test)
        self.train_acc = accuracy_score(y_train, train_preds)
        self.test_acc = accuracy_score(y_test, test_preds)
        # Storing the full model object as an artifact lets me reload it later
        # via Metaflow's Client API without saving to disk manually
        self.model = clf
        self.feature_names = list(self.df.columns)

        print(f"n_estimators={self.n_estimators}, max_depth={self.max_depth}")
        print(f"Train acc: {self.train_acc:.4f}, Test acc: {self.test_acc:.4f}")
        print(f"Model type: {type(clf).__name__}")
        self.next(self.verify)

    @step
    def verify(self):
        """Quick sanity — log extra info and confirm artifacts are accessible."""
        self.run_id = current.run_id
        print(f"Run ID: {self.run_id}")
        # classification_report isn't auto-captured, so I generate and log it
        # as an artifact for later reference in the UI
        iris = load_iris()
        _, X_test, _, y_test = train_test_split(
            self.df, self.labels, test_size=0.3, random_state=self.seed
        )
        preds = self.model.predict(X_test)
        self.report = classification_report(y_test, preds, target_names=self.target_names, output_dict=True)
        print("Done — artifacts saved. Inspect with:")
        print(f"  Run = Flow('EndToEndExperiment')[{self.run_id!r}]")
        print(f"  Run.data.model, Run.data.test_acc, Run.data.report")
        self.next(self.end)

    @step
    def end(self):
        print("Experiment complete.")


if __name__ == "__main__":
    EndToEndExperiment()
