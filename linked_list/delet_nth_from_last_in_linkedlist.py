# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         p=head
#         count=0
#         while p!=None:
#             count+=1
#             p=p.next
#         print(count)    
#         index=count-n
#         q=head
#         if not head.next:
#             return None
#         if index==0 and q.next:
#             head=q.next
#             return head    
#         while index and q.next:
#             q=q.next
#             index-=1
#         p=q.next    
#         if p.next:
#             p.val=p.next.val
#             p.next=p.next.next
#         else:
#             q.next=None    
#         return head     
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
