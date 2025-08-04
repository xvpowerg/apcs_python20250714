def f_loop(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return  result
def f_r(n):
    if n == 1:
        return 1
    else:
        return n * f_r(n-1)
n = 5
print(f"{n}!=", f_loop(n))
print(f"{n}!=",f_r(n))
