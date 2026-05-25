# kf-002 — Install Kubeflow locally and explore the UI

Tried installing Kubeflow today. Decided to go with the standalone kind-based deployment since I don't have a real K8s cluster handy.

**what I did**

1. Created a kind cluster:
   `kind create cluster --name kubeflow`

   It took a minute to pull the node image and bootstrap the cluster. No issues here.

2. Applied the Kubeflow manifests via kustomize:
   `kubectl apply -k github.com/kubeflow/manifests//kustomize/cluster-scoped-resources?ref=v1.8.0`

   A wall of CRDs scrolled by. Custom Resource Definitions for things like PodDefault, Notebook, and Profile.

3. Applied namespace-scoped resources:
   `kubectl apply -k github.com/kubeflow/manifests//kustomize/env/platform?ref=v1.8.0`

   More scrolling — this time deployments, services, and configmaps in the kubeflow namespace.

4. Checked pod status:
   `kubectl get pods -n kubeflow`

   Most pods were Running after about 5 minutes. `istio-ingressgateway` was still Pending — probably needs more RAM.

5. Port-forwarded the Istio gateway:
   `kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80`

   Hit http://localhost:8080 and the Central Dashboard loaded.

**what I saw in the UI**

- A navigation sidebar with links to Pipelines, Notebooks, Experiments, and Katib.
- A profile/namespace selector at the top.
- The Pipelines section was empty (expected — nothing uploaded yet).
- The Notebooks section had a "New Notebook" button that lets me spin up a Jupyter server with a couple clicks. It asks for a name, namespace, and image.
- The Experiments section looked like a place to group related runs — similar to the concept in the primer.

**stuck on**

- Istio-related pods needed more RAM. I gave Docker 6 GB after the first attempt failed.
- The port-forward command uses `istio-system`, not the `kubeflow` namespace. That tripped me up for a minute — I kept checking the wrong namespace.
- The dashboard URL redirected to Dex for auth on first load. I had to create a static password user in the Dex config to log in.

**next**

Upload a simple pipeline YAML and run it from the Pipelines UI to see the DAG render.
