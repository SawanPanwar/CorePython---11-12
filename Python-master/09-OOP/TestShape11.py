from builtins import print

from Shape import *
from Circle import *
from Triangle import *
from Rectangle import *

r = Rectangle(5, 5, "red", 100)
c = Circle(3)
t = Triangle(2, 5)
s = Shape("red", 5)
print(r.getBorderWidth())
print(r.getColor())
print(r.area())
print(c.area())
print(t.area())
print(s.area())
