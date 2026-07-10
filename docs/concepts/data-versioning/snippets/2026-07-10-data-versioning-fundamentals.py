# last_verified: 2026-07-10 · python

"""con-016 — Data versioning fundamentals exercises (L2)

Three small exercises that mirror DVC-style concepts without
requiring the DVC CLI. I wrote them to make the pointer-file
and snapshot ideas concrete before using an actual tool.
"""

import hashlib
import json
from pathlib import Path


# --- Helpers ---


def file_hash(path: Path) -> str:
    """Return a short SHA-256 fingerprint for a data file."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            digest.update(chunk)
    # first 16 chars is enough to identify a snapshot by eye
    return digest.hexdigest()[:16]


def write_pointer(
    data_file: Path, tag: str, out_dir: Path = Path(".dv_pointers")
) -> Path:
    """Write a lightweight pointer file — the DVC equivalent of .dvc."""
    pointer = {
        "tag": tag,
        "path": str(data_file),
        "md5": file_hash(data_file),
    }
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{data_file.name}.{tag}.json"
    out.write_text(json.dumps(pointer, indent=2))
    print(f"Wrote pointer: {out}")
    return out


def restore_from_pointer(pointer_path: Path, dest: Path) -> None:
    """Restore a data snapshot using the pointer metadata."""
    meta = json.loads(pointer_path.read_text())
    src = Path(meta["path"])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(src.read_bytes())
    print(f"Restored {src.name} => {dest}  (hash={meta['md5']})")


# --- Exercises ---


def exercise_1_snapshot(data_file: str) -> None:
    """Exercise 1: Inspect a dataset snapshot."""
    p = Path(data_file)
    print(f"Snapshot metadata for {p.name}:")
    print(json.dumps({"tag": "v1", "path": str(p), "md5": file_hash(p)}, indent=2))


def exercise_2_pointer(data_file: str, tag: str = "v1") -> None:
    """Exercise 2: Create and verify a pointer file."""
    p = Path(data_file)
    pointer = write_pointer(p, tag)
    # verify read-back by restoring to a temp file
    restored = Path(".dv_pointers") / f"restored_{p.name}"
    restore_from_pointer(pointer, restored)
    # confirm byte-for-byte match
    assert p.read_bytes() == restored.read_bytes(), "byte mismatch after restore"
    print("Byte match confirmed — pointer file is valid.")


def exercise_3_list_versions(tag_dir: str = ".dv_pointers") -> list[dict]:
    """Exercise 3: List all versioned snapshots in one folder."""
    pointers = (
        sorted(Path(tag_dir).glob("*.json")) if Path(tag_dir).exists() else []
    )
    entries = []
    for p in pointers:
        entries.append(json.loads(p.read_text()))
    print(f"Found {len(entries)} versioned snapshot(s):")
    for e in entries:
        print(f"  {e['tag']}: {e['path']}  md5={e['md5']}")
    return entries


if __name__ == "__main__":
    # point these at any dataset files you have
    SAMPLE = Path("sample_data.parquet")
    if SAMPLE.exists():
        exercise_1_snapshot(str(SAMPLE))
        exercise_2_pointer(str(SAMPLE))
        exercise_3_list_versions()
    else:
        print("Create sample_data.parquet to run the exercises.")
