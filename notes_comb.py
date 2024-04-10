import backend_comb
from rich.console import Console
from rich.markdown import Markdown
from rich.layout import Layout
from rich.layout import Panel

console = Console()
notes_manager = backend_comb.NoteManager("notes_directory")

def print_help():
    layout = Layout()
    layout.split_column(Layout(name="upper"), Layout(name="lower"))
    layout["lower"].split_row(Layout(name="left"), Layout(name="right"))
    current_directory = notes_manager.notes_directory
    note_list = str(notes_manager.get_list(current_directory))
    # note_list = []
    # for i in range(len(note_list)):
    #     note_list += note_list[i]

    layout["upper"].update(Panel(f"[bold magenta]|Current Directory:[/bold magenta] \\{current_directory}"
                                 f"\n\n[yellow] Contents:  [/yellow]{note_list}"
                                 ))
    layout["left"].update(
        Panel(
            "\n"
            "   [green]newf[/green]    Create a new folder\n"
            "   [green]change[/green]  Switches current folder\n"
            "   [green]help[/green]    Print this help\n"
            "   [green]quit[/green]    Exit the program\n"
            ,
            title="[bold][cyan]Program Commands[/cyan][/bold]",
            subtitle="", subtitle_align="right"

        )
    )
    layout["right"].update(
        Panel(
            "\n"
            "   [green]add[/green]     Add a note to a file\n"
            "   [green]print[/green]   Print notes from a file\n"
            "   [green]search[/green]  Search notes in a file\n"
            "   [green]new[/green]     Create a new file\n"
            "   [green]delete[/green]  Delete a file\n"
            ,
            title="[bold][cyan]Notes Commands[/cyan][/bold]",
            subtitle="", subtitle_align="left"
        )
    )

    layout["upper"].size = 5
    layout["lower"].size = 9
    main_panel = Panel(layout, title="[bold magenta]<Note Taking App>[/bold magenta]", subtitle="", height=17,
                       width=100)
    console.print(main_panel)
    # print("Commands:")
    # print("  note - Create a quick note")
    # print("  delete - Delete a file")
    # print("  add - Add a note to a file")
    # print("  print - Print notes from a file")
    # print("  search - Print all notes from a file")
    # print("  newf - Create a new folder")
    # print("  change - Switch current folder")
    # #print("  new - Create a new file")
    # print("  deletef - Delete a folder")
    # print("  help - Print this help")
    # print("  quit - Exit the program")

def display():
    current_directory = notes_manager.notes_directory
    note_list = str(notes_manager.get_list(current_directory))
    display = Panel(f"[bold magenta]|Current Directory:[/bold magenta] \\{current_directory}"
            f"\n\n[yellow] Contents:  [/yellow]{note_list}",title="[bold magenta]<Content>[/bold magenta]", subtitle="", height=5,
                       width=100)
    console.print(display)
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
            display()
            file_name = input("Enter name of file to delete: ")
            notes_manager.delete_file(file_name)
            
        elif choice == 'add':
            display()
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
            display()
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
