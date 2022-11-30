# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        if not (head and head.next):
            return head
        prev = None
        curr = head
        nxt = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if not nxt:
                break
            nxt = nxt.next
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not (head and head.next and head.next.next):
            return head
        temp = head
        mid = self.get_mid(temp)
        mid.next = self.reverse(mid.next)
        track = None
        ans = None
        a = temp
        b = mid.next
        mid.next = None
        while a and b:
            if track is None:
                track = a
                ans = track
            else:
                track.next = a
                track = track.next
            a = a.next
            track.next = b
            b = b.next
            track = track.next
        if a or b:
            track.next = a if a else b
        return ans
