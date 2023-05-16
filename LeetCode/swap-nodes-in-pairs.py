# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev = None
        a = head
        b = head.next
        if not b:
            return a
        ans = None
        while b:
            if prev:
                prev.next = b
            prev = a
            nxt = b.next
            b.next = a
            if not ans:
                ans = b
            a, b = nxt, nxt.next if nxt else None
        prev.next = a
        return ans