import pickle

FILENAME = "G:\Python BackEnd\WorkWithFiles\dat\DatFile"

name = "Test"
number = "10"

with open(FILENAME, "wb") as datFile:
    pickle.dump(name, datFile)
    pickle.dump(number, datFile)