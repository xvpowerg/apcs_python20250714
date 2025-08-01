class Stack():
    def __init__(self,capacity):
        self.my_stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
    def push(self,data):
        if self.isFull():
            print("滿了")
        else:
            self.top += 1
            self.my_stack[self.top] = data
    def pop(self): #作業
        pass
    def isFull(self):
        if self.top >= self.capacity - 1:
            return True
        else:
            return False
stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
