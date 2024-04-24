import os
import datetime
from rich.console import Console
from rich.markdown import Markdown
from flask import Flask, request, jsonify

app = Flask(__name__)

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
            print("Folder created.")
    
    def create_folder(self, foldername):
        self.notes_directory = foldername
        if os.path.exists(self.notes_directory):
            self.notes_directory = foldername + '(' + '1' + ')'
            num = int(self.notes_directory[-3])
            while os.path.exists(self.notes_directory):
                num = num + 1
                self.notes_directory = foldername + '(' + str(num) + ')'

    def delete_folder(self, foldername):
        if os.path.exists(foldername):
            choice = input("Are you sure? yes/no: ")
            if choice == 'yes':
                try:
                    os.rmdir(foldername)
                except:
                    choice = input("Folder contains files. Do you want them to be deleted? ")
                    if choice == 'yes':
                        oldfolder = self.notes_directory
                        print("")
                        self.change_folder(foldername)
                        dir = os.listdir(foldername)
                        for file in dir:
                            print(file + " has been deleted.")
                            file = self.get_file_path(file)
                            os.remove(file)
                        os.rmdir(foldername)
                        print("Folder deleted.")
                        self.change_folder(oldfolder)
        else:
            print("Folder does not exist.")
        
    def change_folder(self, foldername):
        if os.path.exists(foldername):
            self.notes_directory = foldername
        else:
            print("Folder does not exist.")
