import pickle
import re
fileobj = open("C:\\Users\\Sawan\\Desktop\\CorePython\\Sandy.txt", 'rb')
file = open("C:\\Users\\Sawan\\Desktop\\CorePython\\ggggg.txt", 'w')
list = pickle.load(fileobj)
print(list)
for i in list:
    if re.search("tina", i):
        continue
    file.write(i)
    file.write("\n")
file.close()

