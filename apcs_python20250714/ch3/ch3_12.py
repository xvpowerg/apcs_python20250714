#While完成99乘法表
for i in range(5):
    print(i,end=" ")
print()
x = 0
while x < 5:
    print(x,end=" ")
    x += 1
print("="*20)

y = 2

while y <= 9:
    z = 1
    while z <= 9:
        print(f"{y}*{z}={y*z}",end=" ")
        z += 1
    print()
    y += 1
    
