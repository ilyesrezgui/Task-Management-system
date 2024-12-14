import csv
from datetime import datetime
from task import Task, PersonalTask, WorkTask

class TaskManager:
    def __init__(self, task_list_file_name="task_list.csv"):
        self.tasks = []
        self.task_list_file_name = task_list_file_name

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self, flag=None):
        for task in self.tasks:
            if flag is None or task.flag == flag:
                print(task)

    def delete_task(self, task_id):
        task_to_delete = next((task for task in self.tasks if task._task_id == task_id), None)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def save_task(self):
        with open(self.task_list_file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["task_id", "title", "due_date", "status", "description", "flag"])
            for task in self.tasks:
                writer.writerow([task._task_id, task.title, task.due_date, task.status, task.description, task.flag])

    def load_task(self):
        try:
            with open(self.task_list_file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task_type = row["flag"]
                    task = PersonalTask(row["title"], row["due_date"]) if task_type == "personal" else WorkTask(row["title"], row["due_date"])
                    task._task_id = int(row["task_id"])
                    task.status = row["status"]
                    task.description = row["description"]
                    self.add_task(task)
        except FileNotFoundError:
            print("Task file not found.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.status == "pending"]


    def get_overdue_tasks(self):
        today = datetime.today().date()
        overdue_tasks = []
        for task in self.tasks:
            try:
                # Convert string due_date to datetime.date if necessary
                due_date = task.due_date
                if isinstance(due_date, str):
                    due_date = datetime.strptime(due_date, "%Y-%m-%d").date() 
                if due_date < today and task.status == "pending":
                    overdue_tasks.append(task)
            except ValueError as e:
                print(f"Error parsing due_date for task {task}: {e}")
        return overdue_tasks

