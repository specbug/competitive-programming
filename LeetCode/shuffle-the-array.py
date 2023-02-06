class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [k for i in range(n) for k in [nums[i], nums[i+n]]]