def add_contact(contact_list, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "is_favorite": False
    }
    contact_list.append(contact)
    print(f"{name} has been added successfully!")

def read_contacts(contact_list):
    print("Your contacts:")
    for index, contact in enumerate(contact_list, start=1):
        favorite_status = "★" if contact["is_favorite"] else " "
        contact_name = contact["name"]
        contact_phone = contact["phone"]
        contact_email = contact["email"]

        print(f"{index}, {contact_name}, {contact_phone}, {contact_email} | favorite[{favorite_status}]")

def update_contact(contact_list, contact_index, new_name, new_phone, new_email):
    adjusted_contact_index = int(contact_index) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contact_list):
        contact_list[adjusted_contact_index]["name"] = new_name
        contact_list[adjusted_contact_index]["phone"] = new_phone
        contact_list[adjusted_contact_index]["email"] = new_email
        print("\nThe contact has been updated successfully!")

def mark_contact_favorite(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contact_list):
        contact_list[adjusted_contact_index]["is_favorite"] = True
        contact_name = contact_list[adjusted_contact_index]["name"]
        print(f"\nNow {contact_name} is a favorite contact!")

def read_favorite_contacts(contact_list):
    print("Your favorite contacts:")
    for index, contact in enumerate(contact_list, start=1):
        favorite_status = "★" if contact["is_favorite"] else " "
        contact_name = contact["name"]
        contact_phone = contact["phone"]
        contact_email = contact["email"]

        if contact["is_favorite"]:
            print(f"{index}, {contact_name}, {contact_phone}, {contact_email} | favorite[{favorite_status}]")

def remove_contact(contact_list, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    contact_name = contact_list[adjusted_contact_index]["name"]
    contact_list.pop(adjusted_contact_index)
    print(f"{contact_name} has been removed from your contacts.")