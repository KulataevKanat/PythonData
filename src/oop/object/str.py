class Car:

    def __init__(self, id, mark, color, model, dateOfManufacture) -> None:
        self.id = id
        self.mark = mark
        self.color = color
        self.model = model
        self.dateOfManufacture = dateOfManufacture

    def display_info(self):
        print(self.__str__)

    def __str__(self) -> str:
        return "\n id: {} \n Марка: {} \n Цвет: {} \n Модель: {} \n Дата начала-окончания производства: {}" \
            .format(self.id, self.mark, self.color, self.model, self.dateOfManufacture)


class Main:
    car1 = Car("10", "Tesla", "Белый", "X 100D", "Январь 2015 - В производстве")
    print(car1.__str__())

    car2 = Car("36", "Toyota", "Чёрный", "Camry", "Январь 2014 - Январь 2017")
    print(car2.__str__())

    car3 = Car("43", "Ford", "Серый", "Mustang Shelby GT 500", "Январь 2009 - Январь 2011")
    print(car3.__str__())

    car4 = Car("16", "Nissan", "Красный", "GT-R", "Январь 2016 - В производстве")
    print(car4.__str__())
