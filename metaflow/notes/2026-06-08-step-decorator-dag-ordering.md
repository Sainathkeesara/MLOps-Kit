# Metaflow @step decorator — how it enforces DAG ordering

I've been digging into how Metaflow's `@step` decorator actually builds and enforces the DAG. There's no separate YAML file or graph definition — the whole shape comes from `self.next()` calls inside each step method.

## How the DAG gets built

Every step in a `FlowSpec` subclass is a method with `@step` on top. When the flow starts, Metaflow reads the bytecode of each step to find every `self.next()` call. The arguments to `self.next()` are references to other step methods on the same class. Metaflow strings those references together to form the graph before running anything.

A linear three-step flow:

```python
class ThreeStepFlow(FlowSpec):

    @step
    def start(self):
        self.next(self.middle)

    @step
    def middle(self):
        self.next(self.end)

    @step
    def end(self):
        pass
```

`start` calls `self.next(self.middle)`, so Metaflow adds an edge from `start → middle`. `middle` calls `self.next(self.end)`, adding `middle → end`. The result is a linear chain.

## Fan-out and fan-in

Passing multiple methods to `self.next()` creates parallel branches:

```python
    @step
    def start(self):
        self.next(self.branch_a, self.branch_b)

    @step
    def branch_a(self):
        self.next(self.join)

    @step
    def branch_b(self):
        self.next(self.join)
```

Both `branch_a` and `branch_b` run in parallel, then converge at `join`. The join step needs `@merge` (or the simpler `step` with `self.next()` handling the merge logic) to resolve both incoming edges.

## What tripped me up

I assumed `@step` would read ordering from a config or decorator argument. It doesn't. If I forget `self.next()` in a step, that step finishes but the flow hangs — nothing tells me at definition time that an edge is missing. The hang only shows up at runtime.

I also tried `self.next("middle")` — passing a string instead of a method reference. Metaflow expects callables, so it throws a runtime error. Easy to fix once you know.

The method references have to be the actual methods, not `self.middle()` (with parens). Calling `self.next(self.middle())` would call `middle` immediately instead of passing it as a reference. That was my third facepalm.

## What I'd try next

I want to experiment with `@merge` to see how it handles joining parallel branches cleanly. Also curious how `@resources` and `@batch` decorators interact with step boundaries — do they override the step-level resource request or add to it?
