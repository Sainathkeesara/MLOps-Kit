# DVC: get started (and where I got stuck)

I followed the official DVC Get Started tutorial today and kept notes on what confused me. This is my raw documentation, in my own words.

## What I did

1. `pip install dvc`
2. `git init` in my project folder
3. `dvc init` — this creates the `.dvc/` directory and adds stuff to `.gitignore`
4. I followed the tutorial example: classifying iris flowers with `decisiontree`
   - `dvc stage add -n train -d train.py -d data/data.xml -m metric.json train.py`
   - Wait, the tutorial syntax here confused me at first
5. `dvc repro` — this runs the pipeline
6. `git add .` and commit

## Where I got stuck

- The `dvc stage add` command with `-d` and `-m` flags — I kept mixing up what goes where. The `-d` flag is for dependencies (things the stage reads) and `-m` is for metrics (things the stage writes that you want to track).
- I accidentally ran `dvc repro` before adding anything to git. The tutorial assumes git is already initialized, but I tried it in a random folder first.
- I didn't realize that `dvc init` modifies `.gitignore` automatically. I had to read the output carefully the first time.
- The dvc.yaml and dvc.lock files that `dvc stage add` creates — I expected them to be named something else. They live in the repo root by default.

## What worked

Once I understood the dependency vs metric split, everything clicked. Running `dvc repro` after making changes to `train.py` correctly reran only what was needed. That's actually pretty useful.

## Tips for next time

- Initialise git BEFORE `dvc init`
- Read `dvc stage add` flags carefully one at a time
- Check `.dvc/` and `.gitignore` after init to understand what was set up
