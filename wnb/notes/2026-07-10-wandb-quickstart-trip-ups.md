---
last_verified: 2026-07-10
tool_version: n/a
---

# Running the W&B quickstart again — sweep focus, CLI gotchas, and config quirks

I already walked through the basic quickstart back in June, so this time I followed the [wandb quickstart](https://docs.wandb.ai/quickstart) again from scratch but paid attention to the sweep tutorial and the CLI login flow. Here's what stood out.

## Steps I followed

1. `pip install wandb` — clean install, no issues.
2. `wandb login` — pasted the API key from the UI. This time I noticed it also creates `~/.netrc` with the key, which means you can skip the prompt by putting the key in that file.
3. Ran the starter script to verify tracking works.
4. Moved on to the sweep tutorial: defined a sweep config, called `wandb.sweep()`, then `wandb.agent()`.

## What tripped me up

**Sweep config vs Python API mismatch.** The quickstart's sweep section starts with YAML, then switches to the Python SDK. I followed the YAML example first and got a `ConfigError: unknown field` because I used `parameters.learning_rate` (snake_case from an older blog post) vs `parameters.learning-rate` (the format the current YAML parser expects). The YAML keys must match what the agent passes — the quickstart doesn't point this out clearly.

**`wandb.agent()` ran synchronous by default.** I expected it to fork or run in the background. Instead it blocks until `count` runs complete. That's fine for a script but surprising if you're used to tools that queue jobs and return immediately. I had to Ctrl+C the terminal and re-read the doc to realize `count=1` would give me just one trial for testing.

**Run names in the UI.** I didn't set `name` in `wandb.init()`, so W&B auto-generated names like `noble-firebrand-47`. Cute, but impossible to find in a list of 20 runs. Setting `name` explicitly (or using `config.run_name`) would have saved time sorting later.

**Config inside the training function.** The sweep example in the docs wraps the training loop in a function and calls `wandb.init()` inside it. I put `wandb.init()` outside by habit, and the sweep agent created runs for the outer init but never logged sweep suggestions. Took me three attempts to realize the sweep agent re-inits per trial — you can't init once and reuse.

## What I'd try next

- Use the YAML sweep config approach (wandb/sweeps) and load it from a file instead of the Python dict — cleaner separation.
- Set `name` dynamically from the sweep parameters so the UI shows `lr-0.01-bs-32` instead of random names.
- Wire it into a shell loop that checks `wandb agent` exit codes and retries if a trial crashes — the agent stops on unhandled exceptions.
