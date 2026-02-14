class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class MyLinkedList:

    def __init__(self):
        self.left=listnode(0)
        self.right=listnode(0)
        self.left.next=self.right
        self.right.prev=self.left

    def get(self, index: int) -> int:
        cur=self.left.next
        while(cur and index>0):
            cur=cur.next
            index-=1
        if cur and index==0 and cur!=self.right:
            return cur.val    
        else:
            return -1    

    def addAtHead(self, val: int) -> None:
        node=listnode(val)
        node.next=self.left.next
        self.left.next=node
        node.prev=self.left
        node.next.prev=node


    def addAtTail(self, val: int) -> None:
        node=listnode(val)
        node.prev=self.right.prev
        self.right.prev=node
        node.next=self.right
        node.prev.next=node


    def addAtIndex(self, index: int, val: int) -> None:
        node=listnode(val)
        cur=self.left.next
        while(cur and index>0):
            cur=cur.next
