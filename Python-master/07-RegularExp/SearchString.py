
import re

string = "The rain in Spain"
result = re.search('the', string)

if result:
   print("String Found ")
else:
   print("Not found")  