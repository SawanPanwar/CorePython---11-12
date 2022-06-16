list1 = [1, 2, 3, 4, 5, 6]
list2 = list1.copy()
list2.reverse()
list3 = []

for i in range (len(list1)):
    list3.append(list1[i]+list2[i])
print(list3)

for i in list3:
    print(i)


