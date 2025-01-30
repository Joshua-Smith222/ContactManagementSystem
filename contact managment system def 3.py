import re
import os

contacts = {}

def display_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for phone, details in contacts.items():
        print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Notes: {details['notes']}")
