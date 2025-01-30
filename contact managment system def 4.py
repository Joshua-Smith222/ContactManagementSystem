import re
import os

contacts = {}
validate_phone = {} #temporary tell i pair with def 1.
validate_email = {}#temporary tell i pair with def 2.

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter a valid phone number.")
        phone = input("Enter phone number: ")

    email = input("Enter email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter email address: ")

    address = input("Enter address: ")
    notes = input("Enter any notes: ")

    contacts[phone] = {
        'name': name,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully!")
