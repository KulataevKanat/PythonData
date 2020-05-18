import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\dimensionalDictionaryWriter.csv"

user = {"name": "Test", "number": "50"}

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "number"]
    writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
    writer.writeheader()
    writer.writerow(user)
