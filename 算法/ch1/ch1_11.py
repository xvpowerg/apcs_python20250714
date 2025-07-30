a1,a2 = 1,3
print(a1,a2,end=" ")
for i in range(3,8):
    a3 = 3 * a2 - 2* a1
    print(a3,end=" ")
    a1 = a2
    a2 = a3
print()    
def myFunc(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return 3 * myFunc(x - 1) - 2 * myFunc(x-2)

for i in range(1,8):
    print(myFunc(i),end=" ")
