

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
