data = input()
myList = data.split(" ")
print(myList)
mapObj =  map(int,myList)
dataList =  list(mapObj)
row = dataList[0]
cls = dataList[1]
print(row,type(row))
print(cls,type(cls))
