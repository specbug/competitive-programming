import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k and nums[0] < 0:
            heapq.heapreplace(nums, -nums[0])
            k -= 1
        if k&1:
            heapq.heapreplace(nums, -nums[0])
        return sum(nums)