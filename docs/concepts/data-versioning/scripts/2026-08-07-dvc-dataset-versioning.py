# last_verified: 2026-08-07 · DVC 3.67.1

import hashlib
import json
import shutil
from pathlib import Path


def file_hash(path):
    """I compute a sha256 hash so I can detect when a dataset changes."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


class DatasetVersioning:
    def __init__(self, root='versioning_demo'):
        self.root = Path(root)
        self.root.mkdir(exist_ok=True)
        self.versions_file = self.root / 'versions.json'
        self.versions = self._load_versions()

    def _load_versions(self):
        if self.versions_file.exists():
            return json.loads(self.versions_file.read_text())
        return {}

    def _save_versions(self):
        self.versions_file.write_text(json.dumps(self.versions, indent=2))

    def snapshot(self, dataset_path, version_name):
        """I copy the dataset and record its hash so I can reproduce later."""
        src = Path(dataset_path)
        if not src.exists():
            raise FileNotFoundError(f"Dataset not found: {dataset_path}")

        dst = self.root / f"{version_name}_{src.name}"
        shutil.copy2(src, dst)

        # Record the snapshot metadata, similar to a .dvc pointer file.
        self.versions[version_name] = {
            'file': str(dst),
            'hash': file_hash(src),
            'original': str(src)
        }
        self._save_versions()
        print(f"Snapshot '{version_name}' created: {dst} (hash={self.versions[version_name]['hash'][:12]}...)")

    def reproduce(self, version_name, output_dir='reproduced'):
        """I restore a specific dataset version so training can be rerun."""
        if version_name not in self.versions:
            raise KeyError(f"Unknown version: {version_name}")

        info = self.versions[version_name]
        out = Path(output_dir)
        out.mkdir(exist_ok=True)
        dst = out / Path(info['original']).name

        shutil.copy2(info['file'], dst)

        # Verify the file hash matches what I recorded.
        actual_hash = file_hash(dst)
        if actual_hash != info['hash']:
            raise RuntimeError(f"Hash mismatch for {version_name}: {actual_hash} != {info['hash']}")

        print(f"Reproduced '{version_name}' -> {dst} (hash verified)")
        return dst


if __name__ == '__main__':
    # I create a dummy dataset to practice versioning.
    demo = Path('demo_data.csv')
    demo.write_text('feature1,feature2,target\n1,2,0\n3,4,1\n')

    v = DatasetVersioning()
    v.snapshot('demo_data.csv', 'v1')

    # Modify the dataset and snapshot again.
    demo.write_text('feature1,feature2,target\n1,2,0\n3,4,1\n5,6,0\n')
    v.snapshot('demo_data.csv', 'v2')

    # Reproduce the original v1 dataset for training.
    v.reproduce('v1', output_dir='training_data')
