# wnb-014 — Exploring the W&B dashboard: runs, projects, and experiment comparison

I logged in to the W&B web UI today to actually look at what happens with my runs. Up to now I'd been running scripts and checking terminal output — time to see the dashboard properly.

**What I explored**

- **Projects page** — lists all projects I've created (wnb-demo, quickstart, etc.). Each shows a latest-run timestamp and quick stats.
- **Run detail view** — clicked into a run from wnb-demo. Saw params, metrics charts, system resources, and the git state W&B auto-captured.
- **Compare mode** — selected two runs from the same project and hit "Compare". The table showed side-by-side config values and metric curves overlaid on one chart.
- **Workspace** — the main project view with a grid of charts. W&B auto-generates line plots for any scalar metric you log.

**What stood out**

- Comparing runs is where W&B shines. I could see which hyperparams differed and how accuracy changed — way easier than grepping terminal logs.
- The auto-logged git hash and Python version are subtle but save time when I forget what code produced a given run.
- Projects group runs by intent. I renamed my ad-hoc runs to meaningful names so I can tell them apart later.

**What I'd try next**

Set up a team project with proper run tags and a custom dashboard panel for the metrics I care about most.
