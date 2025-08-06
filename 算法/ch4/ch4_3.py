def gcd_loop(m,n):
    while n!= 0:
        r = m % n
        m = n
        n = r
    return m     

def gcd_rec(m,n):
    if n == 0:
        return m
    else:
        return gcd_rec(n,m%n)

n1 = int(input("num1="))
n2 = int(input("num2="))
if n1 < n2:
    n1,n2 = n2,n1
gcd1 = gcd_loop(n1,n2)
gcd2 = gcd_rec(n1,n2)
print(gcd1)
print(gcd2)
