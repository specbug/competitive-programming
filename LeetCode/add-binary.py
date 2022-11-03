class Solution:
    def addBinary(self, a: str, b: str) -> str:
            m = len(a)
            n = len(b)
            l = max(m, n)
            a = '0' * (l - m) + a[:]
            b = '0' * (l - n) + b[:]
            ans = []
            c = 0
            for i in range(l-1, -1, -1):
                _a = int(a[i])
                _b = int(b[i])
                _ans = _a + _b + c
                if _ans > 1:
                    c = 1
                else:
                    c = 0
                if _ans & 1 == 0:
                    ans.append('0')
                else:
                    ans.append('1')
            if c > 0:
                ans.append('1')
            return ''.join(ans[::-1])