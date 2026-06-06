# Added `.git/` to README Layout section

Noticed the Layout table in README.md lists all the directories you'd actually see when cloning the repo. But `.git/` was missing. It's a directory that exists in every clone, and someone new to the repo might wonder why there's no mention of it.

I added a line right before `00_index/`:

```
- **`.git/`** — Git version history, branches, and object store
```

Kept it short. The old ordering has `.git/` up top since dots sort before alphanumeric in most listings. Didn't want to over-describe — it's just git metadata, most people know what it is.
