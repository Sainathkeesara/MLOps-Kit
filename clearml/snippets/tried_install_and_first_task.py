# Just installed clearml and tried creating my first task
# I ran: pip install clearml
# Then needed to configure with: clearml-init  # this sets up the server connection

from clearml import Task
import random

# This creates a task and logs it to the server
task = Task.init(project_name="my-first-project", task_name="hello-clearml")

# Log some parameters — they show up in the UI under the task
params = {"learning_rate": 0.01, "batch_size": 32, "epochs": 5}
task.set_parameters(params)

# Do something trivial — just train a pretend model
dummy_accuracy = random.uniform(0.7, 0.95)
task.get_logger().report_scalar("accuracy", "train", dummy_accuracy, iteration=0)

print(f"Logged task {task.id} with accuracy {dummy_accuracy:.3f}")
# TODO: next step — try chaining this into a pipeline with multiple steps
