#Line 2-8 temporary def
add_contact = ()
edit_contact = ()
delete_contact = ()
search_contact =()
display_contacts = ()
export_contacts = ()
import_contacts = ()

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

