import re

def normalize_phone(phone_number):
        
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    if cleaned_number.startswith('+') and len(cleaned_number) == 13:
        return cleaned_number
    elif cleaned_number.startswith('380') and len(cleaned_number) == 12:
        cleaned_number = '+' + cleaned_number
        return cleaned_number
    elif not cleaned_number.startswith('+') and len(cleaned_number) == 10:
        return '+38' + cleaned_number
    else:
        raise ValueError(f"Invalid phone number format: {phone_number}")


# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS distribution:", sanitized_numbers)



