class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        t = 0
        banned = set([k for k in banned if k <= n])
        for i in range(1, n+1):
            if i in banned:
                continue
            maxSum -= i
            if maxSum < 0:
                return t
            t += 1
        return t
