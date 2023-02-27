class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        t = 1
        nums = set(nums)
        for i in range(32):
            n = t << i
            if n not in nums:
                return n