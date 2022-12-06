# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        temp = head
        lt = None
        gt = None
        ans = None
        sub_ans = None
        while temp:
            if temp.val < x:
                if lt is None:
                    lt = temp
                    ans = lt
                else:
                    lt.next = temp
                    lt = lt.next
            else:
                if gt is None:
                    gt = temp
                    sub_ans = gt
                else:
                    gt.next = temp
                    gt = gt.next
            temp = temp.next
        if gt:
            gt.next = None
        if lt:
            lt.next = sub_ans
        else:
            ans = sub_ans
        return ans