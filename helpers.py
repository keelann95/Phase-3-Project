from models.contact import Contact
from models.group import Group
from sqlalchemy.exc import SQLAlchemyError

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    group_name = input("Enter the group name: ")
    try:
        contact = Contact.create(name, phone, email, group_name)
        if contact:
            print(f"Contact '{name}' added successfully!")
        else:
            print("Failed to add contact. Please check if the group exists.")
    except SQLAlchemyError as e:
        print(f"An error occurred while adding the contact: {str(e)}")

def list_contacts():
    try:
        contacts = Contact.all()
        if contacts:
            for contact in contacts:
                print(f"{contact.name} - {contact.phone} - {contact.email} (Group: {contact.group.name})")
        else:
            print("No contacts found.")
    except SQLAlchemyError as e:
        print(f"An error occurred while listing contacts: {str(e)}")

def search_contacts():
    query = input("Search contacts by name or group: ")
    try:
        contacts = Contact.all()
        filtered_contacts = [c for c in contacts if query.lower() in c.name.lower() or (c.group and query.lower() in c.group.name.lower())]
        if filtered_contacts:
            for contact in filtered_contacts:
                print(f"{contact.name} - {contact.phone} - {contact.email} (Group: {contact.group.name if contact.group else 'No Group'})")
        else:
            print(f"No contacts found for '{query}'.")
    except SQLAlchemyError as e:
        print(f"An error occurred while searching contacts: {str(e)}")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    try:
        contact = Contact.find_by_name(name)
        if not contact:
            print(f"No contact found with the name '{name}'")
            return
        new_name = input(f"Enter new name (current: {contact.name}): ") or None
        new_phone = input(f"Enter new phone (current: {contact.phone}): ") or None
        new_email = input(f"Enter new email (current: {contact.email}): ") or None
        new_group = input(f"Enter new group (current: {contact.group.name if contact.group else 'No Group'}): ") or None
        Contact.update(contact, new_name, new_phone, new_email, new_group)
        print(f"Contact '{name}' updated successfully!")
    except SQLAlchemyError as e:
        print(f"An error occurred while updating the contact: {str(e)}")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    try:
        contact = Contact.find_by_name(name)
        if contact:
            Contact.delete(contact)
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"No contact found with the name '{name}'.")
    except SQLAlchemyError as e:
        print(f"An error occurred while deleting the contact: {str(e)}")

def list_groups():
    try:
        groups = Group.all()
        if groups:
            for group in groups:
                print(group.name)
        else:
            print("No groups found.")
    except SQLAlchemyError as e:
        print(f"An error occurred while listing groups: {str(e)}")

def add_group():
    name = input("Enter the new group name: ")
    try:
        group = Group.create(name)
        if group:
            print(f"Group '{name}' added successfully!")
        else:
            print(f"Failed to add group '{name}'.")
    except SQLAlchemyError as e:
        print(f"An error occurred while adding the group: {str(e)}")