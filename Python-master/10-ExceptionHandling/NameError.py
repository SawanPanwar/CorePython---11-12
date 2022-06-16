
#The try block will generate a NameError, because Ram is not defined:
try:
    print("Ram")
except NameError as e:
  print("Exceptio", e)
except:
  print("Something else went wrong")
