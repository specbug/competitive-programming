class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0] * 32
        ans = 0
        for n in nums:
            for i in range(32):
                bit = n >> i & 1
                res[i] = (res[i] + bit) % 3
        for i, bit in enumerate(res):
            if bit:
                ans += 2**i
        if ans > 2**31-1:
            ans = -(2**32 - ans)
        return ans