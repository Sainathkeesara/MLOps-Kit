# last_verified: 2026-09-07 · wandb n/a
"""Reusable W&B report generator for automated experiment dashboards.

Queries runs from a W&B project via the public API, computes per-metric
statistics (min / max / mean / std), and writes either a Markdown summary
or a CSV file suitable for downstream CI notifications or spreadsheet import.

Design notes:
    - Pagination is handled automatically; the default ``per_page`` of 200
      covers projects with up to a few thousand runs without multiple round
      trips.
    - The script never calls ``wandb.init()`` — it operates purely against
      the REST API through ``wandb.Api()``.  This means it can run in CI
      without a W&B login session, as long as ``WANDB_API_KEY`` is set.
    - Metric statistics are computed in-memory.  For projects with tens of
      thousands of runs the ``--limit`` flag should be used to cap the
      working set.

Usage:
    # Markdown report sorted by validation loss (ascending)
    python wandb-report-generator.py \\
        --project my-org/my-project \\
        --metrics val_loss,train_loss,accuracy \\
        --sort-metric val_loss --sort-goal minimize

    # CSV export filtered to finished runs from the last 7 days
    python wandb-report-generator.py \\
        --project my-project \\
        --state finished --days 7 \\
        --format csv --output runs.csv

    # Attach the report to a specific W&B run as an artifact
    python wandb-report-generator.py \\
        --project my-project \\
        --log-artifact-run abc123
"""

from __future__ import annotations

import argparse
import csv
import io
import logging
import os
import statistics
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

try:
    import wandb
except ImportError:
    wandb = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class RunSummary:
    """Lightweight snapshot of a single W&B run."""
    run_id: str
    name: str
    state: str
    created_at: datetime
    tags: List[str] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MetricStats:
    """Descriptive statistics for one metric across a set of runs."""
    name: str
    count: int
    min_val: float
    max_val: float
    mean_val: float
    std_val: float


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _get_api():
    """Return a ``wandb.Api`` instance, raising a clear error if wandb is missing."""
    if wandb is None:
        raise RuntimeError(
            "wandb is not installed. Install it with: pip install wandb"
        )
    return wandb.Api()


def fetch_runs(
    entity: str,
    project: str,
    *,
    metrics: Optional[List[str]] = None,
    state: Optional[str] = None,
    tags: Optional[List[str]] = None,
    days: Optional[int] = None,
    limit: int = 200,
) -> List[RunSummary]:
    """Fetch runs from *entity/project* with optional filters.

    Parameters
    ----------
    entity:
        W&B entity (username or team name).  If ``None``, the API default
        is used.
    project:
        W&B project name.
    metrics:
        If provided, only these metric keys are extracted from each run's
        summary.  ``None`` means *all* summary keys are kept.
    state:
        Filter to runs matching this state (e.g. ``"finished"``,
        ``"running"``, ``"crashed"``).
    tags:
        If provided, only runs that carry *all* of these tags are returned.
    days:
        If provided, only runs created within the last *days* days are
        returned.
    limit:
        Maximum number of runs to retrieve (pagination boundary).
    """
    api = _get_api()
    path = f"{entity}/{project}" if entity else project

    try:
        runs = api.runs(path, per_page=min(limit, 200))
    except Exception as exc:
        raise RuntimeError(f"Failed to list runs for '{path}': {exc}") from exc

    cutoff: Optional[datetime] = None
    if days is not None:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    summaries: List[RunSummary] = []
    for i, run in enumerate(runs):
        if i >= limit:
            break

        # --- state filter ---
        if state and run.state != state:
            continue

        # --- tag filter ---
        run_tags = list(run.tags or [])
        if tags and not all(t in run_tags for t in tags):
            continue

        # --- date filter ---
        created = (
            datetime.fromisoformat(run.created_at.replace("Z", "+00:00"))
            if getattr(run, "created_at", None)
            else datetime.now(timezone.utc)
        )
        if cutoff and created < cutoff:
            continue

        # --- extract metrics ---
        raw_summary: Dict[str, Any] = dict(run.summary or {})
        if metrics:
            selected = {m: raw_summary.get(m) for m in metrics}
        else:
            selected = raw_summary

        summaries.append(
            RunSummary(
                run_id=run.id,
                name=run.name or run.id,
                state=run.state,
                created_at=created,
                tags=run_tags,
                metrics=selected,
                config=dict(run.config or {}),
            )
        )

    logger.info("Fetched %d runs (from %d total).", len(summaries), i + 1)
    return summaries


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def compute_metric_stats(summaries: List[RunSummary], metric: str) -> Optional[MetricStats]:
    """Compute min / max / mean / std for *metric* across *summaries*.

    Runs where the metric is missing or non-numeric are silently skipped.
    Returns ``None`` if no numeric values are found.
    """
    values: List[float] = []
    for s in summaries:
        v = s.metrics.get(metric)
        if v is None:
            continue
        try:
            values.append(float(v))
        except (TypeError, ValueError):
            continue

    if not values:
        return None

    return MetricStats(
        name=metric,
        count=len(values),
        min_val=min(values),
        max_val=max(values),
        mean_val=statistics.mean(values),
        std_val=statistics.pstdev(values) if len(values) > 1 else 0.0,
    )


