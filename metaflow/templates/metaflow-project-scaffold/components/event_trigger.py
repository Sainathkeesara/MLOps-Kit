# last_verified: 2026-08-04 · metaflow 2.10.0
"""Event-trigger helper for Metaflow event-driven flows.

Provides utilities to validate and dispatch event payloads that
trigger Metaflow flows via the @trigger decorator.
"""

import json
import hashlib
from datetime import datetime, timezone


def validate_payload(payload):
    """Validate that an event payload contains the required fields."""
    required = ["source", "event", "branch", "commit_sha"]
    missing = [f for f in required if f not in payload]
    if missing:
        raise ValueError(f"Payload missing required fields: {missing}")
    return True


def normalize_payload(raw_payload):
    """Normalize an incoming event payload to a standard dict."""
    if isinstance(raw_payload, str):
        raw_payload = json.loads(raw_payload)
    return {
        "source": raw_payload.get("source", "unknown"),
        "event": raw_payload.get("event", "unknown"),
        "branch": raw_payload.get("branch", "unknown"),
        "commit_sha": raw_payload.get("commit_sha", ""),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def compute_payload_fingerprint(payload):
    """Compute a deterministic fingerprint for deduplication."""
    canonical = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]