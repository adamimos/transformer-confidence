import os
import json
from bigbench.api import json_task

class BigBenchLoader:
    def __init__(self, task_name):
        self.task_name = task_name
        self.data = []

    def load_data(self):
        task_path = os.path.join('bigbench', 'benchmark_tasks', self.task_name)
        task = json_task.JsonTask(task_path)
        self.data = task.get_test_examples()

    def get_data(self):
        if not self.data:
            self.load_data()
        return self.data
