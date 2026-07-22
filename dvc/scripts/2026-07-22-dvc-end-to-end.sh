#!/bin/bash
# first dvc end-to-end: init repo, track data, set remote, push
# TODO: not sure why `dvc push` is needed before pulling locally
pip install dvc
mkdir -p data
printf "id,score\n1,0.42\n2,0.87\n3,0.15\n" > data/scores.csv
git init
dvc init
dvc add data/scores.csv
git add data/scores.csv.dvc data/.gitignore .dvc/config
git commit -m "track scores.csv with DVC"
mkdir -p /tmp/dvc-remote
dvc remote add -d local /tmp/dvc-remote
dvc push
ls .dvc/cache
