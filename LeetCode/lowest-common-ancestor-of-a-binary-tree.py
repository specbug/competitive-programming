# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def get_lca(node):
            nonlocal ans
            if not node:
                return False, False
            left = get_lca(node.left)
            right = get_lca(node.right)
            pflag = (node is p) or left[0] or right[0]
            qflag = (node is q) or left[1] or right[1]
            if pflag and qflag:
                ans = node
                return False, False
            return pflag, qflag
        get_lca(root)
        return ans