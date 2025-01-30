import os
contacts = {}

def import_contacts():
    try:
        if not os.path.exists('contacts.txt'):
            print("No contacts file found.")
            return
        with open('contacts.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                phone = parts[0].split(': ')[1]
                name = parts[1].split(': ')[1]
                email = parts[2].split(': ')[1]
                address = parts[3].split(': ')[1]
                notes = parts[4].split(': ')[1]

                contacts[phone] = {
                    'name': name,
                    'email': email,
                    'address': address,
                    'notes': notes
                }
        print("Contacts imported successfully.")
    except Exception as e:
        print(f"Error importing contacts: {e}")
