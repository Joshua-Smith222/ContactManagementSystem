import re
import os

def validate_phone(phone):
    return re.match(r"^\+?[1-9]\d{1,14}$", phone) is not None
