def fileInfo():
    fo = open("Test.txt", "r")
    print ("File Name: ", fo.name)
    print ("Mode of Opening: ", fo.mode)
    print ("Is Closed: ", fo.closed)
    
fileInfo()
