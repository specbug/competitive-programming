class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end+1)//2
            if nums[mid-1] != nums[mid] != nums[(mid+1)%n]:
                return nums[mid]
            elif (end-mid-(nums[mid]==nums[mid+1])) & 1:
                start = mid+1
            else:
                end = mid-1-(nums[mid]==nums[mid-1])
        return nums[start]