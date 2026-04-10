'''4.	Create a GUI based task manager where users can add,
 edit and remove tasks. Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).'''
import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]}: {row[1]}")

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return

    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

def delete_task():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showerror("Error", "No task selected!")
        return

    task_id = selected.split(":")[0]
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    load_tasks()

def edit_task():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showerror("Error", "Select a task to edit!")
        return

    task_id = selected.split(":")[0]
    new_task = entry.get()

    if new_task == "":
        messagebox.showerror("Error", "Enter new task!")
        return

    cursor.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

tk.Label(root, text="Task Manager", font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Edit Task", command=edit_task, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white").pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Load existing tasks
load_tasks()

# Run app
root.mainloop()

conn.close() 