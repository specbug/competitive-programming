class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lbound = -1
        mini = -1
        maxi = -1
        ans = 0
        for i, n in enumerate(nums):
            if n == minK:
                mini = i
            if n == maxK:
                maxi = i
            if n < minK or n > maxK:
                lbound = i
            ans += max(0, min(mini, maxi)-lbound)
        return ans
        
