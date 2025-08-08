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
bst = Node()
datas = [20,15,17,30,32,4]
for v in datas:
    bst.insert(v)
bst.inorder()
