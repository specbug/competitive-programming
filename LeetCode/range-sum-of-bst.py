# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if high < low:
            return 0
        def range_sum(node):
            if not node:
                return 0
            l = range_sum(node.left)
            r = range_sum(node.right)
            return l+r+(node.val if low <= node.val <= high else 0)
        return range_sum(root)
