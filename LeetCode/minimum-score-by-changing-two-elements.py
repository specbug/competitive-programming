import math

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        mx1 = mx2 = mx3 = 0
        mn1 = mn2 = mn3 = math.inf
        for n in nums:
            if n > mx1:
                mx1, mx2, mx3 = n, mx1, mx2
            elif n > mx2:
                mx2, mx3 = n, mx2
            elif n > mx3:
                mx3 = n
            if n < mn1:
                mn1, mn2, mn3 = n, mn1, mn2
            elif n < mn2:
                mn2, mn3 = n, mn2
            elif n < mn3:
                mn3 = n
        return min(mx1-mn3, mx2-mn2, mx3-mn1)