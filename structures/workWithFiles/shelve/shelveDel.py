import shelve

FILENAME = "G:\Python BackEnd\WorkWithFiles\shelve\shelveWrite"

print("Удаления значения по ключю.(В случае отсутствия, исключение) :")
with shelve.open(FILENAME) as fileDel:
    value = fileDel.pop("Test10", "NotFound")
    print(value)

print("\n\n-----------------------------------------")

print("Удаление значения методом \"del\":")
with shelve.open(FILENAME) as fileValue:
    del fileValue["Test2"]  # удаляем объект с ключом Test1
    print("объект удалён")

print("\n\n-----------------------------------------")
with shelve.open(FILENAME) as fileAllDel:
    fileAllDel.clear()
    print("Данные с файла ", fileAllDel, " удалены.")
