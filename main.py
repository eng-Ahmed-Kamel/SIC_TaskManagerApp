import json
from Task_manager import Task_manager
from Task import Task
from Work_task import Work_task
from Personal_task import Personal_task

# object make
task_manager = Task_manager()
def Statues_change(statues):
    if statues == "incomplete" or statues == "complete" or statues == "inprogress":
        return True
    else:
        return False

# function to save to data and update
def save():
    jsondata = [obj.to_dic() for obj in task_manager.tasks]
    data = open("p3.json", "w")
    json.dump(jsondata, data, indent=2)
    data.close()

# try and except to cover error of file not found and create
try:
    data = open("p3.json")
    the_data = json.load(data)
    data.close()
    list = []
    for dic in the_data:
        if "task_category" in dic:
            list.append(
                Personal_task(dic["title"], dic["description"], dic["due_date"], dic["status"], dic["task_category"]))
        elif "task_priority" in dic:
            list.append(
                Work_task(dic["title"], dic["description"], dic["due_date"], dic["status"], dic["task_priority"]))
    task_manager.tasks = list
# to force to create file
except FileNotFoundError:
    save()

# ////////////////////////////////////
# start of the code in while loop
while True:
    ## try and except to cover error of value error and try again
    try:
        x = int(input(
            "please enter :\n[1] to add task\n[2] to remove task\n[3] to update task\n[4] to view task\n[5] to Exit\n"))
    except ValueError:
        print('please enter a valid number')
        continue
    if x == 5:
        break
    elif x == 1:  # add part
        while True:
            # try and except to cover error of value error and try again
            try:
                y = int(input("please enter :\n[1] to add work task\n[2] to add personal task\n[0] to back\n"))
                break
            except ValueError:
                print('please enter a valid number')
                continue
        if y == 0:
            continue
        title = input("please enter the title you want to add: ")
        while task_manager.is_title_exist(title):
            print("error occur title is duplicated enter another name")
            title = input("please enter the title you want to add: ")
        description = input("please enter the description you want to add: ")
        due_date = input("please enter the due date you want to add: ")
        statues = "incomplete"
        while not Statues_change(statues):
            print("enter valid statues:(complete,incomplete,inprogress)")
            statues = input("please enter the statues you want to add: ")
        if y == 2:
            task_category = input("please enter the task_category: ")
            # object creation of personal task
            t = Personal_task(title, description, due_date, statues, task_category)
            if task_manager.create(t):
                print("added task successfully")
                save()
        elif y == 1:
            task_priority = input("please enter the task_priority: ")
            # object creation of personal task
            t = Work_task(title, description, due_date, statues, task_priority)
            if task_manager.create(t):
                print("added task successfully")
                save()
    elif x == 2:  # delete part
        # access by task title
        title = input("please enter the title you want to remove: ")
        if task_manager.delete(title):
            print("deleted successfully")
            save()
        else:
            print("title didn't exist")
    elif x == 3:  # update part to change due_date & status & or any attribute
        while True:
            # access by task title
            title = input("please enter the task title you want to update: ")
            attribute = input(
                "please enter what you want to update (title,description,due_date,status): ")
            if attribute != "status":
                change = input("enter the new data: ")
                task_manager.update(title, [attribute, change])
                print("updated successfully")
                save()
                break
            while attribute == "status":
                change = input("enter the new data(complete,incomplete,inprogress): ")
                if Statues_change(change):
                    task_manager.update(title, [attribute, change])
                    save()
                    break
                else:
                    print("operation not done wrong input")
            print("updated successfully")
            break

    elif x == 4:  # view part
        task_manager.view()
    else:
        print('please enter a valid number')