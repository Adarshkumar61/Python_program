# tasks = []
# def addtask(task):
#     tasks.append(task)
# def removetask(tasknumber):
#     try:
#         del tasks[tasknumber - 1]
#     except IndexError:
#         print("Invalid Task number...")
# def viewtask():
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}.{tasks}")
# while True:
#     print("1. Add Task")
#     print("2. Rmove Task")
#     print("3. View Task")
#     print("4. quit...")
#     choice = input("Enter your choice: ")
#     if choice == "add task":
#         task = input("Enter a task: ")
#     elif choice == "remove task":
#         tasknumber = input("enter the task number to remove: ")
#         remove(tasknumber)
#     elif choice == "view":
#         viewtask()
#     elif choice == "quit":
#         break
#     else:
#         print("Invalid option please enter valid option!..")
tasks = []
def addtask(task):
    tasks.append(task)
def remove(tasknumber):
    try:
        del tasks[tasknumber-1]
    except IndexError:
        print("invalid Task number!")
        
def viewtask():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.{tasks}")
while True:
    print("\n1.Add Task")
    print("2.Remove Tasks")
    print("3.View tasks")
    print("4.Quit")
    choice = input("Choose an option(1, 2, 3, 4): ")
    if choice == "1":
        task = input("Enter a task: ")
        addtask(task)
    elif choice == "2":
        tasknumber = int(input("Enter the Task number to remove: "))
        remove(tasknumber)
    elif choice == "3":
        viewtask()
    elif choice == "4":
        break
    else:
        print("Invalid choice. please choose again")