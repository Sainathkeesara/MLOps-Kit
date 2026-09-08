# last_verified: 2026-09-08 · model-serving n/a

"""Combine model serving with containerization for ML deployment.

This script demonstrates the integration pattern between model serving
and containerization. It stages a model artifact, generates a FastAPI
serving application, produces a container configuration, and validates
the bundle before a build. The goal is to show how the two concepts
connect in a production workflow rather than treating them as separate
tutorials.

In a typical stack the model artifact originates from MLflow or BentoML,
the feature lookup comes from Feast, and the image is promoted through
a CI/CD pipeline. This script collapses those moving parts into a single
runnable example so the integration points are visible.

Usage:
    python combining-model-serving-with-containerization.py --mode bundle --model-dir ./model
    python combining-model-serving-with-containerization.py --mode validate --bundle-dir ./serve-bundle
    python combining-model-serving-with-containerization.py --mode containerize --bundle-dir ./serve-bundle
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Optional


def bundle_model_artifacts(
    model_path: Path,
    feature_def_path: Optional[Path],
    output_dir: Path,
) -> dict:
    """Stage model weights, feature definitions, and serving code into a
    versioned bundle directory.

    The bundle layout mirrors what a serving container would see at runtime:
    model weights under /model, feature definitions under /features, and the
    entrypoint script at /app/main.py. Producing this layout explicitly makes
    the integration with containerization transparent.

    Returns a manifest dict describing the staged artifacts and their sha256
    checksums. The manifest is written to manifest.json inside the bundle.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    if not model_path.exists():
        raise FileNotFoundError(f"model_path does not exist: {model_path}")

    model_dest = output_dir / "model"
    model_dest.mkdir(exist_ok=True)

    manifest: dict = {"model": {}, "features": {}, "entrypoint": {}}

    for src in model_path.rglob("*"):
        if src.is_file():
            rel = src.relative_to(model_path)
            dst = model_dest / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
            digest = hashlib.sha256(dst.read_bytes()).hexdigest()[:16]
            manifest["model"][str(rel)] = {
                "size": dst.stat().st_size,
                "sha256": digest,
            }

    if feature_def_path and feature_def_path.exists():
        feature_dest = output_dir / "features"
        feature_dest.mkdir(exist_ok=True)
        dst = feature_dest / feature_def_path.name
        dst.write_bytes(feature_def_path.read_bytes())
        manifest["features"]["path"] = str(dst.relative_to(output_dir))

    generate_fastapi_app(output_dir)
    manifest["entrypoint"]["path"] = "app.py"

    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))

    print(f"Bundle staged at {output_dir}")
    print(f"Manifest written to {manifest_path}")
    return manifest


def generate_fastapi_app(bundle_dir: Path, host: str = "0.0.0.0", port: int = 8080) -> Path:
    """Write a minimal FastAPI application that exposes /predict and /health.

    The generated app loads the staged model at startup and exposes two
    endpoints: /health for readiness checks and /predict for inference.
    In production the model loading logic would be replaced by a real
    framework load (PyTorch, TensorFlow, XGBoost, etc.), and the feature
    store client would initialize here instead of the stub.

    Binding to 0.0.0.0 is intentional: the default 127.0.0.1 bind used
    in local tutorials breaks container and CI testing because external
    clients cannot reach the endpoint.
    """
    bundle_dir.mkdir(parents=True, exist_ok=True)

    if port <= 0 or port > 65535:
        raise ValueError(f"port must be in 1-65535, got {port}")

    source = f"""from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from pathlib import Path

app = FastAPI(title="model-serving", version="0.1.0")

MODEL_DIR = Path(os.environ.get("MODEL_DIR", "/model"))
FEATURES_DIR = Path(os.environ.get("FEATURES_DIR", "/features"))
HOST = os.environ.get("HOST", "{host}")
PORT = int(os.environ.get("PORT", "{port}"))

class PredictRequest(BaseModel):
    inputs: list

class PredictResponse(BaseModel):
    predictions: list
    model_version: str

@app.get("/health")
def health() -> dict:
    return {{"status": "ok", "model_dir": str(MODEL_DIR)}}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    manifest_path = MODEL_DIR / "manifest.json"
    if not manifest_path.exists():
        raise HTTPException(status_code=503, detail="model manifest not found")
    # Production code loads the actual model here. This stub echoes the
    # request length so the endpoint is callable without weights installed.
    predictions = [{{"index": i, "value": len(request.inputs)}} for i in range(len(request.inputs))]
    return PredictResponse(predictions=predictions, model_version="stub-0.1.0")
"""
    app_path = bundle_dir / "app.py"
    app_path.write_text(source)
    print(f"FastAPI app written to {app_path}")
    return app_path


