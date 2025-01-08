# Print todo list activity
print("--my todo list for today--");
print("1. go to school");
print("2. attend classes");
print("3. take a brealk and eat");
print("4. attend 2-4 classes");
print("5. go home.")

# Simple To-Do List in Python

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['task']} [{status}]")
