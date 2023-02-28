# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def has_path_sum(node, k):
            if not node:
                return False
            if not (node.left or node.right):
                return node.val == k
            return has_path_sum(node.left, k-node.val) or has_path_sum(node.right, k-node.val)
        return has_path_sum(root, targetSum)