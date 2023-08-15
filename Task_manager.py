class Task_manager:  # class creation
    # attributes
    def __init__(self):
        self.tasks = []

    # methods
    # 1st method to check if title is found before to handle errors
    def is_title_exist(self, title):
        for task in self.tasks:
            if task.title == title:
                return True
        return False

    # 2nd method to create task
    def create(self, added_task):
        self.tasks.append(added_task)
        return True

    # 3rd method to view tasks you have
    def view(self):
        if len(self.tasks) == 0:
            print("No tasks found")
        for x in self.tasks:
            x.display()
            print("")

    # 4th method to delete task you want
    def delete(self, title):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                self.tasks.remove(self.tasks[i])
                return True
        return False

    # 5th method to update task data
    def update(self, title, change):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                if change[0] == "title":
                    if self.is_title_exist(change[1]):
                        print("title exist")
                        return False
                    self.tasks[i].title = change[1]
                    return True
                elif change[0] == "description":
                    self.tasks[i].description = change[1]
                    return True
                elif change[0] == "due_date":
                    self.tasks[i].due_date = change[1]
                    return True
                elif change[0] == "status":
                    self.tasks[i].status = change[1]
                    return True
                else:
                    print("enter a valid attribute")
                    return False
        print("title doesnt exist")
        return False

