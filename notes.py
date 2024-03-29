# import os
 
# def create_new_file():
#     file_name = input("Enter the name of the new file: ")
#     if not file_name.endswith('.txt'):
#         file_name += '.txt'
#     with open(file_name, 'w') as file:
#         print(f"New file '{file_name}' created.")

# def delete_file():
#     file_name = input("Enter the name of the file to delete: ")
#     if not file_name.endswith('.txt'):
#         file_name += '.txt'
#     try:
#         os.remove(file_name)
#         print(f"File '{file_name}' deleted successfully.")
#     except FileNotFoundError:
#         print(f"File '{file_name}' does not exist.")

# def add_note():
#     file_name = input("Enter the name of the file to add note to: ")
#     if not file_name.endswith('.txt'):
#         file_name += '.txt'
#     note = input("Enter your note: ")
#     with open(file_name, 'a') as file:
#         file.write(note + '\n')
#     print("Note added successfully.")

# def print_notes():
#     file_name = input("Enter the name of the file to print notes from: ")
#     if not file_name.endswith('.txt'):
#         file_name += '.txt'
#     try:
#         with open(file_name, 'r') as file:
#             print("Notes:")
#             print(file.read())
#     except FileNotFoundError:
#         print(f"File '{file_name}' does not exist.")

# def search_notes():
#     file_name = input("Enter the name of the file to search notes from: ")
#     if not file_name.endswith('.txt'):
#         file_name += '.txt'
#     search_term = input("Enter search term: ")
#     try:
#         with open(file_name, 'r') as file:
#             notes = file.readlines()
#             found = False
#             print("Search results:")
#             for note in notes:
#                 if search_term in note:
#                     print(note.strip())
#                     found = True
#             if not found:
#                 print("No matching notes found.")
#     except FileNotFoundError:
#         print(f"File '{file_name}' does not exist.")

# def main():
#     print("Welcome to the Note Taking App!")
#     while True:
#         print("\nOptions:")
#         print("1. Create a new file")
#         print("2. Delete a file")
#         print("3. Add a note to a file")
#         print("4. Print notes from a file")
#         print("5. Search notes from a file")
#         print("6. Exit")
#         choice = input("Enter your choice (1-6): ")
#         if choice == '1':
#             create_new_file()
#         elif choice == '2':
#             delete_file()
#         elif choice == '3':
#             add_note()
#         elif choice == '4':
#             print_notes()
#         elif choice == '5':
#             search_notes()
#         elif choice == '6':
#             print("Exiting Note Taking App. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 6.")

# if __name__ == "__main__":
#     main()

import backends

notes_manager = backends.NoteManager("notes_directory")

def print_help():
    print("Commands:")
    print("  new - Create a new file") 
    print("  delete - Delete a file")
    print("  add - Add a note to a file")
    print("  print - Print notes from a file")
    print("  search - Search notes in a file")
    print("  help - Print this help")
    print("  quit - Exit the program")

def main():
    
    print_help()
    
    while True:
        cmd = input("Enter a command: ")
        
        if cmd == 'quit':
            break
            
        elif cmd == 'help':
            print_help()
            
        elif cmd == 'new':
            file_name = input("Enter name for new file: ")
            notes_manager.create_new_file(file_name)
            
        elif cmd == 'delete':
            file_name = input("Enter name of file to delete: ")
            notes_manager.delete_file(file_name)
            
        elif cmd == 'add':
            file_name = input("Enter name of file to add note to: ")
            print("Enter your notes (type #END# to stop): \n")
            write = 'h0ld'
            note = ''
            while(write!='#END#'):
                write = input()
                if(write !='#END#'):
                    note += write + '\n'

            notes_manager.add_note(file_name, note)


        elif cmd == 'print':
            file_name = input("Enter name of file to print: ")
            notes_manager.get_notes(file_name)
            
        elif cmd == 'search':
            file_name = input("Enter name of file to search: ")
            query = input("Enter search term: ")
            notes_manager.search_notes(file_name, query)
            
        else:
            print("Invalid command. Enter 'help' to see available commands.")
            
if __name__ == '__main__':
    main()