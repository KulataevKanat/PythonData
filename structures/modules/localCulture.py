import locale

locale.setlocale(locale.LC_ALL, "en")  # для  Windows
# locale.setlocale(locale.LC_ALL, "de_DE")   # для MacOS

number = 12345.6789
formatted = locale.format_string("%f", number)
print(formatted)  # 12345,678900

formatted = locale.format_string("%.2f", number)
print(formatted)  # 12345,68

formatted = locale.format_string("%d", number)
print(formatted)  # 12345

formatted = locale.format_string("%e", number)
print(formatted)  # 1,234568e+04

money = 234.678
formatted = locale.currency(money)
print(formatted)  # 234,68 €

print("\nWindows culture:")

locale.setlocale(locale.LC_ALL, "")

number = 12345.6789
formatted = locale.format_string("%.02f", number)
print(formatted)  # 12345,68
print(locale.getlocale())  # ('Russian_Russia', '1251')
