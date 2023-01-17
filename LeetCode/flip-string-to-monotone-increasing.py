class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        a = 0
        for i in s:
            if i == '0':
                a += 1
        ans = a
        for i in s:
            if i == '0':
                a -= 1
                ans = min(ans, a)
            else:
                a += 1
        return ans