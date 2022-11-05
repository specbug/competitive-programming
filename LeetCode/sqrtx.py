class Solution:
    def get_sqrt_recursive(self, x, l, r):
        if x < 2:
            return x
        mid = l + (r - l) // 2
        if mid*mid <= x:
            if (mid+1)*(mid+1) > x:
                return mid
            else:
                return self.get_sqrt_recursive(x, mid+1, r)
        else:
            return self.get_sqrt_recursive(x, l, mid-1)
        
    
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        return self.get_sqrt_recursive(x, 1, x)
