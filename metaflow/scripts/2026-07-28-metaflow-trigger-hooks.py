# last_verified: 2026-07-28 · Metaflow n/a
# first try with @trigger, @trigger_on_finish, and @exit_hook
# I'm trying to wire two flows together and log what each decorator does

from metaflow import FlowSpec, step, trigger, trigger_on_finish, exit_hook


class ParentFlow(FlowSpec):
    @trigger
    @step
    def start(self):
        print("parent: started")
        self.next(self.end)

    @step
    def end(self):
        print("parent: ended")
        self.next(self.after_child)

    @trigger_on_finish(flow="ChildFlow")
    @step
    def after_child(self):
        print("parent: child finished")
        self.next(self.exit)

    @exit_hook
    @step
    def exit(self):
        print("parent: exiting")
        self.next(self.done)

    @step
    def done(self):
        print("parent: done")


class ChildFlow(FlowSpec):
    @trigger
    @step
    def start(self):
        print("child: started")
        self.next(self.end)

    @step
    def end(self):
        print("child: ended")
        self.next(self.exit)

    @exit_hook
    @step
    def exit(self):
        print("child: exiting")
        self.next(self.done)

    @step
    def done(self):
        print("child: done")


if __name__ == "__main__":
    ParentFlow()
    ChildFlow()
