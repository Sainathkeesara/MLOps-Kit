# last_verified: 2026-07-04 · seldon-core n/a
# I installed Seldon Core via Helm first, then tried deploying a model
# helm repo add seldonio https://storage.googleapis.com/seldon-charts
# helm install seldon-core seldonio/seldon-core-operator --namespace seldon-system --create-namespace

from kubernetes import client, config

# Use the SeldonDeployment CRD via the Kubernetes API
config.load_kube_config()

deployment = {
    "apiVersion": "machinelearning.seldon.io/v1",
    "kind": "SeldonDeployment",
    "metadata": {"name": "sklearn-iris"},
    "spec": {
        "name": "iris",
        "predictors": [{
            "graph": {
                "implementation": "SKLEARN_SERVER",
                "modelUri": "gs://your-bucket/models/iris-model.pkl",
                "name": "classifier"
            },
            "name": "default",
            "replicas": 1
        }]
    }
}

# I think I can use the CRD client but for now just shell out to kubectl
import subprocess
import json
with open("/tmp/seldon-deploy.json", "w") as f:
    json.dump(deployment, f)

result = subprocess.run(["kubectl", "apply", "-f", "/tmp/seldon-deploy.json"], capture_output=True, text=True)
print(result.stdout.strip())
# TODO: test prediction — curl the ambassador endpoint
