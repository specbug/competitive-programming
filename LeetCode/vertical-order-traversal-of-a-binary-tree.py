from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, 0, 0])
        ans = dict()
        min_b = 0
        while queue:
            node, i, h = queue.popleft()
            if node:
                min_b = min(min_b, i)
                ans[i] = ans.get(i, []) + [(node.val, h)]
                queue.append([node.left, i-1, h+1])
                queue.append([node.right, i+1, h+1])
        return [[i[0] for i in sorted(ans[r], key=lambda x: (x[1], x[0])) ]for r in range(min_b, min_b+len(ans)+1) if r in ans]
