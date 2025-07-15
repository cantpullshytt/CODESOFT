#Contacts Book (GUI) by Sankalp Mishra!!

import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

CONTACTS_FILE = "my_contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def contact_summary(contact):
    info = f"{contact['name']} 📱 {contact['phone']}"
    return info

class HumanContactsBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Sankalp's Contacts Book")
        self.contacts = load_contacts()
        self.create_widgets()
        self.show_contacts(self.contacts)
        self.selected_index = None

    def create_widgets(self):
        greeting = tk.Label(self.root, text="Hey there! it's a Contacts Book from Sankalp!", font=("Arial", 14))
        greeting.pack(pady=5)

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=2)
        self.search_entry = tk.Entry(self.search_frame, width=25)
        self.search_entry.pack(side=tk.LEFT)
        tk.Button(self.search_frame, text="Find Someone", command=self.search_contacts).pack(side=tk.LEFT)

        tk.Button(self.root, text=" Add New Buddy", command=self.add_contact).pack(pady=2, fill=tk.X)
        tk.Button(self.root, text=" Update Info", command=self.update_contact).pack(pady=2, fill=tk.X)
        tk.Button(self.root, text=" Delete From List", command=self.delete_contact).pack(pady=2, fill=tk.X)

        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        tk.Button(self.root, text="Show Everyone", command=self.show_all).pack(pady=2, fill=tk.X)

        self.talk_label = tk.Label(self.root, text="", fg="#5c5c5c", font=("Arial", 10))
        self.talk_label.pack(pady=2)

    def talk(self, msg):
        self.talk_label.config(text=msg)

    def show_contacts(self, contacts):
        self.listbox.delete(0, tk.END)
        if not contacts:
            self.listbox.insert(tk.END, "Nobody here yet! Let's make a friend")
            self.talk("Try adding a new buddy above!")
        else:
            for c in contacts:
                self.listbox.insert(tk.END, contact_summary(c))
            self.talk(f"Total friends: {len(contacts)}")

    def show_all(self):
        self.show_contacts(self.contacts)
        self.talk("Here's everyone you know!")

    def on_select(self, event):
        if not self.contacts or not self.listbox.curselection():
            self.selected_index = None
            return
        self.selected_index = self.listbox.curselection()[0]
        selected = self.contacts[self.selected_index]
        self.talk(f"Selected: {selected['name']} ({selected['phone']})")

    def add_contact(self):
        self.talk("Let's add someone new! 🎉")
        name = simpledialog.askstring("Name", "What's their name?")
        if not name:
            self.talk("No name? Maybe next time!")
            return
        phone = simpledialog.askstring("Phone", f"{name}'s phone number?")
        if not phone:
            self.talk("No phone? That's okay, but it's better if you have one.")
            return
        email = simpledialog.askstring("Email", f"{name}'s email (leave blank if none):")
        address = simpledialog.askstring("Address", f"Where does {name} live? (optional):")
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email if email else "",
            "address": address if address else ""
        })
        save_contacts(self.contacts)
        self.show_contacts(self.contacts)
        self.talk(f"{name} was added! Say hi to your new friend.")

    def search_contacts(self):
        term = self.search_entry.get().strip().lower()
        results = [c for c in self.contacts if term in c["name"].lower() or term in c["phone"]]
        self.show_contacts(results)
        if not results:
            self.talk("Nobody matched! Maybe check your spelling or add someone new?")
        else:
            self.talk(f"Found {len(results)} friend(s)!")

    def update_contact(self):
        if self.selected_index is None or not self.contacts:
            self.talk("Pick someone from the list to update first!")
            return
        contact = self.contacts[self.selected_index]
        self.talk(f"Updating info for {contact['name']}...")
        name = simpledialog.askstring("Name", "Change name?", initialvalue=contact["name"])
        if not name: name = contact["name"]
        phone = simpledialog.askstring("Phone", "Change phone?", initialvalue=contact["phone"])
        if not phone: phone = contact["phone"]
        email = simpledialog.askstring("Email", "Change email?", initialvalue=contact["email"])
        if email is None: email = contact["email"]
        address = simpledialog.askstring("Address", "Change address?", initialvalue=contact["address"])
        if address is None: address = contact["address"]
        contact.update({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(self.contacts)
        self.show_contacts(self.contacts)
        self.talk(f"{name}'s info updated!")

    def delete_contact(self):
        if self.selected_index is None or not self.contacts:
            self.talk("Pick someone from the list to delete!")
            return
        who = self.contacts[self.selected_index]["name"]
        sure = messagebox.askyesno("Delete Friend", f"Are you sure you want to delete {who}?")
        if sure:
            del self.contacts[self.selected_index]
            save_contacts(self.contacts)
            self.show_contacts(self.contacts)
            self.talk(f"{who} was removed. Farewell, friend!")
        else:
            self.talk("Glad you changed your mind!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HumanContactsBook(root)
    root.mainloop()