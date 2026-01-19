import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Demo Text Editor")
root.geometry("700x500")

text = tk.Text(root, font=("Consolas", 12))
text.pack(expand=True, fill="both")


def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        text.delete(1.0, tk.END)
        with open(file, "r", encoding="utf-8") as f:
            text.insert(tk.END, f.read())


def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, tk.END))


frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Open", command=open_file).pack(side="left", padx=5)
tk.Button(frame, text="Save", command=save_file).pack(side="left", padx=5)

root.mainloop()
