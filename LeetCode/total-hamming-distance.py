class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        mod = int(1e9) + 7
        n = len(nums)
        if n < 2:
            return 0
        res = [0] * 32
        for num in nums:
            for i in range(32):
                bit = (num >> i) & 1
                res[i] += bit
        for i in res:
            if i > 0:
                ans = (ans%mod + (i * (n - i))%mod)%mod
        return ans%mod