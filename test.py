import phonenumbers
from phonenumbers import NumberParseException

def validate_phone(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, 'US')  # Assuming default country is US
        if phonenumbers.is_valid_number(parsed_phone):
            print(f"Valid number: {phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        else:
            print("Invalid phone number.")
    except NumberParseException as e:
        print(f"Error parsing phone number: {e}")

# Test with a phone number
validate_phone("+14155552671")  # Example US number
