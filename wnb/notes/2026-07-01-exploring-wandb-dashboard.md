# wnb-031 — Exploring the W&B dashboard: what's there

I logged into the W&B web UI today to see what panels and views are available. I'd run a few training scripts already but hadn't actually looked at the dashboard in detail.

## What I found

- **Runs table** — lists every run with columns for metrics, params, and system stats. Clicking a run opens the detail view.
- **Charts** — line charts for any logged metric render automatically. I can overlay multiple runs to compare curves.
- **Compare** — select multiple runs and click "Compare" to see side-by-side param diffs and metric plots.
- **Artifacts** — files saved with `wandb.Artifact` show up under the project's Artifacts tab. Model binaries, datasets, and config files all versioned here.
- **Tables** — W&B renders logged `wandb.Table` objects as interactive tables. I filtered rows and sorted by columns directly in the UI.
- **System monitor** — CPU, memory, GPU usage graphs are logged automatically. No extra code needed.

## What tripped me up

**Gotcha 1:** Runs don't appear immediately. I clicked into a run 30s after starting it and saw a "waiting for data" spinner. It takes a few seconds for the first metrics to flush.

**Gotcha 2:** The "Panel" tab confused me. It's not for panels in the run view — it's for creating custom dashboard layouts. I skipped it and focused on the default run view.