# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, start, B, n):
        if n < B:
            if n <= 0:
                return
            return start
        prev = None
        temp = start
        nxt = temp.next
        c = 1
        while temp.next and c < B:
            temp.next = prev
            prev = temp
            temp = nxt
            nxt = nxt.next
            c += 1
        temp.next = prev
        start.next = self.reverse(nxt, B, n-B)
        return temp
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        if n == 1 or k == 1:
            return head
        return self.reverse(head, k, n)