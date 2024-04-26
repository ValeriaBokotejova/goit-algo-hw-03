# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, 
# кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про 
# ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, 
# ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

# Вимоги до завдання:
# Параметр функції users - це список словників, де кожен словник містить ключі name 
# (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. 
# Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію 
# про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
     
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:

        users_birthdays = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

# перевірка чи був вже день народження в цьому році, якщо так - перенесення на наступний рік
        birthday_this_year = users_birthdays.replace(year=today.year)
        if birthday_this_year < today:
            users_birthdays = users_birthdays.replace(year=today.year + 1)
# якщо день народження в майбутнбому в цьому році, то і вітання буде в цьому році а не через рік
        else:
            users_birthdays = birthday_this_year
                   
# перевірка та перенесення дня народження на понеділок якщо він випадає на вихідний
        days_until_birthday = (users_birthdays - today).days
        if 0 <= days_until_birthday <= 7:
            if users_birthdays.weekday() >= 5:
                users_birthdays += timedelta(days=(7 - users_birthdays.weekday()))
        
# додавання користувача до списку з майбутніми днями народження
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": users_birthdays.strftime("%Y.%m.%d")})

    return upcoming_birthdays


# Приклад:
# cписок users:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Test 1", "birthday": "1990.04.27"},
    {"name": "Test 2", "birthday": "1990.04.26"},
    {"name": "Test 3", "birthday": "1990.04.30"}
]

# Використання функції get_upcoming_birthdays:
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)