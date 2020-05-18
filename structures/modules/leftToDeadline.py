from datetime import datetime

now = datetime.now()
print("Введите дату окончания дедлайна в формате \"01/01/2020\"")
deadlineInput = input("-> ")
deadline = datetime.strptime(deadlineInput, "%d/%m/%Y")
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Дней осталось - {} ".format(period.days))
