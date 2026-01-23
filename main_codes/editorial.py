# Simple Text Editor in Python (Tkinter)
# file: text_editor.py

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        text.delete("1.0", tk.END)
        with open(file_path, "r", encoding="utf-8") as f:
            text.insert(tk.END, f.read())

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
