# G:\Python BackEnd\WorkWithFiles

try:
    myFile = open("G:\Python BackEnd\WorkWithFiles\\txt\FileWriter.txt", "w")
    try:
        myFile.write("Hello World")
    except Exception as e:
        print(e)
    finally:
        myFile.close()
except Exception as ex:
    print(ex)
