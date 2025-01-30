contacts = {}

def export_contacts():
    try:
        with open('contacts.txt', 'w') as file:
            for phone, details in contacts.items():
                file.write(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}\n")
        print("Contacts exported successfully to 'contacts.txt'.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")