def generate_container_config(
    bundle_dir: Path,
    base_image: str = "python:3.11-slim",
    port: int = 8080,
) -> Path:
    """Produce a container configuration that packages the FastAPI app,
    model weights, and feature definitions into a single OCI image.

    The configuration writes a Dockerfile and a requirements file inside
    the bundle. The Dockerfile uses a multi-stage layout: the first stage
    installs dependencies, the final stage copies the staged bundle. This
    pattern keeps the runtime image small and makes the serving layer
    reproducible.

    Returns the path to the generated Dockerfile.
    """
    bundle_dir.mkdir(parents=True, exist_ok=True)

    requirements = "fastapi==0.115.0\nuvicorn==0.30.0\npydantic==2.9.0\n"
    (bundle_dir / "requirements.txt").write_text(requirements)

    dockerfile = f"""FROM {base_image} AS builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM {base_image}
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY app.py .
COPY model/ ./model/
COPY features/ ./features/
COPY manifest.json .
EXPOSE {port}
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "{port}"]
"""
    dockerfile_path = bundle_dir / "Dockerfile"
    dockerfile_path.write_text(dockerfile)
    print(f"Container config written to {dockerfile_path}")
    return dockerfile_path


def validate_bundle(bundle_dir: Path) -> bool:
    """Run lightweight sanity checks on the staged bundle before a build.

    Checks that the manifest exists and is valid JSON, that app.py is
    present and non-empty, and that the model directory is not empty.
    Returns True if all checks pass; prints the failing check otherwise.
    """
    ok = True

    manifest_path = bundle_dir / "manifest.json"
    if not manifest_path.exists():
        print("FAIL: manifest.json is missing")
        ok = False
    else:
        try:
            json.loads(manifest_path.read_text())
        except json.JSONDecodeError as exc:
            print(f"FAIL: manifest.json is not valid JSON: {exc}")
            ok = False

    app_path = bundle_dir / "app.py"
    if not app_path.exists() or app_path.stat().st_size == 0:
        print("FAIL: app.py is missing or empty")
        ok = False

    model_dir = bundle_dir / "model"
    if not model_dir.exists() or not any(model_dir.rglob("*")):
        print("FAIL: model directory is empty")
        ok = False

    if ok:
        print("Bundle validation passed")
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Combine model serving with containerization for ML deployment",
    )
    parser.add_argument(
        "--mode",
        choices=["bundle", "validate", "containerize"],
        default="bundle",
        help="Pipeline step to run",
    )
    parser.add_argument("--model-dir", type=Path, default=Path("./model"), help="Source model directory")
    parser.add_argument("--feature-def", type=Path, default=None, help="Optional feature definition file")
    parser.add_argument("--bundle-dir", type=Path, default=Path("./serve-bundle"), help="Output bundle directory")
    parser.add_argument("--base-image", default="python:3.11-slim", help="Container base image")
    parser.add_argument("--port", type=int, default=8080, help="Serving port inside the container")
    args = parser.parse_args()

    if args.mode == "bundle":
        bundle_model_artifacts(args.model_dir, args.feature_def, args.bundle_dir)
    elif args.mode == "validate":
        ok = validate_bundle(args.bundle_dir)
        sys.exit(0 if ok else 1)
    elif args.mode == "containerize":
        if not args.bundle_dir.exists():
            print(f"FAIL: bundle directory does not exist: {args.bundle_dir}", file=sys.stderr)
            sys.exit(1)
        generate_fastapi_app(args.bundle_dir, port=args.port)
        generate_container_config(args.bundle_dir, base_image=args.base_image, port=args.port)


if __name__ == "__main__":
    main()
