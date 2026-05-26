#!/bin/bash
# Track a data pipeline end-to-end with DVC - feature pipeline

dvc init
dvc stage add -n prepare -d data/raw.csv -o data/prepared.csv -- python prepare.py data/raw.csv data/prepared.csv
dvc stage add -n train -d data/prepared.csv -o models/model.pkl -- python train.py data/prepared.csv models/model.pkl
dvc repro
dvc dag
