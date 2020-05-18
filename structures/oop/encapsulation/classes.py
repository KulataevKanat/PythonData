# 1
class Person:
    __name: object
    __age: object

    def __init__(self) -> None:
        super().__init__()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age in range(0, 120):
            self.__age = age
        else:
            print("Недопустимый возвраст")

    def get_age(self):
        return self.__age


# 2
class Table:
    __name: object
    __color: object

    def __init__(self,) -> None:
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
