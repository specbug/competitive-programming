class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        uni_arr = list(range(1, n+1))
        for n in nums:
            uni_arr[n-1] = None
        return [i for i in uni_arr if i]