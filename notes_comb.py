import backends_comb

notes_manager = backends_comb.NoteManager("notes_directory")

def print_help():
    print("Commands:")
    print("  note - Create a quick note")
    print("  delete - Delete a file")
    print("  add - Add a note to a file")
    print("  print - Print notes from a file")
    print("  search - Print all notes from a file")
    print("  newf - Create a new folder")
    print("  change - Switch current folder")
    #print("  new - Create a new file")
    print("  deletef - Delete a folder")
    print("  help - Print this help")
    print("  quit - Exit the program")

def main():
    print_help()
    
    while True:
        choice = input("Enter a command: ")
        
        if choice == 'quit':
            break
            
        elif choice == 'help':
            print_help()

        elif choice == 'note':
            file_name = input("Enter name for new file: ")
            password_protected = input("Would you like to make this note password-protected? (yes/no): ").lower()
            if password_protected == 'yes':
                password = input("Enter password for the note: ")
                notes_manager.create_new_file(file_name, password)
            else:
                notes_manager.create_new_file(file_name)
            note = input("Enter your note: ")
            notes_manager.add_note(file_name, note)
            notes_manager.get_notes(file_name)
           
        elif choice == 'delete':
            file_name = input("Enter name of file to delete: ")
            notes_manager.delete_file(file_name)
            
        elif choice == 'add':
            file_name = input("Enter name of file to add note to: ")
            note = input("Enter your note: ")
            password = input("Enter password for the note (if applicable): ")
            notes_manager.add_note(file_name, note, password)
            notes_manager.get_notes(file_name, password)
         
        elif choice == 'print':
            file_name = input("Enter name of file to print: ")
            password = input("Enter password for the note (if applicable): ")
            notes_manager.get_notes(file_name, password)
            
        elif choice == 'search':
            file_name = input("Enter name of file to search: ")
            query = input("Enter search term: ")
            password = input("Enter password for the note (if applicable): ")
            notes_manager.search_notes(file_name, query, password)

        elif choice == 'newf':
            folder_name = input("Enter name for new folder: ")
            notes_manager.create_folder(folder_name)
            print("Folder created.")

        elif choice == 'change':
            folder_name = input("Enter name for folder: ")
            notes_manager.change_folder(folder_name)

        elif choice == 'new':
            file_name = input("Enter name for new file: ")
            notes_manager.create_new_file(file_name)

        elif choice == 'deletef':
            folder_name = input("Enter name of folder to delete: ")
            notes_manager.delete_folder(folder_name)

        else:
            print("Invalid command. Enter 'help' to see available commands.")
            
if __name__ == '__main__':
    main()
