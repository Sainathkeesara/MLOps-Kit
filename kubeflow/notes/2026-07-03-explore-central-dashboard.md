# kub-026 — Exploring the Kubeflow Central Dashboard

Tried the Central Dashboard today after getting Kubeflow running locally.

## What I saw

The landing page shows a cluster topology view with CPU/memory usage. Top nav has:

- **Pipelines** — opens the KFP UI in a new tab, not a modal
- **Notebook Servers** — can launch Jupyter on the cluster with one click
- **Katib** — hyperparameter tuning interface
- **Volumes** — persistent volume claims listed by name
- **Catalog** — sample workflows you can import

## What tripped me up

1. The "Kubeflow Pipelines SDK" checkbox in Notebook Servers confused me. It's optional - I unchecked it and picked a CPU-only image.

2. The Pipelines tab opens as a separate SPA. The URL changes completely and it feels like leaving the Dashboard.

3. When I tried to run the SDK inside the notebook, `dsl-compile` wasn't in PATH. I had to pip install kfp inside the notebook terminal.

4. Port-forwarding to see the UI: `kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80` — the namespace matters.

## Next

Try launching a notebook with the SDK already installed, then upload and run my hello-world pipeline from kub-025.