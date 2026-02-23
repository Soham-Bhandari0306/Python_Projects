contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()


def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if contact['name'].lower() == search_name:
            print(f"\n Found Contact:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}\n")
            found = True
            break

    if not found:
        print(" Contact not found.\n")


def delete_contact():
    delete_name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact['name'].lower() == delete_name:
            contacts.remove(contact)
            print(" Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def main():
    while True:
        print(" Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.\n")


main()
