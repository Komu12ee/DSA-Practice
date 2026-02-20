# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd=head
        even=head.next
        p=head
        q=head.next
        count=1
        while q and q.next:
            count+=1
            p.next=q.next
            p=q
            q=q.next
        print(count)
        if q and count%2==0:
         p.next=None
         q.next=even    
        elif q:
            q.next=None
            p.next=even 
        return odd
