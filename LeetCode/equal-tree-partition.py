# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def match_sum(node):
            if not node:
                return 0
            l = match_sum(node.left)
            r = match_sum(node.right)
            s = l+r+node.val
            if node is not root:
                sums.add(s)
            return s
        sums = set()
        return match_sum(root)/2 in sums
