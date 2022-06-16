class Person:
    count1 = 0
    def __init__(self, name, id):
        self._name = name #protected
        self.__id = id #private
        Person.count1 += 1

    def getName(self):
        return self._name

    def getId(self):
        return self.__id

    def display_details(self):
        print("Name:%s, ID:%d"%(self.name,self.id))

