class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_s = 0
        min_s = 0
        max_ans = nums[0]
        min_ans = nums[0]
        total = sum(nums)
        for i in range(n):
            if nums[i]+min_s < 0:
                min_s += nums[i]
                min_ans = min(min_ans, min_s)
            else:
                min_s = 0
            max_s += nums[i]
            max_ans = max(max_ans, max_s)
            max_s = max(0, max_s)
        return max(max_ans, total-min_ans) if total > min_ans else max_ans