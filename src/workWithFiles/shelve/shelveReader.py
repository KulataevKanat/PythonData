import shelve

FILENAME = "G:\Python BackEnd\WorkWithFiles\shelve\shelveWrite"

print("\nВывод значения по ключу: ")
with shelve.open(FILENAME) as file:
    key = "Test1"
    if key in file:
        print(file[key])

print("\n-----------------------------------------")

print("Вывод значения по ключю.(В случае отсутствия, исключение) :")
with shelve.open(FILENAME) as fileGet:
    value = fileGet.get("Test9", "Undefined")
    print(value)

print("\n\n-----------------------------------------")

print("Вывод всех данных:")
with shelve.open(FILENAME) as fileAllGet:
    for key in fileAllGet:
        print(key, " - ", fileAllGet[key])

print("\n\n-----------------------------------------")

print("Вывод данных по  ключу и значению: ")
with shelve.open(FILENAME) as filesGetByKeyAndValues:
    print("По ключу: ")
    for key in filesGetByKeyAndValues.keys():
        print(key, end=", ")
    print("\nПо значению: ")
    for value in filesGetByKeyAndValues.values():
        print(value, end=", ")

print("\n\n-----------------------------------------")

print("Вывод кортежей: ")
with shelve.open(FILENAME) as fileTuples:
    for turple in fileTuples.items():
        print(turple)
