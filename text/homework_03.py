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
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def find_next_weekday(d, weekday:int):
  days_ahead = weekday - d,weekday()
  if days_ahead <= 0:
    days_ahead += 7
  return d + timedelta(days=days_ahead)

def prepared_users() -> list:
 for user in users: 
    try:
      birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
      prepared_users.append({"name": user['name'], 'birthday': birthday})
    except ValueError:
      print(f'Некоректна дата народження для користувача {user["name"]}')

day = 7
today = datetime.today().date()
upcoming_birthdays = []

for user in prepared_users:
  birthday_this_year = user["birthday"]. replace(year=today.year)

  if birthday_this_year < today:
    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    if 0 <= (birthday_this_year - today).days <= day:
      if birthday_this_year.weekday() >= 5:
        birthday_this_year = find_next_weekday(birthday_this_year, 0)

    congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
    upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

print(upcoming_birthdays)