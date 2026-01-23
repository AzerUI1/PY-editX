


<h1 align="center"> Simple Python Text Editor (Tkinter)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Author-Azer%20Aslanov-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topic-Text%20Editor-000000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-FFDD00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p align="center">
  <b>A clean, minimal, beginner-friendly graphical text editor written in pure Python using Tkinter.</b>
</p>

---

## Features
- Open text files
- Edit text with a clean UI
- Save
- Save As
- UTF-8 file support
- No external dependencies

---

## Project Structure

Your repo should look like this:

```

 Simple-Python-Text-Editor
┣ text_editor.py
┣ text_editor.1
┣ README.md
┣ LICENSE
┗ .gitignore

````

---

## Python Script (Main)

File: `text_editor.py`

```python
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
````

---

## How to Run

Inside your repo:

```bash
python text_editor.py
```

---

## License

This project is licensed under the BSD-3-Clause license License — see the LICENSE file for details.

---

## Support the Project

If you like this project, please star the repo.

---

## Connect With Me

<p align="left">
  <a href="https://github.com/AzerU11">
    <img src="https://img.shields.io/badge/GitHub-AzerU11-000000?style=for-the-badge&logo=github" />
  </a>
</p>
