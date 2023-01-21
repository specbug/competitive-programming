class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return (nums1 == nums2) - 1
        n = len(nums1)
        s = 0
        c = 0
        for i in range(n):
            x = nums2[i] - nums1[i]
            if x%k != 0:
                return -1
            s += x
            if x > 0:
                c += x
        if s != 0:
            return -1
        return c//k
