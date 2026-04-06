''' create a simple tkinter window with a title and fixed size '''
import tkinter as tk

# Create the main window
window = tk.Tk()

# Set window title
window.title("My Tkinter Window")

# Set fixed window size (width x height)
window.geometry("400x300")

# Disable resizing (optional, to keep size fixed)
window.resizable(False, False)

# Run the application
window.mainloop()