import os
from pyjournal import decision

def jrnlread():

    directory = input("Enter the directory where your journal is located (default is current directory): ") or "."
    journal_name = input("Enter the name of your journal file (default is journal.txt): ") or "journal.txt"
    journal_path = os.path.join(directory, journal_name)
    if os.path.exists(journal_path):
        with open(journal_path, "r") as file:
            content = file.read()
            print("\nJournal Content:\n")
            print(content)
    else:
        print("Journal file not found.")
    backtomenu = input("\nPress R to return to menu.\n\nPress 4 to exit. ")
    if backtomenu.lower() == "r":
        decision()
    elif backtomenu == "4":
            print("Closing.")
            exit()

jrnlread()
