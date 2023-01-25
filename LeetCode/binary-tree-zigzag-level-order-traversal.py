from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque()
        queue.append(root)
        ans = []
        last = root
        rev = False
        level = []
        while queue:
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node is last:
                if rev:
                    level = level[::-1]
                ans.append(level)
                level = []
                rev = not rev
                if queue:
                    last = queue[-1]
        return ans
