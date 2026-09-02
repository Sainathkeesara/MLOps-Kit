# last_verified: 2026-09-02 · data-versioning n/a
"""
con-117 — DVC-style dataset versioning pipeline with reproducible training (L3).

This script combines three concerns that are often treated separately —
dataset versioning, experiment tracking, and reproducible training — into a
single pipeline. A content-addressed store versions the dataset, a JSONL
run log records which data hash each training run consumed, and a reproduce
path restores the exact data version to re-run training deterministically.

The design mirrors the DVC model where the cache is content-addressed by
hash and pointer files are checked into version control. The insight at L3
is that versioning data without tracking the linkage to training runs is
only half the story: the run log stores data_version + data_hash + metric
so that any historical run can be re-executed by hash lookup.

Usage:
    python reproducible-training-pipeline.py --workspace /tmp/demo
    python reproducible-training-pipeline.py --workspace /tmp/demo --reproduce run-v1-<hash>
    python reproducible-training-pipeline.py --workspace /tmp/demo --list
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
class Pointer:
    data_hash: str
    source: str
    size: int
    created_at: str


@dataclass
class RunEntry:
    run_id: str
    data_version: str
    data_hash: str
    metric: float
    created_at: str


class VersionedStore:
    """Content-addressed cache with pointer files and integrity verification."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.cache = root / "cache"
        self.pointers = root / "pointers"
        self.cache.mkdir(parents=True, exist_ok=True)
        self.pointers.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _hash(path: Path) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def add_version(self, src: Path, version: str) -> str:
        if not src.exists():
            raise FileNotFoundError(f"dataset not found: {src}")
        digest = self._hash(src)
        cached = self.cache / digest
        if not cached.exists():
            shutil.copy2(src, cached)
        pointer = Pointer(
            data_hash=digest,
            source=str(src),
            size=src.stat().st_size,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        (self.pointers / f"{version}.json").write_text(
            json.dumps(pointer.__dict__, indent=2)
        )
        return digest

    def restore(self, version: str, dest: Path) -> Path:
        p = self.pointers / f"{version}.json"
        if not p.exists():
            raise KeyError(f"unknown version: {version!r}")
        ptr = Pointer(**json.loads(p.read_text()))
        cached = self.cache / ptr.data_hash
        if not cached.exists():
            raise FileNotFoundError(f"cache miss for {version}: {ptr.data_hash[:12]}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(cached, dest)
        if self._hash(dest) != ptr.data_hash:
            raise RuntimeError(f"integrity check failed for {version}")
        return dest

    def list_versions(self) -> list[str]:
        return sorted(
            (p.stem for p in self.pointers.glob("*.json")),
            key=lambda s: (self.pointers / f"{s}.json").stat().st_mtime,
        )


class RunLog:
    """Append-only experiment log linking runs to data versions."""

    def __init__(self, path: Path) -> None:
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text("")

    def append(self, entry: RunEntry) -> None:
        with open(self.path, "a") as fh:
            fh.write(json.dumps(entry.__dict__) + "\n")

    def all(self) -> list[RunEntry]:
        out: list[RunEntry] = []
        for line in self.path.read_text().splitlines():
            line = line.strip()
            if line:
                out.append(RunEntry(**json.loads(line)))
        return out

    def find(self, run_id: str) -> RunEntry:
        for r in self.all():
            if r.run_id == run_id:
                return r
        raise KeyError(f"run not found: {run_id!r}")


def train(data_path: Path) -> float:
    """Toy training: mean of the last column. Different data yields different metrics."""
    lines = [l for l in data_path.read_text().strip().splitlines() if l.strip()]
    if len(lines) <= 1:
        return 0.0
    vals: list[float] = []
    for row in lines[1:]:
        parts = row.split(",")
        try:
            vals.append(float(parts[-1]))
        except ValueError:
            continue
    return sum(vals) / len(vals) if vals else 0.0


def run_versioned_training(
    store: VersionedStore, log: RunLog, dataset: Path, version: str, workdir: Path
) -> str:
    digest = store.add_version(dataset, version)
    restored = workdir / f"train-{version}.csv"
    store.restore(version, restored)
    metric = train(restored)
    run_id = f"run-{version}-{digest[:8]}"
    log.append(
        RunEntry(
            run_id=run_id,
            data_version=version,
            data_hash=digest,
            metric=metric,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
    )
    print(f"  {version}: hash={digest[:12]} metric={metric:.4f} -> {run_id}")
    return run_id


def reproduce(store: VersionedStore, log: RunLog, run_id: str, workdir: Path) -> float:
    entry = log.find(run_id)
    restored = workdir / f"repro-{run_id}.csv"
    store.restore(entry.data_version, restored)
    metric = train(restored)
    print(f"  reproduce {run_id}: got {metric:.4f} (expected {entry.metric:.4f})")
    if abs(metric - entry.metric) > 1e-9:
        raise RuntimeError(f"reproduction mismatch for {run_id}")
    return metric


def main() -> int:
    parser = argparse.ArgumentParser(
        description="DVC-style versioning pipeline with reproducible training"
    )
    parser.add_argument("--workspace", default="demo_workspace")
    parser.add_argument("--reproduce", metavar="RUN_ID", default=None)
    parser.add_argument("--list", action="store_true", help="list versions and runs")
    args = parser.parse_args()

    root = Path(args.workspace)
    store = VersionedStore(root)
    log = RunLog(root / "runs.jsonl")

    if args.list:
        print("versions:", store.list_versions())
        for r in log.all():
            print(f"  {r.run_id} data={r.data_version} metric={r.metric:.4f}")
        return 0

    if args.reproduce:
        reproduce(store, log, args.reproduce, root / "data")
        return 0

    data_dir = root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    ds = data_dir / "dataset.csv"

    # v1
    ds.write_text("x,y\n1,10\n2,20\n3,30\n")
    print("pipeline: v1 initial")
    r1 = run_versioned_training(store, log, ds, "v1", data_dir)

    # v2 — append row
    ds.write_text("x,y\n1,10\n2,20\n3,30\n4,40\n")
    print("pipeline: v2 appended row")
    r2 = run_versioned_training(store, log, ds, "v2", data_dir)

    # v2 duplicate content — deduplication check
    ds.write_text("x,y\n1,10\n2,20\n3,30\n4,40\n")
    print("pipeline: v2-dup same content as v2 (cache deduplication)")
    run_versioned_training(store, log, ds, "v2-dup", data_dir)

    print("\nverifying reproducibility of v1:")
    reproduce(store, log, r1, data_dir)

    print(f"\nversions: {store.list_versions()}")
    print(f"runs: {len(log.all())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
