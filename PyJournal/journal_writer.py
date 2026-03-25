import os
from datetime import datetime
from pyjournal import decision
def writer():
    directory = input("Enter the directory where you want to save your journal (default is current directory): ") or "."
    journal_name = input("Enter the name of your journal file (default is journal.txt): ") or "journal.txt"
    journal_path = os.path.join(directory, journal_name)

    if not os.path.exists(directory):
        os.makedirs(directory)
    entry = input("Write your journal entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(journal_path, "a") as f:
        f.write(f"{timestamp} - {entry}\n")
    print("Journal entry saved.")
    backtomenu = input("\nPress R to return to menu.\n\nPress 4 to exit. ")
    if backtomenu.lower() == "r":
        decision()
    elif backtomenu == "4":
            print("Closing.")
            exit()

writer()
            

