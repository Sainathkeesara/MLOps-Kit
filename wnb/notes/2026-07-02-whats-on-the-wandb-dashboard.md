# wnb-031 — What's on the W&B dashboard

I opened the W&B web UI today to really look at what's there. I'd been logging runs from scripts but barely clicked around.

**The landing page (Projects)**
A list of all my projects. Each row shows project name, how many runs, latest activity. I clicked into wnb-demo.

**Inside a project — the Workspace tab**
This is the default view. Charts everywhere — W&B auto-plots every scalar metric I logged as a line chart. I see accuracy, loss, learning rate. There's a table of runs on the left with params and metrics columns.

**Run detail view**
Clicked a single run. The Overview tab shows config/hyperparams, summary metrics, and the system diagnostics (CPU, GPU, memory). The Logs tab has stdout/stderr. The Artifacts tab shows what I logged with wandb.Artifact.

**Compare mode**
Checked two runs and hit "Compare". Side-by-side diffs of params and overlaid metric curves. Super useful for seeing which hyperparam tweak actually helped.

**The Charts tab**
Lets me build custom plots from scratch — pick which runs, which metrics, aggregation. I didn't try it yet but it looks powerful.

**Sweeps tab**
Linked to any active or completed sweeps in the project. Shows the sweep config, parameter distributions, and best runs.

**What I'd try next**
Tag my runs with meaningful labels and set up a custom dashboard panel for the metrics I care about most.
