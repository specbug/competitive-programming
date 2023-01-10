class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        min_n = None
        c = 0
        for i in nums:
            if i > 0:
                c += 1
                if min_n is None or i < min_n:
                    min_n = i
        if min_n != 1:
            return 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > c:
                nums[i] = 1
        for i in range(n):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        ans = None
        for r in range(n):
            if nums[r] > 0:
                ans = r+1
                break
        if ans is None:
            return n+1
        return ans
            

