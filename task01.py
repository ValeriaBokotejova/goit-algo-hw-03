from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        difference = input_date - today
        return difference.days
    except ValueError:
        print("Error: Date format should be 'YYYY-MM-DD'")
        return None

# Date example showing positive day difference
positive_difference = "2035-01-01"
print(f"Positive difference: {get_days_from_today(positive_difference)}")

# Date example showing negative day difference
negative_difference = "2020-01-01"
print(f"Negative difference: {get_days_from_today(negative_difference)}")

# Example date with an incorrect date format
incorrect_date_format = "01-01-1990"
get_days_from_today(incorrect_date_format)