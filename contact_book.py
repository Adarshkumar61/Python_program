# contact = []
# def add_contact(task):
#     try:
#         name, details = task.split(",")
#         contact.append([name, details])
#     except ValueError:
#         print("Invalid input Format.")

# def view_contact_list():
#     if not contact:
#         print("Contact list is empty")
#         return
#     for i, contact_info in enumerate(contact, start=1):
#         name, details = contact_info
#         print(f"{i}. Name: {name}, Details: {details}")

# def search_contact(search_item):
#     found_contact = []
#     for contact_info in contact:
#         name, details = contact_info
#         if search_item.lower() in name.lower():
#             found_contact.append(contact_info)
#     if found_contact:
#         print("Searched results: ")
#         for i, contact_info in enumerate(found_contact, start=1):
#             name, details = contact_info
#             print(f"{i}. {name}, Details: {details}")
#     else:
#         print("No contact found with that name...")

# def update_contact():
#     pass

# def delete_contact():
#     pass

# while True:
#     print("\n1. Add Contact")
#     print("2. View Contact List")
#     print("3. Search Contact")
#     print("4. Exit")
#     choice = input("What do you want to do? ")
#     if choice == "1":
#         task = input("Enter your Contact and Name: ")
#         add_contact(task)
#     elif choice == "2":
#         view_contact_list()
#     elif choice == "3":
#         search_item = input("Enter name to search: ")
#         search_contact(search_item)
#     elif choice == "4":
#         print("Contact book is exited.")
#         break
#     else:
#         print("Invalid choice. Please choose a valid option.")
#     choice = input("enter the number: ")
#     if choice == "1":
#         add_contact(task)
#     elif choice == "2":
#         view_contact_list() 

contact = []
def add_contact(add):
    try:
        name, phnumber = add.split(",")
        contact.append([name, phnumber])
    except ValueError:
        print("invalid format")
def delete_contact(num):
    try:
        del contact[num-1]
    except IndexError:
        print("invalid index")
def view_contact():
    for i, todo in enumerate(contact, start=1):
        name, phnumber = todo
        print(f"{i}. Name: {name}, phoneNumber: {phnumber}")
def search_contact(search_item):
    found_contact = []
    for todo in contact:
        name, phnumber = todo
        if search_item in name:
            found_contact.append(todo)
    if todo:
        print("Search results are: ") 
        for i, todo in enumerate(found_contact, start=1):
            name, phnumber = todo
            print(f"{i}. Name: {name},\n PhoneNumber: {phnumber}")
    else:
        print("No contact has been found of this name")           

while True:
    print("1. for Add contact")
    print("2. for Delete Contact")
    print("3. for view Contact")
    print("4. for search contact")
    print("5. for exit contact book")
    choice = input('what you want to do ?')
    if choice == "1":
        add = input("enter contact details(name, phnumber): ")
        add_contact(add)
    elif choice == "2":
        num = int(input("enter the index of contact you want to delete: "))
        delete_contact(num)
    elif choice == "3":
        view_contact()
    elif choice == "4":
        search_item = input("enter the name of contact: ")
        search_contact(search_item)
    elif choice == "5":
        break
    else:
        print("Invalid choice please choose correct input...")
print("existed Contact book")
        