# Note Taking App (README for Backend)


## Overview
The Note Taking App is a Python application designed to manage notes stored in text files. It includes features such as **creating new note files**, **adding notes to existing files**, **deleting files**, **printing notes from file**, and **searching notes within files**.


## Getting Started
To get started with the Note Taking App, follow these steps:

1. **Clone the repository:**  https://github.com/jojordan24/project-1.1.git 
2. **Navigate to the backend directory**
3. **Run the application**


## Dependencies
The backend application has no external dependencies beyond the Python standard library.


## Project Structure
The project structure is:  
Note-Taking-App/  
├──notes.py  
├──backend.py - Main Python code containing the application logic.  
└── README.md - The README file.

## Features
- **Create New File:**  Create a new text file for storing notes.
- **Delete File:**  Delete an existing text file.
- **Add Note to File:**  Append a note with timestamp to an existing text file.
- **Print Notes from File:**  Display all notes stored in a specified text file.
- **Search Notes in File:**  Search for specific notes within a text file.


## Contributing
Contributions are welcome! If you'd like to contribute to Note Taking App, feel free to fork the repository, make your changes, and submit a pull request.

# Commands

## Initialization

To start using the `NoteManager`, initialize it with the path to the directory where notes will be managed:
`notes_manager = backends_comb.NoteManager("notes_directory")`

## Command Reference

Below is a list of commands supported by the system for managing notes and folders.

### `note`

- **Function**: Create a quick note.
- **Details**: Allows the creation of a new note file. If desired, the note can be password-protected.

### `delete`

- **Function**: Delete a file.
- **Details**: Deletes the specified note file from the current folder.

### `add`

- **Function**: Add a note to a file.
- **Details**: Adds a new note to an existing file, with optional password protection.

### `print`

- **Function**: Print notes from a file.
- **Details**: Outputs the contents of the specified note file, supporting password-protected files.

### `search`

- **Function**: Print all notes from a file.
- **Details**: Searches within a file for notes containing the specified terms, supporting password-protected files.

### `newf`

- **Function**: Create a new folder.
- **Details**: Creates a new folder for organizing notes within the specified directory.

### `change`

- **Function**: Switch current folder.
- **Details**: Changes the current working directory to another folder within the specified notes directory.

### `deletef`

- **Function**: Delete a folder.
- **Details**: Deletes the specified folder along with all its contents.

### `help`

- **Function**: Print this help.
- **Details**: Displays a list of available commands and their descriptions.

### `quit`

- **Function**: Exit the program.
- **Details**: Terminates the program.

## Usage

To use these commands, run the `main` function and enter the desired command followed by the necessary information as prompted. The system supports creating, modifying, and managing notes and folders in a user-specified directory.





