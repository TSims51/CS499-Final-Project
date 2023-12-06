#!/usr/bin/env python3

import json
from datetime import datetime

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskDB:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def is_valid_due_date(self, due_date):
        try:
            datetime.strptime(due_date, '%m-%d-%Y')
            return True
        except ValueError:
            return False

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                self.tasks.remove(task)
                self.save_tasks()
                print("\nTask", task_name, "marked as completed and removed from the manager!\n")
                return

        print("\nTask", task_name, "not found. No task marked as completed or removed from the manager.\n")

    def delete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                self.save_tasks()
                print("\nTask", task_name, "deleted!\n")
                return

        print("\nTask", task_name, "not found. No task deleted.\n")

    def list_tasks(self):
        self.sort_tasks_by_due_date()

        for task in self.tasks:
            status = "Completed" if task.completed else "Incomplete"
            current_date = datetime.now()
            due_status = " (Past Due)" if datetime.strptime(task.due_date, '%m-%d-%Y') < current_date else ""
            print(task.name, " (", status, ") - Due: ", task.due_date, due_status)
            print("Description: ", task.description, "\n")

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda task: datetime.strptime(task.due_date, '%m-%d-%Y'))

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            tasks_data = [{'name': task.name, 'description': task.description,
                           'due_date': task.due_date, 'completed': task.completed} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                tasks = [Task(task['name'], task['description'], task['due_date']) for task in tasks_data]
                for i, task in enumerate(tasks):
                    task.completed = tasks_data[i]['completed']
                return tasks
        except FileNotFoundError:
            return []


def menuPrompt():
    return input("Task Menu:\n 1. Add Task\n 2. Mark Task Completed\n 3. Delete Task\n 4. List Tasks\n 5. Exit \n Enter Choice Number: \n")



#============================================================
if __name__ == "__main__":

    taskTracker = TaskDB()

    while True:
        menu_choice = menuPrompt()

        if menu_choice == "1":
            task_name = input("\nEnter Task Name: ")
            task_desc = input("Enter Task Description: ")

            while True:
                task_duedate = input("Enter Task Due Date (MM-DD-YYYY): ")
                if taskTracker.is_valid_due_date(task_duedate):
                    task = Task(task_name, task_desc, task_duedate)
                    taskTracker.add_task(task)
                    print("\nTask Added\n")
                    break
                else:
                    print("\nInvalid due date format. Please enter the date in MM-DD-YYYY format.\n")

        elif menu_choice == "2":
            task_name = input("Enter the name of the completed task: ")
            taskTracker.mark_task_completed(task_name)


        elif menu_choice == "3":
            task_name = input("Enter the name of the task to delete: ")
            taskTracker.delete_task(task_name)


        elif menu_choice == "4":
            taskTracker.list_tasks()


        elif menu_choice == "5":
            break



        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.\n")

    print("Exiting the program.")






