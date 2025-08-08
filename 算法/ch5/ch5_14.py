data=[[1,2],[2,1],[2,5],[5,2],                      #圖形陣列宣告
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3],[3,5],[5,3],
      [4,5],[5,4]]
class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None
        
head = [ListNode()] * 6
for i in range(1,6):
    head[i] = ListNode() 
    head[i].val = i
    print(f"頂點:=>{i}")
    ptr = head[i]
    for j in range(len(data)):
        if data[j][0] == i:
            newnode = ListNode()
            newnode.val =data[j][1] 
            while ptr.next:
                ptr = ptr.next
            ptr.next=newnode     
            print(f"[{newnode.val}]",end="")
    print()        

                
