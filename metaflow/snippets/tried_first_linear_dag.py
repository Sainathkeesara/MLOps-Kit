from metaflow import FlowSpec, step, Parameter


class LinearParamFlow(FlowSpec):
    alpha = Parameter("alpha", default=0.5, type=float)
    num_iters = Parameter("num_iters", default=10, type=int)

    @step
    def start(self):
        print(f"alpha={self.alpha}, num_iters={self.num_iters}")
        self.next(self.mid)

    @step
    def mid(self):
        self.result = sum(self.alpha * i for i in range(self.num_iters))
        print(f"computed result={self.result}")
        self.next(self.end)

    @step
    def end(self):
        print(f"final result={self.result}")


if __name__ == "__main__":
    LinearParamFlow()
