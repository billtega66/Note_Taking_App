## Note Taking App

### Introduction
This project is a Flash Card and Note Management System developed using Python and Flask. It allows users to create, manage, and study flashcards, as well as organize and maintain notes effectively.

### Features
1. **Flash Card Management**:
    - Create flashcards by providing questions and answers.
    - Test yourself by going through the flashcards and checking your answers.
    - Remove flashcards from the pile once you've answered them correctly.

2. **Note Management**:
    - Create and manage text notes.
    - Add, delete, and search notes easily.
    - Organize notes into folders for better categorization.

3. **Checklist Management**:
    - Create and manage checklists within notes.
    - Add, check, uncheck, and delete checklist items.
    - Display the checklist to view all items.

4. **File Transfer**:
    - Transfer files from one folder to another within the system.

5. **File Upload**:
    - Upload photos to the system.

### Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python filename.py`.
4. Access the application through the specified port (usually `http://localhost:5000/`) in your web browser.

### Usage
1. **Flash Card Management**:
    - Use the `/create_cards` endpoint to create flashcards.
    - Use the `/test_cards` endpoint to test yourself with the flashcards.

2. **Note Management**:
    - Use the `/notes/add` endpoint to add new notes.
    - Use the `/notes/print` endpoint to view notes.
    - Use the `/notes/delete` endpoint to delete notes.
    - Use the `/notes/search` endpoint to search for specific notes.

3. **Checklist Management**:
    - Use the `/checklist/add` endpoint to add checklist items.
    - Use the `/checklist/check` endpoint to check checklist items.
    - Use the `/checklist/uncheck` endpoint to uncheck checklist items.
    - Use the `/checklist/display` endpoint to display the checklist.
    - Use the `/checklist/delete` endpoint to delete checklist items.

4. **File Transfer**:
    - Use the `/transfer` endpoint to transfer files between folders.

5. **File Upload**:
    - Use the `/upload/photo` endpoint to upload photos to the system.

### Contributions
Contributions to this project are welcome. Feel free to fork the repository, make changes, and submit pull requests.

### License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per your requirements.
