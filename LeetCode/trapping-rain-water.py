class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        n = len(height)
        ml = height[0]
        mr = height[n - 1]
        i = 1
        j = n - 2
        ans = 0
        while i <= j:
            ml = max(ml, height[i])
            mr = max(mr, height[j])
            if ml <= mr:
                ans += ml - height[i]
                i += 1
            else:
                ans += mr - height[j]
                j -= 1
        return ans
