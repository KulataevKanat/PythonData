name = input("Имя: ")

surname = input("Фамилия: ")

patronymic = input("Отчество: ")

dateOfBirth = input("Дата рожджения: ")

while True:
    try:
        phone = int(input("Номер телефона: "))
        break
    except:
        print("Номер телефона только в числовом значении")
