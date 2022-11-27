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
    
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        h1 = head1
        h2 = head2
        if h1.val <= h2.val:
            temp = h1
            h1 = h1.next
        else:
            temp = h2
            h2 = h2.next
        ans = temp
        while h1 and h2:
            if h1.val <= h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            temp = temp.next
        if h1 or h2:
            temp.next = h1 if h1 else h2
        return ans
    
    def merge_sort(self, head):
        if not (head and head.next):
            return head
        temp = head
        mid = self.get_mid(temp)
        head1 = head
        head2 = mid.next
        mid.next = None
        head1 = self.merge_sort(head1)
        head2 = self.merge_sort(head2)
        return self.merge(head1, head2)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)