import backend_comb as backend_comb
import os
import requests
from rich.console import Console
from rich.markdown import Markdown
from rich.layout import Layout
from rich.layout import Panel
from json.decoder import JSONDecodeError


console = Console()
notes_manager = backend_comb.NoteManager("notes_directory")
checklist_file_path = "checklist.txt"
# flashcard_path = "flashcard.txt"

API_URL = "http://127.0.0.1:5000"  # Localhost and the default Flask port

def print_help():
    # Setting up the layout for the help menu
    layout = Layout()
    layout.split_column(Layout(name="upper"), Layout(name="lower"))
    layout["lower"].split_row(Layout(name="left"), Layout(name="right"))
    current_directory = notes_manager.notes_directory
    note_list = str(notes_manager.get_list(current_directory))

    additional_length = 0
    try:
        count = len(notes_manager.get_list(current_directory))
        additional_length = count / 7

    except:
        additional_length = 0

        # Displaying the current directory and available commands
    layout["upper"].update(Panel(f"[bold magenta]|Current Directory:[/bold magenta] \\{current_directory}"
                                 f"\n\n[yellow] Contents:  [yellow]{note_list} "
                                 ))
    layout["left"].update(
        Panel(
            "\n"
            "   [green]newf[/green]         Create a new folder\n"
            "   [green]deletef[/green]      Delete a folder\n"
            "   [green]change[/green]       Switches current folder\n"
            "   [green]help[/green]         Print this help\n"
            "   [green]quit[/green]         Exit the program\n"
            "   [green]transfer[/green]     Transfer file between folders\n"
            ,
            title="[bold][cyan]Program Commands[/cyan][/bold]",
            subtitle="", subtitle_align="right"

        )
    )
    layout["right"].update(
        Panel(
            "\n"
            "   [green]add[/green]        Add a note to a file\n"
            "   [green]print[/green]      Print notes from a file\n"
            "   [green]search[/green]     Search notes in a file\n"
            "   [green]new[/green]        Create a new file\n"
            "   [green]delete[/green]     Delete a file\n"
            "   [green]checklist[/green]  Create a checklist\n"
            "   [green]quiz[/green]       Create a flashcard quiz\n"
            "   [green]photo[/green]      Upload a photo to a note\n"
            ,
            title="[bold][cyan]Notes Commands[/cyan][/bold]",
            subtitle="", subtitle_align="left"
        )
    )

    layout["upper"].size = 5 + int(additional_length)
    layout["lower"].size = 12
    main_panel = Panel(layout, title="[bold magenta]<Note Taking App>[/bold magenta]", subtitle="", height=19+int(additional_length),
                       width=110)
    console.print(main_panel)

def display():
    # Displaying the current directory and its contents
    current_directory = notes_manager.notes_directory
    note_list = str(notes_manager.get_list(current_directory))
    display = Panel(f"[bold magenta]|Current Directory:[/bold magenta] \\{current_directory}"
            f"\n\n[yellow] Contents:  [/yellow]{note_list}",title="[bold magenta]<Content>[/bold magenta]", subtitle="", height=6,
                       width=100)
    console.print(display)

def display_dir():
    current_directory = notes_manager.notes_directory
    dir_list = notes_manager.get_dir()
    dir_list.remove(current_directory)
    if not dir_list:
        dir_list = "There exists no other directory."
    display = Panel(f"[bold magenta]|Current Directory:[/bold magenta] \\{current_directory}"
                    f"\n\n[magenta] Other Directories:  {dir_list}[/magenta]", title="[bold magenta]<Directory>[/bold magenta]",
                    subtitle="", height=5,
                    width=120)
    console.print(display)


def display_notes(response,file_name):
    current_directory = notes_manager.notes_directory
    count = 4
    lines = response.text.split('\n')
    for i in lines: count += 1
    display = Panel(f"[bold magenta]|Current Path:[/bold magenta] \\{current_directory}\\{file_name}.txt"
                    f"\n\n{response.text}",
                    title=f"[bold magenta]<Note>[/bold magenta]",
                    subtitle="", height=count,
                    width=120)
    console.print(display)

