class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):
        self.my_stack.append(data)
    def my_pop(self):    
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)
stack = Stack()
data = ["ken","Vivin","Lucy","Joy"]
for n in data:
    stack.my_push(n)

print("size:",stack.size())
print(stack.my_pop())    
print("size:",stack.size())    
