# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        temp = head
        n = 1
        while temp.next:
            temp = temp.next
            n += 1
        temp = head
        c = 1
        st = min(k, n-k+1)
        ed = n-st+1
        while temp:
            if c == st:
                s = temp
            elif c == ed:
                temp.val, s.val = s.val, temp.val
            temp = temp.next
            c += 1
        return head