def display_checklist():
    # layout_left = Layout()
    # layout_right = Layout()
    #
    # layout_right.update(
    #     Panel(
    #         "\n"
    #         "   Checklist Menu:         \n"
    #         "   [green]1[/green]    Add Item\n"
    #         "   [green]2[/green]    Check Item\n"
    #         "   [green]3[/green]    Uncheck Checklist\n"
    #         "   [green]4[/green]    Display Checklist\n"
    #         "   [green]5[/green]    Delete Item\n"
    #         "   [green]6[/green]    Exit\n"
    #         ,
    #         title="[bold][cyan]Program Commands[/cyan][/bold]",
    #         subtitle="", subtitle_align="right", width=20
    #
    #     )
    # )
    # layout_left.update(
    #     Panel(
    #         "\n"
    #         # " {notes_manager.display_checklist(checklist_file_path)} "
    #
    #         ,
    #         title="[bold][cyan]Notes Commands[/cyan][/bold]",
    #         subtitle="", subtitle_align="left", width=60
    #     )
    # )
    #
    # console.print(layout_left)
    # console.print(layout_right)

    layout = Layout()
    layout.split_row(Layout(name="left"), Layout(name="right"))

    layout["right"].update(
        Panel(
            "\n"
            "   [green]1[/green] - Add Item\n"
            "   [green]2[/green] - Check Item\n"
            "   [green]3[/green] - Uncheck Checklist\n"
            "   [green]4[/green] - Display Checklist\n"
            "   [green]5[/green] - Delete Item\n"
            "   [green]6[/green] - Exit\n"
            ,
            title="[bold][cyan]Checklist Commands[/cyan][/bold]",
            subtitle="", subtitle_align="right"

        )
    )
    content = notes_manager.display_checklist(checklist_file_path)
    line_count = content.count('\n') + 1
    height_plus = 12 + line_count - 8 if line_count > 8 else 12
    if not content:
        content = "\n [yellow]  The checklist is currently empty.[/yellow]"
    layout["left"].update(
    Panel(f"\n{content}",
        title="[bold][cyan]Checklist Items[/cyan][/bold]",
        subtitle="", subtitle_align="left"
    )


    )
    layout["left"].ratio = 3
    layout["right"].ratio = 2
    main_panel = Panel(layout, title="[bold magenta]<Note Taking App>[/bold magenta]", subtitle="",
                       height=height_plus,
                       width=100)
    console.print(main_panel)


