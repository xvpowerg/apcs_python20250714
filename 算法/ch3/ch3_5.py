from collections import deque
q = deque([1,2,3,4,5])
q.append(6)
print(q)
q.rotate(2) #向右推
print(q)

q.rotate(-3)#向左推
print(q)
first = q.popleft()#移除頭部
print(first)
print(q)
right= q.pop()
print(right)
print(q)
q.insert(0,10)
print(q)
