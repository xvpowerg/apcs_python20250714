h = float(input("身高:"))
w = int(input("體重:"))
bmi = w / ((h / 100) ** 2)
print(f"bmi:{bmi:.2f}")
if  0< bmi <= 18.5:
    print("過輕")
elif 18.5 <  bmi <= 25:
    print("正常")
elif 25 < bmi <= 30:
    print("過重")
elif bmi > 30:
    print("胖胖")
