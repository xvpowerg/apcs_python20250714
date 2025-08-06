def fib_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return nextNum
def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1 or n==2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
def fib_rec_dict(n,memo = None):
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]    
    memo[n] =fib_rec_dict(n-1,memo) + fib_rec_dict(n-2,memo)
    return memo[n]
print(fib_loop(100))
print(fib_rec(10))
print(fib_rec_dict(100))
