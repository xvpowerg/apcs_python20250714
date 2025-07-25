num1 = 10
num2 = 1
num3 = [1,2,3,4]
print("Start")
try:
    print(num1 / num2)
    print(num3[99])
except ZeroDivisionError:    
    print("分母為0錯誤")
except IndexError:
    print("Index錯誤")
print("End")
