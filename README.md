# PY-editX

This project contains a text editor implementation.

## EditX - A Minimal Text Editor in C

EditX is a lightweight, terminal-based text editor written in C, inspired by vim and nano.

### Features

- **File Operations**: Open, edit, and save text files
- **Navigation**: Arrow keys, Home, End, Page Up/Down
- **Editing**: Insert text, delete characters, newlines
- **Status Bar**: Shows filename, line count, and modification status
- **Keyboard Shortcuts**:
  - `Ctrl-S`: Save file
  - `Ctrl-Q`: Quit (warns if unsaved changes)
  - Arrow keys: Navigate cursor
  - Backspace/Delete: Remove characters
  - Enter: Insert newline

### Building

```bash
make
```

### Usage

```bash
# Open an existing file
./editor filename.txt

# Create a new file
./editor
```

### Requirements

- GCC compiler
- POSIX-compliant system (Linux, macOS, etc.)
- Terminal with ANSI escape sequence support
