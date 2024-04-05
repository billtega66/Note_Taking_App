import os
import datetime

class NoteManager:
    def __init__(self, notes_directory):
        self.notes_directory = notes_directory
        if not os.path.exists(notes_directory):
            os.makedirs(notes_directory)

    def get_file_path(self, file_name):
        return os.path.join(self.notes_directory, file_name)

    def createDirectory(self):
        if not os.path.exists(self.notes_directory):
            os.makedirs(self.notes_directory)
    
    def create_folder(self, foldername):
        self.notes_directory = foldername + "/"
        if os.path.exists(self.notes_directory):
            self.notes_directory = foldername + '(' + '1' + ')' + "/"
            num = int(self.notes_directory[-3])
            while os.path.exists(self.notes_directory):
                num = num + 1
                self.notes_directory = foldername + '(' + str(num) + ')' + "/" 

    def delete_folder(self, foldername):
        if os.path.exists(foldername):
            choice = input("Are you sure? ")
            if choice == 'yes':
                os.rmdir(foldername)
        else:
            print("Folder does not exist.")
        
    def change_folder(self, foldername):
        if os.path.exists(foldername):
            self.notes_directory = foldername
        else:
            print("Folder does not exist.")

    def create_new_file(self, file_name, password=None):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
            
        with open(file_path, 'w') as file:
            if password:
                file.write("Password: " + password + "\n")  # Include label 'Password:' before the password
                print("Note created and password-protected.")
            else:
                print("Note created.")

    def delete_file(self, file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File does not exist.")

    def add_note(self, file_name, note, password=None):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, 'a') as file:
            file.write(f"{timestamp} - {note}\n")
        print("Note added successfully.")

    def get_notes(self, file_name, password=None):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            if password and not self.check_password(file_path, password):
                print("Incorrect password. Access denied.")
                return
            with open(file_path, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File does not exist.")

    def search_notes(self, file_name, query, password=None):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            with open(file_path, 'r') as file:
                if password:
                    if not self.check_password(file_path, password):
                        print("Incorrect password. Access denied.")
                        return
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
        
    def check_password(self, file_path, password):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith("Password:"):
                    stored_password = line.split('Password:')[1].strip()
                    return stored_password == password
        return False
