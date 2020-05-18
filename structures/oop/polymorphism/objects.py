from oop.polymorphism.classes import Animal, Dog, Cat

animal = Animal("animal-name")
animal.make_a_sound()
animal.display_info()
dog = Dog("Shnaps")
dog.make_a_sound()
dog.display_info()
cat = Cat("Oleg")
cat.make_a_sound()
cat.display_info()

print()

animals = [Animal("animal-name"), Dog("Shnaps"), Cat("Oleg")]

for animal in animals:
    if isinstance(animal, Dog):
        print(dog.name)
    elif isinstance(animal, Cat):
        print(cat.name)
    else:
        print(animal.name)
