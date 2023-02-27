class Solution:
    def shipWithinDays(self, weights, D):
        left, right = 0, 0
        for i in weights:
            left = max(left, i)
            right += i
        while left < right:
            mid, need, cur = (left + right)//2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left
