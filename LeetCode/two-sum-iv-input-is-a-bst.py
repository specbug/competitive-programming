from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return 0
        q = deque()
        q.append(root)
        hmap = set()
        while q:
            node = q.popleft()
            if node:
                if (k-node.val) in hmap:
                    return True
                hmap.add(node.val)
                q.append(node.left)
                q.append(node.right)
        return False
