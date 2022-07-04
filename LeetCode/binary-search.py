from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.binary_search(nums, n, 0, n, 0, target)

    def binary_search(self, nums, n, l, u, k, target):
        if n == 1:
            if nums[l] == target:
                return k + (u - l) - 1
            else:
                return -1
        m = k + ((n - 1) // 2)
        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.binary_search(nums, len(nums[m + 1:u]), m + 1, u, m + 1, target)
        else:
            return self.binary_search(nums, len(nums[l:m]), l, m, k, target)