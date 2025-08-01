myList = []
#使用迴圈寫入myList 1~10
for i in range(1,11):
    myList.append(i)
print(myList)

myList2 =[i for i in range(1,11)]
print(myList2)

myList3 = [x**2 for x in range(1,11)]
print(myList3)

myList4 = [x + 2 for x in range(1,11)]
print(myList4)
myList5 = [x for x in range(1,11) if x % 2 == 0]
print(myList5)
