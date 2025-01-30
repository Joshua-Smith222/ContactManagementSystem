contacts = {}
add_contact = {}#temporary

def search_contact():
    phone = input("Enter the phone number of the contact to search: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Name: {contact['name']}, Phone: {phone}, Email: {contact['email']}, Address: {contact['address']}, Notes: {contact['notes']}")
    else:
        print("Contact not found.")
        add_option = input("Would you like to add this contact? (y/n): ").lower()
        if add_option == 'y':
            add_contact(phone)
        else:
            print("Contact not added.")
