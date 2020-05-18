from datetime import datetime
import locale
from datetime import timedelta

print("Datetime format: ")
print("Текущая дата: ")
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print("Полный год:")
print(now.strftime("%d/%m/%Y"))
print("Сокращенный год:")
print(now.strftime("%d/%m/%y"))
print("Текущая дата с названием месяца и Текущий день недели:")
print(now.strftime("%d %B %Y (%A)"))
print("Текущая дата и время(ч:м):")
print(now.strftime("%d/%m/%y %I:%M"))

print("\n-----------------------------------------")

print("\nLocale: ")
print("Изменение языка(русский): ")
locale.setlocale(locale.LC_ALL, "")

now = datetime.now()
print(now.strftime("%d %B %Y (%A)"))

print("\nTimedelta: ")
print("Изменение даты, времени и т.д.:")
three_hours = timedelta(hours=3)
print(three_hours)  # 3:00:00
three_hours_thirty_minutes = timedelta(hours=3, minutes=30)  # 3:30:00
print(three_hours_thirty_minutes)
two_days = timedelta(2)  # 2 days, 0:00:00
print(two_days)
two_days_three_hours_thirty_minutes = timedelta(days=2, hours=3, minutes=30)  # 2 days, 3:30:00
print(two_days_three_hours_thirty_minutes)

print("\nСложение дат: ")
now = datetime.now()
print(now)
two_days = timedelta(2)
in_two_days = now + two_days
print("Текущая дата + 2 дня =", in_two_days)

print("\nВычитание времени: ")
now = datetime.now()
till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
print("Текущее время - 10:15 =", till_ten_hours_fifteen_minutes.time())

print("\nВременной промежуток между двумя датами:")
now = datetime.now()
twenty_two_may = datetime(2020, 5, 22)
period = twenty_two_may - now
print("Между датой \"2020/05/22\" и текущей -",
      "{} дня  {} секунд  {} микросекунд".format(period.days, period.seconds, period.microseconds))

print("В секундах: ")
print("Всего: {} секунд".format(period.total_seconds()))