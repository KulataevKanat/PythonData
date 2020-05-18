import pickle

FILENAME = "G:\Python BackEnd\WorkWithFiles\dat\DatFile"

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    number = pickle.load(file)
    print("Name: " + name + "\nNumber: " + number)

