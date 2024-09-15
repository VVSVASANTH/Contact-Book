class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def display_contact(self):
        for contact in self.contacts:
            print(contact)
            
            
def main():
    Contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Quit")
        
        choice = input("Enter the choice: ")
        
        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            contact = Contact(name, phone, email)
            Contact_book.add_contact(contact)
            print("Contact added.")
            
        elif choice == "2":
            name = input("Enter the name of the contact to delete: ")
            Contact_book.delete_contact(name)
            print("Contact deleted.")
            
        elif choice == "3":
            name = input("Enter the name to search: ")
            contact = Contact_book.search_contact(name)
            if contact:
                print("Contact found: ")
                print(contact)
            else:
                print("Contact not found.")
                
        elif choice == "4":
            print("\nAll Contacts: ")
            Contact_book.display_contact()
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid Choice. Please try again.")
            
if __name__ == "__main__":
    main()
    