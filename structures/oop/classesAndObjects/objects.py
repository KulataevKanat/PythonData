from oop.classesAndObjects.classes import Person, Table, Notebook

print("Person class: ")
person1 = Person("Kanat", "Kulataev", "Almazbeckovich", "04/06/2001")
person2 = Person("Bektur", "Muratov", "Almazbeckovich", "26/06/1994")

person1.display_info()
print()
person2.display_info()

print("\nTable class: ")
table1 = Table("Компьютерный", "Дерево", "Коричневый")
table2 = Table("Офисный", "Металл", "Белый")
table3 = Table("Журнальный", "ДСП", "Бордовый")

table1.display_info()
print()
table2.display_info()
print()
table3.display_info()

print("\nNotebook class: ")
notebook1 = Notebook("Lenovo IdeaPad 320", 8, "NVIDIA® GeForce® 920MX", "Intel® Core™ i7 6-го поколения", "Белый")
notebook2 = Notebook("Acer ASPIRE 5", 4, " Intel UHD Graphics 620", "Intel® Core™ i5-8250U", "чёрный")

notebook1.display_info()
print()
notebook2.display_info()