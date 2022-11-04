class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if dividend > INT_MAX:
            return INT_MAX
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1
        if divisor == 1:
            return dividend
        q = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            i = 0
            while b << i <= a:
                i += 1
            q += 2**(i-1)
            if q > INT_MAX:
                return INT_MAX
            a -= b << (i-1)
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if q * abs(divisor) > abs(dividend):
                q += 1
            q *= -1
            if q < INT_MIN:
                return INT_MIN
        return q