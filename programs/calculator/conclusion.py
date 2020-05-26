from calculator.mathOperations import MathOperations
from calculator.questions import Questions
from calculator.exception import Exceptions


class Main:
    mathOperations = MathOperations()
    questions = Questions()
    exceptions = Exceptions()

    while True:
        try:
            firstValue = input(questions.getFirstValue())
            if firstValue.lower().__eq__(exceptions.getExit()):
                break

            mathSign = input(questions.getMathSign())
            if mathSign.lower().__eq__(exceptions.getExit()):
                break

            secondValue = input(questions.getSecondValue())
            if secondValue.lower().__eq__(exceptions.getExit()):
                break

            if mathSign.__eq__(mathOperations.getPlus()):
                print(float(firstValue) + float(secondValue))

            elif mathSign.__eq__(mathOperations.getMinus()):
                print(float(firstValue) - float(secondValue))

            elif mathSign.__eq__(mathOperations.getMultiplication()):
                print(float(firstValue) * float(secondValue))

            elif mathSign.__eq__(mathOperations.getDivision()):
                print(float(firstValue) / float(secondValue))

            else:
                print(exceptions.getFirstException())
                print(exceptions.getSecondException())

        except:
            print(exceptions.getFirstException())
            print(exceptions.getSecondException())

    print(exceptions.getExitPrint())
