import pickle
list = ["viaksh", "shivani", "mohit", "tina", 1]
fileobj = open("C:\\Users\\Sawan\\Desktop\\CorePython\\Object.txt", 'rb')
#pickle.dump(list, fileobj)
print(pickle.load(fileobj))
fileobj.close()