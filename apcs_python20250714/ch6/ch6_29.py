import random
ans = random.randint(1,5)
guess = int(input("請猜一個1~5的數字"))
if guess == ans:
    print("對了")
else:
    print("錯了",ans)    
