# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp.next:
            n += 1
            temp = temp.next
        if n == 0: return
        k = (n+1)//2
        temp = head
        for i in range(1, k):
            temp = temp.next
        temp.next = temp.next.next
        return head