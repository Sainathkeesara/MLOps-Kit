# mfl-033 — Metaflow flow: foreach fan-out, @resources, and @conda isolation
# Level: L3
#
# This flow demonstrates three Metaflow patterns together:
#   1. foreach fan-out — train a model for each hyperparameter pair in parallel
#   2. @resources      — declare CPU/memory so remote backends can schedule properly
#   3. @conda          — pin scikit-learn inside an isolated conda environment
#
# The flow trains small Random Forest classifiers on the Iris dataset across
# a grid of (n_estimators, max_depth) values, then collects every run's
# accuracy into a single summary in the join step.
#
# Run locally:
#   python foreach_resources_conda_flow.py run --with conda
#
# Run on AWS Batch (requires Metaflow batch config):
#   python foreach_resources_conda_flow.py run --with batch:image=python:3.11-slim
#
# Run on Kubernetes (requires Metaflow K8s config):
#   python foreach_resources_conda_flow.py run --with kubernetes
#
# last_verified: 2026-07-19 · Metaflow 2.x

from metaflow import FlowSpec, step, conda, resources, current


class ForeachResourcesCondaFlow(FlowSpec):
    """Train multiple Random Forest models in parallel using foreach,
    declare resources per step, and isolate dependencies with @conda."""

    param_grid = [
        {"n_estimators": 10, "max_depth": 3},
        {"n_estimators": 50, "max_depth": 5},
        {"n_estimators": 100, "max_depth": None},
    ]

    @step
    def start(self):
        """Load the Iris dataset and fan out into one training task per
        hyperparameter combination."""
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split

        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.3, random_state=42
        )
        self.X_train = X_train.tolist()
        self.X_test = X_test.tolist()
        self.y_train = y_train.tolist()
        self.y_test = y_test.tolist()
        print(
            f"start: loaded {len(X_train)} train / {len(X_test)} test samples, "
            f"fanning out across {len(self.param_grid)} configs"
        )
        self.next(self.train_model, foreach="param_grid")

    @conda(libraries={"scikit-learn"})
    @resources(memory=2048, cpu=2)
    @step
    def train_model(self):
        """Train one Random Forest for the current hyperparameter combo.

        The @conda decorator ensures scikit-learn is available inside an
        isolated environment even if the system Python has a different
        version. @resources declares the compute this step needs — meaningful
        on AWS Batch or Kubernetes, advisory (with a warning) when running
        locally.
        """
        import json

        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        params = self.input
        n_estimators = params["n_estimators"]
        max_depth = params["max_depth"]

        try:
            clf = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                random_state=42,
            )
            clf.fit(self.X_train, self.y_train)
            preds = clf.predict(self.X_test)
            acc = accuracy_score(self.y_test, preds)

            self.config = json.dumps(params)
            self.n_estimators = n_estimators
            self.max_depth = max_depth if max_depth is not None else -1
            self.test_acc = round(float(acc), 4)
            print(
                f"train_model [{current.step_run_id}]: "
                f"n_estimators={n_estimators}, max_depth={max_depth}, "
                f"accuracy={acc:.4f}"
            )
        except Exception as exc:
            print(f"train_model [{current.step_run_id}] failed: {exc}")
            raise
        finally:
            self.next(self.evaluate_models)

    @step
    def evaluate_models(self, inputs):
        """Join step: collect accuracy from every parallel training run.

        merge_artifacts merges identically-named artifacts from all branches.
        For foreach-specific artifacts (config, test_acc) we rebuild lists
        manually since merge_artifacts cannot collapse lists from branches.
        """
        import json

        configs = []
        accuracies = []
        n_estimators_list = []
        max_depth_list = []

        for run in inputs:
            configs.append(run.config)
            accuracies.append(run.test_acc)
            n_estimators_list.append(run.n_estimators)
            max_depth_list.append(run.max_depth)

        best_idx = accuracies.index(max(accuracies))
        best_params = json.loads(configs[best_idx])

        self.configs = configs
        self.accuracies = accuracies
        self.n_estimators_list = n_estimators_list
        self.max_depth_list = max_depth_list
        self.best_accuracy = accuracies[best_idx]
        self.best_params = best_params

        print(f"evaluate_models: {len(configs)} runs collected")
        print(
            f"  best: accuracy={self.best_accuracy:.4f}, "
            f"params={best_params}"
        )
        self.next(self.end)

    @step
    def end(self):
        """Summarize the fan-out result."""
        print(f"end: {len(self.accuracies)} models evaluated")
        for cfg, acc in zip(self.configs, self.accuracies):
            print(f"  {cfg} -> accuracy={acc:.4f}")
        print(f"Best params: {self.best_params} (accuracy={self.best_accuracy:.4f})")


if __name__ == "__main__":
    ForeachResourcesCondaFlow()
