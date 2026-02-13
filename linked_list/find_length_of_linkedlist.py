'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        p=head
        count=0
        # print(p.next)
        while(p!=None):
            count += 1
            p=p.next
            # print(p.val)
        return count        
            
