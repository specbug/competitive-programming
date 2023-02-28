# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightmost_leftsubtree(self, curr):
        node = curr.left
        while node.right and node.right is not curr:
            node = node.right
        return node

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        c = 0
        while root:
            if root.left:
                rl_leaf = self.rightmost_leftsubtree(root)
                if rl_leaf.right is None:
                    rl_leaf.right = root
                    root = root.left
                else:
                    c += 1
                    if c == k:
                        return root.val
                    root = root.right
                    rl_leaf.right = None
            else:
                c += 1
                if c == k:
                    return root.val
                root = root.right
