import pickle

FILENAME = "G:\Python BackEnd\WorkWithFiles\dat\datListFile"

with open(FILENAME, "rb") as file:
    usersList = pickle.load(file)
    for i in usersList:
        print("Name:", i[0],
              "\tNumber:\t", i[1],
              "\tIs_Active:", i[2])
