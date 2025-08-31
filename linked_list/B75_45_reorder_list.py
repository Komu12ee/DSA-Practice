# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find mid by slow and fast pointer
        s,c=head,head
        while c and c.next:
            s=s.next
            c=c.next.next

        #reversing the second part 
        prev, curr = None, s
        while curr:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt

      
        # merging both part 
        

        first, second = head, prev
        while second.next:   # stop when second half is fully merged
         tmp1, tmp2 = first.next, second.next
         first.next = second
         second.next = tmp1
         first, second = tmp1, tmp2
    