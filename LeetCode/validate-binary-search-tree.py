# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append([root, -math.inf, math.inf])
        while stack:
            node, lb, ub = stack.pop()
            if node:
                if node.val <= lb or node.val >= ub:
                    return False
                stack.append([node.right, node.val, ub])
                stack.append([node.left, lb, node.val])
        return True