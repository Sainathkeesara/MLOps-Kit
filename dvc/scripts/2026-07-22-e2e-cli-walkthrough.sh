#!/usr/bin/env bash
# last_verified: 2026-07-22 · DVC 3.x

# Start a temp repostory
TMPDIR="$(mktemp -d)"
cd "$TMPDIR" || exit

git init
git config user.email "learner@example.com"
git config user.name "Learner"

dvc init
git add .
git commit -m "init dvc"

# Create a dummy dataset and track it
mkdir -p data
cat > data/raw.csv <<'CSV'
id,value
1,10
2,20
3,30
CSV

dvc add data/raw.csv
git add data/raw.csv.dvc .gitignore
git commit -m "track raw.csv"

# Verify cache and metadata exist
ls -la data/raw.csv.dvc
# Verify remote endpoints
dvc remote list

# End-to-end sanity checks
dvc status
# .dvc file should appear as nothing to commit
# raw.csv should remain untouched on disk