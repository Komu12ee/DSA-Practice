'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        if head==None:
            return Node(x)
        #code here 
        new_node=Node(x)
        p=head
        while(p.next!=None):
            p=p.next
        p.next=new_node
        return head
            
            
