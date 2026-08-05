# last_verified: 2026-08-04 · metaflow 2.10.0
"""Unit tests for the event_trigger helper component."""

from components.event_trigger import (
    validate_payload,
    normalize_payload,
    compute_payload_fingerprint,
)
import pytest


def test_validate_payload_valid():
    payload = {
        "source": "github",
        "event": "push",
        "branch": "main",
        "commit_sha": "abc123",
    }
    assert validate_payload(payload) is True


def test_validate_payload_missing_fields():
    payload = {"source": "github", "event": "push"}
    with pytest.raises(ValueError, match="missing required fields"):
        validate_payload(payload)


def test_normalize_payload_dict():
    payload = {
        "source": "github",
        "event": "push",
        "branch": "main",
        "commit_sha": "abc123",
    }
    result = normalize_payload(payload)
    assert result["source"] == "github"
    assert result["event"] == "push"
    assert result["branch"] == "main"
    assert result["commit_sha"] == "abc123"
    assert "timestamp" in result


def test_normalize_payload_string():
    raw = '{"source": "github", "event": "push", "branch": "main", "commit_sha": "abc123"}'
    result = normalize_payload(raw)
    assert result["source"] == "github"
    assert result["commit_sha"] == "abc123"


def test_compute_payload_fingerprint_deterministic():
    payload = {"source": "github", "event": "push", "branch": "main", "commit_sha": "abc123"}
    fp1 = compute_payload_fingerprint(payload)
    fp2 = compute_payload_fingerprint(payload)
    assert fp1 == fp2
    assert len(fp1) == 16


def test_compute_payload_fingerprint_unique():
    payload_a = {"source": "github", "event": "push", "branch": "main", "commit_sha": "aaa"}
    payload_b = {"source": "github", "event": "push", "branch": "main", "commit_sha": "bbb"}
    assert compute_payload_fingerprint(payload_a) != compute_payload_fingerprint(payload_b)