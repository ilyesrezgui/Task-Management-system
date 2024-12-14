from task_manager import TaskManager
from task import PersonalTask, WorkTask

def display_menu():
    print("\nTask Management System")
    print("1. Create a Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. View Pending Tasks")
    print("7. View Overdue Tasks")
    print("8. Exit")

def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task_type = input("Enter task type (personal/work): ").strip().lower()
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            if task_type == "personal":
                task = PersonalTask(title, due_date)
                priority = input("Enter priority (high/medium/low): ")
                task.set_priority(priority)
            elif task_type == "work":
                task = WorkTask(title, due_date)
                member = input("Enter a team member name: ")
                task.add_team_member(member)
            else:
                print("Invalid task type.")
                continue

            manager.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            filter_type = input("View all tasks or filter by type (all/personal/work): ").strip().lower()
            manager.list_tasks(None if filter_type == "all" else filter_type)

        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: "))
            manager.delete_task(task_id)

        elif choice == "4":
            manager.save_task()
            print("Tasks saved to file.")

        elif choice == "5":
            manager.load_task()
            print("Tasks loaded from file.")

        elif choice == "6":
            print("Pending tasks:")
            for task in manager.get_pending_tasks():
                print(task)

        elif choice == "7":
            print("Overdue tasks:")
            for task in manager.get_overdue_tasks():
                print(task)

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
