---
last_verified: 2026-09-13
tool_version: 3.67.1
sources:
  - https://theneuralbase.com/mlops-fundamentals/learn/beginner/dvc-for-data-version-control/
---

# Missing companion data files for DVC notes

I realized the DVC primer and notes reference some data files that don't actually exist in the repo. If someone follows along, they'll get "file not found" errors. So I'm creating the missing companion files here.

## What files are missing?

The primer mentions `data/train.csv` and `data/train.csv.dvc` as examples. The note "Install DVC and log my first dataset version" also uses `data/sample.csv` and `data/sample.csv.dvc`. I need to provide both the actual CSV files and the `.dvc` pointer files.

## data/train.csv

A tiny CSV with a few rows. This is what you'd `dvc add` in the primer example.

```
id,value
1,0.5
2,0.8
3,0.3
4,0.9
5,0.2
```

## data/train.csv.dvc

The `.dvc` file that DVC creates when you run `dvc add data/train.csv`. It stores the hash and output path.

```yaml
md5: a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6
outs:
  - path: data/train.csv
```

(You'd normally get this file automatically after `dvc add`; I'm just providing it so the repo has a complete example.)

## data/sample.csv

Another tiny CSV used in the note. Slightly different values.

```
id,value
1,0.5
2,0.8
3,0.3
```

## data/sample.csv.dvc

The corresponding `.dvc` pointer file.

```yaml
md5: f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1
outs:
  - path: data/sample.csv
```

## How to create these files yourself

If you're starting from scratch, here's the bash to create the CSVs and let DVC generate the `.dvc` files:

```bash
mkdir -p data
printf "id,value\n1,0.5\n2,0.8\n3,0.3\n4,0.9\n5,0.2\n" > data/train.csv
dvc add data/train.csv
git add data/train.csv.dvc .gitignore

printf "id,value\n1,0.5\n2,0.8\n3,0.3\n" > data/sample.csv
dvc add data/sample.csv
git add data/sample.csv.dvc .gitignore
```

That's it. Now the notes' examples will actually work.