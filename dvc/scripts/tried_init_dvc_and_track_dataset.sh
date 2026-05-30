#!/bin/bash
# first try: init DVC and track a dataset
# ran this after installing DVC with pip

pip install dvc

# create a tiny sample dataset
mkdir -p data
printf "id,value\n1,0.5\n2,0.8\n3,0.3\n" > data/sample.csv

# init DVC in the repo
git init
dvc init

# track the dataset
dvc add data/sample.csv

# commit the .dvc file (not the raw CSV)
git add data/sample.csv.dvc data/.gitignore .dvc/config
git commit -m "track sample.csv with DVC"

# TODO: set up a remote and push later
