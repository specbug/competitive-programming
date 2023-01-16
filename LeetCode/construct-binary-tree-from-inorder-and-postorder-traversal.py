# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        if n == 0:
            return
        if n == 1:
            return TreeNode(inorder[0])
        def tree(start, end):
            if start > end:
                return
            val = postorder.pop()
            root = TreeNode(val)
            index = rel_map[val]
            root.right = tree(index+1, end)
            root.left = tree(start, index-1)
            return root
        rel_map = dict()
        for e, i in enumerate(inorder):
            rel_map[i] = e
        return tree(0, n-1)
