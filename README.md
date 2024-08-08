## Technical Task Description

### Task 1

Create a function `get_days_from_today(date)` that calculates the number of days between a given date and the current date.

**Task Requirements:**
- The function accepts one parameter: 
 `date` — a string representing a date in the format `'YYYY-MM-DD'` (e.g., `'2020-10-09'`).
- The function returns an integer indicating the number of days from the given date to the current date. If the given date is later than the current date, the result should be negative.
- The calculation should only consider days, ignoring hours, minutes, and seconds.
- Use the `datetime` module in Python to work with dates.


### Task 2

To win the lottery's grand prize, several numbers on a lottery ticket must match the numbers randomly drawn within a specific range during the draw. For example, you may need to guess six numbers from 1 to 49 or five numbers from 1 to 36, etc.

You need to write a function `get_numbers_ticket(min, max, quantity)` that helps generate a set of unique random numbers for such lotteries. It will return a random set of numbers within the specified parameters, ensuring all the random numbers in the set are unique.

**Task Requirements:**
- **Parameters:**
  - `min` - the minimum possible number in the set (not less than 1).
  - `max` - the maximum possible number in the set (not more than 1000).
  - `quantity` - the number of numbers to select (value must be between `min` and `max`).
- The function generates the specified number of unique numbers within the given range.
- The function returns a list of randomly selected, sorted numbers. The numbers in the set should not repeat. If the parameters do not meet the specified constraints, the function returns an empty list.


### Task 3

Your company is running an active marketing campaign using SMS messaging. To do this, you collect customer phone numbers from the database, but often encounter numbers recorded in various formats. For example:
- `"    +38(050)123-32-34"`
- `"     0503451234"`
- `"(050)8889900"`
- `"38050-111-22-22"`
- `"38050 111 22 11   "`

Your SMS service can only effectively send messages when phone numbers are presented in the correct format. Therefore, you need a function that automatically normalizes phone numbers to the required format, removing all unnecessary characters and adding the international country code if necessary.

**Task:** Develop a function `normalize_phone(phone_number)` that normalizes phone numbers to the standard format, leaving only digits and the `+` symbol at the beginning.

**Task Requirements:**
- The function parameter `phone_number` is a string containing a phone number in various formats.
- The function removes all characters except digits and the `+` symbol.
- If the international code is missing, the function adds the code `+38`. This accounts for cases where the number starts with `380` (only `+` is added) and where the number starts without a code (adds `+38`).
- The function returns the normalized phone number as a string.


### Task 4

In your organization, you are responsible for organizing birthday greetings for colleagues. To optimize this process, you need to create a function `get_upcoming_birthdays` that helps you determine which colleagues need to be congratulated. The function should return a list of all colleagues whose birthdays are within the next 7 days, including the current day.

**Task Requirements:**
- The function parameter `users` is a list of dictionaries, where each dictionary contains the keys `name` (a string representing the user's name) and `birthday` (a string representing the user's birthday in the format `'YYYY.MM.DD'`).
- The function should identify whose birthdays fall within the next 7 days, including the current day. If a birthday falls on a weekend, the congratulation date should be moved to the next Monday.
- The function returns a list of dictionaries, where each dictionary contains the user's name (`name`) and the congratulation date (`congratulation_date`), formatted as a string in the format `'YYYY.MM.DD'`.

