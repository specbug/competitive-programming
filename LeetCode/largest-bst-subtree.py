# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        INT_MIN = -math.inf
        INT_MAX = math.inf
        maxst = 0
        def max_bst(node):
            nonlocal maxst
            bal = True
            if not node:
                return INT_MIN, INT_MAX, True, 0
            lmax, lmin, _bal, m = max_bst(node.left)
            bal = bal and _bal
            rmax, rmin, _bal, n = max_bst(node.right)
            bal = bal and _bal 
            if not bal:
                return INT_MAX, INT_MIN, False, 0
            if node.val <= lmax or node.val >= rmin:
                return INT_MAX, INT_MIN, False, 0
            st = m+n+1
            maxst = max(st, maxst)
            return max(lmax, rmax, node.val), min(lmin, rmin, node.val), True, st
        max_bst(root)
        return maxst
