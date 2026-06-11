"""Parameterize a Metaflow flow with @parameters decorator.

Following the docs example — passing config values at runtime
instead of hardcoding them inside steps.
"""

from metaflow import FlowSpec, step, Parameter


class ParameterizedHelloFlow(FlowSpec):
    # parameters are defined as class variables with Parameter()
    greeting = Parameter("greeting", default="Hello", type=str)
    name = Parameter("name", default="world", type=str)
    repeat = Parameter("repeat", default=1, type=int)

    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        for i in range(self.repeat):
            print(f"{i + 1}. {self.greeting}, {self.name}!")


if __name__ == "__main__":
    ParameterizedHelloFlow().run()

    # to pass different values at the command line:
    #   python tried_parameterizing_a_flow.py run --greeting "Hi" --name "Metaflow" --repeat 3
