def calc(x,y):
    x += 3
    y += 2
    print("calc ","x:",x,"y:",y)

x,y = 7,15
print("x:",x," y:",y)
calc(x,y)#函式內部的變化不影響外部基本型態變數
print("x:",x," y:",y)
