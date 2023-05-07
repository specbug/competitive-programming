class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                n *= -1
        return n