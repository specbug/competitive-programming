# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return
        cycle = False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                cycle = True
                break
        if not cycle:
            return
        temp = head
        while slow is not temp:
            slow = slow.next
            temp = temp.next
        return slow