from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class NullNode(object):
    def __str__(self):
        return 'null'

    def __repr__(self):
        return self.__str__

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        ans = dict()
        stack = [(root, 0)]
        maxl = 1
        while stack:
            node, i = stack.pop()
            maxl = max(maxl, i)
            val = node.val if node is not None else NullNode()
            if i in ans:
                ans[i] += f' ' + str(val)
            else:
                ans[i] = str(val)
            if node is not None:
                stack.append([node.right, i+1])
                stack.append([node.left, i+1])
        return ' '.join(ans[k] for k in range(maxl+1))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return
        ymap = lambda x: None if x == 'null' else int(x)
        data = list(map(ymap, data.split()))
        queue = deque()
        i = 1
        root = TreeNode(data[0])
        if root is None:
            return
        queue.append(root)
        while queue:
            node = queue.popleft()
            l, r = data[i], data[i+1]
            if l is not None:
                node.left = TreeNode(l)
                queue.append(node.left)
            if r is not None:
                node.right = TreeNode(r)
                queue.append(node.right)
            i += 2
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))