import tkinter as tk
from tkinter import ttk

#只是一個UI介面

def dropdown_selected(event):
    print("Selected item:", event.widget.get())

root = tk.Tk()

# Create the dropdown
dropdown_values = ["Item 1", "Item 2", "Item 3"]
dropdown_var = tk.StringVar(root)
dropdown = ttk.Combobox(root, textvariable=dropdown_var, values=dropdown_values)
dropdown.bind("<<ComboboxSelected>>", dropdown_selected)
dropdown.pack()

root.mainloop()
