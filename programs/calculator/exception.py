class Exceptions:
    __firstException = "Просьба ввести числа, или 'y' для выхода"

    __secondException = "Просьба ввести доступные математические операции, или 'y' для выхода"

    __exit = "y"

    __exitPrint = "Программа закрыта"

    def getFirstException(self):
        return self.__firstException

    def getSecondException(self):
        return self.__secondException

    def getExit(self):
        return self.__exit

    def getExitPrint(self):
        return self.__exitPrint
