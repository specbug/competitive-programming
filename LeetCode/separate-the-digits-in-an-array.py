class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for i in nums for c in str(i)]