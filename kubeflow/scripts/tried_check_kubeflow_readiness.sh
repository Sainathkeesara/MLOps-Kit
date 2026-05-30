#!/bin/bash
# tried_check_kubeflow_readiness.sh
#
# Check if Kubeflow components are Ready after a local deployment.
# Ran this after installing Kubeflow Pipelines on a Kind cluster.

NAMESPACE="${1:-kubeflow}"

echo "=== Kubeflow component readiness check ==="
echo "Namespace: $NAMESPACE"
echo ""

pods=$(kubectl get pods -n "$NAMESPACE" --no-headers 2>/dev/null)

if [ -z "$pods" ]; then
  echo "No pods found in namespace '$NAMESPACE'."
  echo "Is Kubeflow installed?"
  exit 1
fi

total=0
ready=0
pending=0
failed=0

while IFS= read -r line; do
  total=$((total + 1))
  name=$(echo "$line" | awk '{print $1}')
  status=$(echo "$line" | awk '{print $3}')
  restarts=$(echo "$line" | awk '{print $4}')

  if [ "$status" = "Running" ] || [ "$status" = "Completed" ]; then
    ready=$((ready + 1))
  elif [ "$status" = "Pending" ] || [ "$status" = "Init:0/1" ] || [ "$status" = "PodInitializing" ]; then
    pending=$((pending + 1))
    echo "  PENDING: $name ($status)"
  else
    failed=$((failed + 1))
    echo "  FAILED:  $name ($status, restarts: $restarts)"
  fi
done <<< "$pods"

echo ""
echo "--- Summary ---"
echo "  Total pods:  $total"
echo "  Ready:       $ready"
echo "  Pending:     $pending"
echo "  Failed:      $failed"

if [ "$ready" -eq "$total" ]; then
  echo ""
  echo "All components ready."
else
  echo ""
  echo "Some components not ready yet. Wait a bit and re-run."
fi
