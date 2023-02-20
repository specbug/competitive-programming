# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_rightmost_node_left_subtree(self, curr):
        node = curr.left
        while node.right and node.right is not curr:
            node = node.right
        return node

    def get_inorder(self, root):
        if not root:
            return []
        order = []
        while root:
            if root.left:
                r_leaf = self.get_rightmost_node_left_subtree(root)
                if r_leaf.right is root:
                    r_leaf.right = None
                    order.append(root.val)
                    root = root.right
                else:
                    r_leaf.right = root
                    root = root.left
            else:
                order.append(root.val)
                root = root.right
        return order

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        order = self.get_inorder(root1)
        order += self.get_inorder(root2)
        return sorted(order) # linear due to Timsort