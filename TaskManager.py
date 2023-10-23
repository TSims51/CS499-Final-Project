#!/usr/bin/env python3

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskDB:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

    def list_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Incomplete"
            print(f"{task.name} ({status}) - Due: {task.due_date}")
            print(f"Description: {task.description}\n")
