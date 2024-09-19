from helpers import (
    add_contact, list_contacts, search_contacts,
    update_contact, delete_contact, list_groups, add_group
)
from models import initialize_database

def main():
    initialize_database()
    
    while True:
        print("""
        Please select an option:
        0. Exit the program
        1. Add a new contact
        2. List all contacts
        3. Search contacts by group or name
        4. Update contact information
        5. Delete a contact
        6. List all groups
        7. Add a new group
        """)
        
        choice = input("> ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            list_groups()
        elif choice == '7':
            add_group()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()