##from config import JOURNAL_FILE
from datetime import datetime
import os
import subprocess   
config_file = "journal_config.txt"

def decision():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) ##clears tui
    choice = input("\033[1;32mJournal App\033[0m\n 1. Write to journal\n 2. Read journal\n 3. Configure \n 4. Exit\n\nChoose an option: ")
   
    if choice == "1":
        def write_journal():
            # Try to load last used directory from a config file
            last_directory = None
            
            if os.path.exists(config_file):
                with open(config_file, "r") as f:
                    last_directory = f.read().strip()
            
            # Show last used directory or default
            if last_directory and os.path.exists(last_directory):
                print(f"\nRecent directory: {last_directory}")
                use_last_directory = input("Use this directory? (y/n): ").lower()
                if use_last_directory == "y" or use_last_directory == "":
                    directory = last_directory
                else:
                    directory = input("Enter the directory to save your journal: ")
            else:
                directory = input("Enter the directory to save your journal: ")
            
            # Save directory to config
            if os.path.exists(directory):
                with open(config_file, "w") as f:
                    f.write(directory)
            elif not os.path.exists(directory):
                os.makedirs(directory)
                with open(config_file, "w") as f:
                    f.write(directory)
                print("Directory Created Successfully.")

            journal_name = input("Enter the name of your journal file (default is journal.txt): ") or "journal.txt"

            if not os.path.exists(os.path.join(directory, journal_name)):
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                print("Journal file does not exist. Created a new one.")
            else:
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

                print("Saving journal in the existing directory.")

            entry = input("\nWrite your journal entry:\n\nif you dont want to save and return to the menu, press R and then enter.\n\n---> ")

            if entry.lower() == "r":
                return decision()
         
            with open(os.path.join(directory, journal_name), "a") as file:
               
                file.write("\n" + f"{datetime.now().strftime('%Y-%m-%d-%A %H:%M:%S')}" + " - " + entry)
           
            print("Journal Saved.")
        write_journal()

    elif choice == "2":
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                last_directory = f.read().strip()
                journal_name = input("Enter the name of your journal file (default is journal.txt): ") or "journal.txt"
                journal_path = os.path.join(last_directory, journal_name)
                if os.path.exists(journal_path):
                    with open(journal_path, "r") as file:
                        entries = file.readlines()
                        for entry in entries:
                            print(entry.strip())
                else:
                    print("Journal file not found in the last used directory.")

        backtomenu = input("\nPress R to return to menu.\n\nPress 4 to exit. ")
        if backtomenu.lower() == "r":
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) #clears tui
                return decision()
        elif backtomenu == "4":
                print("Closing.")


    elif choice == "3":
       subprocess.Popen(['notepad.exe', config_file], shell=True) and subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) #opens notepad then clears tui
       return decision()
    elif choice == "4":
        print("Exiting.")

    else:
        for invalid_attempts in range(3):
            print("\033[1;31mInvalid choice. Please try again.\033[0m")
            choice = input("Choose an option: ")
            if choice in ["1", "2", "3", "4"]:
                break
        else:
            print("Too many invalid attempts.")

                
        

decision()