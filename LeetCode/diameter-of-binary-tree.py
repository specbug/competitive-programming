# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def get_diameter(node):
            nonlocal ans
            if not node:
                return -1
            left = get_diameter(node.left)
            right = get_diameter(node.right)
            ans = max(ans, left+right+2)
            return max(left, right)+1
        get_diameter(root)
        return ans