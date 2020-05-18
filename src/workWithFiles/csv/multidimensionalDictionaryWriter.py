import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\multidimensionalDictionaryWriter.csv"

users = [
    {"name": "Test1", "number": 10},
    {"name": "Test2", "number": 20},
    {"name": "Test3", "number": 30}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "number"]
    writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)
