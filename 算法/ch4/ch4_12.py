cars=["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
print('氣泡排序法,原始資料為：', cars, sep='')
n = len(cars)
for i in range(1,n):
    for j in range(n-i):
        if cars[j] > cars[j + 1]:
            cars[j],cars[j + 1] = cars[j + 1],cars[j]
    print(f"第{i}次排序的結果:",end="")
    print(cars)
print("氣泡排序後的結果:",cars)    
