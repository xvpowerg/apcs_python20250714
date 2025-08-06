import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)
showData(data)

while True:
    val = int(input("輸入要查詢的數值(1-100),輸入-1離開:"))
    if val == -1:
        break
    for i in range(50):
        if data[i]  == val:
            print(f"數值:{val}在{i+1}位置")
            break
    else:
        print(f"數值:{val}不存在")
    #找到顯示數值與數值位置
