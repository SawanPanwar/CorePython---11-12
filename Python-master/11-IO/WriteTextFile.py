#Write to a file 
def writeFile():
    # Iterate over the lines of the File
    file = open("C:\\Users\\Sawan\\Desktop\\CorePython\\Sandeep.txt", "w") #Open a file
    file.write("Hi\n")
    file.write("This is Python file\n")
    file.write("This is Python file 3")
    file.close() # Close a file

writeFile()
   
