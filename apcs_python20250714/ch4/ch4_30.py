#List
list1 = ["a",'b',"c"]
print(list1)
print(len(list1))
list1.append("e")
print(list1)
list1.append("f")
print(list1)

list2 = ["Ken","Lucy"]

#list1.append(list2)
list1.extend(list2)
#list1 += list2
print(list1)
