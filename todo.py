import sys
import json
import os

tasks_file = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as file:
            tasks = json.load(file)

def save_tasks():
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file)

def show_menu():
    print("\nTo-Do List Application")
    print("=======================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Reorder Tasks")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    save_tasks()
    print("Task added!")

def update_task():
    view_tasks()
    if tasks:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_num - 1] = new_task
            save_tasks()
            print("Task updated!")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if tasks:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task number.")

def reorder_tasks():
    view_tasks()
    if tasks:
        task_num = int(input("\nEnter the task number to move: "))
        if 1 <= task_num <= len(tasks):
            direction = input("Enter 'up' to move up or 'down' to move down: ").strip().lower()
            if direction == 'up' and task_num > 1:
                tasks[task_num - 1], tasks[task_num - 2] = tasks[task_num - 2], tasks[task_num - 1]
                save_tasks()
                print("Task moved up!")
            elif direction == 'down' and task_num < len(tasks):
                tasks[task_num - 1], tasks[task_num] = tasks[task_num], tasks[task_num - 1]
                save_tasks()
                print("Task moved down!")
            else:
                print("Invalid move. The task is already at the boundary.")
        else:
            print("Invalid task number.")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            reorder_tasks()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
