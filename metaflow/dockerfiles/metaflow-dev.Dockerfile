# last_verified: 2026-07-09 · Metaflow 2.19.35

FROM nvidia/cuda:latest-cudnn-devel-ubuntu22.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    CUDA_HOME=/usr/local/cuda

RUN apt-get update && apt-get install -y --no-install-recommends \
      python3.11 python3.11-venv python3-pip \
      build-essential git curl wget ca-certificates gnupg lsb-release \
      docker.io \
      pkg-config libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash

ARG KUBECTL_VERSION=latest
RUN curl -fsSLo /usr/local/bin/kubectl \
      "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" \
  && chmod +x /usr/local/bin/kubectl

RUN curl -fsSLo /usr/local/bin/kustomize \
      https://github.com/kubernetes-sigs/kustomize/releases/latest/download/kustomize_v*_linux_amd64 \
  && chmod +x /usr/local/bin/kustomize

RUN curl -fsSLo /usr/local/bin/minikube \
      https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x /usr/local/bin/minikube

RUN python3.11 -m venv /opt/venv \
  && /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
  && /opt/venv/bin/pip install --no-cache-dir \
       "metaflow==2.19.35" \
       psycopg2-binary \
       boto3 \
       torch torchvision --index-url https://download.pytorch.org/whl/cu124 \
       deepspeed \
  && rm -rf /root/.cache/pip

ENV PATH="/opt/venv/bin:${PATH}"

WORKDIR /workspace

CMD ["/bin/bash"]
