import datetime

print("Date: ")
print("Выставление даты: ")
yesterday = datetime.date(2020, 5, 18)
print(yesterday)  # 2020-05-18

print("\nПолучение текущей даты: ")

today = datetime.date.today()
print(today)
print("Форматирование даты по своему: ")
print("{}/{}/{}".format(today.day, today.month, today.year))

from datetime import time

print("\nTime: ")
print("Выставление времени: ")
print("Метод без параметров: ")
current_time = time()
print(current_time)  # 00:00:00

print("Метод c параметрами(часы:минуты): ")
current_time = time(9, 47)
print(current_time)  # 9:47:00

print("Метод c параметрами(часы:минуты:секунды): ")
current_time = time(9, 48, 10)
print(current_time)  # 9:48:10

from datetime import datetime

print("\nDateTime: ")
print("Выставление даты: ")
deadline = datetime(2020, 5, 18)
print(deadline)  # 2020-05-18 00:00:00

print("Выставление даты и времени: ")
deadline = datetime(2020, 5, 18, 9, 52)
print(deadline)  # 2020-05-18 9:52:00

print("\nПолучение текущей даты и времени:")
now = datetime.now()
print(now)

print("Форматирование даты и времени по своему: ")
print("{}/{}/{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))

print("Получение текущей даты: ")
print(now.date())
print("Получение текущей времени: ")
print(now.time())

print("\n-----------------------------------------")

print("\nПреобразование из строки в дату: ")
print("\"18/05/2020\": ")
deadline = datetime.strptime("18/05/2020", "%d/%m/%Y")
print(deadline)  # 2020-05-18 00:00:00

print("\n\"18/05/2020\" \"9:58\": ")
deadline = datetime.strptime("18/05/2020 9:58", "%d/%m/%Y %H:%M")
print(deadline)  # 2020-05-18 9:58:00

print("\n\"05-18-2020\" \"10:01\":")
deadline = datetime.strptime("05-18-2020 10:01", "%m-%d-%Y %H:%M")
print(deadline)  # 2020-05-18 10:01:00
