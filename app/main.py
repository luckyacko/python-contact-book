import sys

from contact_service.contact_service import ContactService
from contact.contact import Contact

def main():
    contact_service = ContactService()

    while True:
        menue()
        choice = input(">> ")
        match choice:
            case "1":
                create_contact(contact_service)
            case "2":
                delete_contact(contact_service)
            case "3":
                find_contact(contact_service)
            case "4":
                contact_service.show_all_contacts()
            case "5":
                sys.exit()

def create_contact(contact_service):
    name = input("name: ")
    adress = input("address: ")
    number = input("number: ")
    contact = Contact(name, adress, number)
    contact_service.add_contact(contact)

def delete_contact(contact_service):
    name = input("name: ")
    contact_service.delete_contact(name)

def find_contact(contact_service):
    name = input("name: ")
    contact_service.find_contact(name)


def menue():
    print("Welcome to the contact book")
    print("Here you can add, delete and find your contacts")
    print("1. create new contact")
    print("2. delete contact")
    print("3. search for contact")
    print("4. show all ocntacts")
    print("5. exit program")



if __name__ =='__main__':
    main()