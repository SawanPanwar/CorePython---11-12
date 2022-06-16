try:
    num1 = int(input("Enter First Number: "))
    if (num1 > 10):
        raise Exception("Invalid Number")
    print("Number = ",num1)
except Exception as e:
    print(e)
