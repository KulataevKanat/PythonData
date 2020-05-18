import csv

FILENAME = "G:\Python BackEnd\WorkWithFiles\csv\dimensionalDictionaryWriter.csv"
MULTIFILENAME = "G:\Python BackEnd\WorkWithFiles\csv\multidimensionalDictionaryWriter.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    print("Словарь: ")
    for i in reader:
        print(i["name"] + " - " + i["number"])

with open(MULTIFILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    print("\nМногомерный словарь: ")
    for j in reader:
        print(j["name"] + " - " + j["number"])
