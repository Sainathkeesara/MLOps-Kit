from metaflow import FlowSpec, step, Parameter


class ParamBranchMergeFlow(FlowSpec):
    split_point = Parameter("split_point", default=5, type=int)
    name = Parameter("name", default="world", type=str)

    @step
    def start(self):
        print(f"Hello {self.name}, split_point={self.split_point}")
        self.next(self.branch_a, self.branch_b)

    @step
    def branch_a(self):
        self.result = self.split_point * 2
        print(f"Branch A: {self.split_point} * 2 = {self.result}")
        self.next(self.join)

    @step
    def branch_b(self):
        self.result = self.split_point + 10
        print(f"Branch B: {self.split_point} + 10 = {self.result}")
        self.next(self.join)

    @step
    def join(self, inputs):
        # inputs collects artifacts from each branch
        self.results = [inp.result for inp in inputs]
        print(f"Merged from both branches: {self.results}")
        self.next(self.end)

    @step
    def end(self):
        print(f"Done — results: {self.results}")


if __name__ == "__main__":
    ParamBranchMergeFlow()
