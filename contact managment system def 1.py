import re
import os

def validate_phone(phone):
    # Allow optional spaces, dashes, or parentheses in the phone number.
    # The phone number should start with an optional '+' followed by digits and allow spaces/dashes between numbers.
    return re.match(r"^\+?\(?\d{1,3}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$", phone) is not None
