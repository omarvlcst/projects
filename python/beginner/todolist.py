tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"The task named '{task}' has been added to your list of tasks")

def listTasks():
    if not tasks:
        print("Currently, there are no tasks added to the list")
    else:
        print("Current Tasks available:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def removeTask():
    listTasks()
    try:
        taskToRemove = int(input("Select a number from the list of tasks to pick a task to be removed: "))
        if taskToRemove >=0 and taskToRemove < len(tasks):
            tasks.pop(taskToRemove)
            print(f"Task #{taskToRemove} was removed successfully")
        else:
            print(f"Task #{taskToRemove} was not found")
    except:
        print("Invalid input")

if __name__== "__main__":
    ### Create a loop to run the app
    print("\n")
    print("To Do List app: WELCOME!")
    while True:
        print("\n")
        print("Please select one task of the following:")
        print("----------------------------------------")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. List tasks")
        print("4. Quit")

        selection = input("Enter your choice for a task: ")
        if selection =="1":
            addTask()
        elif selection=="2":
            removeTask()
        elif selection=="3":
            listTasks()
        elif selection=="4":
            break
        else:
            print("Invalid input, please try again")
    print("See you later")
