# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        def generate_bst(start, end):
            if start > end:
                return
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = generate_bst(start, mid-1)
            node.right = generate_bst(mid+1, end)
            return node
        return generate_bst(0, len(nums)-1)
