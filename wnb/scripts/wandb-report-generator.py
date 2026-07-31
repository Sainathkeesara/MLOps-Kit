# last_verified: 2026-07-31 · wandb n/a

"""Reusable W&B report generator for automated experiment dashboards.

Queries runs from a W&B project, summarizes metrics and parameters across
the selected runs, and writes a Markdown report file that can be consumed
by humans or fed into downstream CI notifications.

Usage:
    python wandb-report-generator.py --project my-project --entity my-entity
    python wandb-report-generator.py --project my-project --metric accuracy --goal max
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


try:
    import wandb
except ImportError:
    wandb = None


@dataclass
class RunSummary:
    run_id: str
    name: str
    state: str
    created_at: datetime
    metrics: dict = field(default_factory=dict)
    config: dict = field(default_factory=dict)


def _resolve_api():
    if wandb is None:
        raise RuntimeError("wandb is not installed. Install it with: pip install wandb")
    return wandb.Api()


def fetch_runs(
    entity: str,
    project: str,
    metric: Optional[str] = None,
    goal: str = "maximize",
    limit: int = 50,
) -> List[RunSummary]:
    api = _resolve_api()
    runs = api.runs(f"{entity}/{project}", per_page=limit)

    summaries: List[RunSummary] = []
    for run in runs:
        summary = RunSummary(
            run_id=run.id,
            name=run.name,
            state=run.state,
            created_at=datetime.fromisoformat(run.created_at)
            if hasattr(run, "created_at") and run.created_at
            else datetime.utcnow(),
            metrics=dict(run.summary or {}),
            config=dict(run.config or {}),
        )
        summaries.append(summary)

    if metric and summaries:
        reverse = goal == "maximize"
        summaries.sort(
            key=lambda s: s.metrics.get(metric, float("-inf" if reverse else "inf")),
            reverse=reverse,
        )

    return summaries


def build_markdown_report(
    entity: str,
    project: str,
    summaries: List[RunSummary],
    metric: Optional[str] = None,
    goal: str = "maximize",
) -> str:
    lines: List[str] = [
        f"# W&B Experiment Dashboard Report",
        f"",
        f"- **Entity:** `{entity}`",
        f"- **Project:** `{project}`",
        f"- **Generated:** {datetime.utcnow().isoformat()}Z",
        f"- **Runs analyzed:** {len(summaries)}",
    ]

    if metric:
        lines.append(f"- **Sort metric:** `{metric}` ({goal})")

    lines += ["", "## Runs", ""]

    for s in summaries:
        lines.append(f"### {s.name} (`{s.run_id}`)")
        lines.append(f"- **State:** {s.state}")
        lines.append(f"- **Created:** {s.created_at.isoformat()}")

        if metric and metric in s.metrics:
            val = s.metrics[metric]
            lines.append(f"- **{metric}:** {val}")

        if s.config:
            lines.append("- **Parameters:**")
            for k, v in s.config.items():
                lines.append(f"  - `{k}`: {v}")

        lines.append("")

    return "\n".join(lines)


def write_report(report: str, output_path: str) -> str:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    return output_path


def log_artifact(
    entity: str,
    project: str,
    run_id: str,
    file_path: str,
    artifact_name: str = "experiment-dashboard-report",
) -> None:
    api = _resolve_api()
    run = api.run(f"{entity}/{project}/{run_id}")
    run.log_artifact(file_path, name=artifact_name, type="report")


def main() -> None:
    parser = argparse.ArgumentParser(description="W&B automated report generator")
    parser.add_argument("--project", required=True, help="W&B project name")
    parser.add_argument("--entity", default=None, help="W&B entity (team or username)")
    parser.add_argument("--metric", default=None, help="Metric to sort runs by")
    parser.add_argument("--goal", default="maximize", choices=["maximize", "minimize"])
    parser.add_argument("--limit", type=int, default=50, help="Max runs to fetch")
    parser.add_argument("--output", default="wandb-report.md", help="Report file path")
    parser.add_argument(
        "--log-artifact-run",
        default=None,
        help="If set, log the report as a W&B artifact to this run ID",
    )
    args = parser.parse_args()

    entity = args.entity or wandb.Api().default_entity

    summaries = fetch_runs(
        entity=entity,
        project=args.project,
        metric=args.metric,
        goal=args.goal,
        limit=args.limit,
    )

    report = build_markdown_report(
        entity=entity,
        project=args.project,
        summaries=summaries,
        metric=args.metric,
        goal=args.goal,
    )

    path = write_report(report, args.output)
    print(f"Report written to: {path}")

    if args.log_artifact_run:
        try:
            log_artifact(entity, args.project, args.log_artifact_run, path)
            print(f"Logged artifact to run {args.log_artifact_run}")
        except Exception as exc:
            print(f"Warning: could not log artifact — {exc}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=__import__("sys").stderr)
        __import__("sys").exit(1)
