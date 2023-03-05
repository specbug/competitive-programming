from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = deque()
        q.append(root)
        last = root
        ans = []
        s = 0
        while q:
            node = q.popleft()
            s += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node is last:
                ans.append(s)
                s = 0
                if q:
                    last = q[-1]
        if k > len(ans):
            return -1
        return sorted(ans, reverse=True)[k-1]
