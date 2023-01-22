from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        ans = []
        q = deque()
        q.append([root, 0])
        while q:
            node, i = q.popleft()
            if node:
                if i < len(ans):
                    ans[i].append(node.val)
                else:
                    ans.append([node.val])
                q.append([node.left, i+1])
                q.append([node.right, i+1])
        return ans
