from metaflow import FlowSpec, step, Parameter, current
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np


class ModelServingFlow(FlowSpec):
    mode = Parameter("mode", default="train", type=str)
    # mode="predict" loads the model from the last successful run

    @step
    def start(self):
        X, y = make_classification(n_samples=500, random_state=42)
        X_test, y_test = make_classification(n_samples=5, random_state=99)
        self.X_train, self.y_train = X, y
        self.X_test, self.y_test = X_test, y_test
        self.next(self.train_model)

    @step
    def train_model(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        self.accuracy = float(self.model.score(self.X_train, self.y_train))
        print(f"Train accuracy: {self.accuracy:.3f}")
        self.next(self.end)

    @step
    def end(self):
        if self.mode == "predict":
            # Load the most recent successful run's model artifact
            # Metaflow stores artifacts per run; we pull the last one
            flow = type(self).get_latest_successful_run()
            if flow is None:
                print("No previous successful run found — train first")
                return
            step_data = flow["train_model"].task.data
            model = step_data.model
            preds = model.predict(self.X_test)
            print(f"Predictions: {preds}")
        else:
            print("Training done. Run with --mode predict to serve")


if __name__ == "__main__":
    ModelServingFlow()
