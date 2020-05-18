import random

print("random() - (0.0 до 1.0)): ")
number = random.random()
print(number)

print("\nrandom() - (0.0 до 100.0)): ")
number = random.random() * 100
print(number)

print("\nrandint(min, max): ")
number = random.randint(1, 13)
print(number)

print("\nrandrange(start, stop, step): ")
number = random.randrange(10, 50, 5)
print(number)

print("\nchoice(): ")
string = "I write in language {pl}"

pl = list()
pl.append("Java")
pl.append("Python")
pl.append("C++")
pl.append("C")
pl.append("Go")
pl.append("PHP")

random.shuffle(pl)
plChoice = random.choice(pl)

print(string.format(pl=plChoice))
