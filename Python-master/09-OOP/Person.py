class Person:
    'I am Person Class'

    count = 0

    def __del__(self):
        print("I am destructor")

    def __init__(self, name, address):
        self.name = name
        self.address= address
        Person.count += 1

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def __str__(self):
        return "Name = %s \nAddress = %s" % (self.name, self.address)


