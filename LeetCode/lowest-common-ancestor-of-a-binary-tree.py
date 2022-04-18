# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode(val={self.val} left={self.left} right={self.right})'


class Solution:
    def lca_dfs(self, node, p, q):
        if not node:
            return None
        if node.left is None and node.right is None:
            if node.val == p.val or node.val == q.val:
                return node
            return False
        curr = node.val == p.val or node.val == q.val
        left = self.lca_dfs(node.left, p, q)
        right = self.lca_dfs(node.right, p, q)
        if left and right:
            return node
        elif (left or right) and curr:
            return node
        else:
            return left or right or curr

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca_dfs(root, p, q)


def treeify(tree, arr, i, n):
    if i < n:
        if arr[i] is None:
            return None
        t = TreeNode(arr[i])
        tree = t
        tree.left = treeify(tree.left, arr, 2*i+1, n)
        tree.right = treeify(tree.right, arr, 2*i+2, n)
    return tree


def hydrate():
    tree = treeify(None, g_rt, 0, len(g_rt))
    pn = TreeNode(g_p)
    qn = TreeNode(g_q)
    return tree, pn, qn


g_rt = [1,2,3,None,4]
g_p = 4
g_q = 1
solution = Solution()
_tree, _p, _q = hydrate()
print(solution.lowestCommonAncestor(_tree, _p, _q).val)
