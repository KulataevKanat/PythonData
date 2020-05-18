import shelve

FILENAME = "G:\Python BackEnd\WorkWithFiles\shelve\shelveWrite"

with shelve.open(FILENAME) as file:
    file["Test1"] = "TestShelve1"
    file["Test2"] = "TestShelve2"
    file["Test3"] = "TestShelve3"
