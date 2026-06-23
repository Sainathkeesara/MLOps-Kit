# ClearML Web UI — first look

I signed up for the free ClearML hosted tier and started poking around the web UI today. Here's what I found after logging my first task.

## Projects

The top-level container is a "project". When I ran `Task.init(project_name="my-project", ...)`, it created a project automatically in the UI. Each project has its own page with tabs for experiments, artifacts, and logs. I can also create projects manually from the UI before running any code.

## Experiments

Inside a project, each `Task` shows up as an experiment. Clicking into one opens a detail view with:
- **Parameters** — the hyperparameters I logged with `task.set_parameters()`.
- **Metrics** — scalar plots if I logged them with `task.get_logger().report_scalar()`.
- **Console** — stdout/stderr from the running task, live if it's still executing.
- **Artifacts** — uploaded files like models or plots.

I tried logging a metric and it showed up as a chart immediately. That's the main value prop — everything from a run ends up in one place without me wiring up anything extra.

## Dashboards

The dashboard view lets me pin charts from multiple experiments side by side. I selected a couple of runs from the same project and overlaid their loss curves. It's basic but functional — good enough to spot whether a learning rate change actually helped.

## Got stuck

I couldn't figure out how to delete a project from the UI. Turns out you do it from the "Settings" tab on the project page, not from the main project list. Small UX thing.

## What I'd try next

I want to see what happens when I push a task to a remote queue and watch it execute on a ClearML Agent. Also curious whether the dashboard can compare across projects, not just within one.
