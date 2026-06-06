from metaflow import FlowSpec, step


class HelloFlow(FlowSpec):
    @step
    def start(self):
        self.message = "Hello, Metaflow!"
        self.next(self.end)

    @step
    def end(self):
        print(self.message)


if __name__ == "__main__":
    HelloFlow().run()