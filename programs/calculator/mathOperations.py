class MathOperations:
    __plus = "+"
    __minus = "-"
    __multiplication = "*"
    __division = "/"

    def __init__(self) -> None:
        super().__init__()

    def getPlus(self):
        return self.__plus

    def getMinus(self):
        return self.__minus

    def getMultiplication(self):
        return self.__multiplication

    def getDivision(self):
        return self.__division
