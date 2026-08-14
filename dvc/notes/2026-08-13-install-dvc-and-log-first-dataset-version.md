---
last_verified: 2026-08-13
tool_version: 3.67.1
sources:
  - https://doc.dvc.org/command-reference/init
  - https://doc.dvc.org/install
  - https://doc.dvc.org/user-guide/troubleshooting
---

# DVC: install DVC and log my first dataset version

I installed DVC today (`pip install dvc`) and tried to version my first dataset. The install was easy; the init step is where I tripped.

`dvc init` without any flags hard-requires an existing Git repo — it errored immediately in my plain folder. I had to `git init` first, then `dvc init` succeeded. Also learned `dvc init` a second time errors out; to re-init I'd need `-f, --force`.

After init I checked what it created: a `.dvc/` directory (config + default cache location) and entries in `.gitignore`. Two things I'm still keeping straight:

- **`.dvc/`** must be committed to Git — it's the metadata that makes the setup visible to collaborators.
- **`.dvc/cache`** is NOT tracked by Git; it holds the actual data bytes.
- **`.dvcignore`** controls what DVC ignores for data ops; **`.gitignore`** controls Git. They are separate files — ignoring in one does not ignore in the other.

For my first version I used a tiny local CSV so I wouldn't fight a cloud remote:

```bash
dvc add data/sample.csv
git add data/sample.csv.dvc .gitignore
git commit -m "add sample data version"
```

`dvc add` produced `data/sample.csv.dvc` (a pointer file) and moved the real file into the cache. Committing the `.dvc` pointer is what makes the version shareable.

## What I'd try next

Set up a real remote (S3/GCS/local dir) and push data up so `dvc pull` works from another machine. The troubleshooting docs warn that `dvc pull` fails with `Cache 'xxxx' not found` if data was pushed to Git without the data being uploaded to the DVC remote — I want to see that round-trip work end to end.
