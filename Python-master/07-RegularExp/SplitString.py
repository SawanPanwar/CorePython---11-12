
import re 
string = "The rain in Spain" 

result1 = re.split("\s", string)
result2 = re.split("\s", string, 1)
print(result1)
print(result2)
