contacts = {}#temporary

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone not in contacts:
        print("Contact not found.")
        return
    del contacts[phone]
    print("Contact deleted successfully!")
