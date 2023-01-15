class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = []
        for e, i in enumerate(nums):
            if target-i in hash_map:
                return e, hash_map[target-i]
            hash_map[i] = e