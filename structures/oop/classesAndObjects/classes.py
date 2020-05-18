class Person:

    def __init__(self, name, surname, patronymic, dateOfBirth) -> None:
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.dateOfBirth = dateOfBirth

    def display_info(self):
        print("Имя: " + self.name)
        print("Фамилия: " + self.surname)
        print("Отчество: " + self.patronymic)
        print("Дата рождения: " + self.dateOfBirth)


class Table:

    def __init__(self, name, material, color) -> None:
        self.name = name
        self.material = material
        self.color = color

    def display_info(self):
        print("Название стола: " + self.name)
        print("Материал стола: " + self.material)
        print("Цвет стола: " + self.color)


class Notebook:

    def __init__(self, name, RAM, graphicsСard, CPU, color) -> None:
        self.name = name
        self.RAM = RAM
        self.graphicsCard = graphicsСard
        self.CPU = CPU
        self.color = color

    def display_info(self):
        print("Название Ноутбука: " + self.name)
        print("Оперативная память:", self.RAM, "гб")
        print("Видеокарта: " + self.graphicsCard)
        print("Процессор: " + self.CPU)
        print("Цвет Ноутбука: " + self.color)
