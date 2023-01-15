class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = 0
        ds = 0
        for i in nums:
            es += i
            while i!=0:
                ds += i%10
                i = i//10
        return abs(ds-es)