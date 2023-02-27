class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = [str(i) for i in str(num)]
        k = 0
        while k < len(nums)-1 and nums[k] == '9':
            k += 1
        mx = ''.join('9' if i==nums[k] else i for i in nums)
        mn = ''.join('0' if i==nums[0] else i for i in nums)
        return int(mx)-int(mn)