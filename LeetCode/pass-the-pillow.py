class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = time%(2*n-2)+1
        if x >= n:
            x = 2*n-x
        return x
