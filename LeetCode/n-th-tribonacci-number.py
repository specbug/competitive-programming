class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n <= 2:
            return 0 if n == 0 else 1
        ans = a+b+c
        for i in range(3, n+1):
            a, b, ans = b, c, a+b+c
            c = ans
        return ans