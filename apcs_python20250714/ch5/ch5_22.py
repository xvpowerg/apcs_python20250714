
num1 = 10
num2 = 5
num3 = [1,2,3,4]
try:
    print(num1/num2)
    print(num3[9])
except ZeroDivisionError:
    print("分母不可為0錯了")
except IndexError:
    print("IndexError錯")
