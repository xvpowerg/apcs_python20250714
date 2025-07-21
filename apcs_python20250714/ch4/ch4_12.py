#map 用於轉換

def myMap(func,myList):
    result = []
    for v in myList:
        result.append(func(v))
    return result     

list1 = [1,2,3,4,5]
func1 = lambda x:x**2
newList = myMap(func1,list1)
print(list1)
print(newList)

newList = myMap(lambda x:x**2,list1)
print(list1)
print(newList)
