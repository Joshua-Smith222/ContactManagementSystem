contacts = {}

def search_contact():
    phone = input("Enter the phone number of the contact to search: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Name: {contact['name']}, Phone: {phone}, Email: {contact['email']}, Address: {contact['address']}, Notes: {contact['notes']}")
    else:
        print("Contact not found.")
