#!/usr/bin/env python
# last_verified: 2026-07-24 · MLflow n/a

import argparse
import logging

import mlflow
from mlflow.tracking import MlflowClient

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def register_and_promote(
    tracking_uri: str,
    run_id: str,
    model_name: str,
    stage: str = "Staging",
) -> int:
    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()

    model_uri = f"runs:/{run_id}/model"
    registered = mlflow.register_model(model_uri=model_uri, name=model_name)
    version = registered.version
    logger.info("Registered %s version %s (run %s)", model_name, version, run_id)

    client.transition_model_version_stage(
        name=model_name, version=version, stage=stage
    )
    logger.info("Transitioned %s v%s to %s", model_name, version, stage)
    return version


def promote_to_production(
    tracking_uri: str, model_name: str, version: int
) -> None:
    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()
    client.transition_model_version_stage(
        name=model_name, version=version, stage="Production"
    )
    logger.info("Promoted %s v%s to Production", model_name, version)


def list_versions(tracking_uri: str, model_name: str) -> list:
    mlflow.set_tracking_uri(tracking_uri)
    client = MlflowClient()
    versions = client.search_model_versions(f"name='{model_name}'")
    for v in sorted(versions, key=lambda x: int(x.version)):
        logger.info("  v%s — stage: %s, run: %s", v.version, v.current_stage, v.run_id)
    return versions


def main():
    parser = argparse.ArgumentParser(description="Register and manage model versions")
    sub = parser.add_subparsers(dest="command", required=True)

    register = sub.add_parser("register", help="Register a new model version")
    register.add_argument("--tracking-uri", default="http://localhost:5000")
    register.add_argument("--run-id", required=True)
    register.add_argument("--model-name", default="IrisClassifier")
    register.add_argument("--stage", default="Staging", choices=["None", "Staging", "Production", "Archived"])

    promote = sub.add_parser("promote", help="Promote a version to Production")
    promote.add_argument("--tracking-uri", default="http://localhost:5000")
    promote.add_argument("--model-name", default="IrisClassifier")
    promote.add_argument("--version", type=int, required=True)

    ls = sub.add_parser("list", help="List all versions of a model")
    ls.add_argument("--tracking-uri", default="http://localhost:5000")
    ls.add_argument("--model-name", default="IrisClassifier")

    args = parser.parse_args()

    try:
        if args.command == "register":
            version = register_and_promote(
                tracking_uri=args.tracking_uri,
                run_id=args.run_id,
                model_name=args.model_name,
                stage=args.stage,
            )
            print(f"Registered version {version}")
        elif args.command == "promote":
            promote_to_production(
                tracking_uri=args.tracking_uri,
                model_name=args.model_name,
                version=args.version,
            )
            print(f"Version {args.version} promoted to Production")
        elif args.command == "list":
            list_versions(
                tracking_uri=args.tracking_uri,
                model_name=args.model_name,
            )
    except Exception as exc:
        logger.error("Operation failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
