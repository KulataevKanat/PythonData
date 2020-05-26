import pyowm

owm = pyowm.OWM("ee5b93394a79292907548fdf0b8a8813", language="ru")

place = input("Введите город/страну: ")

observation = owm.weather_at_place(place)
weather = observation.get_weather()

temp = weather.get_temperature("celsius")["temp"]

# print(weather)
print("В городе/стране " + place + " сейчас " + weather.get_detailed_status())
print("В городе/стране " + place + " сейчас", temp, "℃")


