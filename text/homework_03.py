   #Перше завдання
from datetime import datetime

def get_days_from_today(date):
     try:
         if isinstance(date, str):
             some_day = datetime.strptime(date, '%Y-%m-%d')
         else:
            some_day = date
     except ValueError:
        return None 

     today = datetime.now()
     date_difference = today - some_day

     return date_difference.days


   #Друге завдання
from random import randint, sample

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
  if not (1 <= min <= max <= 1000):
    return []
  if not (1 <= quantity <= max - min + 1):
    return []

  numbers = set()
  while len(numbers) < quantity:
    numbers.add(randint(min, max))

  return sorted(numbers)


   #Четверте завдання
from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.08.27"}, 
    {"name": "Joana Jith", "birthday": "1998.03.10"}
]

def find_next_weekday(d, weekday: int):
    """Finds the next weekday (0 for Monday) from a given date."""
    days_ahead = (weekday - d.weekday()) % 7 
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)

def prepared_users() -> list:
    """Prepares a list of users with their birthday date objects.
    Handles potential invalid birthday formats."""
    prepared_data = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_data.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')
    return prepared_data

day = 7 
today = datetime.today().date()
upcoming_birthdays = []

prepared_users_list = prepared_users() 

for user in prepared_users_list:
    birthday_this_year = user["birthday"].replace(year=today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    if 0 <= (birthday_this_year - today).days <= day:
        if birthday_this_year.weekday() >= 5:
            birthday_this_year = find_next_weekday(birthday_this_year, 0)

    congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
    upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

print(upcoming_birthdays)
