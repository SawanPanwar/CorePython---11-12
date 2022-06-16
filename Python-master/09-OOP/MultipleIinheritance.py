class Addition:
    def sum(self,a,b):  
        return a+b

class Multiplication:
    def multiply(self,a,b):  
        return a*b

class Derived(Addition, Multiplication):   #derived class inherits both addition and mu,tiplacation base class
    def Divide(self,a,b):  
        return a/b

d = Derived()
print(d.sum(10,20))
print(d.multiply(10,20))
print(d.Divide(10,20))

 
