import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\dimensionalListWriter.csv"
MULTIFILENAME = "G:\Python BackEnd\WorkWithFiles\csv\multidimensionalListWriter.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    print("Список: ")
    for i in reader:
        print(i[0] + " - " + i[1])

with open(MULTIFILENAME, "r", newline="") as multiFile:
    reader = csv.reader(multiFile)
    print("\nМногомерный список: ")
    for j in reader:
        print(j[0] + " - " + j[1])
