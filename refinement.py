import os
from datetime import datetime
import json

# Description: A simplistic, command-line journal application to record and manage daily entries.
# Date: 2025-02-15

journal_entries = []

def view_entries():
    readfile = open("journal.txt", "r")
    print(readfile.read())

def add_entry():
    print("\nCreate Journal Entry")
    timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    with open("journal.txt", "a") as file:
        while True:
            journal_entry = input(f"{timestamp} > ")
            if journal_entry == "ESC":
                print("Entry Saved.")
                break
            timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
            time_input = f"{timestamp} - { journal_entry }"
            file.write(time_input + "\n")
            file.close()

def main():
    while True:
        print("\nRefinement Journal")
        print("\n1. Add Journal Entry")
        print("2. View Journal Entries")
        print("3. Exit Refinement Journal")
        user_choice = input("\nChoose an Option: ")

        if user_choice == "1":
            print("Add Entry Selected")
            add_entry()
        elif user_choice == "2":
            print("View Entries Selected")
            view_entries()
        elif user_choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid Selection, Try again.")

if __name__ == "__main__":
    main()
