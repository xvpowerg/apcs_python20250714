myList = ["A","B","C","D"]
n1 = 10
n2 = 0
print("Start:",myList)
try:
    print(myList[0])
except:
    pass
finally:   
    myList.clear()#100%會執行的



    
print("End:",myList)
