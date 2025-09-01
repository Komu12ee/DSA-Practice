# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # dummy node
        a = dummy            # pointer to build result

        while list1 and list2:
            if list1.val <= list2.val:
                a.next = list1
                list1 = list1.next
            else:
                a.next = list2
                list2 = list2.next
            a = a.next  # move pointer forward

        # attach the rest of the nodes
        a.next = list1 if list1 else list2

        return dummy.next
