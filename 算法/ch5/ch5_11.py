class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    def inorder(self):
           if self.left:
               self.left.inorder()
           print(f"{self.data}",end="->")
           if self.right:
               self.right.inorder()
    def search(self,val):
        if val <self.data:
            if not self.left:
                return f"{val}不存在"
            return self.left.search(val)
        elif val > self.data:
            if not self.right:
                return f"{val}不存在"
            return self.right.search(val)
        else:
            return f"找到了{val}"

bst = Node()
datas = [20,15,17,30,32,4]
for v in datas:
    bst.insert(v)
bst.inorder()
print()
print(bst.search(17))
print(bst.search(25))
