import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()
def bin_search(data,val):
    low,high = 0,len(data) - 1
    mid = -1
    while not low > high:
        mid = (low + high)//2
        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid
    return -1    
data = []
while len(data) < 50:
    ranNum = random.randint(1,100)
    if ranNum not in data :
        data.append(ranNum)
data.sort()
showData(data)

while True:
    val = int(input("請輸入搜尋數值(1-100),輸入-1結束:"))
    if val == -1:
        break
    pos = bin_search(data,val)
    if pos == -1:
        print(f"{val}不存在")
    else:
        print(f"{val}在{pos + 1}位置")

