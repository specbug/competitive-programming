# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightmost_left_subtree(self, curr: TreeNode):
        node = curr.left
        while node.right and node.right is not curr:
            node = node.right
        return node

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        prev = n1 = n2 = None
        while root:
            if root.left:
                right_most = self.rightmost_left_subtree(root)
                if right_most.right is root:
                    right_most.right = None
                    if root.val < prev.val:
                        n2 = root
                        if not n1:
                            n1 = prev
                    prev = root
                    root = root.right
                else:
                    right_most.right = root
                    root = root.left
            else:
                if prev and root.val < prev.val:
                    n2 = root
                    if not n1:
                        n1 = prev
                prev = root
                root = root.right
        n1.val, n2.val = n2.val, n1.val