---
last_verified: 2026-09-15
tool_version: n/a
---

# My first look at the SageMaker Studio console

I opened Studio today from the console just to see what it feels like. I landed on a launcher with notebooks, jobs, and endpoints in the left nav, and I clicked around without a plan.

I started a notebook and ran a couple of cells — it felt like a normal notebook, but I liked that my files and runs showed up next to it instead of in another tab. I then opened the training jobs list and found the test job I had kicked off from my laptop, which made the link between SDK and console click for me.

I got stuck on permissions for a bit. My console user could see things my notebook role could not open, and I had to ask which role I was meant to use. I also closed a kernel and was not sure at first whether the machine behind it had stopped.

What I'd try next: launch one tiny training job straight from a Studio notebook and then send one request to a test endpoint, so I see the whole loop in one place.
