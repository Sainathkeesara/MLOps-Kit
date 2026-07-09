---
last_verified: 2026-07-06
tool_version: n/a
sources:
  - https://www.kubeflow.org/docs/started/installing-kubeflow
---

# Exploring the Kubeflow Central Dashboard (day one)

I logged into the Central Dashboard again, this time actually reading what each tile does instead of just clicking around. Here's what's there.

## What's on the dashboard

The landing page has the cluster topology view on the left (CPU/memory per node) and a grid of app tiles on the right. The tiles I care about right now:

- **Home** — the default landing view with the topology and quick links.
- **Pipelines** — opens the Kubeflow Pipelines (KFP) UI in a new tab. This is where I author and run pipelines.
- **Notebook Servers** — launches Jupyter servers on the cluster. Separate SPA, same look.
- **Katib** — hyperparameter tuning, integrated but its own UI.
- **Artifacts** — MinIO / object-storage browser for artifacts the pipelines write.
- **Volumes** — persistent volume claims I can mount into notebooks and pipelines.
- **Catalog** — sample workflows to import and learn from.

## What I noticed this time

The Dashboard is really a launcher for a set of subprojects. Kubeflow is composable: Pipelines, Notebooks, Katib, Trainer, etc. can run standalone OR as the full Kubeflow Community Distribution. That explains why the "install the whole thing" path felt so heavy earlier — I only needed Pipelines.

The **Artifacts** tile wasn't obvious to me on day one; it's basically a file browser over the bucket the pipelines write to, so I can grab a model or a metrics file without `kubectl exec`.

## What tripped me up

- Clicking a tile opens a *new tab* with a different URL and a different app — easy to lose the thread of "which UI am I in."
- The Notebook Server "New Server" form has a "Kubeflow Pipelines SDK" checkbox that pre-installs `kfp` in the notebook. I missed it day one and had to pip install it myself.
- Roles/permissions: the tiles you see depend on your namespace access. As a fresh user I only saw the default namespace.

## What I'd try next

- Run a pipeline from the Pipelines tile and watch its artifacts show up in the Artifacts tile.
- Open a notebook that can read the same PVCs the pipelines use.
