from Task import Task
# ________________________________________________________________
# work task creation & use of inheritance and polymorphism
class Work_task(Task):
    def __init__(self, title, description, due_date, status, task_priority):
        super().__init__(title, description, due_date, status)
        self.task_priority = task_priority

    def display(self):
        super().display()
        print(f"priority: {self.task_priority}")
        print(self.get_task_type())
    def to_dic(self):
        return {"title": self.title, "description": self.description, "due_date": self.due_date, "status": self.status,
                "task_priority": self.task_priority}

    def get_task_type(self):
        return "work Task"
# ____________________________________________________________________
