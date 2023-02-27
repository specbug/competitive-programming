class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        for i in range(1, len(prices)):
            n = prices[i]
            mn = min(mn, n)
            if prices[i] > prices[i-1]:
                ans = max(ans, prices[i]-mn)
        return ans