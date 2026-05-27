#!/bin/bash
# tried_diagnosing_kubeflow_health.sh
#
# Quick health checks for Kubeflow backend services after a local deploy.
# Ran these against a Kind cluster — kubectl context must be set already.

echo "=== Checking kubeflow namespace pods ==="
kubectl get pods -n kubeflow 2>/dev/null || {
  echo "ERROR: couldn't list pods in namespace 'kubeflow'"
  echo "Is your cluster running and kubectl configured?"
  exit 1
}

echo ""
echo "=== Checking central-dashboard ==="
kubectl get deployment central-dashboard -n kubeflow -o wide 2>/dev/null \
  && echo "central-dashboard: OK" \
  || echo "central-dashboard: NOT FOUND — maybe not deployed yet"

echo ""
echo "=== Checking ml-pipeline (Kubeflow Pipelines) ==="
kubectl get deployment ml-pipeline -n kubeflow -o wide 2>/dev/null \
  && echo "ml-pipeline: OK" \
  || echo "ml-pipeline: NOT FOUND"

echo ""
echo "=== Checking katib (if installed) ==="
kubectl get deployment katib-controller -n kubeflow -o wide 2>/dev/null \
  && echo "katib-controller: OK" \
  || echo "katib-controller: not present (optional component)"

echo ""
echo "=== Pod status summary ==="
kubectl get pods -n kubeflow --no-headers 2>/dev/null | awk '
  { status[$3]++ }
  END {
    for (s in status) print s ":", status[s]
  }
'

echo ""
echo "=== All services (quick list) ==="
kubectl get svc -n kubeflow 2>/dev/null | head -10 || echo "(no services found yet)"
