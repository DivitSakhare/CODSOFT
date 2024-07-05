class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("\nContact List:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contact found.")
            return

        print("\nSearch Results:")
        for contact in results:
            self.display_contact(contact)

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("Current details:")
                self.display_contact(contact)
                name = input("Enter new name (leave blank to keep current): ") or contact.name
                phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                email = input("Enter new email (leave blank to keep current): ") or contact.email
                address = input("Enter new address (leave blank to keep current): ") or contact.address
                contact.name, contact.phone, contact.email, contact.address = name, phone, email, address
                print("Contact updated.")
                return
        print("No contact found.")

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.pop(i)
                print(f"Contact '{contact.name}' deleted.")
                return
        print("No contact found.")

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")
        print("-" * 20)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                contact = Contact(name, phone, email, address)
                contact_book.add_contact(contact)
            elif choice == 2:
                contact_book.view_contacts()
            elif choice == 3:
                search_term = input("Enter name or phone to search: ")
                contact_book.search_contact(search_term)
            elif choice == 4:
                search_term = input("Enter name or phone to update: ")
                contact_book.update_contact(search_term)
            elif choice == 5:
                search_term = input("Enter name or phone to delete: ")
                contact_book.delete_contact(search_term)
            elif choice == 6:
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
