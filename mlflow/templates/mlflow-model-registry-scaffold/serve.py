#!/usr/bin/env python
# last_verified: 2026-07-24 · MLflow n/a

import argparse
import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def serve_model(tracking_uri: str, model_uri: str, port: int, no_conda: bool) -> None:
    cmd = [
        sys.executable, "-m", "mlflow", "models", "serve",
        "--model-uri", model_uri,
        "--port", str(port),
    ]
    if no_conda:
        cmd.append("--no-conda")

    env = {"MLFLOW_TRACKING_URI": tracking_uri}
    logger.info("Starting model server on port %s: %s", port, model_uri)
    subprocess.run(cmd, env={**__import__("os").environ, **env}, check=True)


def main():
    parser = argparse.ArgumentParser(description="Serve a model from the MLflow Model Registry")
    parser.add_argument("--tracking-uri", default="http://localhost:5000")
    parser.add_argument("--model-uri", required=True,
                        help="e.g. models:/IrisClassifier/Staging or runs:/<run_id>/model")
    parser.add_argument("--port", type=int, default=5001)
    parser.add_argument("--no-conda", action="store_true", default=True,
                        help="Skip conda environment activation")
    args = parser.parse_args()

    try:
        serve_model(
            tracking_uri=args.tracking_uri,
            model_uri=args.model_uri,
            port=args.port,
            no_conda=args.no_conda,
        )
    except subprocess.CalledProcessError as exc:
        logger.error("Server exited with code %s: %s", exc.returncode, exc.stderr)
        sys.exit(exc.returncode)
    except Exception as exc:
        logger.error("Failed to start server: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
