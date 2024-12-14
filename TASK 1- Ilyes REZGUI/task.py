from datetime import date

# Base Task class
class Task:
    _task_counter = 0  # Class variable for unique ID assignment

    def __init__(self, title, due_date, flag=None, description=None):
        Task._task_counter += 1
        self._task_id = Task._task_counter
        self.title = title
        self.due_date = due_date
        self.status = "pending"
        self._description = description
        self.flag = flag

    def mark_completed(self):
        self.status = "completed"

    def __str__(self):
        return f"Task ID: {self._task_id}, Title: {self.title}, Due Date: {self.due_date}, Status: {self.status}"

    @property
    def description(self):
        return self._description
    
    def get_id(self):
        return self._task_id
    

    @description.setter
    def description(self, desc):
        if len(desc) > 15:
            raise ValueError("Description must be 15 characters or less.")
        self._description = desc

# PersonalTask class
class PersonalTask(Task):
    def __init__(self, title, due_date, priority="low", description=None):
        super().__init__(title, due_date, flag="personal", description=description)
        self.priority = priority

    def is_high_priority(self):
        return self.priority == "high"

    def set_priority(self, priority):
        if priority in ["high", "medium", "low"]:
            self.priority = priority
        else:
            print("Invalid priority. Use 'high', 'medium', or 'low'.")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Priority: {self.priority}"

# WorkTask class
class WorkTask(Task):
    def __init__(self, title, due_date, description=None, team_members=None):
        super().__init__(title, due_date, flag="work", description=description)
        self.team_members = team_members if team_members is not None else []

    def add_team_member(self, member):
        if member:
            self.team_members.append(member)

    def __str__(self):
        base_str = super().__str__()
        members = ", ".join(self.team_members) if self.team_members else "None"
        return f"{base_str}, Team Members: {members}"


# Create a WorkTask instance
work_task = WorkTask(title="Team Meeting", due_date="2024-11-20", team_members=["Ilyes", "Ali"])
print(work_task)  # Print work task details

# Add a new team member
work_task.add_team_member("Slim")
print(work_task.team_members)  # Output: ['Ilyes', 'Ali', 'Slim']
