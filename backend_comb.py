import os
import datetime
from rich.console import Console
from rich.markdown import Markdown

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

    def get_list(self, foldername):
        if os.path.exists(foldername):
            return os.listdir(foldername)
        else:
            print("Folder does not exist.")

    # def display_notes(self, priority=None):
    #         if priority:
    #             filtered_notes = [note for note in self.notes if note.priority == priority]
    #             for note in sorted(filtered_notes, key=lambda x: x.priority):
    #                 print(note)
    #                 print("-" * 20)
    #         else:
    #             for note in sorted(self.notes, key=lambda x: x.priority):
    #                 print(note)
    #                 print("-" * 20)
    #
    #     def find_note(self, title):
    #         for note in self.notes:
    #             if note.title == title:
    #                 return note
    #         return None




class Node: 
    def __init__(self, question,answer):
        self.question = question
        self.answer = answer
        self.next = None
   

class linked_list(Node): 
    def __init__ (self): 
        self.head = None

    def insertAtEnd(self,question,answer):
        new_node = Node(question,answer)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while (current_node.next != None):
            current_node = current_node.next
            
            
        current_node.next = new_node

        
    
    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
        
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
        

            
class flash_cards(linked_list):
    
    def Instructions():
        print("You are attempting to run this file as flash cards. Here are some things to keep in mind to assure it runs correctly: ")
        print("1. Type the question in one line, then the answer in the next ")
        print ("2. If there is not an even number of lines in the text file, the test will not be able to run")
        print("3. The answers will be space sensitive, so make sure there are no extra spaces anywhere (especially at the end) ")
        print("4. The flash cards will cycle through until you get all of the answers correct")

               
    def create_cards(card_pile, file_name):
        with open('%s.txt' %file_name, 'r') as file:
            lines = file.readlines()
            length = len(lines)
            if (length%2 != 0):
                return 
            count = 0
            while (count <= length - 1):
                Q = lines[count]
                count = count + 1
                A = lines[count]
                count = count + 1
                card_pile.insertAtEnd(Q,A)
    
    def test(card_pile):
        if card_pile.head is None:
            print("PILE IS EMPTY")
            return 
        
        print("Now beginning the test...")
        print()
        
        current = card_pile.head
        while ((current != None) ):
            index = 0
            while ((current != None) ):
                user_input = input(current.question) 
                answer = current.answer
                
                if (answer.lower() == (user_input.lower() + '\n') or answer.lower() == user_input.lower()):
                    print("Correct! Removing from pile")
                    print()
                    current = current.next 
                    card_pile.remove_at_index(index)
                else: 
                    print("Incorrect. The correct answer is: %s" %current.answer)
                    print()
                    current = current.next 
                    index = index + 1 
            current = card_pile.head
            
        print("All questions have been answered correctly")



# Run in this order:
# test = flash_cards()
# test.instructions()
# test.create_cards('hello')
# test.test()
   

