from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = s = nums[0]
        for i in nums[1:]:
            if i > (p+i):
                p = i
            else:
                p += i
            s = max(s, p)
        return s