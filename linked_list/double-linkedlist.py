#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        head=Node(arr[0])
        p=head
        for i in range(1,len(arr)):
            p.next=Node(arr[i])
            p.next.prev=p
            p=p.next
        return head        
            
