import subprocess
import os
import journal_conf
import journal_read

def decision():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True) ##clears tui
    choice = input ("\033[1;32mPyJournal\nALPHA 0.1.0\033[0m" \
                    "\n 1. Write to journal" \
                    "\n 2. Read journal" \
                    "\n 3. Configure" \
                    "\n 4. Exit" \
                    "\n\nChoose an option: ")
    
    if choice == "1":
        print("Opening journal writer...")
        import journal_writer
        journal_writer.writer()

    #elif choice == "2":
       #journal_read.jrnlread()

    elif choice == "3":
        journal_conf.configuration()
    
    elif choice == "4":
        print ("Closing.")
        exit()
    else:
        for invalid_attempts in range(3):
            print("\033[1;31mInvalid choice. Please try again.\033[0m")
            choicerepeat = input("Choose an option: ")
            if choicerepeat in ["1", "2", "3", "4"]:
                break #please fix this, it is very bad code and I am ashamed of it, but it works for now and I will refactor it later
        else:
            print("\033[1;31mToo many invalid attempts.\033[0m")
            exit()
            

decision()
            