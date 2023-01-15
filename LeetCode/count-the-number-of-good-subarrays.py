class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = dict()
        n = len(nums)
        pairs = 0
        ans = 0
        freq[nums[0]] = 1
        i = 0
        for j in range(1, n):
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            pairs += (freq[nums[j]] - 1)
            while pairs >= k:
                freq[nums[i]] -= 1
                pairs -= freq[nums[i]]
                i += 1
            ans += i
        return ans