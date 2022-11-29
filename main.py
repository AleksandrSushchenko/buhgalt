from application.salary import *
from application.db.people import *
import datetime
import requests



calculate_salary()
get_employees()

day = datetime.date(1986,9,11)
print(day)

today = datetime.date.today()
print(today)

x = day.isocalendar()
y = today.isocalendar()

for i in x:
    break

for j in y:
    break

year = j - i

print(year)

print(requests.get("https://yandex.ru"))