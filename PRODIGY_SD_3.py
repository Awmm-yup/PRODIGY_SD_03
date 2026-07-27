import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists! Use the edit option to modify.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")
    print("--------------------")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    print(f"Current Phone: {contacts[name]['phone']}")
    new_phone = input("Enter new phone (leave blank to keep current): ").strip()
    if new_phone:
        contacts[name]['phone'] = new_phone
        
    print(f"Current Email: {contacts[name]['email']}")
    new_email = input("Enter new email (leave blank to keep current): ").strip()
    if new_email:
        contacts[name]['email'] = new_email
        
    save_contacts(contacts)
    print("Contact updated successfully!")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Edit an Existing Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
