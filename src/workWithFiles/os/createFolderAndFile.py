import os

FOLDERNAME = "G:\Python BackEnd\WorkWithFiles\os\FolderTest"
FILENAME = "G:\Python BackEnd\WorkWithFiles\os\FolderTest\FileTest.txt"

os.mkdir(FOLDERNAME)

with open(FILENAME, "w") as file:
    file.write("this os test")
