---
last_verified: 2026-07-22
tool_version: 3.x
sources:
  - https://theneuralbase.com/mlops-fundamentals/learn/beginner/dvc-for-data-version-control/
  - https://fixdevs.com/blog/dvc-not-working/
---

# 2026-07-22 Install DVC and track first dataset with `dvc add`

I just installed DVC with `pip install dvc`. Ran `dvc version` and it printed the version string and the Python runtime. Next I initialized a Git repo and ran `dvc init`, which created a `.dvc/` directory and a `.dvc/config` file. I also noticed it wrote to `.gitignore` automatically so the cache stays out of Git.

For the first dataset, I created a dummy CSV and ran `dvc add data/raw.csv`. DVC created `data/raw.csv.dvc` (the pointer file) and added `data/raw.csv` to `.gitignore`. I committed both the `.dvc` file and the updated `.gitignore`.

A few things I want to remember: `git add -f data/raw.csv` bypasses `.gitignore`, which will fail if the file exceeds GitHub's size limit, so don't do that. The metadata lives in the `.dvc` file, not the raw bytes.