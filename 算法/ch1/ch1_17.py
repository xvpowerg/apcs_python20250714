x = [5,15,25,35,45]
for data in x:
    print(data,end = " ")
print()
for i in range(len(x)):
    print(i,":",x[i],end=" ")
print()    
x.insert(2,100)#插入
print(x)
x.append(200)
print(x)
x[2] = 20
print(x)
x.remove(20)
print(x)
n = x.pop()
print(x)
print(n)
n = x.pop(0)
print(x)
print(n)