def main():
    backend_comb.cls()
    print_help()
    
    while True:
        # Loop to continuously prompt for user input
        notes_manager.createDirectory()
        args = input("Enter a command: ").split()
        choice = args[0]

        if choice == 'quit':
            print("Quitting", end=' ')
            print('.', end=' ')
            print('.', end=' ')
            print('.', end='\n')
            print("Goodbye!")
            break
            
        elif choice == 'help':
            backend_comb.cls()
            print_help()

        elif choice == 'note':
            # Creating a new note
            if len(args) >= 2:
                file_name = args[1]
                password_protected = input("Would you like to make this note password-protected? (yes/no): ").lower()
                if password_protected == 'yes':
                    password = input("Enter password for the note: ")
                    notes_manager.create_new_file(file_name, password)
                else:
                    notes_manager.create_new_file(file_name)
            else:
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
            # Deleting a file
            display()
            if len(args) >= 2:
                file_name = args[1]
            else:
                display()
                file_name = input("Enter name of file to delete: ")
            response = requests.delete(f'http://127.0.0.1:5000/notes/{file_name}')
            print("Delete file successful.")



        elif choice == 'add':
            # Adding a note to a file
            if len(args) >= 2:
                file_name = input("Enter name of file to add note to: ")
                note = input("Enter your note: ")
                password = input("Enter password for the note (if applicable): ")

            else:
                display()
                file_name = input("Enter name of file to add note to: ")
                note = input("Enter your note: ")
                password = input("Enter password for the note (if applicable): ")

            params = {
                'file_name': file_name,
                'note': note,
                'password': password
            }
            response = requests.post(f"{API_URL}/notes/add", params=params)
            if response.status_code == 201:
                print("Note added successfully.")
            else:
                print(f"Failed to retrieve notes: {response.json().get('error', 'Unknown Error')}"), 404

         
        elif choice == 'print':
            # Printing notes from a file
            display()

            if len(args) >= 2:
                file_name = args[1]
                password = input("Enter password (if any): ")

            else:

                display()
                file_name = input("Enter the filename: ")
                password = input("Enter password (if any): ")

            params = {
                'file_name': file_name,
                'password': password
            }

            response = requests.get(f"{API_URL}/notes/print", params=params)

            if response.status_code == 200:
                backend_comb.cls()
                display_notes(response,file_name)
            else:
                print(f"Failed to retrieve notes: {response.json().get('error', 'Unknown Error')}")
            
        elif choice == 'search':
            # Searching for notes in a file
            display()

            if len(args) == 3:
                file_name = args[1]
                query = args[2]
                password = input("Enter password (if any): ")

            if len(args) == 2:
                file_name = args[1]
                query = input("Enter the search query: ")
                password = input("Enter password (if any): ")

            else:
                display()
                file_name = input("Enter the filename: ")
                query = input("Enter the search query: ")
                password = input("Enter password (if any): ")

            params = {
                'file_name': file_name,
                'query': query,
                'password': password
            }

            response = requests.get(f"{API_URL}/notes/search", params=params)
            if response.status_code == 200:
                print("Search Results:")
                notes = response.json()
                for note in notes:
                    print(note)

            else:
                print(f"Failed to retrieve notes: {response.json().get('error', 'Unknown Error')}")

        elif choice == 'newf':
            # Creating a new folder
            if len(args) >= 2:
                folder_name = args[1]

            else:
                folder_name = input("Enter name for new folder: ")

            notes_manager.create_folder(folder_name)

        elif choice == 'change':
            # Changing the current folder
            display_dir()
            if len(args) >= 2:
                folder_name = args[1]

            else:
                folder_name = input("Enter name for folder: ")

            backend_comb.cls()

            notes_manager.change_folder(folder_name)
            print_help()

        elif choice == 'new':
            # Creating a new file
            if len(args) >= 2:
                file_name = args[1]

            else:
                file_name = input("Enter name for new file: ")
            notes_manager.create_new_file(file_name)

        elif choice == 'deletef':
            # Deleting a folder
            display_dir()
            if len(args) >= 2:
                folder_name = args[1]

            else:
                folder_name = input("Enter name of folder to delete: ")
            notes_manager.delete_folder(folder_name)
            
        elif choice == 'checklist':
            print("Entering checklist mode...")
            while True:
                backend_comb.cls()
                display_checklist()

                checklist_choice = input("Command: ")
                if checklist_choice == '1':
                    item_text = input("Enter the checklist item: ")
                    notes_manager.add_checklist_item(checklist_file_path, item_text)

                elif checklist_choice == '2':
                    item_index = int(input("Enter the index of the item to check off: "))
                    notes_manager.check_item(checklist_file_path, item_index-1)

                elif checklist_choice == '3':
                    item_index1 = int(input("Enter the index of the item to uncheck: "))
                    notes_manager.uncheck_item(checklist_file_path, item_index1-1)
                elif checklist_choice == '4':
                    notes_manager.display_checklist(checklist_file_path)

                elif checklist_choice == '5':
                    item_index = int(input("Enter the index of the item to delete: "))
                    notes_manager.delete_checklist_choice(checklist_file_path, item_index-1)

                elif checklist_choice == '6':
                    backend_comb.cls()
                    print_help()
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == 'quiz':
            file_name = input("Enter your file name: ")
            try:
                test = backend_comb.flash_cards(folder_name)
            except UnboundLocalError:
                test = backend_comb.flash_cards("notes_directory")
            test.Instructions()
            test.create_cards(test, file_name)
            test.test(test)

        elif choice == 'photo':
            # Uploading a photo to a note
            if len(args) == 2:
                file_name = args[1]

            else:
                display()
                file_name = input("Enter the filename to add the photo to: ")

            photo_path = input("Enter the path of the photo file: ")
            with open(photo_path, 'rb') as photo_file:
                files = {'photo': photo_file}
                params = {'file_name': file_name}
                response = requests.post(f"{API_URL}/notes/add", params=params, files=files)
                if response.status_code == 201:
                    print("Photo added to the note successfully.")
                else:
                    print(f"Failed to add photo: {response.json().get('error', 'Unknown Error')}")

        else:
            print("Invalid command. Enter 'help' to see available commands.")

        
            
if __name__ == '__main__':
    main()
