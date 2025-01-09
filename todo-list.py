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
            def add_task():
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "done": False})
    print(f"Task '{task_name}' added!")

def mark_done():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['done'] = True
                print(f"Task {task_number} marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
# Main program loop
while True:
    show_menu()
    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            view_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")
