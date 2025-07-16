#ToDoList by Sankalp Mishra!!

import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter your new task: ")
    if task.strip() == "":
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "done": False})
    print(f"Added task: '{task}'")

def update_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter the task number to update: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid task number.")
            return
        new_task = input("Enter the new description: ")
        if new_task.strip() == "":
            print("Task cannot be empty.")
            return
        tasks[idx]["task"] = new_task
        print("Task updated.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter the task number to mark as done: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid task number.")
            return
        tasks[idx]["done"] = True
        print(f"Task '{tasks[idx]['task']}' marked as done!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter the task number to delete: ")) - 1
        if idx < 0 or idx >= len(tasks):
            print("Invalid task number.")
            return
        removed = tasks.pop(idx)
        print(f"Deleted task: '{removed['task']}'")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to Sankalp's To-Do List!")
    tasks = load_tasks()
    while True:
        print("\nChoose an option:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "5":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "6":
            print("Goodbye! Keep crushing your goals")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()