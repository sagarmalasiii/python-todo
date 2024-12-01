import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task(task):
    tasks.append({"task": task, "completed": False})

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display!")
    else:
        print("\n=== TO DO LIST ===")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} [{status}]")

# Delete a task
def delete_task(task_no):
    index = task_no - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print(f"Task {task_no} deleted successfully!")
    else:
        print("Invalid task number!")

# Mark a task as complete
def mark_task_complete(task_no):
    index = task_no - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task {task_no} marked as completed!")
    else:
        print("Invalid task number!")

# Display the menu
def display_menu():
    print("\n...TO DO List...")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

# Main program
tasks = load_tasks()

while True:
    display_menu()
    try:
        user_input = int(input("> "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if user_input == 1:
        task = input("Enter your task: ")
        add_task(task)
        print("Task added successfully!")
    elif user_input == 2:
        view_tasks()
    elif user_input == 3:
        if tasks:
            view_tasks()
            try:
                task_no = int(input("Enter Task No to delete: "))
                delete_task(task_no)
            except ValueError:
                print("Invalid input! Please enter a number.")
        else:
            print("No tasks to delete!")
    elif user_input == 4:
        if tasks:
            view_tasks()
            try:
                task_no = int(input("Enter Task No to mark as complete: "))
                mark_task_complete(task_no)
            except ValueError:
                print("Invalid input! Please enter a number.")
        else:
            print("No tasks to mark as complete!")
    elif user_input == 5:
        save_tasks()
        print("Tasks saved. Exiting program. Goodbye!")
        break
    else:
        print("Invalid Option! Please select a valid option.")
