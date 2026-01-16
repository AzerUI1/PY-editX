# EditX Text Editor - MVP Implementation

## Overview
EditX is a minimal, terminal-based text editor written in C, providing essential text editing capabilities in approximately 600 lines of code.

## Build Instructions
```bash
make
```

This will produce an executable named `editor`.

## Usage
```bash
# Open an existing file
./editor filename.txt

# Start with an empty buffer
./editor
```

## Keyboard Shortcuts
- **Ctrl-S**: Save file
- **Ctrl-Q**: Quit editor
  - If file has unsaved changes, press Ctrl-Q twice to confirm
- **Arrow Keys**: Move cursor
- **Home**: Move to beginning of line
- **End**: Move to end of line
- **Page Up/Down**: Scroll by page
- **Enter**: Insert newline
- **Backspace**: Delete character before cursor
- **Delete**: Delete character at cursor

## Features
1. **File I/O**
   - Open existing files
   - Save modifications
   - Create new files
   - Unsaved changes warning

2. **Text Editing**
   - Insert/delete characters
   - Insert/delete lines
   - Full cursor navigation

3. **User Interface**
   - Status bar showing filename, line count, modification status
   - Message bar for feedback and help
   - Welcome screen for new files

4. **Memory Safety**
   - Comprehensive error handling for memory allocations
   - No memory leaks on allocation failures
   - Graceful degradation on errors

## Technical Details
- Written in ANSI C (C99 standard)
- Uses raw terminal mode for keyboard input
- ANSI escape sequences for screen control
- POSIX-compliant (Linux, macOS, BSD)

## Code Structure
- Terminal handling: Raw mode setup, key reading
- Row operations: Text storage and manipulation
- Editor operations: High-level editing commands
- File I/O: Loading and saving files
- Output: Screen rendering and status display
- Input: Keyboard event processing

## Security Considerations
- All memory allocations are checked for failures
- Buffer operations use safe functions (memcpy, memmove)
- Proper bounds checking on array accesses
- No hardcoded limits on file size

## Limitations
This is an MVP (Minimum Viable Product) and has intentional limitations:
- No syntax highlighting
- No search/replace functionality
- No undo/redo
- No multiple file buffers
- ASCII/UTF-8 text only
- Requires ANSI terminal support

## Future Enhancements
Potential improvements for future versions:
- Syntax highlighting
- Search and replace
- Undo/redo functionality
- Line numbers
- Multiple buffers/tabs
- Configuration file support
