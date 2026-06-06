# kub-006 — Install minikube and Kubeflow CLI, verify local setup

Tried the minikube-based approach for Kubeflow today since the Kind setup was heavy on my machine.

**what I did**

1. Installed minikube:
   ```
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   ```
   Verified with `minikube version`.

2. Started a cluster with enough resources:
   ```
   minikube start --cpus=4 --memory=8192 --driver=docker
   ```
   The driver flag is important - Docker Desktop on my machine runs minikube better this way.

3. Installed the Kubeflow Pipelines SDK:
   ```
   pip install kfp
   ```

4. Got the Kubeflow Pipelines CLI (kfp):
   ```
   which kfp
   kfp --version
   ```

5. Port-forwarded to the service:
   ```
   kubectl port-forward -n kubeflow svc/ml-pipeline-ui 3000:80
   ```
   Wait, the service wasn't there yet - minikube doesn't come with Kubeflow pre-installed. I need to deploy it first.

**what tripped me up**

- The Kubeflow CLI (`kfp`) is just the Pipelines SDK CLI, not a full Kubeflow installer. I confused it with something that would set up the whole platform.
- Minikube's default 2GB memory wasn't enough. Pods were stuck in `Pending` until I restarted with more RAM.
- The port-forward command needs the right namespace. Kubeflow Pipelines usually lives in `kubeflow`, but if you install via the standalone manifests it might be different.
- I tried `minikube addons enable kubeflow` but that doesn't exist - Kubeflow requires separate manifests.

**next**

Wait for Kubeflow to be actually deployed, then use `kfp` commands to compile and upload a pipeline.