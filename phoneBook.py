def save_contact():
    name = input("Enter the contact's name: ")
    number = input("Enter the contact's number: ")
    phonebook = (name,  number)
    print(f"Saved contact {name} with number {number}.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in phonebook:
        del phonebook
        print(f"Deleted contact {name}.")
    else:
        print(f"No contact found with name {name}.")

def search_contacts():
    name = input("Enter the name of the contact to search for: ")
    if name in phonebook:
        print(f"The number is {name} .")
    else:
        print(f"No contact found with name {name}.")

def call_register():
    print("Call register:")
    for name, number in phonebook.items():
        print(f"Name: {name}, Number: {number}")


while True:
    print("\n1. Save Contact\n 2. Delete Contact\n 3. Search Contacts\n 4. Call Register\n 5. Quit")
    print("*********************")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        save_contact()
    elif choice == 2:
        delete_contact()
    elif choice == 3:
        search_contacts()
    elif choice == 4:
        call_register()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please choose a valid option.")
