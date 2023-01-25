# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(tree):
            if not tree:
                return True, 0
            if not (tree.left or tree.right):
                return True, 1
            l_balanced, l = height(tree.left)
            r_balanced, r = height(tree.right)
            return (l_balanced and r_balanced and abs(l-r) < 2), max(l, r)+1
        return height(root)[0]
