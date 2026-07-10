# last_verified: 2026-07-10 · python

"""con-017 — Apply data versioning to track dataset snapshots for reproducible training (L2)

A single script that snapshots datasets, records which version each
training run used, and can restore any snapshot by name. No DVC install
needed — hashlib and shutil make the concept concrete.
"""

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("dataset_snapshots")
MANIFEST = ROOT / "manifest.json"


# --- Snapshot management ---


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def snapshot(data_file: Path, name: str) -> dict:
    """Copy data_file into the snapshot store and record metadata."""
    ROOT.mkdir(exist_ok=True)
    dest = ROOT / f"{name}{data_file.suffix}"
    shutil.copy2(data_file, dest)
    entry = {
        "name": name,
        "file": str(dest),
        "sha256": sha256(dest),
        "bytes": dest.stat().st_size,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    manifest = []
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text())
    manifest.append(entry)
    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"Snapshot '{name}' created (hash={entry['sha256']})")
    return entry


def list_snapshots() -> list[dict]:
    if not MANIFEST.exists():
        return []
    return json.loads(MANIFEST.read_text())


def restore(name: str, dest: Path) -> None:
    """Restore a named snapshot to dest."""
    for entry in list_snapshots():
        if entry["name"] == name:
            src = Path(entry["file"])
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            print(f"Restored '{name}' => {dest}  (hash expected={entry['sha256']})")
            return
    print(f"Snapshot '{name}' not found")


# --- Reproducible training hook ---


def train(tag: str) -> dict:
    """Train on a specific snapshot and log the data version used."""
    restore(tag, Path("training_data.parquet"))
    print(f"Training on snapshot '{tag}' — data version pinned.")
    # ... real training code would follow ...
    return {"snapshot": tag, "status": "ok"}


if __name__ == "__main__":
    sample = Path("sample_data.parquet")
    if sample.exists():
        snapshot(sample, "raw-v1")
        # simulate a second dirty version to show version divergence
        shutil.copy2(sample, ROOT / "raw-v2-temp.parquet")
        snapshot(ROOT / "raw-v2-temp.parquet", "raw-v2-dirty")
        train("raw-v1")
    else:
        print(f"Create {sample} to run the example.")
