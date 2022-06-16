from abc import ABC,abstractmethod
class Polygon(ABC):
   def noofsides(self):
        pass

class Triangle(Polygon):
 # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
  

#run the program
t = Triangle()
t.noofsides()

p  = Pentagon()
p.noofsides()

poly = Polygon()
poly.noofsides()

