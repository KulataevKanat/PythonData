import math

print("возведение числа 2 в степень 3: ")
n1 = math.pow(2, 3)
print(n1)  # 8

print("ту же самую операцию можно выполнить так: ")
n2 = 2 ** 3
print(n2)

print("\nвозведение в квадрат: ")
print(math.sqrt(9))  # 3

print("\nближайшее наибольшее целое число: ")
print(math.ceil(4.56))  # 5

print("\nближайшее наименьшее целое число: ")
print(math.floor(4.56))  # 4

print("\nперевод из радиан в градусы: ")
print(math.degrees(3.14159))  # 180

print("\nперевод из градусов в радианы: ")
print(math.radians(180))  # 3.1415.....

print("\nкосинус: ")
print(math.cos(math.radians(60)))  # 0.5

print("\ncинус: ")
print(math.sin(math.radians(90)))  # 1.0

print("\nтангенс: ")
print(math.tan(math.radians(0)))  # 0.0
print(math.log(8, 2))  # 3.0
print(math.log10(100))  # 2.0

radius = 30
print("\nплощадь круга с радиусом 30: ")
area = math.pi * math.pow(radius, 2)
print(area)

print("\nнатуральный логарифм числа 10: ")
number = math.log(10, math.e)
print(number)
