import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.longer_button = tk.Button(self, text="Longer", command=self.goto_longer_page)
        self.longer_button.pack()

        self.equal_button = tk.Button(self, text="Equal", command=self.goto_equal_page)
        self.equal_button.pack()

        self.shorter_button = tk.Button(self, text="Shorter", command=self.goto_shorter_page)
        self.shorter_button.pack()

    def goto_longer_page(self):
        self.pack_forget()
        LongerPage(self.master)

    def goto_equal_page(self):
        self.pack_forget()
        EqualPage(self.master)

    def goto_shorter_page(self):
        self.pack_forget()
        ShorterPage(self.master)

class LongerPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.return_button = tk.Button(self, text="Return", command=self.goto_main_page, bg="black", fg="white")
        self.label = tk.Label(self, text="You are in Longer Page", bg="black", fg="white")
        self.return_button.pack()

        self.label = tk.Label(self, text="You are in Longer Page", bg="black", fg="white")
        self.label.pack()

    def goto_main_page(self):
        self.pack_forget()
        MainPage(self.master)

class EqualPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.return_button = tk.Button(self, text="Return", command=self.goto_main_page)
        self.return_button.pack()

        self.label = tk.Label(self, text="You are in Equal Page")
        self.label.pack()

    def goto_main_page(self):
        self.pack_forget()
        MainPage(self.master)

class ShorterPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.return_button = tk.Button(self, text="Return", command=self.goto_main_page)
        self.return_button.pack()

        self.label = tk.Label(self, text="You are in Shorter Page")
        self.label.pack()

    def goto_main_page(self):
        self.pack_forget()
        MainPage(self.master)

#宣告 顯示show
root = tk.Tk()
root.configure(bg='black')
main_page = MainPage(root)
main_page.mainloop()


import tkinter as tk
from tkinter import filedialog

def select_source_folder():
    source_path.set(filedialog.askdirectory())

def select_target_folder():
    target_path.set(filedialog.askdirectory())

def button1_click():
    print("Button 1 clicked")
    
root = tk.Tk()

# Create source folder input field
tk.Label(root, text="Source Folder").grid(row=0, column=0)
source_path = tk.StringVar()
tk.Entry(root, textvariable=source_path).grid(row=0, column=1)
tk.Button(root, text="Select Folder", command=select_source_folder).grid(row=0, column=2)

# Create target folder input field
tk.Label(root, text="Target Folder").grid(row=1, column=0)
target_path = tk.StringVar()
tk.Entry(root, textvariable=target_path).grid(row=1, column=1)
tk.Button(root, text="Select Folder", command=select_target_folder).grid(row=1, column=2)

# Create confirm button
tk.Button(root, text="Confirm", command=button1_click).grid(row=2, column=1)


root.mainloop()

