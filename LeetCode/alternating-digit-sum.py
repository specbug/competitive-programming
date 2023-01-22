class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l = len(str(n))
        bmap = {True: 1, False: -1}
        x = 0
        b = l&1
        while n > 0:
            x += n%10*bmap[b]
            b = not b
            n //= 10            
        return x
