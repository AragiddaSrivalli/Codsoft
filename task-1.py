# To-Do List Application

# List to store tasks
todo_list = []

# Function to display menu options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for idx, item in enumerate(todo_list, 1):
            status = "Completed" if item["completed"] else "Pending"
            print(f"{idx}. {item['task']} - {status}")

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]["completed"] = True
                print(f"Task {task_num} marked as completed.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Main loop for the application
def todo_list_app():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the To-Do List application
todo_list_app()
