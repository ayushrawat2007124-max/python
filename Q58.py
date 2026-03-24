''' 6.	Create a contact book where users can store, search, update, and delete contacts. Use dictionary for storing contacts.'''
contacts = {}

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Add Contact
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    # Search Contact
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found!")

    # Update Contact
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Display All Contacts
    elif choice == '5':
        if contacts:
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("Contact book is empty!")

    # Exit
    elif choice == '6':
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice! Please try again.")