# ---------------------------------------------------------------------------
# Report builders
# ---------------------------------------------------------------------------

def _format_md_report(
    entity: str,
    project: str,
    summaries: List[RunSummary],
    sort_metric: Optional[str],
    sort_goal: str,
    metric_list: Optional[List[str]],
) -> str:
    """Build a Markdown report string."""
    lines: List[str] = [
        f"# W&B Experiment Dashboard Report",
        "",
        f"- **Entity:** `{entity}`",
        f"- **Project:** `{project}`",
        f"- **Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"- **Runs analyzed:** {len(summaries)}",
    ]

    if sort_metric:
        lines.append(f"- **Sort metric:** `{sort_metric}` ({sort_goal})")

    # --- statistics table ---
    effective_metrics = metric_list or _discover_metrics(summaries)
    if effective_metrics:
        lines += ["", "## Metric Summary", ""]
        lines.append("| Metric | Count | Min | Max | Mean | Std |")
        lines.append("|--------|-------|-----|-----|------|-----|")
        for m in effective_metrics:
            stats = compute_metric_stats(summaries, m)
            if stats is None:
                lines.append(f"| `{m}` | — | — | — | — | — |")
            else:
                lines.append(
                    f"| `{m}` | {stats.count} "
                    f"| {stats.min_val:.6g} | {stats.max_val:.6g} "
                    f"| {stats.mean_val:.6g} | {stats.std_val:.6g} |"
                )

    # --- sorted run list ---
    sorted_runs = _sort_runs(summaries, sort_metric, sort_goal)
    lines += ["", "## Runs", ""]
    for s in sorted_runs:
        lines.append(f"### {s.name} (`{s.run_id}`)")
        lines.append(f"- **State:** {s.state}")
        lines.append(f"- **Created:** {s.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        if s.tags:
            lines.append(f"- **Tags:** {', '.join(s.tags)}")

        if sort_metric and sort_metric in s.metrics:
            lines.append(f"- **{sort_metric}:** {s.metrics[sort_metric]}")

        if s.config:
            lines.append("- **Parameters:**")
            for k, v in s.config.items():
                lines.append(f"  - `{k}`: {v}")

        if s.metrics:
            lines.append("- **Metrics:**")
            for k, v in s.metrics.items():
                lines.append(f"  - `{k}`: {v}")

        lines.append("")

    return "\n".join(lines)


def _format_csv_report(
    summaries: List[RunSummary],
    sort_metric: Optional[str],
    sort_goal: str,
    metric_list: Optional[List[str]],
) -> str:
    """Build a CSV report string."""
    effective_metrics = metric_list or _discover_metrics(summaries)
    sorted_runs = _sort_runs(summaries, sort_metric, sort_goal)

    buf = io.StringIO()
    fieldnames = ["run_id", "name", "state", "created_at", "tags"] + effective_metrics
    writer = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()

    for s in sorted_runs:
        row: Dict[str, Any] = {
            "run_id": s.run_id,
            "name": s.name,
            "state": s.state,
            "created_at": s.created_at.isoformat(),
            "tags": ";".join(s.tags),
        }
        for m in effective_metrics:
            row[m] = s.metrics.get(m, "")
        writer.writerow(row)

    return buf.getvalue()


def _discover_metrics(summaries: List[RunSummary]) -> List[str]:
    """Return the union of all metric keys across *summaries*, preserving order."""
    seen: Dict[str, None] = {}
    for s in summaries:
        for k in s.metrics:
            if k not in seen:
                seen[k] = None
    return list(seen.keys())


def _sort_runs(
    summaries: List[RunSummary],
    metric: Optional[str],
    goal: str,
) -> List[RunSummary]:
    """Return *summaries* sorted by *metric* (ascending for minimize, descending for maximize)."""
    if not metric:
        return summaries

    reverse = goal == "maximize"
    sentinel = float("-inf" if reverse else "inf")
    return sorted(
        summaries,
        key=lambda s: float(s.metrics.get(metric, sentinel)),
        reverse=reverse,
    )


# ---------------------------------------------------------------------------
# Artifact logging
# ---------------------------------------------------------------------------

def log_artifact(
    entity: str,
    project: str,
    run_id: str,
    file_path: str,
    artifact_name: str = "experiment-dashboard-report",
) -> None:
    """Log *file_path* as a W&B artifact attached to *run_id*.

    This is a best-effort operation — failures are logged as warnings rather
    than aborting the report generation.
    """
    api = _get_api()
    try:
        run = api.run(f"{entity}/{project}/{run_id}")
        run.log_artifact(file_path, name=artifact_name, type="report")
        logger.info("Logged artifact '%s' to run %s.", artifact_name, run_id)
    except Exception as exc:
        logger.warning("Could not log artifact to run %s: %s", run_id, exc)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a summary report from W&B experiment runs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--project", required=True,
        help="W&B project in the form entity/project or just project.",
    )
    parser.add_argument(
        "--entity", default=None,
        help="W&B entity (team or username). Overrides the entity in --project.",
    )
    parser.add_argument(
        "--metrics", default=None,
        help="Comma-separated metric keys to include (default: all).",
    )
    parser.add_argument(
        "--sort-metric", default=None,
        help="Metric used to sort runs in the report.",
    )
    parser.add_argument(
        "--sort-goal", default="maximize",
        choices=["maximize", "minimize"],
        help="Whether higher or lower values are better for --sort-metric.",
    )
    parser.add_argument(
        "--state", default=None,
        help="Filter runs by state (e.g. finished, running, crashed).",
    )
    parser.add_argument(
        "--tags", default=None,
        help="Comma-separated tags; only runs with ALL listed tags are included.",
    )
    parser.add_argument(
        "--days", type=int, default=None,
        help="Only include runs from the last N days.",
    )
    parser.add_argument(
        "--limit", type=int, default=200,
        help="Maximum number of runs to fetch (default: 200).",
    )
    parser.add_argument(
        "--format", default="markdown",
        choices=["markdown", "csv"],
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--output", default="wandb-report.md",
        help="Output file path (default: wandb-report.md).",
    )
    parser.add_argument(
        "--log-artifact-run", default=None,
        help="If set, log the report as a W&B artifact to this run ID.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> None:
    args = _build_parser().parse_args(argv)

    # Resolve entity: explicit --entity overrides the one embedded in --project.
    entity: Optional[str] = args.entity
    project: str = args.project
    if entity is None and "/" in project:
        entity, project = project.split("/", 1)

    if entity is None:
        try:
            api = _get_api()
            entity = api.default_entity  # type: ignore[assignment]
        except Exception:
            logger.warning("Could not determine default entity; passing None to API.")

    metric_list = [m.strip() for m in args.metrics.split(",")] if args.metrics else None
    tag_list = [t.strip() for t in args.tags.split(",")] if args.tags else None

    summaries = fetch_runs(
        entity=entity or "",
        project=project,
        metrics=metric_list,
        state=args.state,
        tags=tag_list,
        days=args.days,
        limit=args.limit,
    )

    if not summaries:
        logger.warning("No runs matched the given filters — report will be empty.")

    if args.format == "csv":
        report = _format_csv_report(summaries, args.sort_metric, args.sort_goal, metric_list)
    else:
        report = _format_md_report(
            entity=entity or "",
            project=project,
            summaries=summaries,
            sort_metric=args.sort_metric,
            sort_goal=args.sort_goal,
            metric_list=metric_list,
        )

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    logger.info("Report written to %s", args.output)

    if args.log_artifact_run:
        log_artifact(entity or "", project, args.log_artifact_run, args.output)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        logger.error("%s", exc)
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Interrupted.")
        sys.exit(130)
