import os

# G:\Python BackEnd\WorkWithFiles\os\FolderTest\FileRenameTest.txt

filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
else:
    print("Файл не существует")
