# Вимоги до завдання:
# Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') 
# та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.


import re
def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if cleaned_number.startswith('+') and len(cleaned_number) == 12:
        return cleaned_number
    elif len(cleaned_number) == 12:
        cleaned_number = '+' + cleaned_number
        return cleaned_number
    else:
        cleaned_number = '+38' + cleaned_number
        return cleaned_number


# Приклад використання:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



