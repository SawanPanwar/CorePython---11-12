
file = open("C:\\Users\\Sawan\\Desktop\\CorePython\\Adnan.txt", "r")
pos = file.seek(5)
f = file.read(10)
print(file.tell())
print(f)
print(pos)
