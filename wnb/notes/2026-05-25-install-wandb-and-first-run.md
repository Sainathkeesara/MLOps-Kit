# wnb-002 — Install wandb and log my first run

I installed wandb today and ran my first experiment. Quick and painless.

**what I did**

1. Installed the package:
   `pip install wandb`

2. Logged in:
   `wandb login`
   It asked for an API key. I grabbed mine from https://wandb.ai/authorize and pasted it in.

3. Created a tiny Python script that calls `wandb.init()`, logs a couple metrics, and calls `wandb.finish()`.

4. Ran it. The terminal output showed a link to the run page in the W&B dashboard.

**what I noticed**

- The dashboard link opened a clean page with the run name, config, and a chart of my metrics — it just works.
- W&B creates a project automatically if you pass a project name that doesn't exist yet.
- The free tier lets you have unlimited runs and projects, which is nice for learning.

**next thing I'll try**

Write a script that actually trains a tiny model and logs metrics per epoch so I can see a real training curve.
