import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_special = special_var.get()

    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Apply some styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TCheckbutton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# Create and place widgets
ttk.Label(root, text="Password Length:", style="TLabel").grid(row=0, column=0, padx=10, pady=10, sticky="w")
length_entry = ttk.Entry(root, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
length_entry.insert(0, "12")  # Default length

special_var = tk.BooleanVar()
special_check = ttk.Checkbutton(root, text="Include Special Characters", variable=special_var, style="TCheckbutton")
special_check.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

generate_button = ttk.Button(root, text="Generate Password", command=generate_password, style="TButton")
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(root, text="Generated Password:", style="TLabel").grid(row=3, column=0, padx=10, pady=10, sticky="w")
password_entry = ttk.Entry(root, width=40, font=("Helvetica", 12))
password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Apply padding and configure grid
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Set a minimum size for the window
root.minsize(400, 200)

# Run the application
root.mainloop()