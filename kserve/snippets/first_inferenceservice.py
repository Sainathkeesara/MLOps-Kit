from kserve import KServeClient, V1beta1InferenceService
from kserve import V1beta1InferenceServiceSpec, V1beta1PredictorSpec
from kserve import V1beta1SKLearnSpec
from kubernetes import client

namespace = "default"
model_name = "sklearn-iris"
model_uri = "gs://your-bucket/models/iris-model.pkl"

isvc = V1beta1InferenceService(
    api_version="serving.kserve.io/v1beta1",
    kind="InferenceService",
    metadata=client.V1ObjectMeta(name=model_name, namespace=namespace),
    spec=V1beta1InferenceServiceSpec(
        predictor=V1beta1PredictorSpec(
            sklearn=V1beta1SKLearnSpec(
                storage_uri=model_uri
            )
        )
    )
)

client = KServeClient()
client.create(isvc)
print(f"InferenceService {model_name} created in namespace {namespace}")
