class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for i in nums:
            if i == 0:
                c += 1
            else:
                s += (c*(c+1))//2
                c = 0
        s += (c*(c+1))//2
        return s