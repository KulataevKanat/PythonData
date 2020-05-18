from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_DOWN, ROUND_05UP, ROUND_CEILING, ROUND_FLOOR

print("Работа без модули Decimal: ")
number = 0.1 + 0.1 + 0.1
print(number)  # 0.30000000000000004

print("Работа с модулем Decimal: ")
number = Decimal("0.1")
number = number + number + number
print(number)  # 0.3

print("\nСложение целого числа и числа с плавающей точкой: ")
number = Decimal("0.1")
number = number + 2
print(number)

print("\n'decimal.Decimal' and 'float': ")
try:
    number = Decimal("0.1")
    number = number + 0.1  # здесь возникнет ошибка
    print(number)
except:
    print("Операции модуля Decimal и типа float не допустимы")

print("\nКол-во символов после дробной части(2): ")
number = Decimal("0.10")
number = 3 * number
print(number)  # 0.30

print("\nОкругление чисел: ")
number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)  # 0.44

number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))  # 0.56

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))  # 1.00

print("или с помощью константой 'ROUND_HALF_EVEN': ")
number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  # 10.02

number = Decimal("10.035")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  # 10.04

print("\nВиды констант: ")
print("'ROUND_HALF_UP' - округляет число в сторону повышения, если после него идет число 5 или выше: ")
number = Decimal("10.026")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))  # 10.03

print("\n'ROUND_HALF_DOWN' - округляет число в сторону повышения, если после него идет число больше 5: ")
number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))  # 10.02

print("\n'ROUND_05UP' - округляет только 0 до единицы, если после него идет 5: ")
number = Decimal("10.005")
print(number.quantize(Decimal("1.00"), ROUND_05UP))  # 10.01

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_05UP))  # 10.02

print("\n'ROUND_CEILING' - округляет число в большую сторону вне зависимости от того, какое число идет после него: ")
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))  # 10.03

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))  # 10.03

print("\n'ROUND_FLOOR' - не округляет число вне зависимости от того, какое число идет после него: ")
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))  # 10.02

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))  # 10.02
