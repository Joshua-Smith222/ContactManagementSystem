contacts = {}
validate_email = {}#temporary place marker.

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone not in contacts:
        print("Contact not found.")
        return
    print("Editing contact...")
    name = input(f"Enter new name (current: {contacts[phone]['name']}): ")
    email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input(f"Enter new email (current: {contacts[phone]['email']}): ")

    address = input(f"Enter new address (current: {contacts[phone]['address']}): ")
    notes = input(f"Enter new notes (current: {contacts[phone]['notes']}): ")

    contacts[phone] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact updated successfully!")
