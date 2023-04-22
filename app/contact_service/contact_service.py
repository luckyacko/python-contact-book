

class ContactService:
    def __init__(self) -> None:
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def delete_contact(self, name):
        for contact in self.contacts:
            if name == contact.name:
                self.contacts.remove(contact)
                return True
        return False

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("--------------------------------")
                print(f"contact name:{contact.name}")
                print(f"contact adress:{contact.adress}")
                print(f"contact number{contact.number}")
                print("--------------------------------")
                return
        print("contact not found")

    def show_all_contacts(self):
        for contact in self.contacts:
            print("--------------------------------")
            print(f"contact name:{contact.name}")
            print(f"contact adress:{contact.adress}")
            print(f"contact number{contact.number}")
            print("--------------------------------")