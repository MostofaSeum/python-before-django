import os
def add_first_task():
    task = input("Enter the task : ")
    with open("todos.txt","w") as f:
        f.write(task)

def add_task():
    task = input("Enter the task : ")
    with open("todos.txt","a") as f:
        f.write(", "+task)

def view_all_tasks():
    with open("todos.txt","r") as f:
        print(f.read())

def delete_task():
    delete = input("Enter the task to delete : ")
    with open("todos.txt","r") as f:
        data = f.read()
    tasks = [task.strip() for task in data.split(",") if task.strip()]
    if delete in tasks:
        tasks.remove(delete)
        new_data = ", ".join(tasks)
        with open("todos.txt","w") as f:
            f.write(new_data)
            print("Task has been deleted")
    else:
        print("Task not found")

while True:
    print("\n Todo Menu ")
    print("1. View Data")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == "1":
        if os.path.exists("todos.txt"):
            view_all_tasks()
        else:
            print("Error: 'todos.txt' file not found. Please add a task first to create it.")
    elif choice == "2":
        if not os.path.exists("todos.txt") or os.path.getsize("todos.txt") == 0:
            add_first_task()
        else:
            add_task()
    elif choice == "3":
        if os.path.exists("todos.txt"):
            delete_task()
        else:
            print("Error: 'todos.txt' file not found. Please add a task first to create it.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select between 1 and 4.")