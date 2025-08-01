myList3x4 = [[1,5,6,7],
             [8,11,9,77],
             [27,96,52,18]]
print(myList3x4)

myList2x3 = []
for i in range(1,3):
    inList = []
    for k in range(1,4):        
        inList.append(i*k)
    myList2x3.append(inList)
print(myList2x3)

p = [[0]*2 for i in range(5)]#5x2的list
print(p)
