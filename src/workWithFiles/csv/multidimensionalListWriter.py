import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\multidimensionalListWriter.csv"

users = [
    ["Test1", 10],
    ["Test2", 20],
    ["Test3", 30]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(users)  # multidimensional list
