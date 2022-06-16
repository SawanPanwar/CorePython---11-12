import Shape
from Shape import *

class Rectangle(Shape):
    def __init__(self):
        self.__length = 0
        self.__width = 0

    def setLength(self, length):
        self.__length = length

    def getLength(self):
        return self.__length

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def area(self):
        a = self.__length * self.__width
        return a