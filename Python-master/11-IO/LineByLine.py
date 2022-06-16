# Read a file line by line
import re
def readLine():
    file = open("C:\\Users\\Sawan\\Desktop\\CorePython\\Kamlesh.txt")  # Open a file
    for line in file:
        if (re.search("@gmail.com", line)):
            print(line, end='')
    file.close()  # Close a file


readLine()
