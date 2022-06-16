import datetime
#Import the datetime module and display the current date:
#x = datetime.datetime.now()
#print(x)
x = datetime.datetime(1996, 7, 25)
print(x)
# format date using strftime() method. Get name of month
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%A"))
print(x.strftime("%a"))


