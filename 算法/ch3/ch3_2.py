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
        
    def isFull(self):
        if self.top >= self.capacity-1:
            return True
        else:
            return False
        
i1 = Item("A1",100)
i2 = Item("B2",150)
i3 = Item("E3",83)
print(i1)
