# kub-004 — Setting up Kind for Kubeflow

I want to run Kubeflow locally so I tried Kind (Kubernetes in Docker) instead of a full cloud setup.

**what I did**

1. Installed Kind:
   ```
   curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
   chmod +x ./kind && sudo mv ./kind /usr/local/bin/kind
   ```
   Verified with `kind version`.

2. Wrote a config for Kubeflow — needs extra port mappings so the dashboard is reachable:
   ```yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
   - role: control-plane
     extraPortMappings:
     - containerPort: 30080
       hostPort: 8080
   ```

3. Created the cluster:
   ```
   kind create cluster --name kubeflow --config kind-config.yaml
   ```
   Took about a minute. Docker pulled the kindest/node image and booted the control plane.

4. Checked it:
   ```
   kubectl cluster-info --context kind-kubeflow
   kubectl get nodes
   kubectl get crd
   ```
   Cluster was running. Only built-in CRDs at this point — Kubeflow adds its own after install.

**what tripped me up**

- Kind defaults to limited resources. Docker on my machine had 2 CPUs and 2 GB RAM allocated. Kubeflow's pods couldn't start until I bumped it to 4 CPUs and 8 GB in Docker Desktop settings.
- Needed `kubectl context` switching. If you have multiple kubeconfig contexts, don't forget `--context kind-kubeflow`.

**next**

Install Kubeflow Pipelines on this cluster and run a hello-world component.
