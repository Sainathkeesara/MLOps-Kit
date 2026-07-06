# last_verified: 2026-07-06 · metaflow 2.19.35

from metaflow import FlowSpec, step


class TinyFlow(FlowSpec):
    @step
    def start(self):
        self.message = "hello from metaflow"
        self.next(self.end)

    @step
    def end(self):
        print(self.message)


if __name__ == "__main__":
    TinyFlow()
