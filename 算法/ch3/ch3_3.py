class Item:
    def __init__(self,title,price):
        self.title = title
        self.price = price
    def __str__(self):
        return f"{self.title}-{self.price}"
class ItemStack:
    def __init__(self,capacity):
        self.my_stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
        
    def push(self,data):
        if self.isFull():
            print("Item已滿")
        else:
           self.top += 1
           self.my_stack[self.top] = data
    def pop(self):
        if self.size():
            data = self.my_stack[self.top];
            self.my_stack[self.top] = None
            self.top -= 1            
            return data
        else:
            print("ItemStack為空")
            return None
    def isFull(self):
        if self.top >= self.capacity-1:
            return True
        else:
            return False
    def size(self):
        return self.top + 1
        
i1 = Item("A1",100)
i2 = Item("B2",150)
i3 = Item("E3",83)
print(i1)
itemStack = ItemStack(3)
itemStack.push(i1)
itemStack.push(i2)
itemStack.push(i3)
print(itemStack.pop())
print(itemStack.pop())
print(itemStack.pop())
print(itemStack.pop())
