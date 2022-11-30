# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_mid(self, head):
        if not (head and head.next):
            return head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
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
            if nxt:
                nxt = nxt.next
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        temp = head
        mid = self.get_mid(temp)
        mid.next = self.reverse(mid.next)
        a = temp
        b = mid.next
        mid.next = None
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        if (a and a is not mid) or b:
            return False
        return True