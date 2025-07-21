count = 1
ans = 5
guess = int(input("猜第一個數字"))
while True:
    if guess == ans:
        print("猜對了")
        break
    elif count >= 5:
        print("猜錯次數過多")
        break
    count += 1
    guess = int(input("再猜一次"))
    
