class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums[:] = sorted(nums[:])
        MOD = int(1e9)+7
        n = len(nums)
        i = 0
        j = n-1
        while i <= j:
            if nums[i]+nums[j] <= target:
                ans = (ans%MOD + 2**(j-i)%MOD)%MOD
                i += 1
            else:
                j -= 1
        return ans