import dvc.api
from dvc.repo import Repo
import pandas as pd
import os

os.chdir("/Users/kill/mlprojects")

repo = Repo()

df = dvc.api.read_csv(
    "data/iris.csv",
    repo=".",
    rev="main"
)

print(df.head())
