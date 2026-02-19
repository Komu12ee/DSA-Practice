class Solution:
    def lengthOfLoop(self, head):
        #code here
        # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return 0
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                p=slow.next
                count=1
                while(p!=slow):
                    count+=1
                    p=p.next
                return count   
       
        return 0
