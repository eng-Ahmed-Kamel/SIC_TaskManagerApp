from Task import Task
# _______________________________________________________________________
# personal task creation & use of inheritance and polymorphism
class Personal_task(Task):
    def __init__(self, title, description, due_date, status, task_category):
        super().__init__(title, description, due_date, status)
        self.task_category = task_category

    def display(self):
        super().display()
        print(f"Category: {self.task_category}")
        print(self.get_task_type())
    def to_dic(self):
        return {"title": self.title, "description": self.description, "due_date": self.due_date, "status": self.status,
                "task_category": self.task_category}

    def get_task_type(self):
        return "Personal Task"


# ________________________________________________________________
