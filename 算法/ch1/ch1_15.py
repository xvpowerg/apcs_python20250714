sum1 = 0

for i  in range(1,101):
    sum1 += i
print("sum1:",sum1)    

def getSum(n):
    if n ==1:
        return 1
    else:
        return getSum(n-1) + n
print("Sum:",getSum(100))
