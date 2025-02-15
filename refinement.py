import os
from datetime import datetime
import json

# Description: A simplistic, command-line journal application to record and manage daily entries.


def add_entry():
    print("\nWrite Journal Entry")
    timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
   
    journal_entry = input(f"{timestamp} > ")

    journal_entry_json = {
        'time': timestamp,
        'journal_entry': journal_entry
    }

    try:
        with open('journal.json', 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        json_data = []
    
    json_data.append(journal_entry)

# def view_entries():
#     print(journal_entries)

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
