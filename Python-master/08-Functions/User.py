def sum(a, b):
    'i am Sum'
    c = a + b
    print('a = ',a)
    print('b = ', b)
    print(c)

def mult(a, b):
    c = a * b
    return c

def open():
    print("Hello Python")

def default(a, b=1):
    print('a = ', a)
    print('b = ', b)


print(sum.__doc__)
