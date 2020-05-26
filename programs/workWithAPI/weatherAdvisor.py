import pyowm

owm = pyowm.OWM("ee5b93394a79292907548fdf0b8a8813", language="ru")

place = input("Введите город/страну: ")

observation = owm.weather_at_place(place)
weather = observation.get_weather()

temp = weather.get_temperature("celsius")["temp"]

if temp <= 10:
    print("В городе/стране " + place + " сейчас температура", temp, "℃." +
          "\nЛучше оденься потеплее.")
elif temp <= 17:
    print("В городе/стране " + place + " сейчас температура", temp, "℃." +
          "\nТепло и не холодно, но лучше что-нибудь накинуть.")
else:
    print("В городе/стране " + place + " сейчас температура", temp, "℃." +
          "\nНа улице жара, выходи на легке.")
