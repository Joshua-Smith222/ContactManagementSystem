import re
import os

# Contact data storage
contacts = {}

# Function to validate phone numbers using regex
import phonenumbers
from phonenumbers import NumberParseException

def validate_phone(phone, default_country='US'):
    try:
        # Parse the phone number with the provided country code
        parsed_phone = phonenumbers.parse(phone, default_country)

        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_phone):
            print("Invalid phone number format. Please enter a valid phone number.")
            return None

        # Format the phone number into international format
        formatted_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        return formatted_phone
    except NumberParseException as e:
        print(f"Error parsing phone number: {e}. Please enter a valid phone number.")
        return None

# Function to validate email addresses using regex
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for phone, details in contacts.items():
        print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}")

# Function to add a new contact
def add_contact(phone=None):
    if not phone:
        # Prompt for phone number only once and ensure it's valid
        while True:
            phone = input("Enter phone number: ")
            if validate_phone(phone) and phone not in contacts:
                break
            elif phone in contacts:
                print("This phone number is already in use. Please enter a different phone number.")
            else:
                print("Invalid phone number. Please enter a valid phone number.")

    name = input("Enter name: ")

    email = input("Enter email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter email address: ")

    address = input("Enter address: ")
    notes = input("Enter any notes: ")

    # Add the new contact to the contacts dictionary
    contacts[phone] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }

    print(f"Contact for {name} added successfully!")


# Function to edit an existing contact
def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")

    if phone not in contacts:
        print("Contact not found.")
        return

    print("Editing contact...")

    # Prompt user to edit the phone number (with validation)
    new_phone = input(f"Enter new phone number (current: {phone}): ")
    while new_phone != phone and new_phone in contacts:
        print("This phone number is already in use. Please enter a different phone number.")
        new_phone = input(f"Enter new phone number (current: {phone}): ")
    while not validate_phone(new_phone):
        print("Invalid phone number. Please enter a valid phone number.")
        new_phone = input(f"Enter new phone number (current: {phone}): ")

    # If the phone number is changed, update the contact in the dictionary
    if new_phone != phone:
        contacts[new_phone] = contacts.pop(phone)
        phone = new_phone  # Update phone to the new value

    # Edit the other contact details
    name = input(f"Enter new name (current: {contacts[phone]['name']}): ")
    email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input(f"Enter new email (current: {contacts[phone]['email']}): ")

    address = input(f"Enter new address (current: {contacts[phone]['address']}): ")
    notes = input(f"Enter new notes (current: {contacts[phone]['notes']}): ")

    # Update the contact details
    contacts[phone] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }

    print("Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone not in contacts:
        print("Contact not found.")
        return
    del contacts[phone]
    print("Contact deleted successfully!")

# Function to search for a contact
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

# Function to export contacts to a text file
def export_contacts():
    try:
        with open('contacts.txt', 'w') as file:
            for phone, details in contacts.items():
                file.write(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}\n")
        print("Contacts exported successfully to 'contacts.txt'.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")

# Function to import contacts from a text file
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

# Function to display the menu and handle user input
def show_menu():
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file (BONUS)")
        print("8. Quit")

        choice = input("Please select an option (1-8): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    show_menu()
