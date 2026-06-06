# mfl-002 — Explore Metaflow UI and inspect a completed flow run

Clicked through the Metaflow UI after running my first flow to see what I could find.

**what I did**

Ran `python flow.py show` for my earlier TinyTrainFlow to open the UI locally:

```
python TinyTrainFlow.py show
```

This spun up a local webserver on port 8050 (I think) and opened the Flow browser in my browser.

**what I saw in the UI**

- The sidebar lists all my flows — found TinyTrainFlow there
- Clicked into it and saw a timeline of run executions
- Each run shows:
  - Step name and status (finished, running, failed)
  - Duration of each step
  - Links to inspect step outputs

Clicked on a specific run, then on the `train_model` step. Could see the model object was stored (showed the RandomForestClassifier details). The `evaluate` step showed the printed accuracy score.

**what I noticed**

- The UI loads fast, no database setup needed
- Failed steps show red and I can click to see error output
- Successful steps have green checkmarks and show their output
- Can compare runs by clicking the run selector dropdown
- Step artifacts (like `self.model`) are inspectable without writing save/load code

**next thing I'll try**

Add `@checkpoint` to save intermediate results and see how that shows up in the UI.