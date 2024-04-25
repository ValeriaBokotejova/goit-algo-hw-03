# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime
def get_days_from_today(date: str) -> int:
    input_date = datetime.strptime(date, '%Y-%m-%d')
    today_date = datetime.today()
    if input_date > today_date:
        days_from_today = input_date - today_date
    else:
        days_from_today = today_date - input_date
        return -days_from_today.days
    return days_from_today.days
date = '2022-06-05'
print(get_days_from_today(date))