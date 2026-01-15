#!/usr/bin/env python3
"""
editX - A Simple Text Editor
A feature-rich text editor built with Python and tkinter
"""

import tkinter as tk
from tkinter import filedialog, messagebox, font
import os


class EditX:
    """Main text editor class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("editX - Untitled")
        self.root.geometry("800x600")
        
        self.current_file = None
        self.is_modified = False
        
        # Create text widget with scrollbar
        self.create_text_area()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
        
        # Track modifications
        self.text_area.bind('<<Modified>>', self.on_text_modified)
        
        # Set up protocol for window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_text_area(self):
        """Create the main text editing area with scrollbar"""
        # Frame to hold text area and scrollbar
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text area
        self.text_area = tk.Text(
            text_frame,
            wrap=tk.WORD,
            undo=True,
            maxundo=-1,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 11)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        scrollbar.config(command=self.text_area.yview)
        
        # Add line numbers support (optional)
        self.text_area.focus_set()
    
    def create_menu_bar(self):
        """Create the menu bar with File, Edit, and Help menus"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing, accelerator="Alt+F4")
        
        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        edit_menu.add_command(label="Find", command=self.find_text, accelerator="Ctrl+F")
        
        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_file_as())
        self.root.bind('<Control-z>', lambda e: self.undo())
        self.root.bind('<Control-y>', lambda e: self.redo())
        self.root.bind('<Control-x>', lambda e: self.cut())
        self.root.bind('<Control-c>', lambda e: self.copy())
        self.root.bind('<Control-v>', lambda e: self.paste())
        self.root.bind('<Control-a>', lambda e: self.select_all())
        self.root.bind('<Control-f>', lambda e: self.find_text())
    
    def on_text_modified(self, event=None):
        """Handle text modification events"""
        if self.text_area.edit_modified():
            self.is_modified = True
            self.update_title()
            self.text_area.edit_modified(False)
    
    def update_title(self):
        """Update window title to show current file and modification status"""
        title = "editX - "
        if self.current_file:
            title += os.path.basename(self.current_file)
        else:
            title += "Untitled"
        
        if self.is_modified:
            title += " *"
        
        self.root.title(title)
    
    def new_file(self):
        """Create a new file"""
        if self.is_modified:
            if not self.ask_save_changes():
                return
        
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.is_modified = False
        self.update_title()
    
    def open_file(self):
        """Open an existing file"""
        if self.is_modified:
            if not self.ask_save_changes():
                return
        
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                self.current_file = file_path
                self.is_modified = False
                self.update_title()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
    
    def save_file(self):
        """Save the current file"""
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                self.is_modified = False
                self.update_title()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
                return False
        else:
            return self.save_file_as()
    
    def save_file_as(self):
        """Save the current file with a new name"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                self.current_file = file_path
                self.is_modified = False
                self.update_title()
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{str(e)}")
                return False
        
        return False
    
    def ask_save_changes(self):
        """Ask user if they want to save changes before closing/creating new"""
        response = messagebox.askyesnocancel(
            "Save Changes?",
            "Do you want to save changes to the current document?"
        )
        
        if response is True:  # Yes
            return self.save_file()
        elif response is False:  # No
            return True
        else:  # Cancel
            return False
    
    def undo(self):
        """Undo the last action"""
        try:
            self.text_area.edit_undo()
        except tk.TclError:
            pass
    
    def redo(self):
        """Redo the last undone action"""
        try:
            self.text_area.edit_redo()
        except tk.TclError:
            pass
    
    def cut(self):
        """Cut selected text"""
        try:
            self.text_area.event_generate("<<Cut>>")
        except tk.TclError:
            pass
    
    def copy(self):
        """Copy selected text"""
        try:
            self.text_area.event_generate("<<Copy>>")
        except tk.TclError:
            pass
    
    def paste(self):
        """Paste text from clipboard"""
        try:
            self.text_area.event_generate("<<Paste>>")
        except tk.TclError:
            pass
    
    def select_all(self):
        """Select all text"""
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return 'break'
    
    def find_text(self):
        """Open find dialog"""
        find_window = tk.Toplevel(self.root)
        find_window.title("Find")
        find_window.geometry("350x100")
        find_window.resizable(False, False)
        
        tk.Label(find_window, text="Find:").grid(row=0, column=0, padx=10, pady=10)
        search_entry = tk.Entry(find_window, width=30)
        search_entry.grid(row=0, column=1, padx=10, pady=10)
        search_entry.focus_set()
        
        def do_find():
            search_term = search_entry.get()
            if search_term:
                start_pos = self.text_area.search(search_term, "1.0", tk.END)
                if start_pos:
                    end_pos = f"{start_pos}+{len(search_term)}c"
                    self.text_area.tag_remove(tk.SEL, "1.0", tk.END)
                    self.text_area.tag_add(tk.SEL, start_pos, end_pos)
                    self.text_area.mark_set(tk.INSERT, end_pos)
                    self.text_area.see(start_pos)
                else:
                    messagebox.showinfo("Find", "Text not found")
        
        tk.Button(find_window, text="Find", command=do_find).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(find_window, text="Close", command=find_window.destroy).grid(row=1, column=2, padx=10, pady=10)
        
        search_entry.bind('<Return>', lambda e: do_find())
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About editX",
            "editX - A Simple Text Editor\n\n"
            "Version 1.0\n\n"
            "A feature-rich text editor built with Python and tkinter.\n\n"
            "Features:\n"
            "- Create, open, and save text files\n"
            "- Cut, copy, paste operations\n"
            "- Undo/Redo support\n"
            "- Find text functionality\n"
            "- Keyboard shortcuts"
        )
    
    def on_closing(self):
        """Handle window closing event"""
        if self.is_modified:
            if self.ask_save_changes():
                self.root.destroy()
        else:
            self.root.destroy()


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = EditX(root)
    root.mainloop()


if __name__ == "__main__":
    main()
