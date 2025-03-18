contacts = {}

while True:
    print("\nWelcome to contact book!")
    print("Choose one of the options below:")
    print("1. Create contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. View all contacts")
    print("6. Count contacts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name of the contact: ")
        if name in contacts:
            print(f"Contact {name} already exists.")
        else:
            mobile = input("Enter mobile number: ")
            email = input("Enter mail_id: ")
            address = input("Enter address: ")
            contacts[name] = {"mobile number": mobile, "email": email, "address": address}
            print(f"Contact name {name} has been created successfully.")

    elif choice == 2:
        name = input("Enter contact name to be updated: ")
        if name in contacts:
            mobile = input("Enter new mobile number: ")
            email = input("Enter new mail_id: ")
            address = input("Enter new address: ")
            contacts[name] = {"mobile number": mobile, "email": email, "address": address}
            print(f"Contact {name} has been updated successfully.")
        else:
            print("Contact does not exist.")
            
    elif choice == 3:
        name = input("Enter contact name to be deleted: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact does not exist.")
            
    elif choice == 4:
        search_name = input("Enter contact name to be searched: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found = Name: {name}, mobile number: {contact['mobile number']}, email: {contact['email']}, address: {contact['address']}")
                found = True
        if not found:
            print("Contact not found.")
            
    elif choice == 5:
        # View all contacts
        if contacts:
            print("\nAll contacts in the contact book:")
            for name, contact in contacts.items():
                print(f"Name: {name}, mobile number: {contact['mobile number']}, email: {contact['email']}, address: {contact['address']}")
        else:
            print("No contacts available.")
            
    elif choice == 6:
        print(f"Total number of contacts in your contact book: {len(contacts)}")
        
    elif choice == 7:
        print("Exiting!")
        break
        
    else:
        print("Invalid input.")