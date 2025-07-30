def testLoop(n):
    print(n)
    if n < 5:
       testLoop(n+1) 

#使用一個for 顯示
for i in range(1,6):
    print(i)
print("="*10)

testLoop(1)
