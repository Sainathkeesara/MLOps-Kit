# last_verified: 2026-07-07 · metaflow

from metaflow import FlowSpec, step


class FirstFlow(FlowSpec):
    @step
    def start(self):
        self.hello = "hello from metaflow"
        self.next(self.end)

    @step
    def end(self):
        print(self.hello)


if __name__ == "__main__":
    FirstFlow()