####################################################
            
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
        with open(file_path, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {note}\n")
        

    def get_notes(self, file_name, password=None):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            if password: 
                if not self.check_password(file_path, password):
                    return jsonify({"error": "Incorrect password. Access denied."}), 401
            with open(file_path, 'r') as file:
                return file.read(), 200
        except FileNotFoundError:
            return jsonify({"error": "File does not exist."}), 404

    def search_notes(self, file_name, query, password=None):
    
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = self.get_file_path(file_name)
        try:
            if password:
                if not self.check_password(file_path, password):
                    return {"error": "Incorrect password. Access denied."}, 403
            with open(file_path, 'r') as file:
                matches = [line.strip() for line in file if query in line]
            if matches:
                return matches
            else:
                return {"message": "No matching notes found."}, 404
        except FileNotFoundError:
            return {"error": "File does not exist."}, 404

        
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



    def add_checklist_item(self, file_path, item_text):
        """Add an item to the checklist in the file."""
        with open(file_path, 'a') as file:
            file.write(f"[ ] {item_text}\n")
        print("Item added to the checklist successfully!")

    def check_item(self, file_path, item_index):
        """Mark an item in the checklist as checked."""
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 0 <= item_index < len(lines):
            lines[item_index] = lines[item_index].replace("[ ]", "[x]", 1)

            with open(file_path, 'w') as file:
                file.writelines(lines)
            print("Item checked successfully!")
        else:
            print("Invalid item index.")

    def uncheck_item(self, file_path, item_index1):
        """Unmarked an item in the checklist"""
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 0 <= item_index1 < len(lines):
            lines[item_index1] = lines[item_index1].replace("[x]", "[ ]", 1)

            with open(file_path, 'w') as file:
                file.writelines(lines)
            print("Item unchecked successfully!")
        else:
            print("Invalid item index.")

    def display_checklist(self, file_path):
        """Display the checklist."""
        with open(file_path, 'r') as file:
            print("Checklist:")
            for index, line in enumerate(file):
                print(f"{index}: {line.strip()}")

    def delete_checklist_choice(self, file_path, item_index):
        """Delete checklist choice"""
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 0 <= item_index < len(lines):
            del lines[item_index]

            with open(file_path, 'w') as file:
                file.writelines(lines)
            print("Item deleted successfully!")
        else:
            print("Invalid item index.") 
    
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
        

class flash_cards(linked_list, NoteManager):
    def __init__(self, notes_directory):
        
        linked_list.__init__(self) 
        NoteManager.__init__(self, notes_directory)  
        self.head = None  

    def Instructions(self):
        print("You are attempting to run this file as flash cards. Here are some things to keep in mind to assure it runs correctly: ")
        print("1. Type the question in one line, then the answer in the next ")
        print ("2. If there is not an even number of lines in the text file, the test will not be able to run")
        print("3. The answers will be space sensitive, so make sure there are not extra spaces anywhere (especially at the end) ")
        print("4. The flash cards will cycle through until you get all of the answers correct")

    @staticmethod
    def create_cards(card_pile, file_name):
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = card_pile.get_file_path(file_name)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                length = len(lines)
                if (length % 2 != 0):
                    print("Not enough lines to make cards")
                    return 
                count = 0
                while (count <= length - 1):
                    Q = lines[count]
                    count = count + 1
                    A = lines[count]
                    count = count + 1
                    card_pile.insertAtEnd(Q, A)
        except FileNotFoundError:
            print("File does not exist.")

    @staticmethod
    def test(card_pile):
        if card_pile.head is None:
            print("PILE IS EMPTY")
            return 
        
        print("Now beginning the test...")
        print()
        
        current = card_pile.head
        while ((current != None)):
            index = 0
            while ((current != None)):
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
        
#############################
note_manager = NoteManager("notes_directory")

@app.route('/notes/add', methods=['POST'])
def add_note_route():
    file_name = request.args.get('file_name')
    note = request.args.get('note')
    password = request.args.get('password')
    if file_name and note:
        note_manager.add_note(file_name, note, password)
        return jsonify({'message': 'Note added successfully'}), 201
    else:
        return jsonify({'error': 'Missing file_name or note parameter'}), 400

@app.route('/notes/search', methods=['GET'])
def api_search_notes():
    query = request.args.get('query')
    file_name = request.args.get('file_name')
    password = request.args.get('password', None)  # Password is optional

    if not query or not file_name:
        return jsonify({"error": "Missing required parameters."}), 400

    result = note_manager.search_notes(file_name, query, password)
    if isinstance(result, list):
        return jsonify(result)
    else:
        return jsonify(result[0]), result[1]

@app.route('/notes/print', methods=['GET'])
def get_notes_route():
    file_name = request.args.get('file_name')
    password = request.args.get('password')
    if not file_name:
        return jsonify({"error": "Please provide a file_name parameter."}), 400
    return note_manager.get_notes(file_name, password)


@app.route('/notes/<file_name>', methods=['DELETE'])
def delete_note(file_name):
    note_manager.delete_file(file_name)
    return jsonify({'message': 'File deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)

# Route for adding a checklist item
@app.route('/checklist/<file_name>', methods=['POST'])
def add_checklist_item(file_name):
    item_text = request.json.get('item_text')
    file_path = note_manager.get_file_path(file_name)
    note_manager.add_checklist_item(file_path, item_text)
    return jsonify({'message': 'Checklist item added successfully'})

# Route for checking a checklist item
@app.route('/checklist/<file_name>/<int:item_index>', methods=['PUT'])
def check_checklist_item(file_name, item_index):
    file_path = note_manager.get_file_path(file_name)
    note_manager.check_item(file_path, item_index)
    return jsonify({'message': 'Checklist item checked successfully'})

# Route for unchecking a checklist item
@app.route('/checklist/<file_name>/<int:item_index>', methods=['DELETE'])
def uncheck_checklist_item(file_name, item_index):
    file_path = note_manager.get_file_path(file_name)
    note_manager.uncheck_item(file_path, item_index)
    return jsonify({'message': 'Checklist item unchecked successfully'})

# Route for displaying the checklist
@app.route('/checklist/<file_name>', methods=['GET'])
def display_checklist(file_name):
    file_path = note_manager.get_file_path(file_name)
    note_manager.display_checklist(file_path)
    return jsonify({'message': 'Checklist displayed successfully'})

# Route for deleting a checklist item
@app.route('/checklist/<file_name>/<int:item_index>', methods=['DELETE'])
def delete_checklist_item(file_name, item_index):
    file_path = note_manager.get_file_path(file_name)
    note_manager.delete_checklist_choice(file_path, item_index)
    return jsonify({'message': 'Checklist item deleted successfully'})

# class Node: 
#     def __init__(self, question,answer):
#         self.question = question
#         self.answer = answer
#         self.next = None
   

# class linked_list(Node): 
#     def __init__ (self): 
#         self.head = None

#     def insertAtEnd(self,question,answer):
#         new_node = Node(question,answer)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         current_node = self.head
#         while (current_node.next != None):
#             current_node = current_node.next
            
            
#         current_node.next = new_node

        
    
#     def remove_first_node(self):
#         if(self.head == None):
#             return
 
#         self.head = self.head.next
        
#     def remove_at_index(self, index):
#         if self.head == None:
#             return
#         current_node = self.head
#         position = 0
#         if position == index:
#             self.remove_first_node()
#         else:
#             while(current_node != None and position+1 != index):
#                 position = position+1
#                 current_node = current_node.next
 
#             if current_node != None:
#                 current_node.next = current_node.next.next
#             else:
#                 print("Index not present")
        

            
# class flash_cards(linked_list):
    
#     def Instructions():
#         print("You are attempting to run this file as flash cards. Here are some things to keep in mind to assure it runs correctly: ")
#         print("1. Type the question in one line, then the answer in the next ")
#         print ("2. If there is not an even number of lines in the text file, the test will not be able to run")
#         print("3. The answers will be space sensitive, so make sure there are no extra spaces anywhere (especially at the end) ")
#         print("4. The flash cards will cycle through until you get all of the answers correct")

               
#     def create_cards(card_pile, file_name):
#         with open('%s.txt' %file_name, 'r') as file:
#             lines = file.readlines()
#             length = len(lines)
#             if (length%2 != 0):
#                 return 
#             count = 0
#             while (count <= length - 1):
#                 Q = lines[count]
#                 count = count + 1
#                 A = lines[count]
#                 count = count + 1
#                 card_pile.insertAtEnd(Q,A)
    
#     def test(card_pile):
#         if card_pile.head is None:
#             print("PILE IS EMPTY")
#             return 
        
#         print("Now beginning the test...")
#         print()
        
#         current = card_pile.head
#         while ((current != None) ):
#             index = 0
#             while ((current != None) ):
#                 user_input = input(current.question) 
#                 answer = current.answer
                
#                 if (answer.lower() == (user_input.lower() + '\n') or answer.lower() == user_input.lower()):
#                     print("Correct! Removing from pile")
#                     print()
#                     current = current.next 
#                     card_pile.remove_at_index(index)
#                 else: 
#                     print("Incorrect. The correct answer is: %s" %current.answer)
#                     print()
#                     current = current.next 
#                     index = index + 1 
#             current = card_pile.head
            
#         print("All questions have been answered correctly")



# # Run in this order:
# # test = flash_cards()
# # test.instructions()
# # test.create_cards('hello')
# # test.test()
   
