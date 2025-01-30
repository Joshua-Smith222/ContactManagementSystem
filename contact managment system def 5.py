contacts = {}
validate_email = {}#temporary place marker.
validate_phone = {}

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

    # Present a menu of editable fields
    print("\nWhat would you like to edit?")
    print("1. Name")
    print("2. Email")
    print("3. Address")
    print("4. Notes")
    print("5. All")
    print("6. Cancel")

    selected_options = input("Enter the numbers of the fields you want to edit (comma separated): ").split(",")

    # Strip any leading/trailing spaces from input
    selected_options = [option.strip() for option in selected_options]

    # Edit name if selected
    if '1' in selected_options:
        name = input(f"Enter new name (current: {contacts[phone]['name']}): ")
        contacts[phone]['name'] = name

    # Edit email if selected
    if '2' in selected_options:
        email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
        while not validate_email(email):
            print("Invalid email address. Please enter a valid email.")
            email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
        contacts[phone]['email'] = email

    # Edit address if selected
    if '3' in selected_options:
        address = input(f"Enter new address (current: {contacts[phone]['address']}): ")
        contacts[phone]['address'] = address

    # Edit notes if selected
    if '4' in selected_options:
        notes = input(f"Enter new notes (current: {contacts[phone]['notes']}): ")
        contacts[phone]['notes'] = notes

    # If the user selected "All" option, prompt for all fields
    if '5' in selected_options:
        name = input(f"Enter new name (current: {contacts[phone]['name']}): ")
        contacts[phone]['name'] = name
        email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
        while not validate_email(email):
            print("Invalid email address. Please enter a valid email.")
            email = input(f"Enter new email (current: {contacts[phone]['email']}): ")
        contacts[phone]['email'] = email
        address = input(f"Enter new address (current: {contacts[phone]['address']}): ")
        contacts[phone]['address'] = address
        notes = input(f"Enter new notes (current: {contacts[phone]['notes']}): ")
        contacts[phone]['notes'] = notes

    # Confirm the update
    print("\nContact updated successfully!")

