# last_verified: 2026-08-11 · data-versioning n/a

"""
con-103 — DVC-style dataset versioning pipeline with reproducible training (L3).

This script implements the core mechanisms that DVC provides — content-addressed
storage, pointer files, and dataset versioning — from scratch in pure Python.
It then integrates those mechanisms with a minimal experiment-tracking log so
that every training run records which dataset version it consumed.

DVC 3.67.1 stores data in a content-addressed cache and records lightweight
pointers in Git [source: https://pypi.org/project/dvc/]. Running `dvc init`
requires an existing Git repository first [source: https://github.com/anumcait/100daysMLOPSJourney/blob/main/Day%2010%20-%20Install%20and%20Initialize%20DVC%20in%20an%20ML%20Project.md],
and after `git checkout` a `dvc checkout` syncs the workspace from pointer
files [source: https://tildalice.io/dvc-basics-track-ml-dataset-3-commands/].
This script mirrors that flow without the external tool: a local cache
directory holds the canonical data, pointer files reference cache entries by
hash, and the run log ties each training run to its data version.

At L3 the key integration is that data versioning, experiment tracking, and
reproducible training are not three separate steps but one pipeline: the run
log stores the data hash alongside the metric, so reproduction is a lookup
followed by a cache restore, not a guess.

Usage:
    python dvc-style-versioning-pipeline.py --workspace /tmp/dvc_demo
    python dvc-style-versioning-pipeline.py --workspace /tmp/dvc_demo --reproduce run-v1-<hash>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class PointerFile:
    """Metadata for a dataset version (stand-in for a .dvc pointer file)."""

    data_hash: str
    original_path: str
    size: int
    created_at: str


@dataclass
class RunRecord:
    """One row in the experiment-tracking log."""

    run_id: str
    data_version: str
    data_hash: str
    metric: float
    created_at: str


# ── DataVersionStore: content-addressed cache + pointer files ─────────────


class DataVersionStore:
    """From-scratch implementation of DVC's cache + pointer model.

    Two directories live under *root*:
    - ``cache/``: content-addressed files named by their sha256 digest.
    - ``pointers/``: JSON pointer files mapping a version tag to a hash.

    This mirrors DVC's ``.dvc/cache`` and ``.dvc`` pointer files: heavy data
    stays in the cache, lightweight pointers are shared. Cache entries are
    immutable and deduplicated — two datasets with identical content share one
    cache file, just as in DVC.
    """

    def __init__(self, root: Path) -> None:
        self.root = root
        self.cache_dir = root / "cache"
        self.pointer_dir = root / "pointers"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.pointer_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _hash_file(path: Path) -> str:
        """Return sha256 hex digest of *path* (content-addressed cache key)."""
        digest = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def _resolve_pointer(self, version: str) -> PointerFile:
        ptr_path = self.pointer_dir / f"{version}.json"
        if not ptr_path.exists():
            raise KeyError(f"unknown data version: {version!r}")
        return PointerFile(**json.loads(ptr_path.read_text()))

    def add(self, source: Path, version: str) -> str:
        """Register *source* as a new dataset version.

        Computes sha256, copies into cache (if new), writes a pointer file.
        Duplicate content shares the cache entry — DVC's deduplication.
        """
        if not source.exists():
            raise FileNotFoundError(f"dataset not found: {source}")

        data_hash = self._hash_file(source)
        cache_entry = self.cache_dir / data_hash
        if not cache_entry.exists():
            shutil.copy2(source, cache_entry)
            print(f"  cached {source.name} -> cache/{data_hash[:12]}")

        pointer = PointerFile(
            data_hash=data_hash,
            original_path=str(source),
            size=source.stat().st_size,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        ptr_path = self.pointer_dir / f"{version}.json"
        ptr_path.write_text(json.dumps(pointer.__dict__, indent=2))
        print(f"  pointer {version}.json -> {data_hash[:12]} ({pointer.size} bytes)")
        return data_hash

    def checkout(self, version: str, dest: Path) -> Path:
        """Restore a dataset version from cache to *dest*.

        Mirrors ``dvc checkout``: the pointer tells us which hash to fetch,
        the cache provides the bytes, and we verify integrity on restore.
        """
        ptr = self._resolve_pointer(version)
        cache_file = self.cache_dir / ptr.data_hash
        if not cache_file.exists():
            raise FileNotFoundError(
                f"cache entry missing for {version}: {ptr.data_hash[:12]}"
            )
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cache_file, dest)
        actual = self._hash_file(dest)
        if actual != ptr.data_hash:
            raise RuntimeError(
                f"integrity check failed for {version}: "
                f"expected {ptr.data_hash[:16]}, got {actual[:16]}"
            )
        print(f"  restored {version} -> {dest.name} (hash verified)")
        return dest

    def versions(self) -> list[str]:
        """All registered version tags, ordered by creation time."""
        ptrs = sorted(
            self.pointer_dir.glob("*.json"),
            key=lambda p: p.stat().st_mtime,
        )
        return [p.stem for p in ptrs]


# ── RunLog: experiment-tracking integration ─────────────────────────────────


class RunLog:
    """Minimal experiment-tracking log tying runs to data versions.

    At L3 the insight is that versioning data without tracking which version
    each run used is only half the job. This JSONL log lets a practitioner
    look up any past run, read back its exact data hash, and reproduce the
    result — the same principle MLflow or W&B applies, here without the
    server dependency.
    """

    def __init__(self, log_path: Path) -> None:
        self.log_path = log_path
        log_path.parent.mkdir(parents=True, exist_ok=True)
        if not log_path.exists():
            log_path.write_text("")

    def _read_all(self) -> list[RunRecord]:
        records: list[RunRecord] = []
        for line in self.log_path.read_text().splitlines():
            line = line.strip()
            if line:
                records.append(RunRecord(**json.loads(line)))
        return records

    def log_run(
        self,
        run_id: str,
        data_version: str,
        data_hash: str,
        metric: float,
    ) -> None:
        record = RunRecord(
            run_id=run_id,
            data_version=data_version,
            data_hash=data_hash,
            metric=metric,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        with open(self.log_path, "a") as fh:
            fh.write(json.dumps(record.__dict__) + "\n")
        print(f"  logged {run_id}: data={data_version}, metric={metric:.4f}")

    def find_run(self, run_id: str) -> RunRecord:
        for rec in self._read_all():
            if rec.run_id == run_id:
                return rec
        raise KeyError(f"run not found: {run_id!r}")


# ── Training + pipeline orchestration ──────────────────────────────────────


def train_model(data_path: Path) -> float:
    """Tiny training stand-in: averages the last numeric column of a CSV.

    The metric is derived from the data content, so different versions
    produce different metrics — proving that pinning the data version pins
    the training result.
    """
    content = data_path.read_text()
    rows = [line for line in content.strip().splitlines() if line]
    values: list[float] = []
    for row in rows[1:]:  # skip header
        parts = row.split(",")
        if len(parts) >= 2:
            try:
                values.append(float(parts[-1]))
            except ValueError:
                continue
    return sum(values) / len(values) if values else 0.0


def run_pipeline(
    store: DataVersionStore,
    log: RunLog,
    dataset: Path,
    version: str,
    dest_dir: Path,
) -> str:
    """Version the dataset, train, and log the run. Returns the run_id."""
    data_hash = store.add(dataset, version)
    restored = dest_dir / f"{version}_train.csv"
    store.checkout(version, restored)
    metric = train_model(restored)
    run_id = f"run-{version}-{data_hash[:8]}"
    log.log_run(run_id, version, data_hash, metric)
    return run_id


def reproduce_run(
    store: DataVersionStore,
    log: RunLog,
    run_id: str,
    dest_dir: Path,
) -> float:
    """Restore the exact data version from a past run and re-train.

    Reproduction is a lookup then a cache restore: find the run, read its
    data hash, and confirm the metric matches. Any drift in the data would
    show up here because the cache is content-addressed and immutable.
    """
    rec = log.find_run(run_id)
    restored = dest_dir / f"reproduced_{run_id}.csv"
    store.checkout(rec.data_version, restored)
    metric = train_model(restored)
    print(f"  reproduced {run_id}: metric={metric:.4f} (original={rec.metric:.4f})")
    if abs(metric - rec.metric) > 1e-9:
        raise RuntimeError(
            f"reproduction mismatch: expected {rec.metric:.4f}, got {metric:.4f}"
        )
    return metric


def main() -> int:
    parser = argparse.ArgumentParser(
        description="DVC-style dataset versioning pipeline with reproducible training",
    )
    parser.add_argument(
        "--workspace",
        default="dvc_demo",
        help="root directory for cache, pointers, and run log",
    )
    parser.add_argument(
        "--reproduce",
        metavar="RUN_ID",
        default=None,
        help="reproduce a past training run by run_id",
    )
    args = parser.parse_args()

    root = Path(args.workspace)
    store = DataVersionStore(root)
    log = RunLog(root / "runs.jsonl")
    data_dir = root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    if args.reproduce:
        print(f"Reproducing run: {args.reproduce}")
        reproduce_run(store, log, args.reproduce, data_dir)
        return 0

    # --- v1: initial dataset ---
    dataset = data_dir / "sample.csv"
    dataset.write_text("feature,target\n1,10\n2,20\n3,30\n")
    print("v1: initial dataset")
    run_v1 = run_pipeline(store, log, dataset, "v1", data_dir)

    # --- v2: mutated dataset ---
    dataset.write_text("feature,target\n1,10\n2,20\n3,30\n4,40\n")
    print("\nv2: added a row")
    run_v2 = run_pipeline(store, log, dataset, "v2", data_dir)

    # --- reproduce v1 ---
    print(f"\nReproducing v1 ({run_v1}):")
    reproduce_run(store, log, run_v1, data_dir)

    print(f"\nVersions tracked: {store.versions()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
