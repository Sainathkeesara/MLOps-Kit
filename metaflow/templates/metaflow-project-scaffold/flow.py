"""Four-step Metaflow ML pipeline — load -> preprocess -> train -> evaluate."""

from metaflow import FlowSpec, Parameter, pypi, step

from components.data import load_and_split_data, scale_features
from components.train import train_random_forest
from components.evaluate import evaluate_classifier


class MetaflowMLPipeline(FlowSpec):
    """A template Metaflow pipeline with testing and CI/CD support."""

    test_size = Parameter("test_size", default=0.2, help="Fraction of data for testing")
    seed = Parameter("seed", default=42, help="Random seed")
    n_estimators = Parameter("n_estimators", default=100, help="RandomForest tree count")

    @pypi(libraries={"pandas": ">=1.3.0", "scikit-learn": ">=1.0.0", "numpy": ">=1.21.0"})
    @step
    def start(self):
        self.X_train, self.X_test, self.y_train, self.y_test, self.feature_names = (
            load_and_split_data(test_size=self.test_size, random_state=self.seed)
        )
        self.next(self.preprocess)

    @pypi(libraries={"scikit-learn": ">=1.0.0", "numpy": ">=1.21.0"})
    @step
    def preprocess(self):
        self.X_train_scaled, self.X_test_scaled = scale_features(
            self.X_train, self.X_test
        )
        self.next(self.train)

    @pypi(libraries={"scikit-learn": ">=1.0.0", "numpy": ">=1.21.0"})
    @step
    def train(self):
        self.model, self.train_accuracy = train_random_forest(
            self.X_train_scaled,
            self.y_train,
            n_estimators=self.n_estimators,
            random_state=self.seed,
        )
        print(f"Train accuracy: {self.train_accuracy:.4f}")
        self.next(self.evaluate)

    @pypi(libraries={"scikit-learn": ">=1.0.0", "pandas": ">=1.3.0"})
    @step
    def evaluate(self):
        self.test_accuracy, self.classification_report_str = evaluate_classifier(
            self.model, self.X_test_scaled, self.y_test, self.feature_names
        )
        print(f"Test accuracy: {self.test_accuracy:.4f}")
        print(self.classification_report_str)


if __name__ == "__main__":
    MetaflowMLPipeline().run()
