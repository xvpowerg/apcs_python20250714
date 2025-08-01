myList3x4 = [[1,5,6,7],
             [8,11,9,77],
             [27,96,52,18]]
print(myList3x4[1][1])
print(myList3x4[1][2])
print(myList3x4[2][0])
print("================")
print(len(myList3x4))
print(len(myList3x4[0]))

for r in range(len(myList3x4)):
    for c in range(len(myList3x4[0])):
        print(myList3x4[r][c],end=" ")
    print()    
print("---------------")

for rList in myList3x4:
    for cValue in rList:
        print(cValue,end=" ")
    print()        
