import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        text.delete(1.0, tk.END)
        text.insert(1.0, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(filepath, 'w') as file:
        file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root, height=30, width=60)
text.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
