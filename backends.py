# import os
# import datetime

# class NoteManager:
#     def __init__(self, notes_directory):
#         # self.notes_directory = "C:\\Users\\Kien Quoc\\Documents\\GitHub\\1project-1.1"
#         self.notes_directory = notes_directory


#     def get_file_path(self, file_name):
#         return os.path.join(self.notes_directory, file_name)

#     def create_new_file(self, file_name):
#         if not file_name.endswith('.txt'):
#             file_name += '.txt'
#         file_path = self.get_file_path(file_name)
#         with open(file_path, 'w') as file:
#             print(f"New file '{file_name}' created.")

#     def delete_file(self, file_name):
#         if not file_name.endswith('.txt'):
#             file_name += '.txt'
#         file_path = self.get_file_path(file_name)
#         try:
#             os.remove(file_path)
#             print(f"File '{file_name}' deleted successfully.")
#         except FileNotFoundError:
#             print(f"File '{file_name}' does not exist.")

#     def add_note_to_file(self, file_name, note):
#         if not file_name.endswith('.txt'):
#             file_name += '.txt'
#         file_path = self.get_file_path(file_name)
#         with open(file_path, 'a') as file:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             file.write(f"{timestamp} - {note}\n")
#         print("Note added successfully.")

#     def print_notes_from_file(self, file_name):
#         if not file_name.endswith('.txt'):
#             file_name += '.txt'
#         file_path = self.get_file_path(file_name)
#         try:
#             with open(file_path, 'r') as file:
#                 print(f"Notes from '{file_name}':")
#                 print(file.read())
#         except FileNotFoundError:
#             print(f"File '{file_name}' does not exist.")

#     def search_notes_in_file(self, file_name, search_term):
#         if not file_name.endswith('.txt'):
#             file_name += '.txt'
#         file_path = self.get_file_path(file_name)
#         try:
#             with open(file_path, 'r') as file:
#                 print(f"Search results in '{file_name}':")
#                 found = False
#                 for line in file:
#                     if search_term in line:
#                         print(line.strip())
#                         found = True
#                 if not found:
#                     print("No matching notes found.")
#         except FileNotFoundError:
#             print(f"File '{file_name}' does not exist.")

#     def main(self):
#         print("Welcome to the Note Manager App!")
#         while True:
#             print("\nOptions:")
#             print("1. Create a new file")
#             print("2. Delete a file")
#             print("3. Add a note to a file")
#             print("4. Print notes from a file")
#             print("5. Search notes from a file")
#             print("6. Exit")
#             choice = input("Enter your choice (1-6): ")
#             if choice == '1':
#                 file_name = input("Enter the name of the new file: ")
#                 self.create_new_file(file_name)
#             elif choice == '2':
#                 file_name = input("Enter the name of the file to delete: ")
#                 self.delete_file(file_name)
#             elif choice == '3':
#                 file_name = input("Enter the name of the file to add note to: ")
#                 note = input("Enter your note: ")
#                 self.add_note_to_file(file_name, note)
#             elif choice == '4':
#                 file_name = input("Enter the name of the file to print notes from: ")
#                 self.print_notes_from_file(file_name)
#             elif choice == '5':
#                 file_name = input("Enter the name of the file to search notes from: ")
#                 search_term = input("Enter search term: ")
#                 self.search_notes_in_file(file_name, search_term)
#             elif choice == '6':
#                 print("Exiting Note Manager App. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 6.")

# if __name__ == "__main__":
#     # notes_manager = NoteManager("C:\\Users\\Kien Quoc\\Documents\\GitHub\\project-1.1\\notes_directory")
#     notes_manager.main()

import os
import datetime

# Check if notes_directory exists, create it if needed
if not os.path.exists('notes_directory'):
    os.makedirs('notes_directory')

class NoteManager:

    def __init__(self, notes_directory):
        self.notes_directory = notes_directory 

    def get_file_path(self, file_name):
        return os.path.join(self.notes_directory, file_name)

    def create_new_file(self, file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        open(file_path, 'w').close()
        print("New file '{file_name}' created.")

    def delete_file(self, file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File does not exist.")

    def add_note(self, file_name, note):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        with open(file_path, 'a') as file:
            file.write(f"{note}")
        print("Note added successfully.")

    def get_notes(self, file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            with open(file_path, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File does not exist.")

    def search_notes(self, file_name, query):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            with open(file_path, 'r') as file:
                matches = []
                for line in file:
                    if query in line:
                        matches.append(line.strip())
                if matches:
                    return matches
                else:
                    print("No matching notes found.")
        except FileNotFoundError:
            print("File does not exist.")