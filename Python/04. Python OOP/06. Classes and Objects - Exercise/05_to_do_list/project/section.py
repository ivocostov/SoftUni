from typing import List

from MainProblem.project import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            Task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for index, task in enumerate(self.tasks):
            if task.completed:
                cleared_tasks += 1
                del self.tasks[index]
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        text = f"Section {self.name}:\n"
        for current_task in self.tasks:
            text += f"{current_task.details()}\n"
        return text




