## 程式練習
#請寫一個程式，判斷輸入的整數為否為2或3的倍數
#使用%
#2倍
#3倍
#是2也是3的倍數
#不是2與3的倍數
num = int(input("輸入整數"))
if num % 2 == 0 and num % 3 == 0:
    print("是2也是3的倍數")
elif num % 2 == 0:
    print("是2的倍數")
elif num % 3 == 0:
    print("是3的倍數")
else:
    print("不是2與3的倍數")
