str1 = ["2","8","10"]

def mySum(data):
    result = 0
    for v in data:
        result += v
    return result
#str1 專換的資料
#int 工具函式
newList = list(map(int,str1)) #重要!
value = mySum(newList)
print(value)
