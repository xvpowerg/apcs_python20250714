class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"({self.data})"
    def preorder(self):
        print(f"({self.data})",end="->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
            
nodeA = Node(14)
nodeB = Node(3)
nodeC = Node(16)
nodeD = Node(23)
nodeE = Node(7)
nodeF = Node(20)
print(nodeA)
nodeA.left = nodeB
nodeA.right = nodeE
nodeB.left = nodeC
nodeB.right = nodeD
nodeE.right = nodeF

root = nodeA
root.preorder()
