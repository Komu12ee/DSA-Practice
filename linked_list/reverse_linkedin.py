class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return
        
        l=None
        mid=head
        r=mid.next
        while mid:
            mid.next=l
            l=mid
            if r :
                mid=r
                r=r.next
            else: break    
        return mid
