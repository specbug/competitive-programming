# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def is_same(root1, root2):
            if not (root1 and root2):
                if not (root1 or root2):
                    return True
                return False
            return root1.val == root2.val and is_same(root1.left, root2.right) and is_same(root1.right, root2.left)
        return is_same(root, root)