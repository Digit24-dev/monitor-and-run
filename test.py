import tkinter as tk

# Simple Test GUI

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Test GUI")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 14))
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the application
root.mainloop()
