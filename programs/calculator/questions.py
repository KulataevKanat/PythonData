class Questions:
    __firstValue = "Введите первое число:"
    __secondValue = "Введите второе число:"
    __mathSign = "Введите знак операции (+,-,*,/):"

    def __init__(self) -> None:
        super().__init__()

    def getFirstValue(self):
        return self.__firstValue

    def getSecondValue(self):
        return self.__secondValue

    def getMathSign(self):
        return self.__mathSign
