# My first time wandering the Kubeflow Central Dashboard

Just logged into the Central Dashboard and poked around. Took a ton of screenshots that I won't paste here, but here's my raw impression.

## What I saw

The Dashboard opens to a landing page with a cluster topology view on the left. That shows CPU/memory usage across nodes. Handy for a sanity check, but I expected to see my pipelines there too.

The top nav has:
- **Pipelines** — opens the KFP UI in a new tab
- **Notebook Servers** — SO much potential. I clicked and saw a "Launch" button that creates a Jupyter notebook server on your cluster.
- **Katib** — hyperparameter tuning. I didn't touch it yet but it's there and looks integrated.
- **Volumes** — PVCs listed by name. I have none yet so it's empty.
- **Catalog** — sample workflows you can import.

## What tripped me up

I clicked **Notebook Servers** first thinking it was part of the Dashboard. Nope — it opens a whole separate UI. The URL changes and it feels like a different product. Same design language, but a different SPA.

The "New Server" form has a "Kubeflow Pipelines SDK" checkbox I didn't understand. I unchecked it and just picked a CPU-only image. Server started in ~40 seconds.

When I opened the notebook that came pre-installed, the integrated terminal already had `kfp` available but `dsl-compile` wasn't in PATH. I had to pip install it inside the notebook. Not a big deal but felt late-day-1.

## What I'd try next

- Launch a pipeline from the Pipelines tab, not just upload
- Try Katib with a simple MNIST example
- Check whether the Notebook can access the cluster's PVCs by default

---

That's the central dashboard on day one. Big surface area, most of it untouched.
