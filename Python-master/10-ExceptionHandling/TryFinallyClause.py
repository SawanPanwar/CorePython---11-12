
def hello():
    try:
        c = 100
        return (print(c))
    finally:

        return 2
k = hello()
print(k)  #The finally block is executed even there is a return statement in the try block.