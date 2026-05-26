# DVC: Install and version my first dataset

Installed DVC today: `pip install dvc`. Straightforward — no issues.

Created a new project dir, `git init` and `dvc init`. DVC added `.dvc/` and updated `.gitignore` automatically.

Grabbed a sample CSV (the Iris dataset):

```bash
wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data -O data/iris.csv
```

Tracked it:

```bash
dvc add data/iris.csv
```

This created `data/iris.csv.dvc` and added `data/iris.csv` to `.gitignore`. Staged and committed both files.

Set up a local remote for testing:

```bash
mkdir -p /tmp/dvc-remote
dvc remote add -d local /tmp/dvc-remote
dvc push
```

`dvc push` copied the cached file to `/tmp/dvc-remote/`. Then I wiped the cache (`rm -rf .dvc/cache`) and ran `dvc pull` — it restored `data/iris.csv` from the remote.

What tripped me up: at first I didn't `git add` the `.dvc` file. DVC pushed fine but Git couldn't share the pointer. Have to remember: `.dvc` files go in Git, actual data stays out.
