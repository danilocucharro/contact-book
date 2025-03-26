import crud_agenda

contacts = []
while True:
    print("\n1. To Add a new contact")
    print("2. To see your contacts")
    print("3. To update a contact")
    print("4. To mark contact as favorite")
    print("5. To see your favorite contacts")
    print("6. To remove a contact")
    print("7. To Quit")

    choice = input("What you want to do?\n")

    if choice == "1":
        name = input("Type the contact name: ")
        phone = input("Type the contact phone: ")
        email = input("Type the contact email: ")
        crud_agenda.add_contact(contacts, name, phone, email)

    elif choice == "2":
        crud_agenda.read_contacts(contacts)

    elif choice == "3":
        crud_agenda.read_contacts(contacts)
        contact_index = input("\nFirst type the contact index you want to update: ")
        name = input("Type to edit the contact name: ")
        phone = input("Type to edit the contact phone: ")
        email = input("Type to edit the contact email: ")
        crud_agenda.update_contact(contacts, contact_index, name, phone, email)

    elif choice == "4":
        crud_agenda.read_contacts(contacts)
        contact_index = input("\nFirst type the contact index you want to turn favorite: ")
        crud_agenda.mark_contact_favorite(contacts, contact_index)

    elif choice == "5":
        crud_agenda.read_favorite_contacts(contacts)

    elif choice == "6":
        crud_agenda.read_contacts(contacts)
        contact_index = input("\n Type the index contact you want to remove: ")
        crud_agenda.remove_contact(contacts, contact_index)

    elif choice == "7":
        break

print("End.")