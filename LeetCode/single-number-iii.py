class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        pos = -1
        for i in range(31, -1, -1):
            if (xor >> i) & 1:
                pos = i
                break
        x0 = x1 = 0
        for i in nums:
            if (i >> pos) & 1:
                x1 ^= i
            else:
                x0 ^= i
        return [x0, x1]