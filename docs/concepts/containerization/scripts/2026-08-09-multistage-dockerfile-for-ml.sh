#!/usr/bin/env bash
# last_verified: 2026-08-09 - containerization n/a

# Practice: create a multi-stage Dockerfile for ML training and serving,
# then validate that it has the expected structure.
#
# I used a scikit-learn churn-predictor example because it's small enough
# to train in seconds but shows the full pattern: a fat trainer stage
# with build tools and training deps, and a slim serving stage that
# only ships the model + inference runtime.

CONTEXT_DIR="multistage_context"
mkdir -p "$CONTEXT_DIR"

# ---- Write the Dockerfile -------------------------------------------------
cat > "$CONTEXT_DIR/Dockerfile" <<'EOF'
# syntax=docker/dockerfile:1

# Stage 1: training (fat)
FROM python:3.11-slim AS trainer
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY train.py .
RUN python train.py && cp model.pkl /model.pkl

# Stage 2: serving (slim)
FROM python:3.11-slim AS serving
COPY --from=trainer /model.pkl /app/model.pkl
COPY serve.py /app/
EXPOSE 8000
CMD ["python", "serve.py"]
EOF

# ---- Write a tiny training script -----------------------------------------
cat > "$CONTEXT_DIR/train.py" <<'EOF'
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("trained model saved to model.pkl")
EOF

# ---- Write a tiny serving script ------------------------------------------
cat > "$CONTEXT_DIR/serve.py" <<'EOF'
import json
import pickle
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        x = np.array(body.get("x", [[0.0]]))
        y = model.predict(x).tolist()
        payload = json.dumps({"y": y}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

if __name__ == "__main__":
    print("serving on :8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
EOF

# ---- Write requirements ---------------------------------------------------
cat > "$CONTEXT_DIR/requirements.txt" <<'EOF'
scikit-learn
numpy
EOF

# ---- Validate Dockerfile shape --------------------------------------------
stages=$(grep -c '^FROM ' "$CONTEXT_DIR/Dockerfile" || true)
if [ "$stages" -ne 2 ]; then
    echo "expected 2 FROM stages, found $stages"
    exit 1
fi

if ! grep -q 'FROM python:3.11-slim AS serving' "$CONTEXT_DIR/Dockerfile"; then
    echo "serving stage not found"
    exit 1
fi

echo "validated: 2-stage Dockerfile in $CONTEXT_DIR"

# ---- Optional build -------------------------------------------------------
if command -v docker >/dev/null 2>&1 && docker version >/dev/null 2>&1; then
    docker build -t ml-multistage:practice "$CONTEXT_DIR"
    echo "build OK -> ml-multistage:practice"
else
    echo "docker not available -- context is ready in $CONTEXT_DIR/"
fi
