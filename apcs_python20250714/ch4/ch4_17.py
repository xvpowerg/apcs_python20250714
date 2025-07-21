## Lambda函式練習

## 攝氏溫度轉換華氏溫度程式
cels = [0,10,20,30,40,50,60,70,80,90,100]
tf =list(map(lambda x: 9 / 5 * x + 32,cels))

for c,f in zip(cels,tf):
    print(f"攝氏:{c} 華氏:{f}")

