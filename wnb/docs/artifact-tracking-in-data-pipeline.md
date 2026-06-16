# W&B artifact tracking in a data pipeline

## Purpose

I used W&B artifacts to connect the data steps in a small ML pipeline to the training run. Instead of only logging metrics, the pipeline writes versioned artifacts for the raw input, processed dataset, and model checkpoint, then links those artifacts back to the run that produced or consumed them.

This is one way to wire it together with the Python SDK. It keeps the data pipeline and experiment tracking close, but it does not replace a dedicated data lake or feature store.

## Steps

1. **Create a run for the pipeline stage.** Start the run before any dataset work so every artifact is attached to the same run.

```python
import wandb

run = wandb.init(project="mlops-kit-demo", name="data-pipeline-artifacts")
```

2. **Log the raw dataset as an artifact.** I saved the source file to a temp directory, added it to an artifact with `type="dataset"`, and called `run.log_artifact()`.

```python
artifact = wandb.Artifact("raw-customer-data", type="dataset")
artifact.add_file("data/raw/customers.csv")
raw = run.log_artifact(artifact)
```

3. **Use the artifact reference in the next stage.** For a downstream processing step, I pulled the artifact into a local directory before running transformations.

```python
raw_dir = raw.download()
# process files in raw_dir, then write data/processed/customers.parquet
```

4. **Log the processed dataset and model.** After the pipeline finishes, I logged both outputs. The model artifact points back to the data that trained it.

```python
processed = wandb.Artifact("processed-customer-data", type="dataset")
processed.add_file("data/processed/customers.parquet")
run.log_artifact(processed)

model = wandb.Artifact("customer-churn-model", type="model")
model.add_file("models/churn_model.joblib")
run.log_artifact(model)
```

5. **Finish the run after all logging is done.** Calling `run.finish()` closes the run and makes the artifact lineage visible in the W&B UI.

```python
run.finish()
```

## Verify

I checked the run page for three linked artifacts: raw dataset, processed dataset, and model. The artifact tab showed the version aliases, and the run page showed which stage produced each artifact. I also checked that a fresh run could call `artifact.download()` on the logged raw dataset and get the same file layout.

The main thing I learned is that artifacts are more useful when the pipeline names them consistently. `customers-v1` is easier to trace than `dataset-final-final`, and the run page becomes the map between data version, model version, and training metrics.
