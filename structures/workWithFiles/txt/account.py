from workWithFiles.txt.accountSettings import *

FILENAME = "G:\Python BackEnd\WorkWithFiles\\txt\Account.txt"

reg = list()
reg.append("Имя: " + name + "\n" +
           "Фамилия: " + surname + "\n" +
           "Отчество: " + patronymic + "\n" +
           "Дата рождения: " + dateOfBirth + "\n" +
           "Номер телефона: " + "+" + str(phone))

with open(FILENAME, "w") as file:
    for i in reg:
        file.write(i)

with open(FILENAME, "r") as fileRead:
    read = fileRead.read()
    print("\n" + read)
