# last_verified: 2026-07-13 · containerization n/a

"""
I wrote this little script to practice the "multi-stage build" idea from the
Containerization primer. The goal: one Dockerfile where a fat training stage
produces a model, and a tiny serving stage ships only onnxruntime + the
exported model. Running it writes a build context (Dockerfile + train.py +
serve.py) and optionally builds the image to smoke-test it.

Base image python:3.11-slim and the multi-stage pattern come straight from the
research notes for this cycle. I deliberately do NOT pin library versions here
-- this is a learning exercise, not a locked-down deploy artifact.
"""

import os
import subprocess
import sys

BUILD_DIR = "build_context"

DOCKERFILE = r"""# syntax=docker/dockerfile:1

# ---- Stage 1: training (fat) ----
# Installs training deps, exports an ONNX model, then exits.
FROM python:3.11-slim AS train

WORKDIR /build
RUN pip install --no-cache-dir numpy onnx

COPY train.py .
RUN python train.py --out /build/model.onnx

# ---- Stage 2: serving (slim) ----
# Only onnxruntime + the exported model. No training toolchain.
FROM python:3.11-slim AS serve

WORKDIR /app
RUN pip install --no-cache-dir onnxruntime numpy

COPY --from=train /build/model.onnx /app/model.onnx
COPY serve.py .

EXPOSE 8080
CMD ["python", "serve.py"]
"""

TRAIN_PY = r"""import argparse

import numpy as np
import onnx
from onnx import TensorProto, helper


def build_linear_onnx(path: str) -> None:
    # y = 2*x + 1  (a trivial ONNX model so the build needs no dataset)
    x = helper.make_tensor_value_info("x", TensorProto.FLOAT, [None, 1])
    y = helper.make_tensor_value_info("y", TensorProto.FLOAT, [None, 1])
    w = helper.make_tensor(
        "w", TensorProto.FLOAT, [1, 1], [2.0]
    )
    b = helper.make_tensor(
        "b", TensorProto.FLOAT, [1], [1.0]
    )
    node_mul = helper.make_node("MatMul", ["x", "w"], ["mul"])
    node_add = helper.make_node("Add", ["mul", "b"], ["y"])
    graph = helper.make_graph([node_mul, node_add], "linear", [x], [y])
    model = helper.make_model(graph, opset_imports=[helper.make_opsetid("", 13)])
    onnx.save(model, path)
    print(f"wrote {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="model.onnx")
    args = ap.parse_args()
    build_linear_onnx(args.out)
"""

SERVE_PY = r"""import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import numpy as np
import onnxruntime as ort

SESSION = ort.InferenceSession("model.onnx")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        x = np.array(body.get("x", [[0.0]]), dtype="float32")
        out = SESSION.run(None, {"x": x})[0]
        payload = json.dumps({"y": out.tolist()}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    print("onnxruntime serving on :8080")
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
"""


def write_context() -> str:
    os.makedirs(BUILD_DIR, exist_ok=True)
    for name, content in (
        ("Dockerfile", DOCKERFILE),
        ("train.py", TRAIN_PY),
        ("serve.py", SERVE_PY),
    ):
        with open(os.path.join(BUILD_DIR, name), "w") as fh:
            fh.write(content)
    return BUILD_DIR


def validate(dockerfile: str) -> None:
    # I expect exactly two build stages and a slim onnxruntime final stage.
    stages = dockerfile.count("FROM ")
    assert stages == 2, f"expected 2 stages, found {stages}"
    assert "onnxruntime" in dockerfile, "final stage must install onnxruntime"
    assert "EXPOSE 8080" in dockerfile, "serving stage should expose a port"
    print(f"validated: {stages} stages, onnxruntime present, port exposed")


def smoke_test(build_dir: str) -> None:
    if subprocess.run(["docker", "version"], capture_output=True).returncode != 0:
        print("docker not available -- skipping build (context is ready in "
              f"{build_dir}/)")
        return
    tag = "containerization-practice:latest"
    result = subprocess.run(
        ["docker", "build", "-t", tag, build_dir],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("docker build failed:\n" + result.stderr)
        sys.exit(1)
    print(f"smoke-test build OK -> {tag}")


if __name__ == "__main__":
    ctx = write_context()
    validate(DOCKERFILE)
    smoke_test(ctx)
    print(f"done. build context written to {ctx}/")
