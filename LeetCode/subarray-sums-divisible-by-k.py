class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        mod_map = dict()
        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i-1]
            x = nums[i]%k
            mod_map[x] = mod_map.get(x, 0) + 1
            ans += (mod_map[x] - 1)
            ans += int(x == 0)
        return ans
