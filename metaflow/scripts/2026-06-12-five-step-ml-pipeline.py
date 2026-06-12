"""mfl-011 — 5-step ML pipeline with Metaflow from scratch.

Purpose: Build a complete ML pipeline as a Metaflow FlowSpec with five sequential
steps — load, clean, feature engineering, train, and evaluate. Demonstrates how
Metaflow handles data flow between steps via self-references and the @step decorator.

Steps:
  1. start       — Load the Iris dataset as a DataFrame
  2. clean_data  — Train/test split with configurable test size
  3. feature_engineering — Standard scaling (fit on train, transform both)
  4. train_model — RandomForest classifier, fit on scaled train data
  5. evaluate_model — Accuracy on train and test sets, classification report
"""

from metaflow import FlowSpec, step, Parameter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd


class FiveStepMLPipeline(FlowSpec):
    """A 5-step ML pipeline — load → clean → feature engineering → train → evaluate."""

    test_size = Parameter("test_size", default=0.2, help="Fraction of data for testing")
    seed = Parameter("seed", default=42, help="Random seed for reproducibility")
    n_estimators = Parameter("n_estimators", default=100, help="Number of trees in the forest")

    @step
    def start(self):
        """Step 1 — Load data from sklearn and wrap in a DataFrame."""
        iris = load_iris()
        self.df = pd.DataFrame(iris.data, columns=[f"feature_{i}" for i in range(iris.data.shape[1])])
        self.target = iris.target
        self.target_names = list(iris.target_names)
        print(f"Loaded {len(self.df)} samples, {self.df.shape[1]} features")
        self.next(self.clean_data)

    @step
    def clean_data(self):
        """Step 2 — Handle missing values and split into train/test."""
        if self.df.isnull().sum().sum() > 0:
            self.df = self.df.fillna(self.df.mean())
            print("Filled {} missing values")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.df, self.target,
            test_size=self.test_size,
            random_state=self.seed,
            stratify=self.target
        )
        print(f"Train: {len(self.X_train)} samples, Test: {len(self.X_test)} samples")
        self.next(self.feature_engineering)

    @step
    def feature_engineering(self):
        """Step 3 — Standardize features using training distribution."""
        self.scaler = StandardScaler()
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        print(f"Scaled {self.X_train_scaled.shape[1]} features (mean=0, std=1)")
        self.next(self.train_model)

    @step
    def train_model(self):
        """Step 4 — Train a RandomForest classifier on scaled data."""
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.seed
        )
        self.model.fit(self.X_train_scaled, self.y_train)
        self.train_acc = self.model.score(self.X_train_scaled, self.y_train)
        print(f"Train accuracy: {self.train_acc:.4f}")
        self.next(self.evaluate_model)

    @step
    def evaluate_model(self):
        """Step 5 — Evaluate on held-out test set and print detailed metrics."""
        self.test_acc = self.model.score(self.X_test_scaled, self.y_test)
        self.predictions = self.model.predict(self.X_test_scaled)
        self.class_report = classification_report(
            self.y_test, self.predictions,
            target_names=self.target_names,
            output_dict=False
        )
        print(f"Test accuracy: {self.test_acc:.4f}")
        print("\nClassification report:")
        print(self.class_report)


if __name__ == "__main__":
    FiveStepMLPipeline().run()
