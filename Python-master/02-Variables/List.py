list1 = ['a', 'b', 'c', 'd', 'e' ]

list2 = [1, 1, 3, 4, 5]

list3 = list1 + list2

list4 = list1 * 2

list5 = list1[1:3]

list6 = list1[2:]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
list1[1] ='h'
print(list1)
del list1[1]
print(list1)
print(type(list1))
print(len(list1))
print(list1[-2])
list2.append(6)
print(list2)
print(list2.count(1))

