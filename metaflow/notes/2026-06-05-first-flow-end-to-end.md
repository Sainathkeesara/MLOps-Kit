# Metaflow: first end-to-end flow

Installed Metaflow with `pip install metaflow` — no issues there. Then I tried writing my first flow.

Started with a simple linear flow — a `Start` step, a `train` step, and an `End` step. The `@step` decorator is how you mark each method as a step. Kinda like Airflow DAGs but way simpler to write — you don't need a separate DAG definition file.

First run went smoothly:

```bash
python my_first_flow.py run
```

The output shows each step executing in order. Metaflow prints a timeline with durations. I ran it a few times and noticed it caches results — second run was instant because it used the cache from the first run.

Got stuck when I tried passing a parameter. I forgot to add `@parameter` decorator on the class. Once I added it, the flow picked up `--my-param` from the CLI automatically.

Then I added a branching step — `@step` with `next()` pointing to two parallel steps and a `join` step. Metaflow handles the merge with a `inputs` parameter that collects artifacts from upstream steps.

The UI (`metaflow tutorial` or `python my_flow.py show`) is pretty basic but shows the DAG structure. Not as polished as Airflow's UI but it gets the job done.

What tripped me up: artifact scope. Objects assigned to `self` in one step are available in downstream steps, but I kept trying to access them from sibling steps (nope — only ancestors). Once I wrapped my head around the DAG data flow it made sense.

Next I want to try Metaflow's `@resources` to request GPUs and see how it handles larger data.
