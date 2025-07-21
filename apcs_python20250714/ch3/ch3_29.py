def weighted_sum(c,e=80,m=60):
    return c + e * 2 + m * 3

x = weighted_sum(100,m=90)#命名參數
print("x:",x)
y = weighted_sum(e =2,c=5,m=7 )
print("y:",y)
