''' 2.	Design a GUI based basic calculator for performing basic arithmetic operations.
'''
import tkinter as tk

# Function to handle button clicks
def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear input
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for btn in buttons:
    button = tk.Button(frame, text=btn, font=("Arial", 15), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

    if btn == "=":
        button.bind("<Button-1>", lambda e: calculate())
    else:
        button.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 15), command=clear)
clear_btn.pack(fill=tk.BOTH, padx=10, pady=5)

# Run app
root.mainloop() 