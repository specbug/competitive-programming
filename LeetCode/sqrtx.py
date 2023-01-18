class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        l = 0
        r = x
        while l <= r:
            m = l + (r-l)//2
            if m*m <= x and (m+1)*(m+1) > x:
                return m
            elif m*m < x:
                l = m+1
            else:
                r = m-1
        return m
