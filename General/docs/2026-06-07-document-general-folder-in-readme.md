# Document General/ folder in README Layout section

I noticed the General/ folder wasn't listed in the README Layout section even though it's a
real top-level directory with cross-tool docs. The Repo Auditor flagged this as an anomaly.

Fixed it by adding a line between feast/ and kubeflow/ (alphabetical order):

    - **`General/`** — Cross-tool documentation and project-level guides

The Coverage table doesn't have a General row since it's not a tool, so only the Layout
section needed updating. Quick fix.
