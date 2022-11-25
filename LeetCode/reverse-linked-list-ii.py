# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        st = None
        ed = None
        prev = None
        temp = head
        nxt = temp.next
        if not nxt:
            return head
        c = 1
        while c < right:
            if c < left:
                ed = temp
                temp = temp.next
                nxt = nxt.next
            else:
                if not st:
                    st = temp
                temp.next = prev
                prev = temp
                temp = nxt
                nxt = nxt.next
            c += 1
        temp.next = prev
        st.next = nxt
        if ed:
            ed.next = temp
        else:
            return temp
        return head