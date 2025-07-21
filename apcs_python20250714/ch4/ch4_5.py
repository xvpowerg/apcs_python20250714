def func(myList):
    print("func() 1:",myList)
    myList[2] = "Hi"
    print("func() 2:",myList)

myList = [10,20,30]
print("全域1:",myList)
func(myList)
print("全域2:",myList)
