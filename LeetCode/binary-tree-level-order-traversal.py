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
        stack = [(root, 0)]
        while stack:
            node, i = stack.pop()
            if node:
                if i < len(ans):
                    ans[i].append(node.val)
                else:
                    ans.append([node.val])
                stack.append([node.right, i+1])
                stack.append([node.left, i+1])
        return ans
