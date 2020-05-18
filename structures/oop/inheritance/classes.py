class Person:
    __id: int
    __fullname: object
    __age: int

    def __init__(self) -> None:
        super().__init__()

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_fullname(self):
        return self.__fullname

    def set_fullname(self, fullname):
        self.__fullname = fullname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display_info(self):
        print("ID:", self.__id)
        print("ФИО:", self.__fullname)
        print("Возраст:", self.__age)


class Employee(Person):

    def details(self, company):
        print(self.get_fullname() + " работал в компании " + company)
