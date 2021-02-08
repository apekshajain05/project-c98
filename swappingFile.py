def swapFileData():
    file1=input("Enter first file's name")
    file2=input("Enter second file's name ")
    # data_a=open(file1,'r')
    # data_b=open(file2,'r')
    # data_b=open(file1,'w')
    # data_a=open(file2,'w')
    with open(file1,'r' ) as a:
        data_a=a.read()
    with open(file2,'r') as b:
        data_b=b.read()
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)
   
swapFileData()