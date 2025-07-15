#ToDoList (GUI) by Sankalp Mishra!!

import tkinter as tk
from tkinter import messagebox, simpledialog
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

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App by Sankalp Mishra!")
        self.tasks = load_tasks()
        self.create_widgets()
        self.refresh_listbox()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=40, selectmode=tk.SINGLE)
        self.listbox.pack()

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(fill=tk.X)

        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.pack(fill=tk.X)

        self.done_button = tk.Button(self.frame, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(fill=tk.X)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(fill=tk.X)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        if not self.tasks:
            self.listbox.insert(tk.END, "Your to-do list is empty!")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task["done"] else "❌"
            self.listbox.insert(tk.END, f"{idx}. {task['task']} [{status}]")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter your new task:")
        if task and task.strip():
            self.tasks.append({"task": task.strip(), "done": False})
            save_tasks(self.tasks)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        sel = self.listbox.curselection()
        if not sel or not self.tasks:
            messagebox.showwarning("Warning", "Please select a task to update.")
            return
        idx = sel[0]
        new_task = simpledialog.askstring("Update Task", "Enter the new description:")
        if new_task and new_task.strip():
            self.tasks[idx]["task"] = new_task.strip()
            save_tasks(self.tasks)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def mark_done(self):
        sel = self.listbox.curselection()
        if not sel or not self.tasks:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")
            return
        idx = sel[0]
        self.tasks[idx]["done"] = True
        save_tasks(self.tasks)
        self.refresh_listbox()
        messagebox.showinfo("Success", f"Task '{self.tasks[idx]['task']}' marked as done! 🎉")

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel or not self.tasks:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        idx = sel[0]
        confirm = messagebox.askyesno("Delete Task", f"Delete '{self.tasks[idx]['task']}'?")
        if confirm:
            del self.tasks[idx]
            save_tasks(self.tasks)
            self.refresh_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()