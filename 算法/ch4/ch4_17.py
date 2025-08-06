import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[0]*50
for i in range(50):
    data[i] = random.randint(1,100)
    
showData(data)

while val != -1:
    find = 0
    val = int(input("輸入(1~100)輸入-1離開:"))
    for i in range(50):
        if data[i] == val:
            print(f"{val}在第{i+1}的位置")
            find+=1
    if find == 0 and val != -1:
        print(f"{val}不存在")
