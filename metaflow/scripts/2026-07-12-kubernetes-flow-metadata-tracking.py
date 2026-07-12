"""mfl-031 — Metaflow flow with @kubernetes decorator and cloud metadata tracking.

L2 — I followed the Metaflow docs to move a training step onto Kubernetes
using @kubernetes instead of running everything locally. The flow has three
steps: start (local data prep), train_on_k8s (runs inside a K8s pod), and
end (local metadata inspection). I also tag artifacts with current.run_id
and current.flow_name so I can find the exact run later in the UI or via
the Client API.
"""

from metaflow import FlowSpec, Parameter, current, kubernetes, step


class KubernetesMetadataFlow(FlowSpec):
    """Practice flow: run a training step on Kubernetes with run-level metadata."""

    n_estimators = Parameter("n_estimators", default=30, help="Number of trees")
    seed = Parameter("seed", default=42, help="Random seed")

    @step
    def start(self):
        """Prepare a tiny dataset locally before shipping artifacts to the pod.

        I keep data prep local because it's fast and I want to inspect the
        raw arrays before they get serialized and sent to Kubernetes.
        """
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split

        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.3, random_state=self.seed
        )
        self.X_train = X_train.tolist()
        self.y_train = y_train.tolist()
        self.X_test = X_test.tolist()
        self.y_test = y_test.tolist()
        self.feature_names = list(iris.feature_names)
        self.target_names = list(iris.target_names)
        print(f"start: loaded {len(X_train)} train / {len(X_test)} test samples")
        self.next(self.train_on_k8s)

    @kubernetes(image="python:3.11-slim")
    @step
    def train_on_k8s(self):
        """Train a small RandomForest inside a Kubernetes pod.

        The @kubernetes decorator tells Metaflow to schedule this step as a
        K8s pod instead of running it on my laptop. Metaflow serializes the
        artifacts from the previous step, ships them to the pod, runs the
        code, and persists the outputs automatically.
        """
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        clf = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.seed,
            max_depth=3,
        )
        clf.fit(self.X_train, self.y_train)
        preds = clf.predict(self.X_test)
        acc = accuracy_score(self.y_test, preds)

        self.model = clf
        self.test_acc = float(acc)
        self.run_meta = {
            "flow": current.flow_name,
            "run_id": current.run_id,
            "step": current.step_name,
        }
        print(f"train_on_k8s: accuracy={acc:.4f}")
        print(f"Metadata: {self.run_meta}")
        self.next(self.end)

    @step
    def end(self):
        """Final step — confirm the run and show how to retrieve artifacts."""
        print(f"end: flow={current.flow_name}, run_id={current.run_id}")
        print(f"end: final test_acc={self.test_acc:.4f}")
        print("Inspect later with:")
        print(f"  run = Flow('KubernetesMetadataFlow')['{current.run_id}']")
        print(f"  run.data.model, run.data.test_acc")


if __name__ == "__main__":
    KubernetesMetadataFlow()
