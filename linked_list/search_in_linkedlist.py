'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        #Code here
        p=head
        while(p!=None):
            if p.data==key:
                return True
            else:
                p=p.next
        return False        
        
