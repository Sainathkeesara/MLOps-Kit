# last_verified: 2026-08-12 · metaflow n/a
# mfl-045 — my first Metaflow flow, end to end, with a simple data transform
from metaflow import FlowSpec, step

class FirstTransformFlow(FlowSpec):
    @step
    def start(self):
        self.data = [1, 2, 3, 4, 5]
        self.next(self.transform)

    @step
    def transform(self):
        self.squared = [x * x for x in self.data]
        self.next(self.end)

    @step
    def end(self):
        print(self.squared)
