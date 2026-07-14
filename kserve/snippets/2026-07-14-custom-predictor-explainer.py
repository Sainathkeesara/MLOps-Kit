# last_verified: 2026-07-14 · kserve n/a

"""
Trying to build a KServe InferenceService with a custom predictor and
an Alibi explainer using the Python SDK. The built-in sklearn runtime
worked fine last time, but I need a custom predictor for models that
don't fit into the pre-built runtimes (e.g. a custom PyTorch model
with preprocessing steps baked in).

Breakdown:
1. Custom Model class (what you put in the model server image)
2. InferenceService resource with a custom container predictor + explainer
"""

# --- Part 1: Custom predictor definition ---
# This would go in a separate file (model.py) in the model server image.
# The KServe Model base class handles the HTTP/gRPC server — I just
# override load() and predict().

from typing import Dict, List
import joblib
import numpy as np
from kserve import Model, ModelServer


class TrainedModelPredictor(Model):
    """Custom predictor that loads a pickled model and runs inference."""

    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self._model = None
        self.load()

    def load(self) -> bool:
        # The model artifact gets mounted at /mnt/models by KServe
        # when you set STORAGE_URI as an env var on the container.
        model_path = "/mnt/models/model.pkl"
        self._model = joblib.load(model_path)
        self.ready = True
        print(f"{self.name}: loaded model from {model_path}")
        return True

    def predict(self, payload: Dict, headers: List[str] = None) -> Dict:
        # KServe sends {"instances": [[...], [...]]} by default
        instances = payload["instances"]
        results = self._model.predict(np.array(instances))
        return {"predictions": results.tolist()}


# Entry point when this file runs inside the model-server container.
# kserve.ModelServer registers the model and starts the KServe
# inference REST/gRPC server.
if __name__ == "__main__":
    predictor = TrainedModelPredictor("custom-iris")
    ModelServer().start([predictor])


# --- Part 2: Deploy the InferenceService with custom predictor + explainer ---
# This script runs from your workstation / CI, not from the model container.
# It creates a KServe InferenceService resource on the cluster.

from kubernetes import client
from kserve import (
    KServeClient,
    V1beta1InferenceService,
    V1beta1InferenceServiceSpec,
    V1beta1PredictorSpec,
    V1beta1ExplainerSpec,
    V1beta1AlibiExplainerSpec,
)

NAMESPACE = "default"
SERVICE_NAME = "custom-iris-predictor"

# The image you'd build from Part 1 and push to your registry
CUSTOM_IMAGE = "my-registry/custom-iris-predictor:latest"

# Alibi-Explain explainer using AnchorTabular
explainer_spec = V1beta1ExplainerSpec(
    alibi=V1beta1AlibiExplainerSpec(
        type="AnchorTabular",
        storage_uri="gs://your-bucket/explainer/iris-metadata",
    )
)

# Predictor using a custom container (not the built-in sklearn runtime)
predictor_spec = V1beta1PredictorSpec(
    containers=[
        client.V1Container(
            name="custom-predictor",
            image=CUSTOM_IMAGE,
            env=[
                client.V1EnvVar(
                    name="STORAGE_URI",
                    value="gs://your-bucket/models/iris-model.pkl",
                )
            ],
            ports=[client.V1ContainerPort(container_port=8080)],
        )
    ]
)

isvc = V1beta1InferenceService(
    api_version="serving.kserve.io/v1beta1",
    kind="InferenceService",
    metadata=client.V1ObjectMeta(name=SERVICE_NAME, namespace=NAMESPACE),
    spec=V1beta1InferenceServiceSpec(
        predictor=predictor_spec,
        explainer=explainer_spec,
    ),
)

KServeClient().create(isvc)
print(f"InferenceService {SERVICE_NAME} created with custom predictor + explainer")

# Verify it's ready:
#   kubectl get inferenceservice custom-iris-predictor -o yaml
# The status.conditions should show Ready=True once Knative provisions the revision.
