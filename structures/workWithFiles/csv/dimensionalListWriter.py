import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\dimensionalListWriter.csv"

user = ["Test", 50]

with open(FILENAME, "w", newline="") as file:
    user.append()
    writer = csv.writer(file, delimiter=';')
    writer.writerow(user)  # dimensional list
