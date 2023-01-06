class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_el = -1
        ans = 0
        for i in costs:
            if i > max_el:
                max_el = i
        bucket = [0]*(max_el+1)
        for i in costs:
            bucket[i] += 1
        for i, k in enumerate(bucket):
            if i == 0:
                continue
            ans += min(k, coins//i)
            coins -= min(coins, i*k)
            if coins == 0 or coins < i:
                break
        return ans