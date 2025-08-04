import math
def is_peime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primList(number):
    prims = []
    for n in range(2,number+1):
        if is_peime(n):
           prims.append(n)
    return  prims

N =int(input("請輸入一個正整數"))
pNumbers = primList(N)
print("有哪些質數:",pNumbers)
    
