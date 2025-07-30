sum2 = 0

for j in range(1,11):
    sum2 += j**2
print(sum2)

def getSum(n):
    if n == 1:
        return 1
    else:
       return getSum(n-1) + n**2
print(getSum(10))        
