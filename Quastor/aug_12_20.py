"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

Input - [6, 1, 3, 3, 3, 6, 6]
Output - 1
Input - [13, 19, 13, 13]
Output - 19

Do this in O(N) time and O(1) space.
"""


def find_unique(nums):
    res = [0] * 32
    ans = 0
    for n in nums:
        for i in range(32):
            bit = n >> i & 1 # interpret: div by 2 to calc binary
            res[i] = (res[i] + bit) % 3
    for i, bit in enumerate(res):
        if bit:
            ans += 2**i
    return ans