list1 = [1,2,3,5,8,13,21,34,55,89]
print(list1)
newList = filter(lambda x:x%2 == 0,list1)
print(newList)
print(list(newList))
