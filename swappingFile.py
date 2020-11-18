def swapFileData():
    file1 = input(" Enter the name of file1 to be exchanged : ")
    file2 = input(" Enter the name of file2 to be exchanged : ")
    f1 = open(file1, 'r+')
    f1.read()
    data_a=str(f1.read())
    f1.close()
    f2 = open(file2, 'r+')
    f2.read()
    data_b=str(f2.read())
    f2.close()
    f1 = open(file1, 'r+')
    f2 = open(file2, 'r+')
    f1.write(data_b)
    f2.write(data_a)


swapFileData()
