# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_traversal(self, node: TreeNode):
        if node is None:
            return [None]
        ans = [node.val]
        ans += self.preorder_traversal(node.left)
        ans += self.preorder_traversal(node.right)
        return ans

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        p_tree = self.preorder_traversal(p)
        q_tree = self.preorder_traversal(q)
        return p_tree == q_tree
