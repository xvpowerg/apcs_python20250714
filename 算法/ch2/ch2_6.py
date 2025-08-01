num = int(input("請輸入陣列個數"))
arr = [0] * num
for i in range(num):
    arr[i] =  int(input(f"輸入第{i+1}筆整數"))
#print(arr)
    
for j in range(num - 1):
    if arr[j] >= arr[j + 1]:
        print("不是遞增陣列")
        break
else:
    print("是遞增陣列")



