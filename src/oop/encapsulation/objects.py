from oop.encapsulation.classes import Person, Table

print("class Person: ")
person = Person()
person.set_name("Канат")
person.set_age(18)
print(person.get_name())
print(person.get_age())

print("\nclass Table: ")
table = Table()
table.name = "Компьютерный"
table.color = "Коричневый"
print(table.name)
print(table.color)
