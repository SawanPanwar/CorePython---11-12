import Binary
from Binary import *

p1 = Person("sandeep", "indore", 25)
print(p1.getName())
print(p1.getAddress())
print(p1.getAge())
print(p1)
print(p1.__doc__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)
print(Person.__dict__)
print(p1.__dict__)
d = p1.__dict__
print(d.keys())
print(d.values())



