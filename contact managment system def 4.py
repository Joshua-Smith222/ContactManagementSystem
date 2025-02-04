import re
import os

contacts = {}
validate_phone = {} #temporary tell i pair with def 1.
validate_email = {}#temporary tell i pair with def 2.

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

