---
last_verified: 2026-09-12
tool_version: n/a
---

# DVC: install DVC and log my first dataset version

I installed DVC in a small Git project and made my first attempt to record a dataset version. I used a tiny CSV so I could focus on the workflow instead of a large download.

I worked through the first versioning attempt and paid attention to the files created along the way. The main thing I wanted to understand was how to keep a dataset version associated with the project without treating every data change as a large Git commit.

My next step is to connect shared storage, upload the data there, and confirm that another checkout can restore the same version.

## What I'd try next

I want to change the CSV, record another version, and compare the two records. Then I'll repeat the flow with a larger file and see where the workflow feels slow or unclear.
