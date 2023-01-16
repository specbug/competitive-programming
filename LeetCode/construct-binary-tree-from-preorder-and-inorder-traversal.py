# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        if n == 0:
            return
        if n == 1:
            return TreeNode(inorder[0])
        def tree(start, end):
            if start > end:
                return
            val = preorder.pop()
            root = TreeNode(val)
            index = rel_map[val]
            root.left = tree(start, index-1)
            root.right = tree(index+1, end)
            return root
        preorder.reverse()
        rel_map = dict()
        for e, i in enumerate(inorder):
            rel_map[i] = e
        return tree(0, n-1)