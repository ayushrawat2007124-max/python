'''5.	Design a login and signup authentication system.
'''
import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# ---------------- HASH FUNCTION ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- SIGNUP FUNCTION ----------------
def signup():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hash_password(password)))
        conn.commit()
        messagebox.showinfo("Success", "Account created successfully!")
    except:
        messagebox.showerror("Error", "Username already exists!")

# ---------------- LOGIN FUNCTION ----------------
def login():
    username = entry_user.get()
    password = hash_password(entry_pass.get())

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("350x300")

tk.Label(root, text="Authentication System", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Signup", command=signup, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Login", command=login, bg="green", fg="white").pack(pady=5)

root.mainloop()

conn.close()