class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(new_contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact["name"].lower() or keyword.lower() in contact["phone"].lower()]
        for result in results:
            print(f"Name: {result['name']}, Phone: {result['phone']}")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                if new_phone:
                    contact["phone"] = new_phone
                if new_email:
                    contact["email"] = new_email
                if new_address:
                    contact["address"] = new_address
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"].lower() != name.lower()]

    def display_menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == 2:
                self.view_contact_list()
            elif choice == 3:
                keyword = input("Enter name or phone to search: ")
                self.search_contact(keyword)
            elif choice == 4:
                name = input("Enter name of contact to update: ")
                new_phone = input("Enter new phone (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")
                self.update_contact(name, new_phone, new_email, new_address)
            elif choice == 5:
                name = input("Enter name of contact to delete: ")
                self.delete_contact(name)
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.display_menu()