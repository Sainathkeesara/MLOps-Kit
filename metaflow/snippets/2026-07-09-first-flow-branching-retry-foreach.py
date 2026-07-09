# last_verified: 2026-07-09 · Metaflow 2.19.35

from metaflow import FlowSpec, step, retry


class BranchRetryForeachFlow(FlowSpec):
    """First flow combining branching, retry, and foreach.

    I started with the bare HelloFlow and kept adding the
    tutorial patterns one at a time. The trickiest part was
    remembering that the join step needs an `inputs` parameter
    to pull artifacts back from each branch.
    """

    # --- config ---
    num_checks = 3
    items_to_process = ["alpha", "beta", "gamma"]

    @step
    def start(self):
        # start and end are mandatory — missing either crashes at runtime
        self.next(self.check_flaky, self.process_items)

    @step
    @retry(times=3, minutes=2)
    def check_flaky(self):
        # @retry defaults to 3 attempts with 2-minute waits, but I set it
        # explicitly here so the behavior is obvious when reading the code.
        import random

        self.flip = random.choice([True, False])
        print(f"check_flaky attempt: flip={self.flip}")
        if not self.flip:
            raise RuntimeError("transient failure — retrying")
        self.next(self.join)

    @step
    def process_items(self):
        # foreach spawns one parallel task per list item; the tasks are
        # unnamed, so the join step iterates over `inputs` rather than
        # referencing them by name.
        self.results = []
        for item in self.items_to_process:
            self.results.append(f"processed-{item}")
        self.next(self.join)

    @step
    def join(self, inputs):
        # after a branch, the join step must accept `inputs` to access
        # artifacts from each incoming path; otherwise I get a KeyError
        # at runtime when trying to read `inputs.check_flaky.flip`
        self.branch_result = inputs.check_flaky.flip
        self.foreach_results = [r for r in inputs.process_items.results]
        print(f"join sees flip={self.branch_result}")
        print(f"join sees foreach={self.foreach_results}")
        self.next(self.end)

    @step
    def end(self):
        # every flow needs an end step or the run never finishes
        print("done")


if __name__ == "__main__":
    BranchRetryForeachFlow()
