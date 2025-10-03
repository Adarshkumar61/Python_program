contact = []
def create_con(create):
    try:
        name, phnumber, email = create.split()
        contact.append([name, phnumber, email])
    except IndexError:
        print("wrong input format..")
        
def view_con():
    if not contact:
        print("list is empty")
    for i, todo in enumerate(contact, start=1):
        name, phnumber, email = todo
        print(f"{i}. name: {name}\n phone number: {phnumber}\n Email: {email}")    
        
def update():
    number = input("enter the contact name for updation: ")
    found_contact = []
    for todo in contact:
        name, phnumber, email = todo
        if number in name:
            found_contact = todo
            break
    if found_contact:
        print("Enter the updated details for update..")
        name = input("enter the updated name: ")
        phnumber = input("enter the updated mobile number: ")
        email = input("enter the updated email: ")
        index = contact.index(found_contact)
        contact[index] = name, phnumber, email
        print("Updation succesfull..")
    else:
        print("Contect not matched..")
        
def search(number):
    found_contact = []
    for todo in contact:
        name, phnumber, email = todo
        if number in name:
           found_contact.append(todo)
    if todo:
        print("your search results are:")
        for i, todo in enumerate (found_contact, start=1):
            name, phnumber, email = todo
            print(f"{i}. name: {name}\n Phone number: {phnumber}\n Email: {email}")
    else:
        ("no contact matched....")        
           
def delete(cont_number):
    try:
        del contact[cont_number - 1]
    except IndexError:
        print("wrong format...")
        
while True:
    print("1. create contact..")
    print("2. View contact..")
    print("3. update Contact..")
    print("4. Contact Search...")
    print("5. contact delete..")
    print("6. for quit contact app..")
    choice = input("Enter what do u want to do (1,2,3,4,5,6): ")
    
    if choice == "1":
        create = input("enter details (name, phnumber, email): ")
        create_con(create)
        
    elif choice == "2":
        view_con()
        
    elif choice == "3":
        update()
        
    elif choice == "4":
        number = input("enter the name: ")
        search(number)
        
    elif choice == "5":
        cont_number = int(input("enter the contact index you want to delete(index starts from 1 here): "))
        delete(cont_number)
    
    elif choice == "6":
        break
    
    else:
        print("invalid input please inter corret input") 