class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        slow, fast = head, head  # both start at head
        while fast and fast.next:  # move until end is reached
            slow = slow.next         # 1 step
            fast = fast.next.next    # 2 steps
            if slow == fast:         # cycle found
                return True
        return False                 # no cycle
