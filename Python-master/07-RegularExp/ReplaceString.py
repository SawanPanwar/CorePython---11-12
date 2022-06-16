import re
string = "The rain in Spain"
result = re.sub("\s", " ,", string)
print(result)
