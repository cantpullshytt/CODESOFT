#Contacts Book by Sankalp Mishra!!

import json
import os

CONTACTS_FILE = "my_contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except:
            print("Couldn't read contacts, starting fresh!")
            return []
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def show_contacts(contacts):
    if not contacts:
        print("No friends yet! Add someone to get started")
        return
    print("\nHere's your contact list:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} ({c['phone']})")

def add_contact(contacts):
    print("\nLet's add a new buddy!")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"Added {name} to your contacts!")

def search_contacts(contacts):
    term = input("\nSearch by name or phone: ").strip().lower()
    found = [c for c in contacts if term in c["name"].lower() or term in c["phone"]]
    if not found:
        print("No matches found! Try again.")
    else:
        print("Found:")
        for c in found:
            print(f"- {c['name']} ({c['phone']})")

def update_contact(contacts):
    show_contacts(contacts)
    try:
        idx = int(input("Who do you want to update? (number): ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid choice.")
            return
        print("Just hit enter to leave unchanged.")
        contact = contacts[idx]
        name = input(f"New name for {contact['name']} (or press enter): ").strip()
        phone = input(f"New phone for {contact['phone']} (or press enter): ").strip()
        email = input(f"New email (or press enter): ").strip()
        address = input(f"New address (or press enter): ").strip()
        if name: contact["name"] = name
        if phone: contact["phone"] = phone
        if email: contact["email"] = email
        if address: contact["address"] = address
        save_contacts(contacts)
        print("Updated!")
    except ValueError:
        print("That's not a number... try again!")

def delete_contact(contacts):
    show_contacts(contacts)
    try:
        idx = int(input("Who should we delete? (number): ")) - 1
        if idx < 0 or idx >= len(contacts):
            print("Invalid choice.")
            return
        gone = contacts.pop(idx)
        save_contacts(contacts)
        print(f"Deleted {gone['name']}. Farewell!")
    except ValueError:
        print("That's not a number... try again!")

def main():
    print("Welcome to Sankalp's Contacts Book!")
    contacts = load_contacts()
    while True:
        print("\nPick an option:")
        print("1. Show everyone")
        print("2. Add someone")
        print("3. Search")
        print("4. Update info")
        print("5. Delete someone")
        print("6. Quit")
        choice = input("What do you want to do? (1-6): ").strip()
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("See you later! 👋")
            break
        else:
            print("Hmm, I didn't get that. Try again!")

if __name__ == "__main__":
    main()