list1 = [1,2,3,5,8,13,21,34,55,89]
def myFilter(func,datas):
    result = []
    for v in datas:
        if func(v):
            result.append(v)
    return result            
#list1內容是偶數的收集成一個新的list
myFunc = lambda x : x % 2 == 0
newList = myFilter(myFunc,list1)
print(newList)
