from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Get the birthday date for this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If the birthday already occurred this year, consider the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        
        # Check if the birthday is within the next 7 days
        if 0 <= days_until_birthday <= 7:
            # If the birthday falls on a weekend, move it to the next Monday
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": user["name"], 
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Example:
users = [
    {"name": "John Doe", "birthday": "1985.05.23"},
    {"name": "Jane Smith", "birthday": "1990.09.27"},
    {"name": "Test 1", "birthday": "1990.08.10"},
    {"name": "Test 2", "birthday": "1990.08.16"},
    {"name": "Test 3", "birthday": "1990.08.11"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of congratulations for this week:")
print("Name                 | Congratulation Date")
print("---------------------|-------------------")

for birthday in upcoming_birthdays:
    print(f"{birthday['name']:<20} | {birthday['congratulation_date']}")