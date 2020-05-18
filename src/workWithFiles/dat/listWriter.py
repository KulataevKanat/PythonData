import pickle

FILENAME = "G:\Python BackEnd\WorkWithFiles\dat\datListFile"

users = [
    ["Test1", 10, True],
    ["Test2", 20, True],
    ["Test3", 30, False]

]

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)
