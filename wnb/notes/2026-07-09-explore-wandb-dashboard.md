# wnb-033 — Exploring the W&B dashboard: projects, runs, and artifacts

I logged into the W&B web UI for the first time today and clicked through the main panels to see how data flows between them.

## Projects page

The landing page lists every project with run count and last-active timestamp. Clicking a project name drops me into the workspace view for that project. Creating a project in code (`wandb.init(project="my-project")`) is what makes it appear here — nothing shows up until a run logs at least one metric.

## Workspace (runs view)

The default tab inside a project. The run table on the left shows config params and metrics as columns. I can reorder columns and pin the ones I care about (loss, accuracy). Charts auto-plot any metric that's been logged — no setup step. I can overlay multiple runs to compare curves directly.

## Artifacts tab

Artifacts logged with `wandb.Artifact` show up here as a lineage graph. Each artifact has a version tag (v0, v1 …) and a list of runs that produced or consumed it. Clicking an artifact shows its file contents preview, metadata, and the runs that used it. This is the first place I'd look to understand which dataset version a model was trained on.

## What tripped me up

**Gotcha 1:** Runs don't appear immediately. I refreshed 30 seconds after starting a run and saw "waiting for data" — the first metrics take a few seconds to flush from the SDK to the server.

**Gotcha 2:** The "Panel" tab is for custom dashboard layouts, not the default run view. I opened it expecting more detail on a single run and was confused by the empty canvas.
