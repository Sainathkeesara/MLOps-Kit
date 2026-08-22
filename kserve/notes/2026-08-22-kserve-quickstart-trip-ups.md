---
last_verified: 2026-08-22
tool_version: "—"
---

# KServe quickstart — what tripped me up

> Following the official KServe quickstart and writing up what worked, where it broke, and what I'd try next.

## What I did

Followed the official KServe quickstart to deploy a scikit-learn Iris classifier on a Kubernetes cluster. Started by installing the KServe Python SDK with `pip install kserve` and verifying the cluster had KServe installed via `kubectl get pods -n kserve`. Then I wrote a minimal InferenceService YAML that points at a pre-trained model stored in a public S3 bucket. The YAML declares the predictor, the runtime (default sklearn server), and the model URI in a 20-line manifest.

Applied the manifest with `kubectl apply -f isvc.yaml`. KServe created the InferenceService resource and the predictor pod came up within a minute. I verified the endpoint by curling `/v1/models/iris` — it returned a prediction JSON with class probabilities. The latency was around 40ms per request, which felt reasonable for a CPU-only sklearn model.

Next I added a canary rollout section to the same YAML to split traffic 90/10 between the original model and a new version. KServe created a new revision and the traffic split worked as expected. I sent a few hundred requests and roughly 10% hit the new revision, confirming the rollout was live without any downtime.

## Got stuck on

The first real blocker was Knative networking. My test cluster didn't have a cloud provider LoadBalancer provisioned, so `kubectl get svc -n knative-serving` showed the external IP as `<pending>` for over ten minutes. Without an external IP, I couldn't reach the inference endpoint from outside the cluster. The workaround was `kubectl port-forward` to the Knative activator service on port 80, but that's not a sustainable pattern for real traffic.

The second issue was model access. My second test used a private S3 bucket without credentials configured. The predictor pod started but immediately crashed with a 403 from S3. I had to either make the bucket public or attach a service account with read permissions. For local testing, public buckets are faster. I also noticed that if the model URI has a trailing slash or wrong extension, the predictor fails to load and the pod stays in a CrashLoopBackOff state.

## What I'd try next

I want to test the ModelMesh runtime for multi-model serving — it pools multiple models in a single pod set instead of spinning up one predictor per model, which should cut resource usage. I also want to try the raw Kubernetes deployment mode inside a Kind cluster to compare cold-start times without the Knative dependency. Finally, I want to add a transformer step for input preprocessing to see how the request/response transformation pipeline works.
