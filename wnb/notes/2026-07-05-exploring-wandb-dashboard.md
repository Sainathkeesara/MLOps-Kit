---
last_verified: 2026-07-05
tool_version: n/a
sources: []
---

# wnb-033 — Explore the W&B dashboard: projects, runs, and artifacts

I spent some time clicking through the W&B web UI today to understand the three main sections.

**Projects page** — the landing view. Lists every project I've created, with run count and last activity. I clicked into my `wnb-demo` project to see what's inside.

**Runs table** — inside a project, the Workspace tab shows all runs as a table. Columns for params, metrics, and system stats. I can sort, filter, and group runs. Clicking a run opens the detail view with config, charts, and logs.

**Artifacts tab** — this is separate from the run detail. At the project level, the Artifacts tab shows a version tree of everything logged with `wandb.Artifact` — datasets, model binaries, preprocessing objects. Each artifact has a full version history with lineage (which run produced it, which runs consumed it).

I hadn't appreciated how artifacts connect runs. You can mark an artifact as an input to one run and output of another, and W&B draws the dependency graph. That's the real value — traceability across experiments.
