class Animal:
    name: str

    def __init__(self, name) -> None:
        self.name = name

    @staticmethod
    def make_a_sound():
        return print("animal-sound")

    def display_info(self):
        print("Name:", self.name)


class Dog(Animal):

    @staticmethod
    def make_a_sound():
        return print("Гав-Гав")


class Cat(Animal):

    @staticmethod
    def make_a_sound():
        return print("Мяу...")
