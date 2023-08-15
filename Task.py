# _______________________________________________________
# task class creation to do inheritance and polymorphism
class Task:
    # attributes
    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    # method to convert into dictionary
    def to_dic(self):
        return {"title": self.title, "description": self.description, "due_date": self.due_date, "status": self.status}

    # method to display data
    def display(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")

    # method to return task type
    def get_task_type(self):
        return "Generic Task"


# _______________________________________________________________________
