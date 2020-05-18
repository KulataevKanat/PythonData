# G:\Python BackEnd\WorkWithFiles

with open("G:\Python BackEnd\WorkWithFiles\\txt\WithConstruction.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
