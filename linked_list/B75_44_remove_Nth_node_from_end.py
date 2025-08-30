# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,curr=head,head
        temp=prev
        count=0
        if not(prev.next):
            if n==1:
             head=None
             return head
        for i in range(n):
            if curr.next:
              count+=1
              curr=curr.next
        if count<n-1:
            return head   
        # if curr.next:
        #     curr=curr.next  
        if not(curr.next) and n-1==count:
            head= prev.next
            return head        
        while curr.next:
            prev=prev.next
            curr=curr.next
        temp=prev
        prev=prev.next
        temp.next=prev.next
        prev.next=None
        return head

