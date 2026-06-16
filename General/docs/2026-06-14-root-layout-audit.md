# Root layout audit for README

The active task had no item name in the backticks, so I checked the actual repo root instead of guessing. I see `.git/`, `00_index/`, `CHANGELOG.md`, `General/`, `README.md`, `dvc/`, `feast/`, `kubeflow/`, `metaflow/`, `mlflow/`, and `wnb/`.

Most of those were already in README Layout. I added `.git/` because it is visible in a clone and an older note said it was added but the README line was not there. I also added `dvc/configs/` under `dvc/` because the working tree already had an uncommitted note for that folder and the README still only showed the parent `dvc/` line.

I bumped the General docs count from 6 to 13 and the file badge from 78 to 81 so the top of the README matches the files I added in this pass.
