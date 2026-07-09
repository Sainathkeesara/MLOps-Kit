---
last_verified: 2026-07-05
tool_version: n/a
sources: []
---

# wnb-033 — Exploring the W&B dashboard: projects, runs, and artifacts

I already poked around the dashboard before but today I specifically focused on how projects, runs, and artifacts connect.

**Projects page** — the landing list. Each project shows run count and last activity time. I clicked into my `wnb-demo` project to see what's there.

**Workspace (runs view)** — the default tab after you enter a project. The run table on the left shows columns for config params and metrics. I noticed I can reorder columns and pin the ones I care about (loss, accuracy). The charts auto-plot everything — no setup needed.

**Artifacts tab** — this was new to me. It shows a lineage graph: which artifact versions a run consumed (input) and produced (output). I had logged a dataset with `wandb.Artifact` in an earlier run and could see it here with its version tag (v0, v1). Clicking an artifact shows the metadata, file contents preview, and which runs used it. I didn't realize artifacts track this much detail out of the box.

**What I'd try next** — link an artifact from one run as input to another run, then walk the lineage to see the full DAG.

