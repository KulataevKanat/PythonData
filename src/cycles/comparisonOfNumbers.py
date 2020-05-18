#! Программа Сравнение чисел

print("Для выхода нажмите exit")

while True:
    try:
        value1 = input("Введите первое число: ")
        if value1.lower().__eq__("exit"):
            break  # выход из цикла
        value2 = input("Введите второе число: ")
        if value2.lower().__eq__("exit"):
            break  # выход из цикла
        if int(value1) > int(value2):
            print(value1 + " больше " + value2)
        elif int(value1) == int(value2):
            print(value1 + " и " + value2 + " равны.")
        else:
            print(value1 + " меньше " + value2)

    except:
        print("Просьба ввести числа, или 'exit' для окончания")

print("сравнение чисел окончено")
