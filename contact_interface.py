import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contact_list = []

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        # Create labels and entries
        self.name_label = tk.Label(self.frame1, text="Name:")
        self.name_label.pack(side=tk.LEFT)

        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack(side=tk.LEFT)

        self.phone_label = tk.Label(self.frame1, text="Phone Number:")
        self.phone_label.pack(side=tk.LEFT)

        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.pack(side=tk.LEFT)

        # Create buttons
        self.add_button = tk.Button(self.frame2, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT)

        self.view_button = tk.Button(self.frame2, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(side=tk.LEFT)

        self.search_label = tk.Label(self.frame2, text="Search:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.frame2)
        self.search_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.frame2, text="Search", command=self.search_contacts)
        self.search_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(self.frame3, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.frame3, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(self.frame3, text="Quit", command=self.root.quit)
        self.quit_button.pack(side=tk.LEFT)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.contact_list.append([name, phone])
        messagebox.showinfo("Contact Added", "Contact has been added successfully.")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def view_contacts(self):
        contacts = ""
        for i, contact in enumerate(self.contact_list):
            contacts += f"{i+1}. Name: {contact[0]}, Phone Number: {contact[1]}\n"
        messagebox.showinfo("Contacts", contacts)

    def search_contacts(self):
        search_term = self.search_entry.get()
        found_contacts = [contact for contact in self.contact_list if search_term in contact[0]]
        contacts = ""
        for i, contact in enumerate(found_contacts):
            contacts += f"{i+1}. Name: {contact[0]}, Phone Number: {contact[1]}\n"
        if contacts:
            messagebox.showinfo("Search Results", contacts)
        else:
            messagebox.showinfo("Search Results", "No contacts found.")
        self.search_entry.delete(0, tk.END)

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        for contact in self.contact_list:
            if contact[0] == name:
                new_name = simpledialog.askstring("Update Name", "Enter new name:")
                new_phone = simpledialog.askstring("Update Phone", "Enter new phone number:")
                contact[0] = new_name
                contact[1] = new_phone
                messagebox.showinfo("Contact Updated", "Contact has been updated successfully.")
                return
        messagebox.showinfo("Contact Not Found", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        for contact in self.contact_list:
            if contact[0] == name:
                self.contact_list.remove(contact)
                messagebox.showinfo("Contact Deleted", "Contact has been deleted successfully.")
                return
        messagebox.showinfo("Contact Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
