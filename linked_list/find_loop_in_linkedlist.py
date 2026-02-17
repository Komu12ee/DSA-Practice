# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        p=head
        q=p.next.next
        while q and q.next:
            if q==p:
                return True
            else:
                p=p.next
                q=q.next.next
        return False            
