#!/usr/bin/env python
# last_verified: 2026-07-25 · MLflow n/a
"""Reusable helper for automated experiment comparison and model promotion.

Functions:
    get_best_run         — return the run_id with the highest metric in an experiment
    register_and_promote — register a run's model artifact and transition it to a stage
    compare_and_promote  — convenience: find the best run then register + promote
"""

import logging
from typing import Optional

import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def get_best_run(
    experiment_name: str,
    metric: str = "accuracy",
    max_results: int = 20,
) -> Optional[str]:
    """Return the run_id with the highest value for *metric* in the experiment."""
    client = MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)
    if experiment is None:
        logger.warning("Experiment '%s' not found.", experiment_name)
        return None

    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        run_view_type=ViewType.ALL,
        max_results=max_results,
        order_by=[f"metrics.{metric} DESC"],
    )
    if not runs:
        logger.warning("No runs found in experiment '%s'.", experiment_name)
        return None

    best = runs[0]
    best_val = best.data.metrics.get(metric)
    logger.info(
        "Best run: %s — %s = %.4f",
        best.info.run_id,
        metric,
        best_val if best_val is not None else float("nan"),
    )
    return best.info.run_id


def register_and_promote(
    run_id: str,
    model_name: str,
    stage: str = "Staging",
    artifact_path: str = "model",
) -> Optional[int]:
    """Register the model logged under *artifact_path* in *run_id* and promote it to *stage*.

    Returns the registered version number, or None on failure.
    """
    client = MlflowClient()
    model_uri = f"runs:/{run_id}/{artifact_path}"
    try:
        mv = mlflow.register_model(model_uri=model_uri, name=model_name)
        logger.info("Registered model '%s' as version %s.", model_name, mv.version)

        client.transition_model_version_stage(
            name=model_name,
            version=mv.version,
            stage=stage,
        )
        logger.info("Promoted '%s' v%s to %s.", model_name, mv.version, stage)
        return mv.version
    except Exception as exc:
        logger.error("Failed to register or promote model: %s", exc)
        return None


def compare_and_promote(
    experiment_name: str,
    model_name: str,
    metric: str = "accuracy",
    stage: str = "Staging",
    artifact_path: str = "model",
) -> Optional[int]:
    """Find the best run in *experiment_name*, register its model, and promote it.

    This is the main entry point for automated model promotion workflows.
    Call it after a set of training runs complete to auto-promote the best one.
    """
    run_id = get_best_run(experiment_name, metric)
    if run_id is None:
        return None
    return register_and_promote(run_id, model_name, stage, artifact_path)


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("iris-classifier")

    version = compare_and_promote("iris-classifier", "IrisRandomForest")
    if version is not None:
        print(f"Done — version {version} promoted.")
    else:
        print("No model was promoted; check the logs above.")
