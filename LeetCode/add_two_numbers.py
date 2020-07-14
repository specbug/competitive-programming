# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l_out = ListNode(0)
        l3 = l_out
        this_carry = 0
        while l1 or l2 or this_carry!=0:
            
            this_sum = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + this_carry)
            
            if this_sum >= 10:
                this_carry = 1
                this_sum = this_sum - 10
                
            else:
                this_carry = 0
                
            l3.next = ListNode(this_sum)
            l3 = l3.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return l_out.next